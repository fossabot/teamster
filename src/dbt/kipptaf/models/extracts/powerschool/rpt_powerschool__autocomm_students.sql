with
    grad_path as (
        select distinct
            s._dbt_source_relation,
            s.student_number,
            m.final_grad_path as s_nj_stu_x__graduation_pathway_math,
            e.final_grad_path as s_nj_stu_x__graduation_pathway_ela,
        from {{ ref("int_students__graduation_path_codes") }} as s
        left join
            {{ ref("int_students__graduation_path_codes") }} as m
            on s.student_number = m.student_number
            and m.discipline = 'Math'
            and m.grade_level = 12
        left join
            {{ ref("int_students__graduation_path_codes") }} as e
            on s.student_number = e.student_number
            and e.discipline = 'ELA'
            and e.grade_level = 12
    )

select
    se.student_number,
    se.student_web_id,
    se.student_web_password,
    se.advisory_name as team,
    se.lunch_status as eligibility_name,
    se.lunch_balance as total_balance,
    se.advisor_lastfirst as home_room,
    se.student_web_password as web_password,
    se.student_web_id || '.fam' as web_id,
    se.academic_year + (13 - se.grade_level) as graduation_year,
    g.s_nj_stu_x__graduation_pathway_math,
    g.s_nj_stu_x__graduation_pathway_ela,
    regexp_extract(se._dbt_source_relation, r'(kipp\w+)_') as code_location,
    format_date('%m/%d/%Y', de.district_entry_date) as district_entry_date,
    format_date('%m/%d/%Y', de.district_entry_date) as school_entry_date,
    if(se.enroll_status = 0, 1, 0) as student_allowwebaccess,
    if(se.enroll_status = 0, 1, 0) as allowwebaccess,
    if(se.is_retained_year, 1, 0) as retained_tf,
    case
        when se.grade_level in (0, 5, 9)
        then 'A'
        when se.grade_level in (1, 6, 10)
        then 'B'
        when se.grade_level in (2, 7, 11)
        then 'C'
        when se.grade_level in (3, 8, 12)
        then 'D'
        when se.grade_level = 4
        then 'E'
    end as track,

from {{ ref("base_powerschool__student_enrollments") }} as se
left join
    {{ ref("int_powerschool__district_entry_date") }} as de
    on se.studentid = de.studentid
    and {{ union_dataset_join_clause(left_alias="se", right_alias="de") }}
    and de.rn_entry = 1
left join
    grad_path as g
    on se.student_number = g.student_number
    and {{ union_dataset_join_clause(left_alias="se", right_alias="g") }}
where
    se.academic_year = {{ var("current_academic_year") }}
    and se.rn_year = 1
    and se.grade_level != 99
