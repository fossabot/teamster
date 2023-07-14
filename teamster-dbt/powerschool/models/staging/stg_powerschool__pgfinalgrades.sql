{{
    teamster_utils.generate_staging_model(
        unique_key="dcid.int_value",
        transform_cols=[
            {"name": "dcid", "extract": "int_value"},
            {"name": "id", "extract": "int_value"},
            {"name": "sectionid", "extract": "int_value"},
            {"name": "studentid", "extract": "int_value"},
            {"name": "percent", "extract": "double_value"},
            {"name": "points", "extract": "double_value"},
            {"name": "pointspossible", "extract": "double_value"},
            {"name": "varcredit", "extract": "double_value"},
            {"name": "gradebooktype", "extract": "int_value"},
            {"name": "calculatedpercent", "extract": "double_value"},
            {"name": "isincomplete", "extract": "int_value"},
            {"name": "isexempt", "extract": "int_value"},
            {"name": "whomodifiedid", "extract": "int_value"},
        ],
        except_cols=[
            "_dagster_partition_fiscal_year",
            "_dagster_partition_date",
            "_dagster_partition_hour",
            "_dagster_partition_minute",
        ],
    )
}}

select *
from staging
