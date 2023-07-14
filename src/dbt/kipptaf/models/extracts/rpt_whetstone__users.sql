with
    people as (
        select
            sr.employee_number as user_internal_id,
            sr.report_to_employee_number as manager_internal_id,
            sr.google_email as user_email,
            sr.department_home_name as course_name,
            sr.preferred_name_given_name
            || ' '
            || sr.preferred_name_family_name as user_name,
            if(
                sr.home_work_location_powerschool_school_id != 0,
                sr.home_work_location_name,
                null
            ) as school_name,
            if(sr.assignment_status in ('Terminated', 'Deceased'), 1, 0) as inactive,
            if(
                sr.primary_grade_level_taught = 0,
                'K',
                safe_cast(sr.primary_grade_level_taught as string)
            ) as grade_abbreviation,

            case
                /* network admins */
                when sr.department_home_name = 'Executive'
                then 'Regional Admin'
                when
                    sr.department_home_name in (
                        'Teaching and Learning',
                        'School Support',
                        'New Teacher Development'
                    )
                    and sr.job_title in (
                        'Achievement Director',
                        'Chief Academic Officer',
                        'Chief Of Staff',
                        'Director',
                        'Head of Schools',
                        'Director High School Literacy Curriculum',
                        'Director Literacy Achievement',
                        'Director Math Achievement',
                        'Director Middle School Literacy Curriculum',
                        'Head of Schools in Residence',
                        'Assistant Dean',
                        'Assistant School Leader',
                        'Assistant School Leader, SPED',
                        'Dean',
                        'Dean of Students',
                        'Director of New Teacher Development',
                        'School Leader in Residence',
                        'School Leader'
                    )
                then 'Sub Admin'
                when
                    sr.department_home_name = 'Special Education'
                    and sr.job_title
                    in ('Managing Director', 'Director', 'Achievement Director')
                then 'Sub Admin'
                when sr.department_home_name = 'Human Resources'
                then 'Sub Admin'
                /* school admins */
                when sr.job_title = 'School Leader'
                then 'School Admin'
                when
                    sr.department_home_name = 'School Leadership'
                    and sr.job_title in (
                        'Assistant Dean',
                        'Assistant School Leader',
                        'Assistant School Leader, SPED',
                        'Dean',
                        'Dean of Students',
                        'Director of New Teacher Development',
                        'School Leader in Residence'
                    )
                then 'School Assistant Admin'
                /* basic roles */
                when sr.management_position_indicator
                then 'Coach'
                when
                    sr.job_title in (
                        'Teacher',
                        'Teacher ESL',
                        'Co-Teacher',
                        'Learning Specialist',
                        'Learning Specialist Coordinator',
                        'Teacher in Residence',
                        'Teaching Fellow'
                    )
                then 'Teacher'
                else 'No Role'
            end as role_name
        from {{ ref("base_people__staff_roster") }} as sr
        where
            sr.user_principal_name is not null
            and coalesce(sr.worker_termination_date, current_date('America/New_York'))
            >= date({{ var("current_academic_year") }} - 1, 7, 1)
            and sr.department_home_name != 'Data'
    ),

    observation_group_membership_union as (
        select observation_group_id, user_id, 'Teacher' as role_name,
        from {{ ref("stg_schoolmint_grow__schools_observationgroups_observees") }}

        union all

        select observation_group_id, user_id, 'Coach' as role_name,
        from {{ ref("stg_schoolmint_grow__schools_observationgroups_observers") }}
    ),

    observation_groups as (
        select
            sog.school_id,
            sog.observation_group_id,
            sog.observation_group_name,

            ogm.user_id,
            ogm.role_name,
        from {{ ref("stg_schoolmint_grow__schools_observationgroups") }} as sog
        inner join
            observation_group_membership_union as ogm
            on sog.observation_group_id = ogm.observation_group_id
    ),

    observation_groups_agg as (
        select
            user_id,
            school_id,
            observation_group_name,
            string_agg(role_name, ';') as role_names,
        from observation_groups
        where observation_group_name = 'Teachers'
        group by user_id, school_id, observation_group_name
    ),

    roles_union as (
        select user_id, role_id, role_name,
        from {{ ref("stg_schoolmint_grow__users_roles") }}
        where role_name != 'No Role'

        union distinct

        select og.user_id, r.role_id, r.name as role_name,
        from observation_groups as og
        inner join {{ ref("stg_schoolmint_grow__roles") }} as r on og.role_name = r.name

        union distinct

        select u.user_id, r.role_id as role_id, r.name as role_name,
        from {{ ref("base_people__staff_roster") }} as s
        inner join
            {{ ref("stg_schoolmint_grow__users") }} as u
            on s.employee_number = u.internalid
        inner join
            {{ ref("stg_schoolmint_grow__roles") }} as r on r.name = 'School Admin'
        where s.job_title = 'School Leader'
    ),

    roles_agg as (
        select
            user_id,
            '"' || string_agg(distinct role_id, '" , "') || '"' as role_ids,
            '"' || string_agg(distinct role_name, '" , "') || '"' as role_names,
        from roles_union
        group by user_id
    )

