import os

import pendulum
from dagster import (
    AssetsDefinition,
    DynamicPartitionsDefinition,
    OpExecutionContext,
    Output,
    asset,
)
from fastavro import block_reader
from sqlalchemy import literal_column, select, table, text


def construct_sql(table_name, columns, partition_column, window_start=None):
    if partition_column is None or window_start is None:
        constructed_where = ""
    elif window_start == pendulum.from_timestamp(0).to_iso8601_string():
        constructed_where = ""
    else:
        window_start = pendulum.from_format(
            string=window_start, fmt="YYYY-MM-DDTHH:mm:ssZ"
        )

        window_start_fmt = window_start.format("YYYY-MM-DDTHH:mm:ss.SSSSSS")

        constructed_where = (
            f"{partition_column} >= TO_TIMESTAMP('{window_start_fmt}'"
            ", 'YYYY-MM-DD\"T\"HH24:MI:SS.FF6')"
        )

    return (
        select(*[literal_column(col) for col in columns])
        .select_from(table(table_name))
        .where(text(constructed_where))
    )


def build_powerschool_table_asset(
    asset_name,
    code_location,
    partitions_def: DynamicPartitionsDefinition = None,
    columns=["*"],
    op_tags={},
    metadata={},
) -> AssetsDefinition:
    partition_column = metadata.get("partition_column")

    @asset(
        name=asset_name,
        key_prefix=[code_location, "powerschool"],
        partitions_def=partitions_def,
        metadata=metadata,
        op_tags=op_tags,
        required_resource_keys={"ps_db", "ps_ssh"},
        io_manager_key="gcs_fp_io",
        output_required=False,
    )
    def _asset(context: OpExecutionContext):
        sql = construct_sql(
            table_name=asset_name,
            columns=columns,
            partition_column=partition_column,
            window_start=context.partition_key if partition_column else None,
        )

        ssh_tunnel = context.resources.ps_ssh.get_tunnel(
            remote_port=1521,
            remote_host=os.getenv(f"{code_location.upper()}_PS_SSH_REMOTE_BIND_HOST"),
            local_port=1521,
        )

        try:
            context.log.info("Starting SSH tunnel")
            ssh_tunnel.start()

            file_path = context.resources.ps_db.engine.execute_query(
                query=sql, partition_size=100000, output_format="avro"
            )

            try:
                with open(file=file_path, mode="rb") as fo:
                    num_records = sum(block.num_records for block in block_reader(fo))
            except FileNotFoundError:
                num_records = 0

            context.log.info(f"Found {num_records} records")
            if num_records > 0:
                yield Output(value=file_path, metadata={"records": num_records})
        finally:
            context.log.info("Stopping SSH tunnel")
            ssh_tunnel.stop()

    return _asset
