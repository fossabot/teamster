from dagster import config_from_files

from teamster.core.iready.assets import build_sftp_asset

from .. import CODE_LOCATION

config_dir = f"src/teamster/{CODE_LOCATION}/config/assets/iready"

sftp_assets = [
    build_sftp_asset(code_location=CODE_LOCATION, source_system="iready", **a)
    for a in config_from_files([f"{config_dir}/assets.yaml"])["assets"]
]

__all__ = [
    *sftp_assets,
]
