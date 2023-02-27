from collections import namedtuple

import pendulum
from dagster import (
    AssetsDefinition,
    OpExecutionContext,
    Output,
    TimeWindowPartitionsDefinition,
    asset,
)

from teamster.core.deanslist.schema import get_avro_schema
from teamster.core.resources.deanslist import DeansList
from teamster.core.utils.classes import FiscalYear


def build_deanslist_endpoint_asset(
    asset_name,
    code_location,
    api_version,
    school_ids,
    partitions_def: TimeWindowPartitionsDefinition = None,
    op_tags={},
    params={},
) -> AssetsDefinition:
    @asset(
        name=asset_name,
        key_prefix=[code_location, "deanslist"],
        partitions_def=partitions_def,
        op_tags=op_tags,
        required_resource_keys={"deanslist"},
        io_manager_key="gcs_avro_io",
        output_required=False,
    )
    def _asset(context: OpExecutionContext):
        if partitions_def is not None:
            partition_key = pendulum.parser.parse(context.partition_key)

            if context.partition_time_window.start == partitions_def.start:
                FY = namedtuple("FiscalYear", ["start", "end"])
                start_date = pendulum.date(2022, 7, 1)
                fiscal_year = FY(start=start_date, end=partition_key)
                partition_key = start_date
            else:
                fiscal_year = FiscalYear(datetime=partition_key, start_month=7)

            for k, v in params.items():
                if isinstance(v, str):
                    params[k] = v.format(
                        start_date=fiscal_year.start.to_date_string(),
                        end_date=fiscal_year.end.to_date_string(),
                        modified_date=partition_key.to_date_string(),
                    )

        dl: DeansList = context.resources.deanslist

        total_row_count = 0
        all_data = []
        for school_id in school_ids:
            row_count, data = dl.get_endpoint(
                api_version=api_version,
                endpoint=asset_name,
                school_id=school_id,
                **params,
            )

            total_row_count += row_count
            all_data.extend(data)

        if total_row_count is not None:
            yield Output(
                value=(all_data, get_avro_schema(name=asset_name, version=api_version)),
                metadata={"records": total_row_count},
            )

    return _asset
