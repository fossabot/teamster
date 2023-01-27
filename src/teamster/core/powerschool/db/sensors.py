from datetime import timedelta

from dagster import AssetSelection, build_resources, config_from_files, sensor
from dagster._core.definitions.asset_reconciliation_sensor import (
    AssetReconciliationCursor,
    reconcile,
)
from sqlalchemy import text

from teamster.core.resources.sqlalchemy import oracle
from teamster.core.resources.ssh import ssh_resource


def build_powerschool_incremental_sensor(
    name, asset_selection, where_column, run_tags=None
):
    @sensor(name=name, asset_selection=asset_selection, minimum_interval_seconds=3600)
    def _sensor(context):
        cursor = (
            AssetReconciliationCursor.from_serialized(
                context.cursor, context.repository_def.asset_graph
            )
            if context.cursor
            else AssetReconciliationCursor.empty()
        )
        context.log.info(cursor)

        run_requests, updated_cursor = reconcile(
            repository_def=context.repository_def,
            asset_selection=asset_selection,
            instance=context.instance,
            cursor=cursor,
            run_tags=run_tags,
        )
        context.log.info(updated_cursor)

        with build_resources(
            resources={
                "ps_db": oracle,
                "ps_ssh": ssh_resource,
            },
            resource_config={
                "ps_db": {
                    "config": config_from_files(
                        ["src/teamster/core/resources/config/db_powerschool.yaml"]
                    )
                },
                "ps_ssh": {
                    "config": config_from_files(
                        ["src/teamster/core/resources/config/ssh_powerschool.yaml"]
                    )
                },
            },
        ) as resources:
            ssh_tunnel = resources.ps_ssh.get_tunnel()
            ssh_tunnel.start()

            asset_keys_filtered = {}
            for (
                asset_key,
                time_window_partitions_subset,
            ) in (
                updated_cursor.materialized_or_requested_root_partitions_by_asset_key.items()
            ):
                for window in time_window_partitions_subset._included_time_windows:
                    window_end = window.end - timedelta(days=1)
                    query = text(
                        (
                            "SELECT COUNT(*) "
                            f"FROM {asset_key.path[-1]} "
                            f"WHERE {where_column} >= TO_TIMESTAMP_TZ("
                            f"'{window.start.isoformat(timespec='microseconds')}', "
                            "'YYYY-MM-DD\"T\"HH24:MI:SS.FF6TZH:TZM') "
                            f"AND {where_column} < TO_TIMESTAMP_TZ("
                            f"'{window_end.isoformat(timespec='microseconds')}', "
                            "'YYYY-MM-DD\"T\"HH24:MI:SS.FF6TZH:TZM')"
                        )
                    )

                    [(count,)] = resources.ps_db.execute_query(
                        query=query,
                        partition_size=1,
                        output=None,
                    )

                    if count > 0:
                        asset_keys_filtered[asset_key] = time_window_partitions_subset

        ssh_tunnel.stop()

        cursor_filtered = AssetReconciliationCursor(
            latest_storage_id=updated_cursor.latest_storage_id,
            materialized_or_requested_root_asset_keys=set(),
            materialized_or_requested_root_partitions_by_asset_key=asset_keys_filtered,
        )
        context.log.info(cursor_filtered)

        run_requests, updated_cursor = reconcile(
            repository_def=context.repository_def,
            asset_selection=AssetSelection.keys(*asset_keys_filtered),
            instance=context.instance,
            cursor=cursor_filtered,
            run_tags=run_tags,
        )
        context.log.info(run_requests)

        return run_requests

    return _sensor
