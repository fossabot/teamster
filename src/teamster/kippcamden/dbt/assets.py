import json
import pathlib

from teamster.core.dbt.assets import build_dbt_assets, build_dbt_external_source_assets
from teamster.core.dbt.dagster_dbt_translator import CustomDagsterDbtTranslator

from .. import CODE_LOCATION

manifest = json.loads(
    s=pathlib.Path(f"src/dbt/{CODE_LOCATION}/target/manifest.json").read_text()
)

dagster_dbt_translator = CustomDagsterDbtTranslator(
    asset_key_prefix=CODE_LOCATION, source_asset_key_prefix=CODE_LOCATION
)

dbt_assets = build_dbt_assets(
    manifest=manifest,
    dagster_dbt_translator=dagster_dbt_translator,
    exclude="tag:stage_external_sources",
)

dbt_external_source_assets = build_dbt_external_source_assets(
    code_location=CODE_LOCATION,
    manifest=manifest,
    dagster_dbt_translator=dagster_dbt_translator,
)

assets = [
    dbt_assets,
    dbt_external_source_assets,
]
