from dagster import StaticPartitionsDefinition, config_from_files

from teamster.core.google.forms.assets import build_google_forms_assets
from teamster.core.google.sheets.assets import build_gsheet_asset

from .. import CODE_LOCATION

config_dir = f"src/teamster/{CODE_LOCATION}/google/config"

google_sheets_assets = [
    build_gsheet_asset(code_location=CODE_LOCATION, **asset)
    for asset in config_from_files([f"{config_dir}/assets.yaml"])["assets"]
]

google_forms_assets = build_google_forms_assets(
    code_location=CODE_LOCATION,
    partitions_def=StaticPartitionsDefinition(
        ["1jpeMof_oQ9NzTw85VFsA5A7G9VrH3XkSc_nZDFz07nA"]
    ),
)

__all__ = [
    *google_sheets_assets,
    *google_forms_assets,
]
