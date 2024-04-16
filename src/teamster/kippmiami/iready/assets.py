import pathlib

from dagster import (
    MultiPartitionsDefinition,
    StaticPartitionsDefinition,
    config_from_files,
)

from teamster.core.iready.schema import ASSET_SCHEMA
from teamster.core.sftp.assets import build_sftp_asset

from .. import CODE_LOCATION

_all = [
    build_sftp_asset(
        asset_key=[CODE_LOCATION, "iready", a["asset_name"]],
        ssh_resource_key="ssh_iready",
        avro_schema=ASSET_SCHEMA[a["asset_name"]],
        partitions_def=MultiPartitionsDefinition(
            {
                "subject": StaticPartitionsDefinition(["ela", "math"]),
                "academic_year": StaticPartitionsDefinition(
                    a["partition_keys"]["academic_year"]
                ),
            }
        ),
        slugify_replacements=[["%", "percent"]],
        **a,
    )
    for a in config_from_files(
        [f"{pathlib.Path(__file__).parent}/config/assets.yaml"],
    )["assets"]
]
