{{
    incremental_merge_source_file(
        source(var("code_location"), this.identifier | replace("stg", "src")),
        file_uri=get_gcs_uri(
            code_location=var("code_location"),
            system_name="powerschool",
            model_name=this.identifier | replace("stg_powerschool__", ""),
            partition_path=var("partition_path"),
        ),
        unique_key="gradeschoolconfigid",
        transform_cols=[
            {"name": "gradeschoolconfigid", "type": "int_value"},
            {"name": "schoolsdcid", "type": "int_value"},
            {"name": "yearid", "type": "int_value"},
            {"name": "defaultdecimalcount", "type": "int_value"},
            {"name": "iscalcformulaeditable", "type": "int_value"},
            {"name": "isdropscoreeditable", "type": "int_value"},
            {"name": "iscalcprecisioneditable", "type": "int_value"},
            {"name": "iscalcmetriceditable", "type": "int_value"},
            {"name": "isrecentscoreeditable", "type": "int_value"},
            {"name": "ishigherstndautocalc", "type": "int_value"},
            {"name": "ishigherstndcalceditable", "type": "int_value"},
            {"name": "ishighstandardeditable", "type": "int_value"},
            {"name": "iscalcmetricschooledit", "type": "int_value"},
            {"name": "isstandardsshown", "type": "int_value"},
            {"name": "isstandardsshownonasgmt", "type": "int_value"},
            {"name": "istraditionalgradeshown", "type": "int_value"},
            {"name": "iscitizenshipdisplayed", "type": "int_value"},
            {"name": "termbinlockoffset", "type": "int_value"},
            {"name": "lockwarningoffset", "type": "int_value"},
            {"name": "issectstndweighteditable", "type": "int_value"},
            {"name": "minimumassignmentvalue", "type": "int_value"},
            {"name": "isgradescaleteachereditable", "type": "int_value"},
            {"name": "isstandardslimited", "type": "int_value"},
            {"name": "isstandardslimitededitable", "type": "int_value"},
            {"name": "isusingpercentforstndautocalc", "type": "int_value"},
        ],
    )
}}
