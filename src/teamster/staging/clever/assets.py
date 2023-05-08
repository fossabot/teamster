from dagster import config_from_files

from teamster.core.clever.assets import build_sftp_asset

from .. import CODE_LOCATION

config_dir = f"src/teamster/{CODE_LOCATION}/config/assets/clever"

sftp_assets = [
    build_sftp_asset(code_location=CODE_LOCATION, source_system="clever", **a)
    for a in config_from_files([f"{config_dir}/assets.yaml"])["assets"]
]

__all__ = [
    *sftp_assets,
]