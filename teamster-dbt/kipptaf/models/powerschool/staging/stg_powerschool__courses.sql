{{
    dbt_utils.union_relations(
        relations=[
            source("kippnewark_powerschool", "stg_powerschool__courses"),
            source("kippcamden_powerschool", "stg_powerschool__courses"),
            source("kippmiami_powerschool", "stg_powerschool__courses"),
        ]
    )
}}
