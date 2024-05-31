import re

import pendulum
from dagster import (
    AddDynamicPartitionsRequest,
    DynamicPartitionsDefinition,
    MultiPartitionKey,
    MultiPartitionsDefinition,
    RunRequest,
    SensorEvaluationContext,
    SensorResult,
    _check,
    sensor,
)

from teamster.core.ssh.resources import SSHResource
from teamster.kipptaf import CODE_LOCATION
from teamster.kipptaf.adp.payroll.assets import assets


@sensor(
    name=f"{CODE_LOCATION}_adp_payroll_sftp_sensor",
    minimum_interval_seconds=(60 * 10),
    asset_selection=assets,
)
def adp_payroll_sftp_sensor(
    context: SensorEvaluationContext, ssh_couchdrop: SSHResource
):
    now = pendulum.now()
    run_requests = []
    dynamic_partitions_requests = []

    tick_cursor = float(context.cursor or "0.0")

    try:
        files = ssh_couchdrop.listdir_attr_r(
            remote_dir=f"/teamster-{CODE_LOCATION}/couchdrop/adp/payroll", files=[]
        )
    except Exception as e:
        context.log.exception(e)
        return SensorResult(skip_reason=str(e))

    for asset in assets:
        add_dynamic_partition_keys = set()

        asset_identifier = asset.key.to_python_identifier()
        metadata_by_key = asset.metadata_by_key[asset.key]

        partitions_def = _check.inst(
            obj=asset.partitions_def, ttype=MultiPartitionsDefinition
        )

        date_partition = _check.inst(
            obj=partitions_def.get_partitions_def_for_dimension("date"),
            ttype=DynamicPartitionsDefinition,
        )

        context.log.info(asset_identifier)
        pattern = re.compile(
            pattern=f"{metadata_by_key["remote_dir"]}/{metadata_by_key["remote_file_regex"]}"
        )

        file_matches = [
            f
            for f in files
            if pattern.match(string=f.filepath)
            and f.st_mtime > tick_cursor
            and f.st_size > 0
        ]

        for f in file_matches:
            match = _check.not_none(value=pattern.match(string=f.filepath))

            group_dict = match.groupdict()

            partition_key = MultiPartitionKey(group_dict)

            context.log.info(f"{f.filename}: {partition_key}")
            add_dynamic_partition_keys.add(group_dict["date"])
            run_requests.append(
                RunRequest(
                    run_key=f"{asset_identifier}__{partition_key}__{now.timestamp()}",
                    asset_selection=[asset.key],
                    partition_key=partition_key,
                )
            )

        dynamic_partitions_requests.append(
            AddDynamicPartitionsRequest(
                partitions_def_name=_check.str_param(
                    obj=date_partition.name, param_name="partitions_def_name"
                ),
                partition_keys=list(add_dynamic_partition_keys),
            )
        )

    if run_requests:
        tick_cursor = now.timestamp()

    return SensorResult(
        run_requests=run_requests,
        dynamic_partitions_requests=dynamic_partitions_requests,
        cursor=str(tick_cursor),
    )


sensors = [
    adp_payroll_sftp_sensor,
]
