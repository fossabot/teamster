from dagster import RunRequest, build_schedule_from_partitioned_job, schedule

from teamster.core.utils.variables import LOCAL_TIME_ZONE

from .. import CODE_LOCATION
from . import assets, jobs


@schedule(
    cron_schedule="0 0 * * *",
    execution_timezone=LOCAL_TIME_ZONE.name,
    job=jobs.static_partition_asset_job,
)
def static_partition_asset_job_schedule():
    for school_id in assets.school_ids:
        yield RunRequest(
            run_key=(
                CODE_LOCATION + "_deanslist_static_partition_asset_job_" + school_id
            ),
            partition_key=school_id,
        )


multi_partition_asset_job_schedule = build_schedule_from_partitioned_job(
    job=jobs.multi_partition_asset_job, hour_of_day=0, minute_of_hour=0
)

__all__ = [
    static_partition_asset_job_schedule,
    multi_partition_asset_job_schedule,
]
