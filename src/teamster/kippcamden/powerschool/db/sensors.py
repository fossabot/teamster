import os

import pendulum
from dagster import (
    AssetSelection,
    SensorEvaluationContext,
    build_resources,
    config_from_files,
    sensor,
)
from dagster._core.definitions.asset_reconciliation_sensor import (
    AssetReconciliationCursor,
)
from dagster._utils.caching_instance_queryer import CachingInstanceQueryer
from dagster_ssh import ssh_resource
from sqlalchemy import text

from teamster.core.utils.variables import LOCAL_TIME_ZONE
from teamster.kippcamden.powerschool.db import assets


def get_asset_count(asset, db):
    window_end = pendulum.now(tz=LOCAL_TIME_ZONE.name).start_of("hour")
    window_start = window_end.subtract(hours=24)

    window_end_fmt = window_end.format("YYYY-MM-DDTHH:mm:ss.SSSSSS")
    window_start_fmt = window_start.format("YYYY-MM-DDTHH:mm:ss.SSSSSS")

    query = text(
        "SELECT COUNT(*) "
        f"FROM {asset.asset_key.path[-1]} "
        f"WHERE {asset.metadata['partition_column']} >= "
        f"TO_TIMESTAMP('{window_start_fmt}', 'YYYY-MM-DD\"T\"HH24:MI:SS.FF6') "
        f"AND {asset.metadata['partition_column']} < "
        f"TO_TIMESTAMP('{window_end_fmt}', 'YYYY-MM-DD\"T\"HH24:MI:SS.FF6')"
    )

    [(count,)] = db.execute_query(
        query=query,
        partition_size=1,
        output=None,
    )

    return count


@sensor(asset_selection=AssetSelection.assets(*assets.partition_assets))
def test_dynamic_partition_sensor(context: SensorEvaluationContext):
    target_asset_selection = AssetSelection.assets(*assets.partition_assets)

    instance_queryer = CachingInstanceQueryer(instance=context.instance)
    asset_graph = context.repository_def.asset_graph

    # check if asset has ever been materialized or requested
    cursor = (
        AssetReconciliationCursor.from_serialized(context.cursor, asset_graph)
        if context.cursor
        else AssetReconciliationCursor.empty()
    )

    context.instance.get_latest_materialization_event
    never_materialized_or_requested = set(
        asset_key
        for asset_key in target_asset_selection.resolve(asset_graph.assets)
        if not cursor.was_previously_materialized_or_requested(asset_key)
        and not context.instance.get_latest_materialization_event(asset=asset_key)
    )
    context.log.info(never_materialized_or_requested)

    # check if asset has any modified records from past X hours
    with build_resources(
        resources={"ps_ssh": ssh_resource},
        resource_config={
            "ps_ssh": {
                "config": config_from_files(
                    ["src/teamster/core/resources/config/ssh_powerschool.yaml"]
                )
            }
        },
    ) as resources:
        ssh_port = 1521
        ssh_tunnel = resources.ps_ssh.get_tunnel(
            remote_port=ssh_port,
            remote_host=os.getenv("PS_SSH_REMOTE_BIND_HOST"),
            local_port=ssh_port,
        )

        ssh_tunnel.check_tunnels()
        if ssh_tunnel.tunnel_is_up.get(("127.0.0.1", ssh_port)):
            context.log.info("Restarting SSH tunnel")
            ssh_tunnel.restart()
        else:
            context.log.info("Starting SSH tunnel")
            ssh_tunnel.start()

        try:
            for asset in asset_graph.assets:
                context.log.info(asset)

                count = get_asset_count(asset=asset, db=resources.ps_db)

                context.log.debug(f"count: {count}")
                if count > 0:
                    ...

        finally:
            context.log.info("Stopping SSH tunnel")
            ssh_tunnel.stop()


__all__ = [test_dynamic_partition_sensor]
