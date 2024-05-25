import pathlib

from dagster import config_from_files, load_assets_from_current_module

from teamster.core.datagun.assets import build_bigquery_extract_asset
from teamster.kippcamden.config import CODE_LOCATION, LOCAL_TIMEZONE

powerschool_extract_assets = [
    build_bigquery_extract_asset(
        timezone=LOCAL_TIMEZONE, bucket_name=f"teamster-{CODE_LOCATION}", **a
    )
    for a in config_from_files(
        [f"{pathlib.Path(__file__).parent}/config/powerschool.yaml"]
    )["assets"]
]

assets = [
    *load_assets_from_current_module(key_prefix=CODE_LOCATION),
]
