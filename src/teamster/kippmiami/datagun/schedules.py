from dagster import ScheduleDefinition

from teamster.core.utils.variables import LOCAL_TIME_ZONE
from teamster.kippmiami.datagun.jobs import powerschool_extract_assets_job

powerschool_extract_assets_schedule = ScheduleDefinition(
    job=powerschool_extract_assets_job,
    cron_schedule="15 2 * * *",
    execution_timezone=LOCAL_TIME_ZONE.name,
)

__all__ = [powerschool_extract_assets_schedule]
