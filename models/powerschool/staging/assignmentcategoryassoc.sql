{%- set code_location = "kippcamden" -%}

{%- set source_name = model.fqn[1] -%}
{%- set model_name = this.identifier -%}
{%- set file_uri = (
    "gs://teamster-"
    ~ code_location
    ~ "/dagster/"
    ~ code_location
    ~ "/"
    ~ source_name
    ~ "/"
    ~ model_name
    ~ "/"
    ~ var("partition")
) -%}

{{
    incremental_merge_source_file(
        source_name=source_name,
        model_name=model_name,
        file_uri=file_uri,
        unique_key="assignmentcategoryassocid",
        transform_cols=[
            {"name": "assignmentcategoryassocid", "type": "int_value"},
            {"name": "assignmentsectionid", "type": "int_value"},
            {"name": "teachercategoryid", "type": "int_value"},
            {"name": "yearid", "type": "int_value"},
            {"name": "isprimary", "type": "int_value"},
            {"name": "whomodifiedid", "type": "int_value"},
        ],
    )
}}
