import pendulum
from dagster import AssetsDefinition, RunRequest, ScheduleEvaluationContext, schedule
from sqlalchemy import text

from teamster.core.sqlalchemy.resources import OracleResource
from teamster.core.ssh.resources import SSHConfigurableResource


def build_dynamic_partition_schedule(
    cron_schedule,
    code_location,
    execution_timezone,
    asset_defs: list[AssetsDefinition],
):
    schedule_name = f"{code_location}_powerschool_last_modified_schedule"

    @schedule(
        cron_schedule=cron_schedule,
        job_name="foo",
        name=schedule_name,
        execution_timezone=execution_timezone,
    )
    def _schedule(
        context: ScheduleEvaluationContext,
        ssh_powerschool: SSHConfigurableResource,
        db_powerschool: OracleResource,
    ):
        ssh_tunnel = ssh_powerschool.get_tunnel(remote_port=1521, local_port=1521)

        try:
            context.log.debug("Starting SSH tunnel")
            ssh_tunnel.start()

            asset_selection = []
            for asset in asset_defs:
                asset_key = asset.key

                event = context.instance.get_latest_materialization_event(asset_key)

                latest_materialization = pendulum.from_timestamp(
                    event.asset_materialization.metadata.get(
                        "latest_materialization_timestamp", 0
                    )
                )

                is_requested = False

                asset_key_string = asset_key.to_python_identifier()
                context.log.debug(asset_key_string)

                if latest_materialization.timestamp() == 0:
                    is_requested = True
                else:
                    partition_column = asset.metadata_by_key[asset_key][
                        "partition_column"
                    ]

                    latest_materialization_fmt = latest_materialization.in_timezone(
                        execution_timezone
                    ).format("YYYY-MM-DDTHH:mm:ss.SSSSSS")

                    [(count,)] = db_powerschool.engine.execute_query(
                        query=text(
                            "SELECT COUNT(*) "
                            f"FROM {asset_key.path[-1]} "
                            f"WHERE {partition_column} >= "
                            f"TO_TIMESTAMP('{latest_materialization_fmt}', "
                            "'YYYY-MM-DD\"T\"HH24:MI:SS.FF6')"
                        ),
                        partition_size=1,
                        output_format=None,
                    )

                    context.log.debug(f"count: {count}")

                    if count > 0:
                        is_requested = True

                if is_requested:
                    asset_selection.append(asset_key)

        finally:
            context.log.debug("Stopping SSH tunnel")
            ssh_tunnel.stop()

        yield RunRequest(run_key=schedule_name, asset_selection=asset_selection)

    return _schedule
