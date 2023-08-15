select student_id, safe_cast(local_student_id as int) as local_student_id,
{#
    _english_proficiency_date,
    _exit_date,
    _gate,
    _has_504_plan,
    _last_mod_time,
    _migrant,
    _nslp,
    _residence_district,
    account_id,
    ag_satisfied,
    aka_first_name,
    aka_last_name,
    aka_middle_name,
    aka_name_suffix,
    avid_enter_date,
    avid_exit_date,
    avid_grade_level_id,
    birth_city,
    birth_country,
    birth_date,
    birth_order,
    birth_state,
    birthdate_verification,
    bus_depart_num,
    bus_depart_time,
    bus_num,
    case_manager_504,
    cellphone,
    child_care,
    correspondence_language,
    creation_time,
    cumulative_file_recvd_from,
    cumulative_file_recvd_on,
    cumulative_file_sent_on,
    cumulative_file_sent_to,
    district_enter_date,
    email,
    english_proficiency,
    entered_grade_level_id,
    expected_graduation_year,
    expected_receiver_school,
    first_name,
    foster_care_id,
    gender,
    graduation_date,
    graduation_requirement_year,
    graduation_status,
    hazard_id,
    home_address_is_mailing_address,
    home_address_verification_date,
    homeless_dwelling_type,
    hsee_ela_date,
    hsee_ela_score,
    hsee_ela_status,
    hsee_math_date,
    hsee_math_score,
    hsee_math_status,
    import_student_id,
    info_sharing_opt_out,
    interdistrict_transfer,
    internet_release,
    is_f1_visa,
    is_foster_care,
    is_hispanic,
    is_homeless,
    last_name,
    last_school_year,
    local_lunch_id,
    lunch_balance,
    lunch_id,
    mentor_name,
    middle_name,
    migrant_ed_student_id,
    military_family,
    military_family_indicator,
    military_leave_date,
    military_recruitment,
    mothers_maiden_name,
    name_suffix,
    next_school_site_id,
    nickname,
    parent_education_level,
    passed_hsee_ela,
    passed_hsee_math,
    photo_release,
    pickup_time,
    pre_k_funding_source,
    pre_k_length,
    previous_id,
    primary_ethnicity,
    primary_language,
    prior_district,
    prior_school,
    prior_to_k_experience,
    reported_first_name,
    reported_gender,
    reported_last_name,
    reported_middle_name,
    resident_county_id,
    residential_status,
    school_enter_date,
    service_learning_hours,
    social_security_number,
    special_needs_status,
    sst_date,
    state_student_id,
    student_guid,
    three_years_us_schooling,
    us_abroad,
    username,
#}
from {{ source("illuminate", "students") }}
where not _fivetran_deleted