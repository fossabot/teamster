{{
    dbt_utils.union_relations(
        relations=[
            source("kippnewark_powerschool", "stg_powerschool__phonenumber"),
            source("kippcamden_powerschool", "stg_powerschool__phonenumber"),
            source("kippmiami_powerschool", "stg_powerschool__phonenumber"),
        ]
    )
}}
