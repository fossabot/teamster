{{
    teamster_utils.transform_cols_base_model(
        transform_cols=[
            {"name": "phonenumberid", "extract": "int_value"},
            {"name": "issms", "extract": "int_value"},
        ],
        except_cols=[
            "_dagster_partition_fiscal_year",
            "_dagster_partition_date",
            "_dagster_partition_hour",
            "_dagster_partition_minute",
        ],
    )
}}

{# {{
    teamster_utils.incremental_merge_source_file(
        file_uri=teamster_utils.get_gcs_uri(partition_path=var("partition_path")),
        unique_key="phonenumberid",
        transform_cols=[
            {"name": "phonenumberid", "extract": "int_value"},
            {"name": "issms", "extract": "int_value"},
        ],
        except_cols=[
            "_dagster_partition_fiscal_year",
            "_dagster_partition_date",
            "_dagster_partition_hour",
            "_dagster_partition_minute",
        ],
    )
}} #}

