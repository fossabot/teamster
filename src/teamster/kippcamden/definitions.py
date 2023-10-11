from dagster import (
    AutoMaterializePolicy,
    Definitions,
    EnvVar,
    config_from_files,
    load_assets_from_modules,
)
from dagster_dbt import DbtCliResource
from dagster_gcp import (
    BigQueryResource,
    ConfigurablePickledObjectGCSIOManager,
    GCSResource,
)
from dagster_k8s import k8s_job_executor

from teamster.core.deanslist.resources import DeansListResource
from teamster.core.google.io.resources import gcs_io_manager
from teamster.core.sqlalchemy.resources import OracleResource, SqlAlchemyEngineResource
from teamster.core.ssh.resources import SSHConfigurableResource

from . import (
    CODE_LOCATION,
    GCS_PROJECT_NAME,
    datagun,
    dbt,
    deanslist,
    edplan,
    pearson,
    powerschool,
    titan,
)

resource_config_dir = f"src/teamster/{CODE_LOCATION}/config/resources"

defs = Definitions(
    executor=k8s_job_executor,
    assets=[
        *load_assets_from_modules(modules=[datagun], group_name="datagun"),
        *load_assets_from_modules(modules=[deanslist], group_name="deanslist"),
        *load_assets_from_modules(modules=[edplan], group_name="edplan"),
        *load_assets_from_modules(modules=[pearson], group_name="pearson"),
        *load_assets_from_modules(modules=[powerschool], group_name="powerschool"),
        *load_assets_from_modules(modules=[titan], group_name="titan"),
        *load_assets_from_modules(
            modules=[dbt], auto_materialize_policy=AutoMaterializePolicy.eager()
        ),
    ],
    jobs=[*datagun.jobs, *deanslist.jobs],
    schedules=[*datagun.schedules, *powerschool.schedules, *deanslist.schedules],
    sensors=[*powerschool.sensors, *edplan.sensors, *titan.sensors],
    resources={
        "io_manager": ConfigurablePickledObjectGCSIOManager(
            gcs=GCSResource(project=GCS_PROJECT_NAME), gcs_bucket="teamster-kippcamden"
        ),
        "io_manager_gcs_avro": gcs_io_manager.configured(
            config_from_files([f"{resource_config_dir}/io_avro.yaml"])
        ),
        "io_manager_gcs_file": gcs_io_manager.configured(
            config_from_files([f"{resource_config_dir}/io_filepath.yaml"])
        ),
        "gcs": GCSResource(project=GCS_PROJECT_NAME),
        "dbt_cli": DbtCliResource(project_dir=f"src/dbt/{CODE_LOCATION}"),
        "db_bigquery": BigQueryResource(project=GCS_PROJECT_NAME),
        "db_powerschool": OracleResource(
            engine=SqlAlchemyEngineResource(
                dialect="oracle",
                driver="oracledb",
                username="PSNAVIGATOR",
                host="localhost",
                database="PSPRODDB",
                port=1521,
                password=EnvVar("KIPPCAMDEN_PS_DB_PASSWORD"),
            ),
            version="19.0.0.0.0",
            prefetchrows=100000,
            arraysize=100000,
        ),
        "deanslist": DeansListResource(
            subdomain="kippnj",
            api_key_map="/etc/secret-volume/deanslist_api_key_map_yaml",
        ),
        "ssh_couchdrop": SSHConfigurableResource(
            remote_host="kipptaf.couchdrop.io",
            username=EnvVar("COUCHDROP_SFTP_USERNAME"),
            password=EnvVar("COUCHDROP_SFTP_PASSWORD"),
        ),
        "ssh_cpn": SSHConfigurableResource(
            remote_host="sftp.careevolution.com",
            username=EnvVar("CPN_SFTP_USERNAME"),
            password=EnvVar("CPN_SFTP_PASSWORD"),
        ),
        "ssh_edplan": SSHConfigurableResource(
            remote_host="secureftp.easyiep.com",
            username=EnvVar("KIPPCAMDEN_EDPLAN_SFTP_USERNAME"),
            password=EnvVar("KIPPCAMDEN_EDPLAN_SFTP_PASSWORD"),
        ),
        "ssh_powerschool": SSHConfigurableResource(
            remote_host="pskcna.kippnj.org",
            remote_port=EnvVar("KIPPCAMDEN_PS_SSH_PORT"),
            username=EnvVar("KIPPCAMDEN_PS_SSH_USERNAME"),
            password=EnvVar("KIPPCAMDEN_PS_SSH_PASSWORD"),
            tunnel_remote_host=EnvVar("KIPPCAMDEN_PS_SSH_REMOTE_BIND_HOST"),
        ),
        "ssh_pythonanywhere": SSHConfigurableResource(
            remote_host="ssh.pythonanywhere.com",
            username=EnvVar("PYTHONANYWHERE_SFTP_USERNAME"),
            password=EnvVar("PYTHONANYWHERE_SFTP_PASSWORD"),
        ),
        "ssh_titan": SSHConfigurableResource(
            remote_host="sftp.titank12.com",
            username=EnvVar("KIPPCAMDEN_TITAN_SFTP_USERNAME"),
            password=EnvVar("KIPPCAMDEN_TITAN_SFTP_PASSWORD"),
        ),
    },
)