select
    p.user_internal_id,
    p.user_name,
    p.user_email,
    p.inactive,
    case
        when
            current_date('America/New_York')
            = date({{ var("current_academic_year") }}, 8, 1)
        then null
        when p.role_name = 'Coach'
        then 'observees;observers'
        when p.role_name like '%Admin%'
        then 'observers'
        else 'observees'
    end as group_type,
    case
        when
            current_date('America/New_York')
            = date({{ var("current_academic_year") }}, 8, 1)
        then null
        else 'Teachers'
    end as group_name,

    u.user_id,
    u.email as user_email_ws,
    u.name as user_name_ws,
    u.inactive as inactive_ws,
    u.defaultinformation_school as school_id_ws,
    u.defaultinformation_gradelevel as grade_id_ws,
    u.defaultinformation_course as course_id_ws,
    u.coach as coach_id_ws,
    u.archivedat as archived_at,

    um.user_id as coach_id,

    sch.school_id,

    gr.tag_id as grade_id,

    cou.tag_id as course_id,

    '[' || er.role_ids || ']' as role_id_ws,

    og.role_names as group_type_ws,

    '[' || case
        /* removing last year roles every August*/
        when current_date('America/New_York') = date(2023, 8, 1)
        then '"' || p.role_name || '"'
        /* no roles = add assigned role */
        when er.role_names is null
        then '"' || p.role_name || '"'
        /* assigned role already exists = use existing */
        when regexp_contains(er.role_names, p.role_name)
        then er.role_names
        /* add assigned role */
        else '"' || p.role_name || '",' || er.role_names
    end
    || ']' as role_names,

    '[' || case
        /* removing last year roles every August*/
        when current_date('America/New_York') = date(2023, 8, 1)
        then '"' || r.role_id || '"'
        /* no roles = add assigned role */
        when er.role_ids is null
        then '"' || r.role_id || '"'
        /* assigned role already exists = use existing */
        when regexp_contains(er.role_ids, r.role_id)
        then er.role_ids
        /* add assigned role */
        else '"' || r.role_id || '",' || er.role_ids
    end
    || ']' as role_id,
from people as p
left join
    {{ ref("stg_schoolmint_grow__users") }} as u on p.user_internal_id = u.internalid
left join
    {{ ref("stg_schoolmint_grow__users") }} as um
    on p.manager_internal_id = um.internalid
left join {{ ref("stg_schoolmint_grow__schools") }} as sch on p.school_name = sch.name
left join
    {{ ref("stg_schoolmint_grow__generic_tags") }} as cou
    on p.course_name = cou.name
    and cou.tag_type = 'courses'
    and cou.archivedat is null
left join
    {{ ref("stg_schoolmint_grow__generic_tags") }} as gr
    on p.grade_abbreviation = gr.abbreviation
    and gr.tag_type = 'grades'
    and gr.archivedat is null
left join {{ ref("stg_schoolmint_grow__roles") }} as r on p.role_name = r.name
left join roles_agg as er on u.user_id = er.user_id
left join
    observation_groups_agg as og
    on u.user_id = og.user_id
    and sch.school_id = og.school_id
where p.role_name != 'No Role'