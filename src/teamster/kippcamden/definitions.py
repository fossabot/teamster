from dagster import Definitions, config_from_files, load_assets_from_modules
from dagster_dbt import dbt_cli_resource
from dagster_gcp import bigquery_resource, gcs_resource
from dagster_gcp.gcs import gcs_pickle_io_manager
from dagster_k8s import k8s_job_executor
from dagster_ssh import ssh_resource

from teamster.core.resources.deanslist import deanslist_resource
from teamster.core.resources.google import gcs_avro_io_manager, gcs_filepath_io_manager
from teamster.core.resources.sqlalchemy import mssql, oracle

from . import CODE_LOCATION, datagun, dbt, deanslist, powerschool

core_resource_config_dir = "src/teamster/core/config/resources"
local_resource_config_dir = f"src/teamster/{CODE_LOCATION}/config/resources"

defs = Definitions(
    executor=k8s_job_executor,
    assets=(
        load_assets_from_modules(modules=[powerschool.assets], group_name="powerschool")
        + load_assets_from_modules(modules=[datagun.assets], group_name="datagun")
        + load_assets_from_modules(modules=[deanslist.assets], group_name="deanslist")
        + load_assets_from_modules(modules=[dbt.assets])
    ),
    jobs=datagun.jobs.__all__ + deanslist.jobs.__all__,
    schedules=(
        datagun.schedules.__all__
        + powerschool.schedules.__all__
        + deanslist.schedules.__all__
    ),
    sensors=powerschool.sensors.__all__ + dbt.sensors.__all__,
    resources={
        "warehouse": mssql.configured(
            config_from_files([f"{core_resource_config_dir}/warehouse.yaml"])
        ),
        "bq": bigquery_resource.configured(
            config_from_files([f"{core_resource_config_dir}/gcs.yaml"])
        ),
        "gcs": gcs_resource.configured(
            config_from_files([f"{core_resource_config_dir}/gcs.yaml"])
        ),
        "sftp_pythonanywhere": ssh_resource.configured(
            config_from_files([f"{core_resource_config_dir}/sftp_pythonanywhere.yaml"])
        ),
        "ps_db": oracle.configured(
            config_from_files(
                [
                    f"{core_resource_config_dir}/db_powerschool.yaml",
                    f"{local_resource_config_dir}/db_powerschool.yaml",
                ]
            )
        ),
        "ps_ssh": ssh_resource.configured(
            config_from_files([f"{local_resource_config_dir}/ssh_powerschool.yaml"])
        ),
        "io_manager": gcs_pickle_io_manager.configured(
            config_from_files([f"{local_resource_config_dir}/io.yaml"])
        ),
        "dbt": dbt_cli_resource.configured(
            {
                "project-dir": f"teamster-dbt/{CODE_LOCATION}",
                "profiles-dir": f"teamster-dbt/{CODE_LOCATION}",
            }
        ),
        "gcs_fp_io": gcs_filepath_io_manager.configured(
            config_from_files([f"{local_resource_config_dir}/io.yaml"])
        ),
        "sftp_cpn": ssh_resource.configured(
            config_from_files([f"{local_resource_config_dir}/sftp_cpn.yaml"])
        ),
        "deanslist": deanslist_resource.configured(
            config_from_files([f"{core_resource_config_dir}/deanslist.yaml"])
        ),
        "gcs_avro_io": gcs_avro_io_manager.configured(
            config_from_files([f"{local_resource_config_dir}/io.yaml"])
        ),
    },
)
