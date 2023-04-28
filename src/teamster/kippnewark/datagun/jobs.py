from dagster import AssetSelection, define_asset_job

from .assets import nps_extract_assets, powerschool_extract_assets

nps_extract_asset_job = define_asset_job(
    name="datagun_nps_extract_asset_job",
    selection=AssetSelection.assets(*nps_extract_assets),
)

powerschool_extract_asset_job = define_asset_job(
    name="datagun_powerschool_extract_asset_job",
    selection=AssetSelection.assets(*powerschool_extract_assets),
)

__all__ = [
    nps_extract_asset_job,
    powerschool_extract_asset_job,
]
