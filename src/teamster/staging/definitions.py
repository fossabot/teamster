from dagster import (
    AutoMaterializePolicy,
    Definitions,
    EnvVar,
    config_from_files,
    load_assets_from_modules,
)
from dagster_airbyte import AirbyteCloudResource
from dagster_dbt import DbtCliResource
from dagster_fivetran import FivetranResource
from dagster_gcp import (
    BigQueryResource,
    ConfigurablePickledObjectGCSIOManager,
    GCSResource,
)
from dagster_k8s import k8s_job_executor

from teamster.core.adp.resources import (
    AdpWorkforceManagerResource,
    AdpWorkforceNowResource,
)
from teamster.core.alchemer.resources import AlchemerResource
from teamster.core.amplify.resources import MClassResource
from teamster.core.deanslist.resources import DeansListResource
from teamster.core.google.directory.resources import GoogleDirectoryResource
from teamster.core.google.forms.resources import GoogleFormsResource
from teamster.core.google.io.resources import gcs_io_manager
from teamster.core.google.sheets.resources import GoogleSheetsResource
from teamster.core.ldap.resources import LdapResource
from teamster.core.schoolmint.grow.resources import SchoolMintGrowResource
from teamster.core.smartrecruiters.resources import SmartRecruitersResource
from teamster.core.sqlalchemy.resources import OracleResource, SqlAlchemyEngineResource
from teamster.core.ssh.resources import SSHConfigurableResource
from teamster.staging import (  # renlearn,
    CODE_LOCATION,
    GCS_PROJECT_NAME,
    achieve3k,
    adp,
    airbyte,
    alchemer,
    amplify,
    clever,
    dbt,
    deanslist,
    edplan,
    fivetran,
    google,
    iready,
    ldap,
    powerschool,
    schoolmint,
    smartrecruiters,
    titan,
)

resource_config_dir = f"src/teamster/{CODE_LOCATION}/config/resources"

