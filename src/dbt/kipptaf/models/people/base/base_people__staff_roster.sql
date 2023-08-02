{%- set ref_staff_history = ref("base_people__staff_roster_history") -%}

with
    staff_roster_active as (
        select
            {{
                dbt_utils.star(
                    from=ref_staff_history,
                    except=[
                        "work_assignment__fivetran_start",
                        "work_assignment__fivetran_end",
                        "work_assignment__fivetran_active",
                    ],
                )
            }},
        from {{ ref_staff_history }}
        where work_assignment__fivetran_active
    ),

    deduplicate as (
        {{
            dbt_utils.deduplicate(
                relation="staff_roster_active",
                partition_by="associate_oid",
                order_by="is_prestart desc, primary_indicator desc, assignment_status_effective_date desc",
            )
        }}
    )

select *
from deduplicate
