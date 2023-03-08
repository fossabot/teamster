from teamster.core.dbt.assets import build_external_source_asset, build_staging_assets

from .. import CODE_LOCATION, deanslist, powerschool

dbt_src_assets = [
    build_external_source_asset(a)
    for a in [*powerschool.db.assets.__all__, *deanslist.assets.__all__]
]

dbt_stg_assets = build_staging_assets(
    manifest_json_path=f"teamster-dbt/{CODE_LOCATION}/target/manifest.json",
    key_prefix=[CODE_LOCATION, "dbt"],
    assets=[*powerschool.db.assets.__all__, *deanslist.assets.__all__],
)

__all__ = [
    *dbt_src_assets,
    *dbt_stg_assets,
]
