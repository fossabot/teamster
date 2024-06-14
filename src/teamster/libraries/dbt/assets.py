import json

from dagster import AssetExecutionContext, Output
from dagster_dbt import DbtCliResource, dbt_assets
from dagster_dbt.utils import dagster_name_fn

from teamster.libraries.dbt.asset_decorator import dbt_external_source_assets


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
        selected_views = {}
        selected_others = []
        code_version_change = []
        code_version_same = []

        for output_name in context.selected_output_names:
            node: dict = [
                {
                    "dagster_name": dagster_name_fn(dbt_resource_props),
                    **dbt_resource_props,
                }
                for dbt_resource_props in manifest["nodes"].values()
                if dagster_name_fn(dbt_resource_props) == output_name
            ][0]

            if node["config"]["materialized"] == "view":
                selected_views[context.asset_key_for_output(node["dagster_name"])] = (
                    node
                )
            else:
                selected_others.append(node)

        for (
            asset_key,
            code_version,
        ) in context.instance.get_latest_materialization_code_versions(
            asset_keys=selected_views.keys()
        ).items():
            if context.assets_def.code_versions_by_key[asset_key] != code_version:
                code_version_change.append(selected_views[asset_key])
            else:
                code_version_same.append(selected_views[asset_key])

        selection = [
            ".".join(node["fqn"]) for node in selected_others + code_version_change
        ]

        dbt_build = dbt_cli.cli(
            args=["build", "--select", " ".join(selection)],
            manifest=manifest,
            dagster_dbt_translator=dagster_dbt_translator,
        )

        for event in dbt_build.stream_raw_events():
            context.log.info(event)

        for output_name in context.selected_output_names:
            yield Output(value=None, output_name=output_name)

        # dagster._core.errors.DagsterInvariantViolationError: Asset "kipptaf/extracts/rpt_gsheets__kippfwd_collab_matriculation" was yielded before its dependency "kipptaf/kippadb/int_kippadb__roster".Multiassets yielding multiple asset outputs must yield them in topological order.

    return _assets


def build_dbt_external_source_assets(
    manifest,
    dagster_dbt_translator,
    select="fqn:*",
    exclude=None,
    partitions_def=None,
    name=None,
    op_tags=None,
):
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
            for dbt_resource_props in manifest["sources"].values()
            if dagster_name_fn(dbt_resource_props) in context.selected_output_names
        ]

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
