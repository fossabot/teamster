import json
from typing import Sequence

import pendulum
from dagster import AssetIn, AssetsDefinition, OpExecutionContext, Output, asset
from dagster_dbt import DbtCliResource, load_assets_from_dbt_manifest
from google.cloud import bigquery

from teamster.core.resources.google import parse_date_partition_key


def build_external_source_asset(asset_definition: AssetsDefinition):
    code_location, package_name, asset_name = asset_definition.key.path

    @asset(
        name=f"src_{package_name}__{asset_name}",
        key_prefix=[code_location, "dbt", package_name],
        ins={"upstream": AssetIn(key=[code_location, package_name, asset_name])},
        required_resource_keys={"warehouse_bq", "dbt"},
        compute_kind="dbt",
        # partitions_def=asset_definition.partitions_def,
        group_name="staging",
    )
    def _asset(context: OpExecutionContext, upstream):
        context.log.debug(upstream)

        dataset_name = f"{code_location}_{package_name}"

        # create BigQuery dataset, if not exists
        bq: bigquery.Client = context.resources.warehouse_bq
        context.log.info(f"Creating dataset {dataset_name}")
        bq.create_dataset(dataset=dataset_name, exists_ok=True)

        # dbt run-operation stage_external_sources
        dbt: DbtCliResource = context.resources.dbt

        dbt_output = dbt.run_operation(
            macro="stage_external_sources",
            args={"select": f"{package_name}.src_{package_name}__{asset_name}"},
            vars={"ext_full_refresh": True},
        )

        return Output(upstream, metadata=dbt_output.result)

    return _asset


def partition_key_to_vars(partition_key):
    path = parse_date_partition_key(pendulum.parse(text=partition_key))
    path.append("data")

    return {"partition_path": "/".join(path)}


def build_staging_assets(
    manifest_json_path,
    key_prefix,
    assets: Sequence[AssetsDefinition],
    partitions_def=None,
):
    with open(file=manifest_json_path) as f:
        manifest_json = json.load(f)

    _assets = [
        load_assets_from_dbt_manifest(
            manifest_json=manifest_json,
            select=f"stg_{a.key.path[-2]}__{a.key.path[-1]}+",
            key_prefix=key_prefix,
            source_key_prefix=key_prefix[:2],
            partitions_def=partitions_def,
            partition_key_to_vars_fn=(
                partition_key_to_vars if partitions_def is not None else None
            ),
        )
        for a in assets
    ]

    return [s for sublist in _assets for s in sublist]
