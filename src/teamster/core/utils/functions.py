import re

import pendulum
from dagster import (
    AssetCheckResult,
    AssetCheckSeverity,
    AssetCheckSpec,
    MetadataValue,
    MultiPartitionKey,
)

from teamster.core.utils.classes import FiscalYear


def regex_pattern_replace(pattern: str, replacements: dict):
    for group in re.findall(r"\(\?P<\w+>[\w\[\]\+\-\\]*\)", pattern):
        group_key = re.search(r"(?<=<)(\w+)(?=>)", group).group()

        group_value = replacements.get(group_key, "")

        pattern = pattern.replace(group, group_value)

    return pattern


def parse_partition_key(partition_key, dimension=None):
    try:
        date_formats = iter(
            [
                "YYYY-MM-DDTHH:mm:ss.SSSSSSZ",
                "YYYY-MM-DDTHH:mm:ssZ",
                "YYYY-MM-DDTHH:mm:ss.SSSSSS[Z]",
                "YYYY-MM-DDTHH:mm:ss[Z]",
                "YYYY-MM-DD",
            ]
        )

        while True:
            try:
                partition_key_parsed = pendulum.from_format(
                    string=partition_key, fmt=next(date_formats)
                )

                # save resync file with current timestamp
                if partition_key_parsed == pendulum.from_timestamp(0):
                    partition_key_parsed = pendulum.now()

                break
            except ValueError:
                partition_key_parsed = None

        pk_fiscal_year = FiscalYear(datetime=partition_key_parsed, start_month=7)

        return [
            f"_dagster_partition_fiscal_year={pk_fiscal_year.fiscal_year}",
            f"_dagster_partition_date={partition_key_parsed.to_date_string()}",
            f"_dagster_partition_hour={partition_key_parsed.format('HH')}",
            f"_dagster_partition_minute={partition_key_parsed.format('mm')}",
        ]
    except StopIteration:
        if dimension is not None:
            return [f"_dagster_partition_{dimension}={partition_key}"]
        else:
            return [f"_dagster_partition_key={partition_key}"]


def get_partition_key_path(partition_key, path):
    if isinstance(partition_key, MultiPartitionKey):
        for dimension, key in partition_key.keys_by_dimension.items():
            path.extend(parse_partition_key(partition_key=key, dimension=dimension))
    else:
        path.extend(parse_partition_key(partition_key=partition_key))

    path.append("data")

    return path


def partition_key_to_vars(partition_key):
    path = get_partition_key_path(partition_key=partition_key, path=[])
    return {"partition_path": "/".join(path)}


def get_avro_schema_valid_check_spec(asset):
    return AssetCheckSpec(
        name="avro_schema_valid",
        asset=asset,
        description=(
            "Checks output records against the supplied schema and warns if any "
            "unexpected fields are discovered"
        ),
    )


def check_avro_schema_valid(asset_key, records, schema):
    extras = set().union(*(d.keys() for d in records)) - set(
        field["name"] for field in schema["fields"]
    )

    return AssetCheckResult(
        passed=len(extras) == 0,
        asset_key=asset_key,
        check_name="avro_schema_valid",
        metadata={"extras": MetadataValue.text(", ".join(extras))},
        severity=AssetCheckSeverity.WARN,
    )
