{{
    dbt_utils.union_relations(
        relations=[
            source(
                "kippnewark_powerschool", "stg_powerschool__personemailaddressassoc"
            ),
            source(
                "kippcamden_powerschool", "stg_powerschool__personemailaddressassoc"
            ),
            source(
                "kippmiami_powerschool", "stg_powerschool__personemailaddressassoc"
            ),
        ]
    )
}}