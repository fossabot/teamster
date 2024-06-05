import json

from dagster import AssetExecutionContext, Output
from dagster_dbt import DagsterDbtTranslator, DbtCliResource, dbt_assets
from dagster_dbt.utils import dagster_name_fn

from teamster.core.dbt.asset_decorator import dbt_external_source_assets


def _dagster_name_fn(unique_id: str) -> str:
    return unique_id.replace(".", "_").replace("-", "_").replace("*", "_star")


def build_dbt_assets(
    manifest,
    dagster_dbt_translator,
    select="fqn:*",
    exclude=None,
    partitions_def=None,
    name=None,
    op_tags=None,
):
    @dbt_assets(
        manifest=manifest,
        select=select,
        exclude=exclude,
        name=name,
        partitions_def=partitions_def,
        dagster_dbt_translator=dagster_dbt_translator,
        op_tags=op_tags,
    )
    def _assets(context: AssetExecutionContext, dbt_cli: DbtCliResource):
        selected_views = set()
        selected_others = set()

        # selected_views_child_map = {
        #     _dagster_name_fn(unique_id): children
        #     for unique_id, children in manifest["child_map"].items()
        #     if _dagster_name_fn(unique_id) in context.selected_output_names
        # }

        selected_asset_keys = set()
        for unique_id_dagster_name in selected_views:
            selected_asset_keys.add(
                context.asset_key_for_output(unique_id_dagster_name)
            )

            # for child_unique_id in children:
            #     selected_asset_keys.add(
            #         context.asset_key_for_output(_dagster_name_fn(child_unique_id))
            #     )

        changed_code_versions = {
            k: v
            for k, v in context.instance.get_latest_materialization_code_versions(
                asset_keys=selected_asset_keys
            ).items()
            if k in context.assets_def.code_versions_by_key
            and context.assets_def.code_versions_by_key[k] != v
        }

        dbt_build = dbt_cli.cli(args=["build"], context=context)

        yield from dbt_build.stream()

    return _assets


def build_dbt_external_source_assets(
    manifest,
    dagster_dbt_translator: DagsterDbtTranslator,
    select="fqn:*",
    exclude=None,
    partitions_def=None,
    name=None,
    op_tags=None,
):
    sources = manifest["sources"].values()

    @dbt_external_source_assets(
        manifest=manifest,
        select=select,
        exclude=exclude,
        name=name,
        partitions_def=partitions_def,
        dagster_dbt_translator=dagster_dbt_translator,
        op_tags=op_tags,
    )
    def _assets(context: AssetExecutionContext, dbt_cli: DbtCliResource):
        selection = [
            f"{dbt_resource_props["source_name"]}.{dbt_resource_props["name"]}"
            for dbt_resource_props in sources
            if dagster_name_fn(dbt_resource_props) in context.selected_output_names
        ]

        # run dbt stage_external_sources
        dbt_run_operation = dbt_cli.cli(
            args=[
                "run-operation",
                "stage_external_sources",
                "--args",
                json.dumps({"select": " ".join(selection)}),
                "--vars",
                json.dumps({"ext_full_refresh": "true"}),
            ],
            manifest=manifest,
            dagster_dbt_translator=dagster_dbt_translator,
        )

        for event in dbt_run_operation.stream_raw_events():
            context.log.info(event)

        for output_name in context.selected_output_names:
            yield Output(value=None, output_name=output_name)

    return _assets
