from dagster import ScheduleDefinition

from teamster.core.utils.variables import LOCAL_TIME_ZONE
from teamster.kippmiami.powerschool.db import jobs

powerschool_nonpartition_assets_job_schedule = ScheduleDefinition(
    job=jobs.powerschool_nonpartition_assets_job,
    cron_schedule="0 0 * * *",
    execution_timezone=LOCAL_TIME_ZONE.name,
)

__all__ = [powerschool_nonpartition_assets_job_schedule]
