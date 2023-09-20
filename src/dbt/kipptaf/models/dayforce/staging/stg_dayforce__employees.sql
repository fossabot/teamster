select
    df_employee_number,
    preferred_last_name,
    common_name,
    last_name,
    first_name,
    ethnicity,
    gender,
    primary_on_site_department_entity,
    primary_on_site_department,
    primary_site_entity,
    primary_site,
    legal_entity_name,
    primary_job,
    position_title,
    status,
    status_reason,
    mobile_number,
    address,
    city,
    state,
    postal_code,
    paytype,
    payclass,
    jobs_and_positions_flsa_status,
    is_manager,
    employee_s_manager_s_df_emp_number_id,
    salesforce_id,
    adp_associate_id,
    grades_taught,
    subjects_taught,
    job_family,
    annual_salary,
    primary_on_site_department_clean,
    primary_site_clean,
    legal_entity_name_clean,
    adp_associate_id_clean,
    birth_date,
    original_hire_date,
    position_effective_from_date,
    position_effective_to_date,
    rehire_date,
    termination_date,
    fivetran_synced,
    modified,
from {{ source("dayforce", "src_dayforce__employees") }}
