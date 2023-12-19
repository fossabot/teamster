import copy
import gc

import pendulum
from dagster import (
    AssetExecutionContext,
    AssetsDefinition,
    MultiPartitionsDefinition,
    Output,
    StaticPartitionsDefinition,
    asset,
)

from teamster.core.deanslist.resources import DeansListResource
from teamster.core.deanslist.schema import ASSET_FIELDS
from teamster.core.utils.classes import FiscalYear
from teamster.core.utils.functions import (
    check_avro_schema_valid,
    get_avro_record_schema,
    get_avro_schema_valid_check_spec,
)


def build_deanslist_static_partition_asset(
    code_location,
    asset_name,
    api_version,
    partitions_def: StaticPartitionsDefinition | None = None,
    op_tags={},
    params={},
) -> AssetsDefinition:
    asset_key = [code_location, "deanslist", asset_name.replace("-", "_")]

    @asset(
        key=asset_key,
        metadata=params,
        io_manager_key="io_manager_gcs_avro",
        partitions_def=partitions_def,
        op_tags=op_tags,
        group_name="deanslist",
        check_specs=[get_avro_schema_valid_check_spec(asset_key)],
    )
    def _asset(context: AssetExecutionContext, deanslist: DeansListResource):
        endpoint_content = deanslist.get(
            api_version=api_version,
            endpoint=asset_name,
            school_id=int(context.partition_key),
            params=params,
        )

        data = endpoint_content["data"]
        schema = get_avro_record_schema(
            name=asset_name, fields=ASSET_FIELDS[asset_name][api_version]
        )

        yield Output(
            value=(data, schema), metadata={"records": endpoint_content["row_count"]}
        )

        yield check_avro_schema_valid(
            asset_key=context.asset_key, records=data, schema=schema
        )

    return _asset


def build_deanslist_multi_partition_asset(
    code_location,
    asset_name,
    api_version,
    partitions_def: MultiPartitionsDefinition,
    op_tags={},
    params={},
) -> AssetsDefinition:
    asset_key = [code_location, "deanslist", asset_name.replace("-", "_")]

    @asset(
        key=asset_key,
        metadata=params,
        io_manager_key="io_manager_gcs_avro",
        partitions_def=partitions_def,
        op_tags=op_tags,
        group_name="deanslist",
        check_specs=[get_avro_schema_valid_check_spec(asset_key)],
    )
    def _asset(context: AssetExecutionContext, deanslist: DeansListResource):
        keys_by_dimension: dict = context.partition_key.keys_by_dimension  # type: ignore

        school_partition = keys_by_dimension["school"]
        date_partition = pendulum.from_format(
            string=keys_by_dimension["date"], fmt="YYYY-MM-DD"
        ).subtract(days=1)

        # determine if endpoint is within time-window
        if set(["StartDate", "EndDate"]).issubset(params.keys()) or set(
            ["sdt", "edt"]
        ).issubset(params.keys()):
            is_time_bound = True
        else:
            is_time_bound = False

        # TODO: date_partition == inception_date for first partition

        # determine start and end dates
        partition_fy = FiscalYear(datetime=date_partition, start_month=7)

        fy_period = partition_fy.end - partition_fy.start

        total_row_count = 0
        all_data = []
        for month in fy_period.range(unit="months"):  # type: ignore
            composed_params = copy.deepcopy(params)

            for k, v in composed_params.items():
                if isinstance(v, str):
                    composed_params[k] = v.format(
                        start_date=month.start_of("month").to_date_string(),
                        end_date=month.end_of("month").to_date_string(),
                    )

            endpoint_content = deanslist.get(
                api_version=api_version,
                endpoint=asset_name,
                school_id=int(school_partition),
                params={
                    "UpdatedSince": date_partition.to_date_string(),
                    **composed_params,
                },
            )

            row_count = endpoint_content["row_count"]
            data = endpoint_content["data"]

            del endpoint_content
            gc.collect()

            if row_count > 0:
                total_row_count += row_count
                all_data.extend(data)

                del data
                gc.collect()

            # break loop for endpoints w/o start/end dates
            if not is_time_bound:
                break

        schema = get_avro_record_schema(
            name=asset_name, fields=ASSET_FIELDS[asset_name][api_version]
        )

        yield Output(value=(all_data, schema), metadata={"records": total_row_count})

        yield check_avro_schema_valid(
            asset_key=context.asset_key, records=all_data, schema=schema
        )

    return _asset
