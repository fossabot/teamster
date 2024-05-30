import random

from dagster import materialize

from teamster.core.resources import get_io_manager_gcs_avro
from teamster.kipptaf.resources import TABLEAU_SERVER_RESOURCE
from teamster.kipptaf.tableau.assets import workbook


def test_workbook():
    partition_keys = workbook.partitions_def.get_partition_keys()  # pyright: ignore[reportOptionalMemberAccess]

    partition_key = partition_keys[random.randint(a=0, b=(len(partition_keys) - 1))]

    result = materialize(
        assets=[workbook],
        resources={
            "io_manager_gcs_avro": get_io_manager_gcs_avro(
                code_location="test", test=True
            ),
            "tableau": TABLEAU_SERVER_RESOURCE,
        },
        partition_key=partition_key,
    )

    assert result.success
    assert (
        result.get_asset_materialization_events()[0]
        .event_specific_data.materialization.metadata["records"]  # pyright: ignore[reportOperatorIssue, reportAttributeAccessIssue, reportOptionalMemberAccess]
        .value
        > 0
    )
    assert result.get_asset_check_evaluations()[0].metadata.get("extras").text == ""  # pyright: ignore[reportOptionalMemberAccess]
