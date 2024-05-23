import random

from dagster import (
    AssetsDefinition,
    DynamicPartitionsDefinition,
    instance_for_test,
    materialize,
)

from teamster.core.resources import get_io_manager_gcs_avro
from teamster.kipptaf.adp.workforce_manager.assets import (
    accrual_reporting_period_summary,
    time_details,
)
from teamster.kipptaf.resources import ADP_WORKFORCE_MANAGER_RESOURCE


def _test_asset(asset: AssetsDefinition):
    date_partitions_def = asset.partitions_def.get_partitions_def_for_dimension("date")  # pyright: ignore[reportAttributeAccessIssue, reportOptionalMemberAccess]

    with instance_for_test() as instance:
        if isinstance(date_partitions_def, DynamicPartitionsDefinition):
            instance.add_dynamic_partitions(
                partitions_def_name=date_partitions_def.name,  # pyright: ignore[reportArgumentType]
                partition_keys=["foo"],
            )

            partition_keys = asset.partitions_def.get_partition_keys(  # pyright: ignore[reportOptionalMemberAccess]
                dynamic_partitions_store=instance
            )
        else:
            partition_keys = asset.partitions_def.get_partition_keys()  # pyright: ignore[reportOptionalMemberAccess]

        result = materialize(
            assets=[asset],
            instance=instance,
            partition_key=partition_keys[
                random.randint(a=0, b=(len(partition_keys) - 1))
            ],
            resources={
                "io_manager_gcs_avro": get_io_manager_gcs_avro("staging"),
                "adp_wfm": ADP_WORKFORCE_MANAGER_RESOURCE,
            },
        )

    assert result.success
    assert (
        result.get_asset_materialization_events()[0]
        .event_specific_data.materialization.metadata["records"]  # pyright: ignore[reportOperatorIssue, reportAttributeAccessIssue, reportOptionalMemberAccess]
        .value
        > 0
    )
    assert result.get_asset_check_evaluations()[0].metadata.get("extras").text == ""  # pyright: ignore[reportOptionalMemberAccess]


def test_asset_adp_workforce_manager_accrual_reporting_period_summary():
    _test_asset(accrual_reporting_period_summary)


def test_asset_adp_workforce_manager_time_details():
    _test_asset(time_details)
