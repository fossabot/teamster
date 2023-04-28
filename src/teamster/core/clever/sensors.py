import json
import re

import pendulum
from dagster import (
    AssetSelection,
    ResourceParam,
    RunRequest,
    SensorEvaluationContext,
    SensorResult,
    sensor,
)
from dagster_ssh import SSHResource


def build_sftp_sensor(code_location, asset_defs, minimum_interval_seconds=None):
    @sensor(
        name=f"{code_location}_clever_sftp_sensor",
        minimum_interval_seconds=minimum_interval_seconds,
        asset_selection=AssetSelection.assets(*asset_defs),
    )
    def _sensor(
        context: SensorEvaluationContext,
        sftp_clever_reports: ResourceParam[SSHResource],
    ):
        now = pendulum.now()
        cursor: dict = json.loads(context.cursor or "{}")
        context.instance.get_asset_keys

        conn = sftp_clever_reports.get_connection()

        with conn.open_sftp() as sftp_client:
            ls = {}
            for asset in asset_defs:
                remote_filepath = asset.metadata_by_key[asset.key]["remote_filepath"]

                ls[remote_filepath] = sftp_client.listdir_attr(path=remote_filepath)

        conn.close()

        run_requests = []
        for remote_filepath, files in ls.items():
            last_run = cursor.get(remote_filepath, 0)
            asset = [a for a in asset_defs if a.name == remote_filepath][0]

            partition_keys = set()
            for f in files:
                context.log.info(f"{f.filename}: {f.st_mtime} - {f.st_size}")
                if f.st_mtime >= last_run and f.st_size > 0:
                    match = re.match(
                        pattern=r"(\d{4}-\d{2}-\d{2})[-\w+]+-(\w+).csv",
                        string=f.filename,
                    )

                    partition_keys.add("|".join(match.groups()))

            if partition_keys:
                for pk in list(partition_keys):
                    run_requests.append(
                        RunRequest(
                            run_key=f"{asset.key.to_python_identifier()}_{pk}",
                            asset_selection=[asset.key],
                            partition_key=pk,
                        )
                    )
                cursor[remote_filepath] = now.timestamp()

        return SensorResult(run_requests=run_requests, cursor=json.dumps(obj=cursor))

    return _sensor
