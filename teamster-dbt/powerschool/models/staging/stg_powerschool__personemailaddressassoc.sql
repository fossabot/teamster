{{
    teamster_utils.generate_staging_model(
        unique_key="personemailaddressassocid.int_value",
        transform_cols=[
            {"name": "personemailaddressassocid", "extract": "int_value"},
            {"name": "personid", "extract": "int_value"},
            {"name": "emailaddressid", "extract": "int_value"},
            {"name": "emailtypecodesetid", "extract": "int_value"},
            {"name": "isprimaryemailaddress", "extract": "int_value"},
            {"name": "emailaddresspriorityorder", "extract": "int_value"},
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
