import json
import re

import pendulum
from dagster import (
    AssetsDefinition,
    AssetSelection,
    RunRequest,
    SensorEvaluationContext,
    SensorResult,
    SkipReason,
    sensor,
)
from paramiko.ssh_exception import SSHException

from teamster.core.ssh.resources import SSHConfigurableResource


def get_ls(context, source_system, asset_defs):
    cursor: dict = json.loads(context.cursor or "{}")
    ssh: SSHConfigurableResource = getattr(context.resources, f"sftp_{source_system}")

    try:
        conn = ssh.get_connection()
    except SSHException as e:
        context.log.error(e)
        return SensorResult(skip_reason=SkipReason(str(e)))
    except ConnectionResetError as e:
        context.log.error(e)
        return SensorResult(skip_reason=SkipReason(str(e)))

    ls = {}
    with conn.open_sftp() as sftp_client:
        for asset in asset_defs:
            ls[asset.key.to_python_identifier()] = {
                "asset": asset,
                "files": sftp_client.listdir_attr(
                    path=asset.metadata_by_key[asset.key]["remote_filepath"]
                ),
            }
    conn.close()

    return cursor, ls


def build_sftp_sensor(
    code_location,
    source_system,
    asset_defs: list[AssetsDefinition],
    timezone,
    minimum_interval_seconds=None,
    partition_key_fn=None,
    dynamic_partition_fn=None,
):
    @sensor(
        name=f"{code_location}_{source_system}_sftp_sensor",
        minimum_interval_seconds=minimum_interval_seconds,
        asset_selection=AssetSelection.assets(*asset_defs),
        required_resource_keys={f"sftp_{source_system}"},
    )
    def _sensor(context: SensorEvaluationContext):
        cursor, ls = get_ls(
            context=context, source_system=source_system, asset_defs=asset_defs
        )

        run_requests = []
        dynamic_partitions_requests = []
        for asset_identifier, asset_dict in ls.items():
            context.log.info(asset_identifier)

            last_run = cursor.get(asset_identifier, 0)
            asset = asset_dict["asset"]
            files = asset_dict["files"]

            asset_metadata = asset.metadata_by_key[asset.key]

            updates = []
            for f in files:
                match = re.match(
                    pattern=asset_metadata["remote_file_regex"], string=f.filename
                )

                if match is not None:
                    context.log.info(f"{f.filename}: {f.st_mtime} - {f.st_size}")
                    if f.st_mtime > last_run and f.st_size > 0:
                        updates.append(
                            {"mtime": f.st_mtime, "partition_key": partition_key_fn()}
                        )

            partition_keys = set()
            if updates:
                for u in updates:
                    partition_key = u["partition_key"]

                    run_requests.append(
                        RunRequest(
                            run_key=f"{asset_identifier}_{partition_key}_{u['mtime']}",
                            asset_selection=[asset.key],
                            partition_key=partition_key,
                        )
                    )

                    partition_keys.add(partition_key)

            dynamic_partitions_requests.append(dynamic_partition_fn())

            cursor[asset_identifier] = pendulum.now(tz=timezone).timestamp()

        return SensorResult(
            run_requests=run_requests,
            cursor=json.dumps(obj=cursor),
            dynamic_partitions_requests=dynamic_partitions_requests,
        )

    return _sensor
