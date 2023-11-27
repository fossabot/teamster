from dagster import Definitions, EnvVar, load_assets_from_modules
from dagster_dbt import DbtCliResource
from dagster_gcp import BigQueryResource, GCSPickleIOManager, GCSResource
from dagster_k8s import k8s_job_executor

from teamster import GCS_PROJECT_NAME
from teamster.core.deanslist.resources import DeansListResource
from teamster.core.google.io.resources import gcs_io_manager
from teamster.core.sqlalchemy.resources import OracleResource, SqlAlchemyEngineResource
from teamster.core.ssh.resources import SSHResource
from teamster.kippcamden import (
    CODE_LOCATION,
    datagun,
    dbt,
    deanslist,
    edplan,
    pearson,
    powerschool,
    titan,
)

GCS_RESOURCE = GCSResource(project=GCS_PROJECT_NAME)

defs = Definitions(
    executor=k8s_job_executor,
    assets=[
        *load_assets_from_modules(modules=[datagun], group_name="datagun"),
        *load_assets_from_modules(modules=[dbt]),
        *load_assets_from_modules(modules=[deanslist], group_name="deanslist"),
        *load_assets_from_modules(modules=[edplan], group_name="edplan"),
        *load_assets_from_modules(modules=[pearson], group_name="pearson"),
        *load_assets_from_modules(modules=[powerschool], group_name="powerschool"),
        *load_assets_from_modules(modules=[titan], group_name="titan"),
    ],
    jobs=[*datagun.jobs, *deanslist.jobs],
    schedules=[
        *datagun.schedules,
        *dbt.schedules,
        *powerschool.schedules,
        *deanslist.schedules,
    ],
    sensors=[*powerschool.sensors, *edplan.sensors, *titan.sensors],
    resources={
        "gcs": GCS_RESOURCE,
        "io_manager": GCSPickleIOManager(
            gcs=GCS_RESOURCE, gcs_bucket=f"teamster-{CODE_LOCATION}"
        ),
        "io_manager_gcs_avro": gcs_io_manager.configured(
            config_or_config_fn={
                "gcs_bucket": f"teamster-{CODE_LOCATION}",
                "io_format": "avro",
            }
        ),
        "io_manager_gcs_file": gcs_io_manager.configured(
            config_or_config_fn={
                "gcs_bucket": f"teamster-{CODE_LOCATION}",
                "io_format": "filepath",
            }
        ),
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
        "ssh_couchdrop": SSHResource(
            remote_host="kipptaf.couchdrop.io",
            username=EnvVar("COUCHDROP_SFTP_USERNAME"),
            password=EnvVar("COUCHDROP_SFTP_PASSWORD"),
        ),
        "ssh_cpn": SSHResource(
            remote_host="sftp.careevolution.com",
            username=EnvVar("CPN_SFTP_USERNAME"),
            password=EnvVar("CPN_SFTP_PASSWORD"),
        ),
        "ssh_edplan": SSHResource(
            remote_host="secureftp.easyiep.com",
            username=EnvVar("KIPPCAMDEN_EDPLAN_SFTP_USERNAME"),
            password=EnvVar("KIPPCAMDEN_EDPLAN_SFTP_PASSWORD"),
        ),
        "ssh_powerschool": SSHResource(
            remote_host="pskcna.kippnj.org",
            remote_port=EnvVar("KIPPCAMDEN_PS_SSH_PORT").get_value(),
            username=EnvVar("KIPPCAMDEN_PS_SSH_USERNAME"),
            password=EnvVar("KIPPCAMDEN_PS_SSH_PASSWORD"),
            tunnel_remote_host=EnvVar("KIPPCAMDEN_PS_SSH_REMOTE_BIND_HOST"),
        ),
        "ssh_pythonanywhere": SSHResource(
            remote_host="ssh.pythonanywhere.com",
            username=EnvVar("PYTHONANYWHERE_SFTP_USERNAME"),
            password=EnvVar("PYTHONANYWHERE_SFTP_PASSWORD"),
        ),
        "ssh_titan": SSHResource(
            remote_host="sftp.titank12.com",
            username=EnvVar("KIPPCAMDEN_TITAN_SFTP_USERNAME"),
            password=EnvVar("KIPPCAMDEN_TITAN_SFTP_PASSWORD"),
        ),
    },
)
