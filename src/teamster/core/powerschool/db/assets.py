from datetime import datetime, timedelta
from pathlib import Path
from typing import Optional

from dagster import FreshnessPolicy, HourlyPartitionsDefinition, Output, asset
from sqlalchemy import literal_column, select, table, text

from teamster.core.utils.variables import LOCAL_TIME_ZONE


def construct_sql(context, table_name, columns, where_column, partition_start_date):
    if partition_start_date is not None:
        end_datetime = context.partition_time_window.start
        start_datetime = end_datetime - timedelta(hours=1)

        if end_datetime == datetime.strptime(
            partition_start_date, "%Y-%m-%dT%H:%M:%S.%f%z"
        ):
            constructed_where = (
                f"{where_column} < TO_TIMESTAMP_TZ('"
                f"{end_datetime.isoformat(timespec='microseconds')}"
                "', 'YYYY-MM-DD\"T\"HH24:MI:SS.FF6TZH:TZM') OR "
                f"{where_column} IS NULL"
            )
        else:
            constructed_where = (
                f"{where_column} >= TO_TIMESTAMP_TZ('"
                f"{start_datetime.isoformat(timespec='microseconds')}"
                "', 'YYYY-MM-DD\"T\"HH24:MI:SS.FF6TZH:TZM') AND "
                f"{where_column} < TO_TIMESTAMP_TZ('"
                f"{end_datetime.isoformat(timespec='microseconds')}"
                "', 'YYYY-MM-DD\"T\"HH24:MI:SS.FF6TZH:TZM')"
            )
    else:
        constructed_where = ""

    return (
        select(*[literal_column(col) for col in columns])
        .select_from(table(table_name))
        .where(text(constructed_where))
    )


def count(context, sql) -> int:
    query_text = f"SELECT COUNT(*) FROM {sql.get_final_froms()[0].name}"

    if sql.whereclause.text == "":
        query = text(query_text)
    else:
        query = text(f"{query_text} WHERE {sql.whereclause.text}")

    [(count,)] = context.resources.ps_db.execute_query(
        query=query,
        partition_size=1,
        output=None,
    )

    return count


def table_asset_factory(
    asset_name,
    code_location,
    partition_start_date=None,
    freshness_policy=None,
    columns=["*"],
    where_column="",
):
    if partition_start_date is not None:
        hourly_partitions_def = HourlyPartitionsDefinition(
            start_date=partition_start_date,
            timezone=str(LOCAL_TIME_ZONE),
            fmt="%Y-%m-%dT%H:%M:%S.%f%z",
        )
    else:
        hourly_partitions_def = None

    if freshness_policy is not None:
        freshness_policy = FreshnessPolicy(**freshness_policy)

    @asset(
        name=asset_name,
        key_prefix=["powerschool", code_location],
        partitions_def=hourly_partitions_def,
        freshness_policy=freshness_policy,
        io_manager_key="ps_io",
        required_resource_keys={"ps_db", "ps_ssh"},
        output_required=False,
    )
    def powerschool_table(context) -> Optional[Path]:
        sql = construct_sql(
            context=context,
            table_name=asset_name,
            columns=columns,
            where_column=where_column,
            partition_start_date=partition_start_date,
        )

        ssh_tunnel = context.resources.ps_ssh.get_tunnel()

        context.log.info("Starting SSH tunnel")
        ssh_tunnel.start()

        row_count = count(context=context, sql=sql)
        context.log.info(f"Found {row_count} rows")

        if row_count > 0:
            filename = context.resources.ps_db.execute_query(
                query=sql, partition_size=100000, output="avro"
            )
        else:
            filename = None

        yield Output(value=filename, metadata={"records": row_count})

        context.log.info("Stopping SSH tunnel")
        ssh_tunnel.stop()

    return powerschool_table
