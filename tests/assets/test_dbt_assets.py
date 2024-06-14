import json
import pathlib

from dagster import (
    AssetExecutionContext,
    AssetMaterialization,
    DagsterInstance,
    materialize,
)
from dagster_dbt import DbtCliResource, dbt_assets

from teamster.libraries.core.resources import get_dbt_cli_resource
from teamster.libraries.dbt.dagster_dbt_translator import CustomDagsterDbtTranslator

MANIFEST = json.loads(
    s=pathlib.Path("src/dbt/kipptaf/target/manifest.json").read_text()
)

MANIFEST_NODES = MANIFEST["nodes"]

DAGSTER_DBT_TRANSLATOR = CustomDagsterDbtTranslator(
    asset_key_prefix="kipptaf", source_asset_key_prefix="kipptaf"
)


@dbt_assets(
    manifest=MANIFEST,
    exclude="tag:stage_external_sources",
    dagster_dbt_translator=DAGSTER_DBT_TRANSLATOR,
)
def _test_dbt_assets(context: AssetExecutionContext, dbt_cli: DbtCliResource):
    asset_materialization_keys = []

    latest_code_versions = context.instance.get_latest_materialization_code_versions(
        asset_keys=list(context.selected_asset_keys)
    )

    new_code_version_asset_keys = [
        asset_key
        for asset_key, current_code_version in context.assets_def.code_versions_by_key.items()
        if current_code_version != latest_code_versions.get(asset_key)
    ]

    new_code_version_node_names = set()
    for a in new_code_version_asset_keys:
        new_code_version_node_names.add(f"model.{a.path[0]}.{a.path[-1]}")

    for output_name in context.selected_output_names:
        node = [
            v for k, v in MANIFEST_NODES.items() if k.replace(".", "_") == output_name
        ][0]

        node_asset_key = DAGSTER_DBT_TRANSLATOR.get_asset_key(node)

        if node["config"]["materialized"] != "view":
            pass
        elif node_asset_key in new_code_version_asset_keys:
            pass
        elif set(node["depends_on"]["nodes"]) in new_code_version_node_names:
            pass
        else:
            # trunk-ignore(pyright/reportAttributeAccessIssue)
            context.selected_asset_keys.remove(node_asset_key)

    if context.selected_asset_keys:
        dbt_parse = dbt_cli.cli(args=["compile"], context=context)

        yield from dbt_parse.stream()
    else:
        for asset_key in asset_materialization_keys:
            yield AssetMaterialization(asset_key=asset_key)


def test_dbt_assets():
    from teamster.code_locations.kipptaf.dbt.assets import dbt_assets

    result = materialize(
        assets=[dbt_assets],
        resources={"dbt_cli": get_dbt_cli_resource(code_location="kipptaf", test=True)},
        instance=DagsterInstance.from_config(
            config_dir=".dagster/home", config_filename="dagster-cloud.yaml"
        ),
        selection=[
            "kipptaf/extracts/rpt_deanslist__college_admission_tests",
            "kipptaf/extracts/rpt_deanslist__student_misc",
            "kipptaf/extracts/rpt_gsheets__kfwd_flc",
            "kipptaf/extracts/rpt_gsheets__kfwd_rem_roster",
            "kipptaf/extracts/rpt_gsheets__kfwd_taf_contact_feed",
            "kipptaf/extracts/rpt_gsheets__kippfwd_collab_matriculation",
            "kipptaf/extracts/rpt_gsheets__kippfwd_collab_roster",
            "kipptaf/extracts/rpt_gsheets__kippfwd_contacts",
            "kipptaf/extracts/rpt_gsheets__njsmart_transfer_unverified",
            "kipptaf/extracts/rpt_powerschool__autocomm_students",
            "kipptaf/kippadb/base_kippadb__application",
            "kipptaf/kippadb/base_kippadb__contact",
            "kipptaf/kippadb/int_kippadb__contact_note_rollup",
            "kipptaf/kippadb/int_kippadb__enrollment_pivot",
            "kipptaf/kippadb/int_kippadb__persistence",
            "kipptaf/kippadb/int_kippadb__roster",
            "kipptaf/kippadb/int_kippadb__standardized_test_unpivot",
            "kipptaf/kippadb/qa_kippadb__duplicate_enrollments",
            "kipptaf/kippadb/stg_kippadb__account",
            "kipptaf/kippadb/stg_kippadb__contact_note",
            "kipptaf/kippadb/stg_kippadb__contact",
            "kipptaf/kippadb/stg_kippadb__employment",
            "kipptaf/kippadb/stg_kippadb__gpa",
            "kipptaf/kippadb/stg_kippadb__record_type",
            "kipptaf/kippadb/stg_kippadb__standardized_test",
            "kipptaf/kippadb/stg_kippadb__subsequent_financial_aid_award",
            "kipptaf/kippadb/stg_kippadb__term",
            "kipptaf/kippadb/stg_kippadb__user",
            "kipptaf/students/int_students__graduation_path_codes",
            "kipptaf/tableau/rpt_tableau__ap_assessment_dashboard",
            "kipptaf/tableau/rpt_tableau__college_assessment_dashboard_historic",
            "kipptaf/tableau/rpt_tableau__college_assessment_dashboard",
            "kipptaf/tableau/rpt_tableau__gpa_analysis",
            "kipptaf/tableau/rpt_tableau__graduation_requirements",
            "kipptaf/tableau/rpt_tableau__kfwd_contact_notes",
            "kipptaf/tableau/rpt_tableau__kfwd_dashboard",
            "kipptaf/tableau/rpt_tableau__kfwd_persistence",
            "kipptaf/tableau/rpt_tableau__kfwd_spi",
            "kipptaf/tableau/rpt_tableau__kfwd_verification",
            "kipptaf/zendesk/int_zendesk__ticket_metrics_union",
            "kipptaf/zendesk/stg_zendesk__ticket_audits__events",
            "kipptaf/zendesk/stg_zendesk__ticket_metrics_archive",
            "kipptaf/zendesk/stg_zendesk__ticket_metrics",
        ],
    )

    assert result.success


def test_external_source_dbt_assets():
    from teamster.code_locations.kipptaf.dbt.assets import external_source_dbt_assets

    result = materialize(
        assets=[external_source_dbt_assets],
        resources={"dbt_cli": get_dbt_cli_resource(code_location="kipptaf", test=True)},
        selection=["kipptaf/google_forms/src_google_forms__form"],
    )

    assert result.success
