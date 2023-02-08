{%- set code_location = "kippcamden" -%}

{%- set source_name = model.fqn[1] -%}
{%- set model_name = this.identifier -%}

{{
    incremental_merge_source_file(
        source_name=source_name,
        model_name=model_name,
        file_uri=get_gcs_uri(
            code_location, source_name, model_name, var("partition_path")
        ),
        unique_key="",
        transform_cols=[
            {"name": "dcid", "type": "int_value"},
            {"name": "id", "type": "int_value"},
            {"name": "teacher", "type": "int_value"},
            {"name": "termid", "type": "int_value"},
            {"name": "no_of_students", "type": "int_value"},
            {"name": "schoolid", "type": "int_value"},
            {"name": "noofterms", "type": "int_value"},
            {"name": "trackteacheratt", "type": "int_value"},
            {"name": "maxenrollment", "type": "int_value"},
            {"name": "distuniqueid", "type": "int_value"},
            {"name": "wheretaught", "type": "int_value"},
            {"name": "rostermodser", "type": "int_value"},
            {"name": "pgversion", "type": "int_value"},
            {"name": "grade_level", "type": "int_value"},
            {"name": "campusid", "type": "int_value"},
            {"name": "exclude_ada", "type": "int_value"},
            {"name": "gradescaleid", "type": "int_value"},
            {"name": "excludefromgpa", "type": "int_value"},
            {"name": "buildid", "type": "int_value"},
            {"name": "schedulesectionid", "type": "int_value"},
            {"name": "wheretaughtdistrict", "type": "int_value"},
            {"name": "excludefromclassrank", "type": "int_value"},
            {"name": "excludefromhonorroll", "type": "int_value"},
            {"name": "parent_section_id", "type": "int_value"},
            {"name": "attendance_type_code", "type": "int_value"},
            {"name": "maxcut", "type": "int_value"},
            {"name": "exclude_state_rpt_yn", "type": "int_value"},
            {"name": "sortorder", "type": "int_value"},
            {"name": "programid", "type": "int_value"},
            {"name": "excludefromstoredgrades", "type": "int_value"},
            {"name": "gradebooktype", "type": "int_value"},
            {"name": "whomodifiedid", "type": "int_value"},
        ],
    )
}}
