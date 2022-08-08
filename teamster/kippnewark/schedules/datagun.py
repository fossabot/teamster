import os

from dagster import ScheduleDefinition, config_from_files

from teamster.kippnewark.jobs.datagun import datagun_etl_sftp

LOCAL_TIME_ZONE = os.getenv("LOCAL_TIME_ZONE")

powerschool_datagun = ScheduleDefinition(
    name="powerschool_datagun_nwk",
    job=datagun_etl_sftp,
    cron_schedule="15 2 * * *",
    execution_timezone=LOCAL_TIME_ZONE,
    run_config=config_from_files(
        [
            "./teamster/common/config/datagun/resource.yaml",
            "./teamster/common/config/google/resource.yaml",
            "./teamster/local/config/datagun/query-powerschool.yaml",
        ]
    ),
    tags={
        "dagster-k8s/config": {
            "container_config": {
                "resources": {"limits": {"cpu": "500m", "memory": "512Mi"}}
            }
        }
    },
)

nps_datagun = ScheduleDefinition(
    name="nps_datagun",
    job=datagun_etl_sftp,
    cron_schedule="0 0 * * *",
    execution_timezone=LOCAL_TIME_ZONE,
    run_config=config_from_files(
        [
            "./teamster/common/config/datagun/resource.yaml",
            "./teamster/common/config/google/resource.yaml",
            "./teamster/local/config/datagun/query-nps.yaml",
        ]
    ),
)

__all__ = [
    "powerschool_datagun",
    "nps_datagun",
]
