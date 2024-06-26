with
    observation_rollup as (
        select employee_number, academic_year, avg(observation_score) as final_score,
        from {{ ref("int_performance_management__observations") }}
        where observation_type_abbreviation = 'PM' and term_code in ('PM2', 'PM3')
        group by employee_number, academic_year
    )

select
    *,

    case
        when final_score >= 3.495
        then 4
        when final_score >= 2.745
        then 3
        when final_score >= 1.745
        then 2
        when final_score < 1.75
        then 1
    end as final_tier,
from observation_rollup
