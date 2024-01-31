with
    suspension_type as (
        select penalty_name, 'ISS' as suspension_type,
        from
            unnest(
                [
                    'In School Suspension',
                    'KM: In-School Suspension',
                    'KNJ: In-School Suspension'
                ]
            ) as penalty_name

        union all

        select penalty_name, 'OSS' as suspension_type,
        from
            unnest(
                [
                    'Out of School Suspension',
                    'KM: Out-of-School Suspension',
                    'KNJ: Out-of-School Suspension'
                ]
            ) as penalty_name
    ),

    suspension_dates as (
        select
            i._dbt_source_relation,
            i.student_school_id as student_number,
            i.create_ts_academic_year as academic_year,

            min(p.start_date) as first_suspension_date,

            min(
                if(s.suspension_type = 'ISS', p.start_date, null)
            ) as first_suspension_date_iss,
            min(
                if(s.suspension_type = 'OSS', p.start_date, null)
            ) as first_suspension_date_oss,
        from {{ ref("stg_deanslist__incidents") }} as i
        inner join
            {{ ref("stg_deanslist__incidents__penalties") }} as p
            on i.incident_id = p.incident_id
            and {{ union_dataset_join_clause(left_alias="i", right_alias="p") }}
            and p.is_suspension
        inner join suspension_type as s on p.penalty_name = s.penalty_name
        group by i._dbt_source_relation, i.student_school_id, i.create_ts_academic_year
    )

select
    co.student_number,
    co.lastfirst,
    co.academic_year,
    co.region,
    co.school_level,
    co.school_abbreviation as school,
    co.grade_level,
    co.advisory_name as team,
    co.entrydate,
    co.exitdate,
    co.special_education_code,
    co.is_504,
    co.lep_status,
    co.gender,
    co.ethnicity,
    co.is_out_of_district,
    co.is_self_contained,

    date_day,

    s.first_suspension_date,
    s.first_suspension_date_iss,
    s.first_suspension_date_oss,

    if(co.spedlep like 'SPED%', 'IEP', 'No IEP') as iep_status,

    if(date_day >= s.first_suspension_date, 1, 0) as is_susp_running,
    if(date_day >= s.first_suspension_date_iss, 1, 0) as is_iss_running,
    if(date_day >= s.first_suspension_date_oss, 1, 0) as is_oss_running,
from {{ ref("base_powerschool__student_enrollments") }} as co
inner join
    unnest(
        generate_date_array(
            date({{ var("current_academic_year") }} - 1, 8, 1),
            current_date('{{ var("local_timezone") }}')
        )
    ) as date_day
    on date_day between co.entrydate and date(co.academic_year + 1, 6, 30)
left join
    suspension_dates as s
    on co.student_number = s.student_number
    and co.academic_year = s.academic_year
    and {{ union_dataset_join_clause(left_alias="co", right_alias="s") }}
where
    co.rn_year = 1
    and co.academic_year >= {{ var("current_academic_year") }} - 1
    and co.grade_level != 99
