with
    scaffold as (
        select
            ur.user_id,
            ur.role_name,

            u.internal_id,

            rt.type,
            rt.code,
            rt.name,
            rt.start_date,
            rt.end_date,
            rt.academic_year,

            sr.employee_number,
            sr.preferred_name_lastfirst,
            sr.business_unit_home_name,
            sr.home_work_location_name,
            sr.home_work_location_grade_band,
            sr.home_work_location_powerschool_school_id,
            sr.department_home_name,
            sr.primary_grade_level_taught,
            sr.job_title,
            sr.report_to_preferred_name_lastfirst,
            sr.worker_original_hire_date,
            sr.assignment_status,
        from {{ ref("stg_schoolmint_grow__users__roles") }} as ur
        left join {{ ref("stg_schoolmint_grow__users") }} as u on ur.user_id = u.user_id
        left join
            {{ ref("stg_reporting__terms") }} as rt on ur.role_name = rt.grade_band
        left join
            {{ ref("base_people__staff_roster") }} as sr
            on u.internal_id = safe_cast(sr.employee_number as string)
        where ur.role_name != 'Whetstone'
    ),

    boxes as (
        select
            observation_id,
            measurement,
            `value` as text_box_value,
            null as checkbox_value,
            'textbox' as question_type,
        from
            {{
                ref(
                    "stg_schoolmint_grow__observations__observation_scores__text_boxes"
                )
            }}
    ),

    observations as (
        select
            o.observation_id,
            o.teacher_id,
            o.rubric_name,
            o.created,
            o.observed_at,
            o.observer_name,
            o.observer_email,
            o.score as overall_score,
            array_to_string(o.list_two_column_a, '|') as glows,
            array_to_string(o.list_two_column_b, '|') as grows,

            os.measurement as score_measurement_id,
            os.percentage as score_percentage,
            os.value_score as row_score_value,

            m.name as measurement_name,
            m.scale_min as measurement_scale_min,
            m.scale_max as measurement_scale_max,

            case
                when o.rubric_name like '%Coaching%'
                then 'PM'
                when o.rubric_name like '%Walkthrough%'
                then 'WT'
                when o.rubric_name like '%O3%'
                then 'O3'
            end as reporting_term_type,
            case
                when lower(o.rubric_name) not like '%etr%'
                then null
                when o.score < 1.75
                then 1
                when o.score >= 1.75 and o.score < 2.75
                then 2
                when o.score >= 2.75 and o.score < 3.5
                then 3
                when o.score > 3.5
                then 4
            end as tier,
            case
                when
                    o.rubric_name = 'Coaching Tool: Coach ETR and Reflection'
                    and date(
                        o.observed_at
                    ) between date({{ var("current_fiscal_year") }}, 7, 1) and date(
                        {{ var("current_fiscal_year") }}, 10, 31
                    )
                then 'BOY (Coach)'
                when
                    o.rubric_name = 'Coaching Tool: Teacher Reflection'
                    and date(
                        o.observed_at
                    ) between date({{ var("current_fiscal_year") }}, 7, 1) and date(
                        {{ var("current_fiscal_year") }}, 10, 31
                    )
                then 'BOY (Self)'
                when
                    o.rubric_name = 'Coaching Tool: Coach ETR and Reflection'
                    and date(
                        o.observed_at
                    ) between date({{ var("current_fiscal_year") }}, 11, 1) and (
                        date({{ var("current_fiscal_year") }}, 3, 1) - 1
                    )
                then 'MOY (Coach)'
                when
                    o.rubric_name = 'Coaching Tool: Teacher Reflection'
                    and date(
                        o.observed_at
                    ) between date({{ var("current_fiscal_year") }}, 11, 1) and (
                        date({{ var("current_fiscal_year") }}, 3, 1) - 1
                    )
                then 'MOY (Self)'
                when
                    o.rubric_name = 'Coaching Tool: Coach ETR and Reflection'
                    and date(
                        o.observed_at
                    ) between date({{ var("current_fiscal_year") }}, 3, 1) and date(
                        {{ var("current_fiscal_year") }}, 6, 30
                    )
                then 'EOY (Coach)'
                when
                    o.rubric_name = 'Coaching Tool: Teacher Reflection'
                    and date(
                        o.observed_at
                    ) between date({{ var("current_fiscal_year") }}, 3, 1) and date(
                        {{ var("current_fiscal_year") }}, 6, 30
                    )
                then 'EOY (Self)'
            end as reporting_term_name,
            regexp_replace(
                regexp_replace(b.text_box_value, r'<[^>]*>', ''), r'&nbsp;', ' '
            ) as text_box,
        from {{ ref("stg_schoolmint_grow__observations") }} as o
        left join
            {{ ref("stg_schoolmint_grow__observations__observation_scores") }} as os
            on o.observation_id = os.observation_id
        left join
            {{ ref("stg_schoolmint_grow__measurements") }} as m
            on os.measurement = m.measurement_id
        left join
            boxes as b
            on os.observation_id = b.observation_id
            and os.measurement = b.measurement
        where
            o.is_published
            and o.observed_at >= timestamp(date({{ var("current_fiscal_year") }}, 7, 1))
    ),

    observation_details as (
        select
            s.user_id,
            s.role_name,
            s.internal_id,
            s.type,
            s.code,
            'ETR + S&O' as score_type,
            s.name,
            s.start_date,
            s.end_date,
            s.academic_year,
            s.employee_number,
            s.preferred_name_lastfirst,
            s.business_unit_home_name,
            s.home_work_location_name,
            s.home_work_location_grade_band,
            s.home_work_location_powerschool_school_id,
            s.department_home_name,
            s.primary_grade_level_taught,
            s.job_title,
            s.report_to_preferred_name_lastfirst,
            s.worker_original_hire_date,
            s.assignment_status,

            o.observation_id,
            o.teacher_id,
            o.rubric_name,
            o.created,
            o.observed_at,
            o.observer_name,
            o.overall_score,
            o.glows,
            o.grows,
            o.score_measurement_id,
            o.score_percentage,
            o.row_score_value,
            o.measurement_name,
            o.measurement_scale_min,
            o.measurement_scale_max,
            o.reporting_term_type,
            o.tier,
            o.reporting_term_name,
            o.text_box,

            row_number() over (
                partition by s.type, s.name, s.internal_id, o.score_measurement_id
                order by o.observed_at desc
            ) as rn_submission,
        from scaffold as s
        left join
            observations as o
            on cast(o.observed_at as date) between s.start_date and s.end_date
            /* Matches on name for PM Rounds to distinguish Self and Coach */
            and s.type = 'PM'
            and s.name = o.reporting_term_name
            and s.user_id = o.teacher_id

        union all

        select
            s.user_id,
            s.role_name,
            s.internal_id,
            s.type,
            s.code,
            '' as score_type,
            s.name,
            s.start_date,
            s.end_date,
            s.academic_year,
            s.employee_number,
            s.preferred_name_lastfirst,
            s.business_unit_home_name,
            s.home_work_location_name,
            s.home_work_location_grade_band,
            s.home_work_location_powerschool_school_id,
            s.department_home_name,
            s.primary_grade_level_taught,
            s.job_title,
            s.report_to_preferred_name_lastfirst,
            s.worker_original_hire_date,
            s.assignment_status,

            o.observation_id,
            o.teacher_id,
            o.rubric_name,
            o.created,
            o.observed_at,
            o.observer_name,
            o.overall_score,
            o.glows,
            o.grows,
            o.score_measurement_id,
            o.score_percentage,
            o.row_score_value,
            o.measurement_name,
            o.measurement_scale_min,
            o.measurement_scale_max,
            o.reporting_term_type,
            o.tier,
            o.reporting_term_name,
            o.text_box,

            row_number() over (
                partition by s.type, s.name, s.internal_id, o.score_measurement_id
                order by o.observed_at desc
            ) as rn_submission,
        from scaffold as s
        left join
            observations as o
            on cast(o.observed_at as date) between s.start_date and s.end_date
            /* matches only on type and date for weekly forms */
            and s.type in ('WT', 'O3')
            and s.type = o.reporting_term_type
            and s.user_id = o.teacher_id
    ),

    historical_overall_scores as (
        select
            employee_number,
            academic_year,
            pm_term as code,
            etr_score,
            so_score,
            overall_score,
            etr_tier,
            so_tier,
            overall_tier as tier,
        from
            {{
                source(
                    "performance_management",
                    "src_performance_management__scores_overall_archive",
                )
            }}

        union distinct

        select
            employee_number,
            academic_year,
            code,
            null as etr_score,
            null as so_score,
            overall_score,
            null as etr_tier,
            null as so_tier,
            tier,
        from observation_details
        where type = 'PM' and overall_score is not null
    ),

    historical_detail_scores as (
        select
            subject_employee_number as employee_number,
            academic_year,
            pm_term as code,
            score_type,
            observer_employee_number,
            null as observer_name,
            observed_at,
            measurement_name,
            score_value as row_score_value,

        from
            {{
                source(
                    "performance_management",
                    "src_performance_management__scores_detail_archive",
                )
            }}

        union all

        select
            employee_number,
            academic_year,
            code,
            score_type,
            null as observer_employee_number,
            observer_name,
            observed_at,
            measurement_name,
            row_score_value,

        from observation_details
        where type = 'PM' and overall_score is not null
    ),

    historical_data as (
        select
            ds.employee_number,
            ds.academic_year,
            ds.code,
            '' as `name`,
            ds.score_type,
            ds.observer_employee_number,
            ds.observer_name,
            ds.observed_at,
            ds.measurement_name,
            ds.row_score_value,

            os.etr_score,
            os.so_score,
            os.overall_score,
            os.etr_tier,
            os.so_tier,
            os.tier,
        from historical_detail_scores as ds
        left join
            historical_overall_scores as os
            on ds.employee_number = os.employee_number
            and ds.academic_year = os.academic_year
            and ds.code = os.code
    )