defs = Definitions(
    executor=k8s_job_executor,
    assets=[
        *load_assets_from_modules(modules=[achieve3k], group_name="achieve3k"),
        *load_assets_from_modules(modules=[adp], group_name="adp"),
        *load_assets_from_modules(modules=[alchemer], group_name="alchemer"),
        *load_assets_from_modules(modules=[amplify], group_name="amplify"),
        *load_assets_from_modules(modules=[clever], group_name="clever"),
        *load_assets_from_modules(modules=[deanslist], group_name="deanslist"),
        *load_assets_from_modules(modules=[edplan], group_name="edplan"),
        *load_assets_from_modules(modules=[google], group_name="google"),
        *load_assets_from_modules(modules=[iready], group_name="iready"),
        *load_assets_from_modules(modules=[ldap], group_name="ldap"),
        *load_assets_from_modules(modules=[powerschool], group_name="powerschool"),
        # *load_assets_from_modules(modules=[renlearn], group_name="renlearn"),
        *load_assets_from_modules(modules=[schoolmint], group_name="schoolmint_grow"),
        *load_assets_from_modules(modules=[titan], group_name="titan"),
        *load_assets_from_modules(
            modules=[smartrecruiters], group_name="smartrecruiters"
        ),
        *load_assets_from_modules(modules=[airbyte]),
        *load_assets_from_modules(modules=[fivetran]),
        *load_assets_from_modules(
            modules=[dbt], auto_materialize_policy=AutoMaterializePolicy.eager()
        ),
    ],
    resources={
        "io_manager": ConfigurablePickledObjectGCSIOManager(
            gcs=GCSResource(project=GCS_PROJECT_NAME), gcs_bucket="teamster-staging"
        ),
        "io_manager_gcs_avro": gcs_io_manager.configured(
            config_from_files([f"{resource_config_dir}/io_avro.yaml"])
        ),
        "io_manager_gcs_file": gcs_io_manager.configured(
            config_from_files([f"{resource_config_dir}/io_filepath.yaml"])
        ),
        "gcs": GCSResource(project=GCS_PROJECT_NAME),
        "dbt_cli": DbtCliResource(project_dir=f"/root/app/src/dbt/{CODE_LOCATION}"),
        "db_bigquery": BigQueryResource(project=GCS_PROJECT_NAME),
        "db_powerschool": OracleResource(
            engine=SqlAlchemyEngineResource(
                dialect="oracle",
                driver="oracledb",
                username="PSNAVIGATOR",
                host="localhost",
                database="PSPRODDB",
                port=1521,
                password=EnvVar("STAGING_PS_DB_PASSWORD"),
            ),
            version="19.0.0.0.0",
            prefetchrows=100000,
            arraysize=100000,
        ),
        "adp_wfm": AdpWorkforceManagerResource(
            subdomain=EnvVar("ADP_WFM_SUBDOMAIN"),
            app_key=EnvVar("ADP_WFM_APP_KEY"),
            client_id=EnvVar("ADP_WFM_CLIENT_ID"),
            client_secret=EnvVar("ADP_WFM_CLIENT_SECRET"),
            username=EnvVar("ADP_WFM_USERNAME"),
            password=EnvVar("ADP_WFM_PASSWORD"),
        ),
        "adp_wfn": AdpWorkforceNowResource(
            client_id=EnvVar("ADP_WFN_CLIENT_ID"),
            client_secret=EnvVar("ADP_WFN_CLIENT_SECRET"),
            cert_filepath="/etc/secret-volume/adp_wfn_cert",
            key_filepath="/etc/secret-volume/adp_wfn_key",
        ),
        "airbyte": AirbyteCloudResource(api_key=EnvVar("AIRBYTE_API_KEY")),
        "alchemer": AlchemerResource(
            api_token=EnvVar("ALCHEMER_API_TOKEN"),
            api_token_secret=EnvVar("ALCHEMER_API_TOKEN_SECRET"),
            api_version="v5",
        ),
        "deanslist": DeansListResource(
            subdomain="kippnj",
            api_key_map="/etc/secret-volume/deanslist_api_key_map_yaml",
        ),
        "fivetran": FivetranResource(
            api_key=EnvVar("FIVETRAN_API_KEY"), api_secret=EnvVar("FIVETRAN_API_SECRET")
        ),
        "google_forms": GoogleFormsResource(
            service_account_file_path="/etc/secret-volume/gcloud_service_account_json"
        ),
        "google_directory": GoogleDirectoryResource(
            customer_id="C029u7m0n",
            service_account_file_path="/etc/secret-volume/gcloud_service_account_json",
            delegated_account="dagster@apps.teamschools.org",
        ),
        "gsheets": GoogleSheetsResource(
            service_account_file_path="/etc/secret-volume/gcloud_service_account_json"
        ),
        "ldap": LdapResource(
            host="ldap1.kippnj.org",
            port=636,
            user=EnvVar("LDAP_USER"),
            password=EnvVar("LDAP_PASSWORD"),
        ),
        "mclass": MClassResource(
            username=EnvVar("AMPLIFY_USERNAME"), password=EnvVar("AMPLIFY_PASSWORD")
        ),
        "schoolmint_grow": SchoolMintGrowResource(
            client_id=EnvVar("SCHOOLMINT_GROW_CLIENT_ID"),
            client_secret=EnvVar("SCHOOLMINT_GROW_CLIENT_SECRET"),
            district_id=EnvVar("SCHOOLMINT_GROW_DISTRICT_ID"),
            api_response_limit=3200,
        ),
        "smartrecruiters": SmartRecruitersResource(
            smart_token=EnvVar("SMARTRECRUITERS_SMARTTOKEN")
        ),
        "ssh_achieve3k": SSHConfigurableResource(
            remote_host="xfer.achieve3000.com",
            username=EnvVar("ACHIEVE3K_SFTP_USERNAME"),
            password=EnvVar("ACHIEVE3K_SFTP_PASSWORD"),
        ),
        "ssh_adp": SSHConfigurableResource(
            remote_host="sftp.kippnj.org",
            username=EnvVar("ADP_SFTP_USERNAME"),
            password=EnvVar("ADP_SFTP_PASSWORD"),
        ),
        "ssh_blissbook": SSHConfigurableResource(
            remote_host="sftp.blissbook.com",
            remote_port="3022",
            username=EnvVar("BLISSBOOK_SFTP_USERNAME"),
            password=EnvVar("BLISSBOOK_SFTP_PASSWORD"),
        ),
        "ssh_clever": SSHConfigurableResource(
            remote_host="sftp.clever.com",
            username=EnvVar("CLEVER_SFTP_USERNAME"),
            password=EnvVar("CLEVER_SFTP_PASSWORD"),
        ),
        "ssh_clever_reports": SSHConfigurableResource(
            remote_host="reports-sftp.clever.com",
            username=EnvVar("CLEVER_REPORTS_SFTP_USERNAME"),
            password=EnvVar("CLEVER_REPORTS_SFTP_PASSWORD"),
        ),
        "ssh_coupa": SSHConfigurableResource(
            remote_host="fileshare.coupahost.com",
            username=EnvVar("COUPA_SFTP_USERNAME"),
            password=EnvVar("COUPA_SFTP_PASSWORD"),
        ),
        "ssh_deanslist": SSHConfigurableResource(
            remote_host="sftp.deanslistsoftware.com",
            username=EnvVar("DEANSLIST_SFTP_USERNAME"),
            password=EnvVar("DEANSLIST_SFTP_PASSWORD"),
        ),
        "ssh_edplan": SSHConfigurableResource(
            remote_host="secureftp.easyiep.com",
            username=EnvVar("KIPPNEWARK_EDPLAN_SFTP_USERNAME"),
            password=EnvVar("KIPPNEWARK_EDPLAN_SFTP_PASSWORD"),
        ),
        "ssh_egencia": SSHConfigurableResource(
            remote_host="eusftp.egencia.com",
            username=EnvVar("EGENCIA_SFTP_USERNAME"),
            key_file="/etc/secret-volume/id_rsa_egencia",
        ),
        "ssh_illuminate": SSHConfigurableResource(
            remote_host="sftp.illuminateed.com",
            username=EnvVar("ILLUMINATE_SFTP_USERNAME"),
            password=EnvVar("ILLUMINATE_SFTP_PASSWORD"),
        ),
        "ssh_iready": SSHConfigurableResource(
            remote_host="prod-sftp-1.aws.cainc.com",
            username=EnvVar("IREADY_SFTP_USERNAME"),
            password=EnvVar("IREADY_SFTP_PASSWORD"),
        ),
        "ssh_kipptaf": SSHConfigurableResource(
            remote_host="sftp.kippnj.org",
            username=EnvVar("KTAF_SFTP_USERNAME"),
            password=EnvVar("KTAF_SFTP_PASSWORD"),
        ),
        "ssh_idauto": SSHConfigurableResource(
            remote_host="sftp.kippnj.org",
            username=EnvVar("KTAF_SFTP_USERNAME"),
            password=EnvVar("KTAF_SFTP_PASSWORD"),
        ),
        "ssh_littlesis": SSHConfigurableResource(
            remote_host="upload.littlesis.app",
            username=EnvVar("LITTLESIS_SFTP_USERNAME"),
            password=EnvVar("LITTLESIS_SFTP_PASSWORD"),
        ),
        "ssh_powerschool": SSHConfigurableResource(
            remote_host="psteam.kippnj.org",
            remote_port=EnvVar("STAGING_PS_SSH_PORT"),
            username=EnvVar("STAGING_PS_SSH_USERNAME"),
            password=EnvVar("STAGING_PS_SSH_PASSWORD"),
            tunnel_remote_host=EnvVar("STAGING_PS_SSH_REMOTE_BIND_HOST"),
        ),
        "ssh_razkids": SSHConfigurableResource(
            remote_host="sftp.learninga-z.com",
            remote_port="22224",
            username=EnvVar("RAZKIDS_SFTP_USERNAME"),
            password=EnvVar("RAZKIDS_SFTP_PASSWORD"),
        ),
        "ssh_read180": SSHConfigurableResource(
            remote_host="imports.education.scholastic.com",
            username=EnvVar("READ180_SFTP_USERNAME"),
            password=EnvVar("READ180_SFTP_PASSWORD"),
        ),
        "ssh_renlearn": SSHConfigurableResource(
            remote_host="sftp.renaissance.com",
            username=EnvVar("KIPPNJ_RENLEARN_SFTP_USERNAME"),
            password=EnvVar("KIPPNJ_RENLEARN_SFTP_PASSWORD"),
        ),
        "ssh_titan": SSHConfigurableResource(
            remote_host="sftp.titank12.com",
            username=EnvVar("KIPPNEWARK_TITAN_SFTP_USERNAME"),
            password=EnvVar("KIPPNEWARK_TITAN_SFTP_PASSWORD"),
        ),
    },
)
