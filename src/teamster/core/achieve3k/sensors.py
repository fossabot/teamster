import json
import re

import pendulum
from dagster import (
    AddDynamicPartitionsRequest,
    AssetsDefinition,
    AssetSelection,
    RunRequest,
    SensorEvaluationContext,
    SensorResult,
    sensor,
)

from teamster.core.sftp.sensors import get_sftp_ls
from teamster.core.ssh.resources import SSHConfigurableResource


def build_sftp_sensor(
    code_location,
    source_system,
    asset_defs: list[AssetsDefinition],
    timezone,
    minimum_interval_seconds=None,
):
    @sensor(
        name=f"{code_location}_{source_system}_sftp_sensor",
        minimum_interval_seconds=minimum_interval_seconds,
        asset_selection=AssetSelection.assets(*asset_defs),
    )
    def _sensor(
        context: SensorEvaluationContext, ssh_achieve3k: SSHConfigurableResource
    ):
        cursor, ls = get_sftp_ls(
            context=context, ssh=ssh_achieve3k, asset_defs=asset_defs
        )

        run_requests = []
        dynamic_partitions_requests = []
        for asset_identifier, asset_dict in ls.items():
            asset = asset_dict["asset"]
            files = asset_dict["files"]

            last_run = cursor.get(asset_identifier, 0)

            partition_keys = []
            for f in files:
                match = re.match(
                    pattern=asset.metadata_by_key[asset.key]["remote_file_regex"],
                    string=f.filename,
                )

                if match is not None:
                    context.log.info(f"{f.filename}: {f.st_mtime} - {f.st_size}")
                    if f.st_mtime > last_run and f.st_size > 0:
                        partition_keys.append(match.group(1))

            if partition_keys:
                for pk in partition_keys:
                    run_requests.append(
                        RunRequest(
                            run_key=f"{asset_identifier}_{pk}",
                            asset_selection=[asset.key],
                            partition_key=pk,
                        )
                    )

                dynamic_partitions_requests.append(
                    AddDynamicPartitionsRequest(
                        partitions_def_name=asset_identifier,
                        partition_keys=partition_keys,
                    )
                )

                cursor[asset_identifier] = pendulum.now(tz=timezone).timestamp()

        return SensorResult(
            run_requests=run_requests,
            cursor=json.dumps(obj=cursor),
            dynamic_partitions_requests=dynamic_partitions_requests,
        )

    return _sensor
