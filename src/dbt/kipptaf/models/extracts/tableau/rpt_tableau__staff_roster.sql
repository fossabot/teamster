select
    employee_number as df_employee_number,
    worker_id as associate_id,
    position_id as position_id,
    payroll_file_number as file_number,
    legal_name_given_name as first_name,
    legal_name_family_name as last_name,
    preferred_name_given_name as preferred_first,
    preferred_name_family_name as preferred_last,
    preferred_name_lastfirst as preferred_name,
    business_unit_home_name as legal_entity_name,
    home_work_location_name as location_description,
    department_home_name as home_department_description,
    job_title as job_title_description,
    management_position_indicator as is_management,
    assignment_status as position_status,
    assignment_status_reason as termination_reason_description,
    worker_original_hire_date as original_hire_date,
    worker_rehire_date as rehire_date,
    worker_termination_date as termination_date,
    work_assignment_actual_start_date as position_start_date,
    payroll_group_code as payroll_company_code,
    worker_type as worker_category_description,
    worker_group_value as benefits_eligibility_class_description,
    wage_law_coverage_short_name as flsa_description,
    ethnicity_long_name as eeo_ethnic_description,
    birth_date as birth_date,
    legal_address_line_one as `address`,
    legal_address_city_name as primary_address_city,
    legal_address_country_subdivision_level_1 as primary_address_state_territory_code,
    legal_address_postal_code as primary_address_zip_postal_code,
    communication_person_mobile as personal_contact_personal_mobile,
    mail as mail,
    user_principal_name as userprincipalname,
    report_to_employee_number as manager_df_employee_number,
    report_to_worker_id as manager_custom_assoc_id,
    report_to_preferred_name_lastfirst as manager_name,
    report_to_mail as manager_mail,
    race_ethnicity,
    is_hispanic,
    race_ethnicity_reporting,
    gender_identity,
    relay_status,
    community_grew_up,
    community_professional_exp,
    alumni_status,
    path_to_education,
    primary_grade_level_taught,

    {# retired fields, kept to not break tableau #}
    null as salesforce_job_position_name_custom,
    null as is_regional_staff,
    null as maiden_name,
    null as eeo_ethnic_code,
    null as subject_dept_custom,
    null as job_title_custom,
    null as location_custom,
    null as this_is_a_management_position,
    null as reports_to_name,
    null as gender,
    null as grades_taught_custom,
from {{ ref("base_people__staff_roster") }}
