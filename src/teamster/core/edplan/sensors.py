import json
import re

import pendulum
from paramiko.ssh_exception import SSHException

from dagster import (
    AssetsDefinition,
    AssetSelection,
    RunRequest,
    SensorEvaluationContext,
    SensorResult,
    SkipReason,
    sensor,
)
from teamster.core.sftp.sensors import get_sftp_ls
from teamster.core.ssh.resources import SSHConfigurableResource


def build_sftp_sensor(
    sensor_name,
    asset_defs: list[AssetsDefinition],
    timezone,
    minimum_interval_seconds=None,
):
    @sensor(
        name=sensor_name,
        minimum_interval_seconds=minimum_interval_seconds,
        asset_selection=AssetSelection.assets(*asset_defs),
    )
    def _sensor(context: SensorEvaluationContext, ssh_edplan: SSHConfigurableResource):
        cursor: dict = json.loads(context.cursor or "{}")
        now = pendulum.now(tz=timezone)

        try:
            ls = get_sftp_ls(ssh=ssh_edplan, asset_defs=asset_defs)
        except SSHException as e:
            context.log.error(e)
            return SensorResult(skip_reason=SkipReason(str(e)))
        except ConnectionResetError as e:
            context.log.error(e)
            return SensorResult(skip_reason=SkipReason(str(e)))

        run_requests = []
        for asset_identifier, asset_dict in ls.items():
            asset = asset_dict["asset"]
            files = asset_dict["files"]

            last_run = cursor.get(asset_identifier, 0)

            for f in files:
                match = re.match(
                    pattern=asset.metadata_by_key[asset.key]["remote_file_regex"],
                    string=f.filename,
                )

                if match is not None:
                    context.log.info(f"{f.filename}: {f.st_mtime} - {f.st_size}")
                    if f.st_mtime > last_run and f.st_size > 0:
                        run_requests.append(
                            RunRequest(
                                run_key=f"{asset_identifier}_{f.st_mtime}",
                                asset_selection=[asset.key],
                                partition_key=pendulum.from_timestamp(
                                    timestamp=f.st_mtime
                                ).to_date_string(),
                            )
                        )

                cursor[asset_identifier] = now.timestamp()

        return SensorResult(run_requests=run_requests, cursor=json.dumps(obj=cursor))

    return _sensor
