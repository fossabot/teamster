import pendulum
from dagster import (
    DailyPartitionsDefinition,
    MultiPartitionsDefinition,
    StaticPartitionsDefinition,
    config_from_files,
)

from teamster.core.deanslist.assets import build_deanslist_endpoint_asset
from teamster.core.utils.variables import LOCAL_TIME_ZONE

from .. import CODE_LOCATION

school_ids = config_from_files(
    [f"src/teamster/{CODE_LOCATION}/deanslist/config/school_ids.yaml"]
)["school_ids"]

static_partitions_def = StaticPartitionsDefinition(school_ids)

multi_partitions_def = MultiPartitionsDefinition(
    partitions_defs={
        "date": DailyPartitionsDefinition(
            start_date="2023-03-06", timezone=LOCAL_TIME_ZONE.name, end_offset=1
        ),
        "school": static_partitions_def,
    }
)

static_partition_assets = [
    build_deanslist_endpoint_asset(
        code_location=CODE_LOCATION,
        partitions_def=static_partitions_def,
        **endpoint,
    )
    for endpoint in config_from_files(
        [f"src/teamster/{CODE_LOCATION}/deanslist/config/static-partition-assets.yaml"]
    )["endpoints"]
]

multi_partition_assets = [
    build_deanslist_endpoint_asset(
        code_location=CODE_LOCATION,
        partitions_def=multi_partitions_def,
        inception_date=pendulum.date(2016, 7, 1),
        **endpoint,
    )
    for endpoint in config_from_files(
        [f"src/teamster/{CODE_LOCATION}/deanslist/config/multi-partition-assets.yaml"]
    )["endpoints"]
]

__all__ = [
    *static_partition_assets,
    *multi_partition_assets,
]
