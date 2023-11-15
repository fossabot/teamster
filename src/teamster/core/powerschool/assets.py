import pendulum
from dagster import (
    AssetExecutionContext,
    AssetsDefinition,
    MonthlyPartitionsDefinition,
    Output,
    asset,
)
from fastavro import block_reader
from sqlalchemy import literal_column, select, table, text

from teamster.core.sqlalchemy.resources import OracleResource
from teamster.core.ssh.resources import SSHConfigurableResource
from teamster.core.utils.classes import FiscalYearPartitionsDefinition


def build_powerschool_table_asset(
    asset_name,
    code_location,
    partitions_def: FiscalYearPartitionsDefinition | MonthlyPartitionsDefinition = None,
    select_columns=["*"],
    partition_column=None,
    op_tags={},
) -> AssetsDefinition:
    @asset(
        key=[code_location, "powerschool", asset_name],
        partitions_def=partitions_def,
        metadata={"partition_column": partition_column},
        op_tags=op_tags,
        io_manager_key="io_manager_gcs_file",
    )
    def _asset(
        context: AssetExecutionContext,
        ssh_powerschool: SSHConfigurableResource,
        db_powerschool: OracleResource,
    ):
        now = pendulum.now()

        asset_metadata = context.assets_def.metadata_by_key[context.assets_def.key]

        partition_column = asset_metadata["partition_column"]

        if not context.has_partition_key:
            constructed_where = ""
        elif (
            context.partition_key
            == context.assets_def.partitions_def.get_first_partition_key()
        ):
            constructed_where = ""
        else:
            window_start = pendulum.from_format(
                string=context.partition_key, fmt="YYYY-MM-DDTHH:mm:ssZZ"
            )

            window_start_fmt = window_start.format("YYYY-MM-DDTHH:mm:ss.SSSSSS")

            if isinstance(
                context.assets_def.partitions_def, FiscalYearPartitionsDefinition
            ):
                window_end = window_start.add(years=1)
            elif isinstance(
                context.assets_def.partitions_def, MonthlyPartitionsDefinition
            ):
                window_end = window_start.add(months=1)

            window_end = window_end.subtract(days=1).format(
                "YYYY-MM-DDTHH:mm:ss.SSSSSS"
            )

            constructed_where = (
                f"{partition_column} BETWEEN "
                f"TO_TIMESTAMP('{window_start_fmt}', 'YYYY-MM-DD\"T\"HH24:MI:SS.FF6') "
                "AND "
                f"TO_TIMESTAMP('{window_end}', 'YYYY-MM-DD\"T\"HH24:MI:SS.FF6')"
            )

        sql = (
            select(*[literal_column(col) for col in select_columns])
            .select_from(table(asset_name))
            .where(text(constructed_where))
        )

        ssh_tunnel = ssh_powerschool.get_tunnel(remote_port=1521, local_port=1521)

        try:
            context.log.info("Starting SSH tunnel")
            ssh_tunnel.start()

            file_path = db_powerschool.engine.execute_query(
                query=sql, partition_size=100000, output_format="avro"
            )

            try:
                with file_path.open(mode="rb") as f:
                    num_records = sum(block.num_records for block in block_reader(f))
            except FileNotFoundError:
                num_records = 0

            yield Output(
                value=file_path,
                metadata={
                    "records": num_records,
                    "latest_materialization_timestamp": now.timestamp(),
                },
            )
        finally:
            context.log.info("Stopping SSH tunnel")
            ssh_tunnel.stop()

    return _asset
