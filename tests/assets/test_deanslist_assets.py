import random

from dagster import materialize

from teamster.core.resources import DEANSLIST_RESOURCE, get_io_manager_gcs_avro


def _test_asset(assets, asset_name, partition_key: str | None = None):
    asset = [a for a in assets if a.key.path[-1] == asset_name][0]

    if partition_key is None:
        partition_keys = asset.partitions_def.get_partition_keys()

        partition_key = partition_keys[random.randint(a=0, b=(len(partition_keys) - 1))]

    result = materialize(
        assets=[asset],
        partition_key=partition_key,
        resources={
            "io_manager_gcs_avro": get_io_manager_gcs_avro("staging"),
            "deanslist": DEANSLIST_RESOURCE,
        },
    )

    assert result.success
    assert (
        result.get_asset_materialization_events()[0]
        .event_specific_data.materialization.metadata["records"]  # type: ignore
        .value
        > 0
    )
    assert result.get_asset_check_evaluations()[0].metadata.get("extras").text == ""


def test_asset_deanslist_lists_kippnewark():
    from teamster.kippnewark.deanslist.assets import static_partition_assets

    _test_asset(assets=static_partition_assets, asset_name="lists")


def test_asset_deanslist_terms_kippnewark():
    from teamster.kippnewark.deanslist.assets import static_partition_assets

    _test_asset(assets=static_partition_assets, asset_name="terms")


def test_asset_deanslist_roster_assignments_kippnewark():
    from teamster.kippnewark.deanslist.assets import static_partition_assets

    _test_asset(assets=static_partition_assets, asset_name="roster_assignments")


def test_asset_deanslist_users_kippnewark():
    from teamster.kippnewark.deanslist.assets import static_partition_assets

    _test_asset(assets=static_partition_assets, asset_name="users")


def test_asset_deanslist_rosters_kippnewark():
    from teamster.kippnewark.deanslist.assets import static_partition_assets

    _test_asset(assets=static_partition_assets, asset_name="rosters")


def test_asset_deanslist_students_kippnewark():
    from teamster.kippnewark.deanslist.assets import static_partition_assets

    _test_asset(assets=static_partition_assets, asset_name="students")


def test_asset_deanslist_behavior_kippnewark():
    from teamster.kippnewark.deanslist.assets import multi_partition_monthly_assets

    _test_asset(assets=multi_partition_monthly_assets, asset_name="behavior")


def test_asset_deanslist_homework_kippnewark():
    from teamster.kippnewark.deanslist.assets import multi_partition_monthly_assets

    _test_asset(assets=multi_partition_monthly_assets, asset_name="homework")


def test_asset_deanslist_incidents_kippnewark():
    from teamster.kippnewark.deanslist.assets import multi_partition_monthly_assets

    _test_asset(assets=multi_partition_monthly_assets, asset_name="incidents")


def test_asset_deanslist_comm_log_kippnewark():
    from teamster.kippnewark.deanslist.assets import multi_partition_fiscal_assets

    _test_asset(assets=multi_partition_fiscal_assets, asset_name="comm_log")


def test_asset_deanslist_followups_kippnewark():
    from teamster.kippnewark.deanslist.assets import multi_partition_fiscal_assets

    _test_asset(assets=multi_partition_fiscal_assets, asset_name="followups")


def test_asset_deanslist_lists_kippcamden():
    from teamster.kippnewark.deanslist.assets import static_partition_assets

    _test_asset(assets=static_partition_assets, asset_name="lists")


def test_asset_deanslist_terms_kippcamden():
    from teamster.kippcamden.deanslist.assets import static_partition_assets

    _test_asset(assets=static_partition_assets, asset_name="terms")


def test_asset_deanslist_roster_assignments_kippcamden():
    from teamster.kippcamden.deanslist.assets import static_partition_assets

    _test_asset(assets=static_partition_assets, asset_name="roster_assignments")


