select
    a.assignment_id,
    a.name as assignment_name,
    a.type as assignment_type,
    a.created as assignment_date,
    a.user_id,
    a.user_name,
    a.creator_id,
    a.creator_name,

    ast.tag_id,
    ast.tag_name,

    sr.home_work_location_name as user_default_school_name,
    sr.department_home_name as user_default_course_name,
    sr.primary_grade_level_taught as user_default_gradelevel_name,
    sr.job_title as primary_job,
    sr.department_home_name as primary_on_site_department,

    rt.academic_year,
    rt.name as reporting_term_name,

    null as assignment_status,
    null as exclude_from_bank,
    null as mastered_date,
    null as user_email,
    null as creator_email,
from {{ ref("stg_schoolmint_grow__assignments") }} as a
inner join
    {{ ref("stg_schoolmint_grow__assignments__tags") }} as ast
    on a.assignment_id = ast.assignment_id
inner join {{ ref("stg_schoolmint_grow__users") }} as u on a.user_id = u.user_id
left join
    {{ ref("base_people__staff_roster") }} as sr
    on u.internal_id = safe_cast(sr.employee_number as string)
left join
    {{ ref("stg_reporting__terms") }} as rt
    on cast(a.created as date) between rt.start_date and rt.end_date
    and rt.type = 'RT'
    and rt.school_id = 0
where a.type = 'goal'