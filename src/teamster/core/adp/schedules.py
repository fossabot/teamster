from dagster import (
    AddDynamicPartitionsRequest,
    AssetsDefinition,
    DynamicPartitionsDefinition,
    ResourceParam,
    ScheduleEvaluationContext,
    schedule,
)

from teamster.core.adp.resources import WorkforceManagerResource


def build_adp_wfm_schedule(
    cron_schedule,
    code_location,
    source_system,
    job,
    asset_defs: list[AssetsDefinition],
):
    @schedule(
        cron_schedule=cron_schedule,
        name=f"{code_location}_{source_system}_wfm_schedule",
        job=job,
    )
    def _schedule(
        context: ScheduleEvaluationContext,
        adp_wfm: ResourceParam[WorkforceManagerResource],
    ):
        for asset in asset_defs:
            date_partition: DynamicPartitionsDefinition = (
                asset.partitions_def.get_partitions_def_for_dimension("date")
            )
            symbolic_id_partition = (
                asset.partitions_def.get_partitions_def_for_dimension("symbolic_id")
            )

            dynamic_partition_keys = set()
            for symbolic_id in symbolic_id_partition.get_partition_keys():
                symbolic_period_record = adp_wfm.request(
                    method="POST",
                    endpoint="v1/commons/symbolicperiod/read",
                    json={
                        "where": {
                            "currentUser": True,
                            "symbolicPeriodId": symbolic_id,
                        }
                    },
                ).json()

                dynamic_partition_keys.add(symbolic_period_record["begin"])

            yield AddDynamicPartitionsRequest(
                partitions_def_name=date_partition.name,
                partition_keys=list(dynamic_partition_keys),
            )

    return _schedule
