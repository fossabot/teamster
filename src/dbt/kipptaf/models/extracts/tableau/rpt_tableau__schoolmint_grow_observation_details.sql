select
    employee_number,
    observer_employee_number,
    observation_id,
    teacher_id,
    rubric_name,
    rubric_id,
    observer_name,
    observer_email,
    observed_at,
    glows,
    grows,
    score_measurement_id,
    row_score_value,
    last_modified_date,
    last_modified_date_lead,
    measurement_name,
    text_box,
    score_measurement_type,
    score_measurement_shortname,
    etr_score,
    so_score,
    overall_score,
    coalesce(od.form_term, t.code) as form_term,
    coalesce(od.form_type, t.type) as form_type,
    coalesce(od.academic_year, t.academic_year) as academic_year,
from {{ ref("stg_reporting__terms") }} as t
join
    {{ ref("int_performance_management__observation_details") }} as od
    on t.name = od.rubric_name
    and t.lockbox_date between od.last_modified_date and od.last_modified_date_lead

    -- select
    -- od.user_id,
    -- od.role_name,
    -- od.internal_id,
    -- od.form_type,
    -- od.form_term,
    -- od.form_short_name,
    -- od.form_long_name,
    -- od.score_type,
    -- od.score_measurement_type,
    -- od.score_measurement_shortname,
    -- od.start_date,
    -- od.end_date,
    -- od.academic_year,
    -- od.observation_id,
    -- od.teacher_id,
    -- od.created,
    -- od.observed_at,
    -- od.observer_name,
    -- od.observer_employee_number,
    -- od.etr_score,
    -- od.so_score,
    -- od.overall_score,
    -- od.glows,
    -- od.grows,
    -- od.score_measurement_id,
    -- od.score_percentage,
    -- od.row_score_value,
    -- od.measurement_name,
    -- od.text_box,
    -- od.rn_submission,
    -- od.etr_tier,
    -- od.so_tier,
    -- od.overall_tier,
    -- sr.employee_number,
    -- sr.preferred_name_lastfirst as teammate,
    -- sr.business_unit_home_name as entity,
    -- sr.home_work_location_name as location,
    -- sr.home_work_location_grade_band as grade_band,
    -- sr.home_work_location_powerschool_school_id,
    -- sr.department_home_name as department,
    -- sr.primary_grade_level_taught as grade_taught,
    -- sr.job_title,
    -- sr.report_to_preferred_name_lastfirst as manager,
    -- sr.worker_original_hire_date,
    -- sr.assignment_status,
    -- sr.mail,
    -- sr.report_to_mail,
    -- sr.sam_account_name,
    -- sr.report_to_sam_account_name,
    -- from {{ ref("int_performance_management__observation_details") }} as od
    -- left join
    -- {{ ref("base_people__staff_roster_history") }} as sr
    -- on od.internal_id = safe_cast(sr.employee_number as string)
    -- and coalesce(
    -- od.observed_at,
    -- od.start_date
    -- ) between safe_cast(sr.work_assignment_start_date as date) and safe_cast(
    -- sr.work_assignment_end_date as date
    -- )
    
