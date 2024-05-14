import pathlib

from dagster import (
    MultiPartitionsDefinition,
    StaticPartitionsDefinition,
    config_from_files,
)

from teamster.core.pearson.schema import ASSET_SCHEMA
from teamster.core.sftp.assets import build_sftp_asset
from teamster.kippnewark import CODE_LOCATION

config_dir = pathlib.Path(__file__).parent / "config"

njgpa = build_sftp_asset(
    asset_key=[CODE_LOCATION, "pearson", "njgpa"],
    remote_dir="/data-team/kippnewark/pearson/njgpa",
    remote_file_regex="pc(?P<administration>[a-z])(?P<fiscal_year>\d+)_NJ-\d+_\w+GPA\w+\.csv",
    avro_schema=ASSET_SCHEMA["njgpa"],
    ssh_resource_key="ssh_couchdrop",
    partitions_def=MultiPartitionsDefinition(
        {
            "fiscal_year": StaticPartitionsDefinition(["22", "23"]),
            "administration": StaticPartitionsDefinition(["spr", "fbk"]),
        }
    ),
)

static_partition_assets = [
    build_sftp_asset(
        asset_key=[CODE_LOCATION, "pearson", a["asset_name"]],
        avro_schema=ASSET_SCHEMA[a["asset_name"]],
        ssh_resource_key="ssh_couchdrop",
        partitions_def=StaticPartitionsDefinition(a["partition_keys"]),
        **a,
    )
    for a in config_from_files([f"{config_dir}/assets.yaml"])["assets"]
]

assets = [
    njgpa,
    *static_partition_assets,
]
