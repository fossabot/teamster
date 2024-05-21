from dagster import define_asset_job

from teamster.kipptaf.amplify.assets import assets

mclass_asset_job = define_asset_job(name="mclass_asset_job", selection=assets)

jobs = [
    mclass_asset_job,
]
