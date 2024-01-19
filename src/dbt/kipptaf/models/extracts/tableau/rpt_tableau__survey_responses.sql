select
    survey_id,
    survey_title,
    survey_response_id,
    survey_response_link,
    regexp_replace(answer, r'<[^>]*>', '') as answer,
    regexp_replace(question_title, r'<[^>]*>', '') as question_title,
    lower(question_shortname) as question_shortname,
    code,
    type,
    academic_year,
    employee_number,
    respondent_name,
    is_manager,
    respondent_department_name as department,
    respondent_legal_entity_name as legal_entity,
    respondent_manager_name as manager,
    respondent_primary_job as job_title,
    respondent_primary_site as location,
    race_ethnicity_reporting as race_ethnicity,
    gender,
    mail,
    manager_name,
    manager_email,
    manager_user_principal_name,
    alumni_status,
    community_grew_up,
    community_professional_exp,
    level_of_education,
    primary_grade_level_taught,
    date_started,
    date_submitted,
    answer_value,
    is_open_ended,
from {{ ref("int_surveys__survey_responses") }}