def test_asset_deanslist_users_kippcamden():
    from teamster.kippcamden.deanslist.assets import static_partition_assets

    _test_asset(assets=static_partition_assets, asset_name="users")


def test_asset_deanslist_rosters_kippcamden():
    from teamster.kippcamden.deanslist.assets import static_partition_assets

    _test_asset(assets=static_partition_assets, asset_name="rosters")


def test_asset_deanslist_students_kippcamden():
    from teamster.kippcamden.deanslist.assets import static_partition_assets

    _test_asset(assets=static_partition_assets, asset_name="students")


def test_asset_deanslist_behavior_kippcamden():
    from teamster.kippcamden.deanslist.assets import multi_partition_monthly_assets

    _test_asset(assets=multi_partition_monthly_assets, asset_name="behavior")


def test_asset_deanslist_homework_kippcamden():
    from teamster.kippcamden.deanslist.assets import multi_partition_monthly_assets

    _test_asset(assets=multi_partition_monthly_assets, asset_name="homework")


def test_asset_deanslist_incidents_kippcamden():
    from teamster.kippcamden.deanslist.assets import multi_partition_monthly_assets

    _test_asset(assets=multi_partition_monthly_assets, asset_name="incidents")


def test_asset_deanslist_comm_log_kippcamden():
    from teamster.kippcamden.deanslist.assets import multi_partition_fiscal_assets

    _test_asset(assets=multi_partition_fiscal_assets, asset_name="comm_log")


def test_asset_deanslist_followups_kippcamden():
    from teamster.kippcamden.deanslist.assets import multi_partition_fiscal_assets

    _test_asset(assets=multi_partition_fiscal_assets, asset_name="followups")


def test_asset_deanslist_lists_kippmiami():
    from teamster.kippmiami.deanslist.assets import static_partition_assets

    _test_asset(assets=static_partition_assets, asset_name="lists")


def test_asset_deanslist_terms_kippmiami():
    from teamster.kippmiami.deanslist.assets import static_partition_assets

    _test_asset(assets=static_partition_assets, asset_name="terms")


def test_asset_deanslist_roster_assignments_kippmiami():
    from teamster.kippmiami.deanslist.assets import static_partition_assets

    _test_asset(assets=static_partition_assets, asset_name="roster_assignments")


def test_asset_deanslist_users_kippmiami():
    from teamster.kippmiami.deanslist.assets import static_partition_assets

    _test_asset(assets=static_partition_assets, asset_name="users")


def test_asset_deanslist_rosters_kippmiami():
    from teamster.kippmiami.deanslist.assets import static_partition_assets

    _test_asset(assets=static_partition_assets, asset_name="rosters")


def test_asset_deanslist_students_kippmiami():
    from teamster.kippmiami.deanslist.assets import static_partition_assets

    _test_asset(assets=static_partition_assets, asset_name="students")


def test_asset_deanslist_behavior_kippmiami():
    from teamster.kippmiami.deanslist.assets import multi_partition_monthly_assets

    _test_asset(assets=multi_partition_monthly_assets, asset_name="behavior")


def test_asset_deanslist_homework_kippmiami():
    from teamster.kippmiami.deanslist.assets import multi_partition_monthly_assets

    _test_asset(assets=multi_partition_monthly_assets, asset_name="homework")


def test_asset_deanslist_incidents_kippmiami():
    from teamster.kippmiami.deanslist.assets import multi_partition_monthly_assets

    _test_asset(assets=multi_partition_monthly_assets, asset_name="incidents")


def test_asset_deanslist_comm_log_kippmiami():
    from teamster.kippmiami.deanslist.assets import multi_partition_fiscal_assets

    _test_asset(assets=multi_partition_fiscal_assets, asset_name="comm_log")


def test_asset_deanslist_followups_kippmiami():
    from teamster.kippmiami.deanslist.assets import multi_partition_fiscal_assets

    _test_asset(assets=multi_partition_fiscal_assets, asset_name="followups")
