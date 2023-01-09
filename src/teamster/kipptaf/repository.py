from dagster import repository

from teamster.core.datagun import jobs as datagun_jobs_core
from teamster.kipptaf.datagun import jobs as datagun_jobs_local
from teamster.kipptaf.datagun import schedules as datagun_schedules


@repository
def datagun():
    core_jobs = [
        v for k, v in vars(datagun_jobs_core).items() if k in datagun_jobs_core.__all__
    ]
    local_jobs = [
        v
        for k, v in vars(datagun_jobs_local).items()
        if k in datagun_jobs_local.__all__
    ]
    jobs = core_jobs + local_jobs
    schedules = [
        v for k, v in vars(datagun_schedules).items() if k in datagun_schedules.__all__
    ]

    return jobs + schedules


__all__ = ["datagun"]
