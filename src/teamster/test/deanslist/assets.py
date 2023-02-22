from dagster import DailyPartitionsDefinition, config_from_files

from teamster.core.deanslist.assets import build_deanslist_endpoint_asset
from teamster.core.utils.variables import LOCAL_TIME_ZONE
from teamster.test import CODE_LOCATION

daily_partitions_def = DailyPartitionsDefinition(
    start_date="2023-02-01", timezone=LOCAL_TIME_ZONE.name
)

school_ids = config_from_files(
    [f"src/teamster/{CODE_LOCATION}/deanslist/config/school_ids.yaml"]
)["school_ids"]

nonpartition_assets = [
    build_deanslist_endpoint_asset(
        code_location=CODE_LOCATION, school_ids=school_ids, **endpoint
    )
    for endpoint in config_from_files(
        [f"src/teamster/{CODE_LOCATION}/deanslist/config/nonpartition-assets.yaml"]
    )["endpoints"]
]

partition_assets = [
    build_deanslist_endpoint_asset(
        code_location=CODE_LOCATION, school_ids=school_ids, **endpoint
    )
    for endpoint in config_from_files(
        [f"src/teamster/{CODE_LOCATION}/deanslist/config/partition-assets.yaml"]
    )["endpoints"]
]