select
    user_id,
    role_name,
    internal_id,
    type,
    code,
    score_type,
    name,
    start_date,
    end_date,
    academic_year,
    employee_number,
    preferred_name_lastfirst,
    business_unit_home_name,
    home_work_location_name,
    home_work_location_grade_band,
    home_work_location_powerschool_school_id,
    department_home_name,
    primary_grade_level_taught,
    job_title,
    report_to_preferred_name_lastfirst,
    worker_original_hire_date,
    assignment_status,
    observation_id,
    teacher_id,
    rubric_name,
    created,
    observed_at,
    observer_name,
    null as etr_score,
    null as so_score,
    overall_score,
    null as etr_tier,
    null as so_tier,
    tier,
    glows,
    grows,
    score_measurement_id,
    score_percentage,
    row_score_value,
    measurement_name,
    text_box,
    rn_submission,

from observation_details
where rn_submission = 1

union all

select
    null as user_id,
    null as role_name,
    null as internal_id,
    'PM' as `type`,
    hd.code,
    hd.score_type,
    hd.name,
    null as start_date,
    null as end_date,
    hd.academic_year,
    hd.employee_number,
    sr.preferred_name_lastfirst,
    sr.business_unit_home_name,
    sr.home_work_location_name,
    sr.home_work_location_grade_band,
    sr.home_work_location_powerschool_school_id,
    sr.department_home_name,
    sr.primary_grade_level_taught,
    sr.job_title,
    sr.report_to_preferred_name_lastfirst,
    sr.worker_original_hire_date,
    sr.assignment_status,

    null as observation_id,
    null as teacher_id,
    null as rubric_name,
    null as created,
    hd.observed_at,
    hd.observer_name,
    hd.etr_score,
    hd.so_score,
    hd.overall_score,
    hd.etr_tier,
    hd.so_tier,
    hd.tier,
    null as glows,
    null as grows,
    null as score_measurement_id,
    null as score_percentage,
    hd.row_score_value,
    hd.measurement_name,
    null as text_box,
    1 as rn_submission,
from historical_data as hd
left join
    {{ ref("base_people__staff_roster") }} as sr
    on hd.employee_number = sr.employee_number
