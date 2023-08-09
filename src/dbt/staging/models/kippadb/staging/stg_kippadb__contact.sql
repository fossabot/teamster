select
    id,
    `name` as `name`,
    `description` as `description`,
    accountid as account_id,
    assistantname as assistant_name,
    assistantphone as assistant_phone,
    birthdate as birthdate,
    createdbyid as created_by_id,
    createddate as created_date,
    department as department,
    email as email,
    emailbounceddate as email_bounced_date,
    emailbouncedreason as email_bounced_reason,
    fax as fax,
    firstname as first_name,
    hasoptedoutofemail as has_opted_out_of_email,
    homephone as home_phone,
    isemailbounced as is_email_bounced,
    jigsaw as jigsaw,
    jigsawcontactid as jigsaw_contact_id,
    lastactivitydate as last_activity_date,
    lastcurequestdate as last_cu_request_date,
    lastcuupdatedate as last_cu_update_date,
    lastmodifiedbyid as last_modified_by_id,
    lastmodifieddate as last_modified_date,
    lastname as last_name,
    lastreferenceddate as last_referenced_date,
    lastvieweddate as last_viewed_date,
    leadsource as lead_source,
    mailingaddress as mailing_address,
    mailingcity as mailing_city,
    mailingcountry as mailing_country,
    mailinggeocodeaccuracy as mailing_geocode_accuracy,
    mailinglatitude as mailing_latitude,
    mailinglongitude as mailing_longitude,
    mailingpostalcode as mailing_postal_code,
    mailingstate as mailing_state,
    mailingstreet as mailing_street,
    masterrecordid as master_record_id,
    mobilephone as mobile_phone,
    otheraddress as other_address,
    othercity as other_city,
    othercountry as other_country,
    othergeocodeaccuracy as other_geocode_accuracy,
    otherlatitude as other_latitude,
    otherlongitude as other_longitude,
    otherphone as other_phone,
    otherpostalcode as other_postal_code,
    otherstate as other_state,
    otherstreet as other_street,
    ownerid as owner_id,
    phone as phone,
    photourl as photo_url,
    recordtypeid as record_type_id,
    reportstoid as reports_to_id,
    salutation as salutation,
    systemmodstamp as system_modstamp,
    title as title,

    academic_status__c as academic_status,
    academics__c as academics,
    accumulated_credits_college__c as accumulated_credits_college,
    accumulated_credits_hs__c as accumulated_credits_hs,
    actual_college_graduation_date__c as actual_college_graduation_date,
    actual_hs_graduation_date__c as actual_hs_graduation_date,
    advising_provider__c as advising_provider,
    any_college_admin__c as any_college_admin,
    any_kipp_hs_enrollment__c as any_kipp_hs_enrollment,
    associate_degree_grad_count__c as associate_degree_grad_count,
    attending_college_enrollments__c as attending_college_enrollments,
    attending_hs_enrollments__c as attending_hs_enrollments,
    bach_degree_admin__c as bach_degree_admin,
    brag_sheet_submitted__c as brag_sheet_submitted,
    campus_staff_type__c as campus_staff_type,
    career_training_program_status__c as career_training_program_status,
    carrier__c as carrier,
    class_quartile__c as class_quartile,
    class_rank__c as class_rank,
    class_rank_percentile__c as class_rank_percentile,
    collaborative_advising_student__c as collaborative_advising_student,
    college_apps_accepted__c as college_apps_accepted,
    college_apps_in_progress_wishlist__c as college_apps_in_progress_wishlist,
    college_apps_submitted__c as college_apps_submitted,
    college_counselor__c as college_counselor,
    college_credits_attempted__c as college_credits_attempted,
    college_cumulative_credits_attempted__c as college_cumulative_credits_attempted,
    college_cumulative_credits_earned__c as college_cumulative_credits_earned,
    college_graduated_from__c as college_graduated_from,
    college_level__c as college_level,
    college_match_display_gpa__c as college_match_display_gpa,
    college_recommendation_complete__c as college_recommendation_complete,
    college_status__c as college_status,
    collegecte_attendingmatric_enrollments__c
    as college_cte_attending_matric_enrollments,
    contact_count__c as contact_count,
    counselor_s_school_name__c as counselor_s_school_name,
    count_active_enrollments__c as count_active_enrollments,
    count_hs_graduated_enrollment__c as count_hs_graduated_enrollment,
    count_of_bach_degree__c as count_of_bach_degree,
    credits_accumlated_hs__c as credits_accumlated_hs,
    credits_accumulated_college__c as credits_accumulated_college,
    cumulative_gpa__c as cumulative_gpa,
    cumulative_gpa_lookup__c as cumulative_gpa_lookup,
    current_academic_status__c as current_academic_status,
    current_college_cumulative_gpa__c as current_college_cumulative_gpa,
    current_college_semester_gpa__c as current_college_semester_gpa,
    current_college_standing__c as current_college_standing,
    current_cumulative_gpa__c as current_cumulative_gpa,
    current_kipp_student__c as current_kipp_student,
    current_level__c as current_level,
    current_transcript_date__c as current_transcript_date,
    current_transcript_term__c as current_transcript_term,
    currently_enrolled_school__c as currently_enrolled_school,
    date_last_opt_in_request__c as date_last_opt_in_request,
    date_no_postsec_pathway_confirmed__c as date_no_postsec_pathway_confirmed,
    date_of_mass_text_opt_in__c as date_of_mass_text_opt_in,
    date_of_out_of_country_move__c as date_of_out_of_country_move,
    dep_post_hs_simple_admin__c as dep_post_hs_simple_admin,
    df_has_fafsa__c as df_has_fafsa,
    df_has_fafsa4caster__c as df_has_fafsa4caster,
    df_has_gpa__c as df_has_gpa,
    dual_enrollment__c as dual_enrollment,
    earned_to_attempted_college_credits__c as earned_to_attempted_college_credits,
    education_level__c as education_level,
    efc_from_fafsa__c as efc_from_fafsa,
    efc_from_fafsa4caster__c as efc_from_fafsa4caster,
    enlisted_in_military__c as enlisted_in_military,
    enrolled_at_ambassador_college__c as enrolled_at_ambassador_college,
    enrolled_at_partner_college__c as enrolled_at_partner_college,
    enrolled_in_kipp_hs_at_least_1_year__c as enrolled_in_kipp_hs_at_least_1_year,
    ethnicity__c as ethnicity,
    expected_college_graduation__c as expected_college_graduation,
    expected_hs_graduation__c as expected_hs_graduation,
    external_student__c as external_student,
    external_student_affiliation__c as external_student_affiliation,
    family_income_bracket__c as family_income_bracket,
    financial__c as financial,
    financial_status__c as financial_status,
    first_generation_college_student__c as first_generation_college_student,
    flag_for_benchmark_follow_up__c as flag_for_benchmark_follow_up,
    frpl_eligible__c as frpl_eligible,
    full_name__c as full_name,
    full_time_employed__c as full_time_employed,
    gender__c as gender,
    gpa_in_major__c as gpa_in_major,
    grad_school_attended__c as grad_school_attended,
    grade_level__c as grade_level,
    has_active_collaborative_consent_form__c as has_active_collaborative_consent_form,
    has_any_college_admin__c as has_any_college_admin,
    has_app_in_progress_wishlist__c as has_app_in_progress_wishlist,
    has_applied_to_a_college__c as has_applied_to_a_college,
    has_been_accepted_to_college__c as has_been_accepted_to_college,
    has_high_school_enrollment__c as has_high_school_enrollment,
    has_hs_graduated_enrollment__c as has_hs_graduated_enrollment,
    has_linkedin_profile__c as has_linked_in_profile,
    has_matric_college_enrollment__c as has_matric_college_enrollment,
    has_taken_placement_test__c as has_taken_placement_test,
    high_school_apps_accepted__c as high_school_apps_accepted,
    high_school_apps_in_progress_wishlist__c as high_school_apps_in_progress_wishlist,
    high_school_apps_submitted__c as high_school_apps_submitted,
    high_school_enrollments_count__c as high_school_enrollments_count,
    high_school_graduated_from__c as high_school_graduated_from,
    high_school_status__c as high_school_status,
    highest_act_diagnostic_score__c as highest_act_diagnostic_score,
    highest_act_score__c as highest_act_score,
    highest_psat_score__c as highest_psat_score,
    highest_sat_score__c as highest_sat_score,
    highest_sat_score_before_march_2016__c as highest_sat_score_before_march_2016,
    hs_recommendation_complete__c as hs_recommendation_complete,
    informed_consent__c as informed_consent,
    intent_to_enlist__c as intent_to_enlist,
    kca_kipp_id__c as kca_kipp_id,
    kipp_college_class__c as kipp_college_class,
    kipp_foundation_id__c as kipp_foundation_id,
    kipp_hs_graduate__c as kipp_hs_graduate,
    kipp_ms_graduate__c as kipp_ms_graduate,
    kipp_region_name__c as kipp_region_name,
    kipp_region_school__c as kipp_region_school,
    language_spoken_at_home__c as language_spoken_at_home,
    last_advisor_activity__c as last_advisor_activity,
    last_alumni_survey_completion_date__c as last_alumni_survey_completion_date,
    last_outreach__c as last_outreach,
    last_successful_advisor_contact__c as last_successful_advisor_contact,
    last_successful_advisor_contact_range__c as last_successful_advisor_contact_range,
    last_successful_contact__c as last_successful_contact,
    last_successful_contact_range__c as last_successful_contact_range,
    latest_fafsa_date__c as latest_fafsa_date,
    latest_pfs_date__c as latest_pfs_date,
    latest_resume__c as latest_resume,
    latest_state_financial_aid_app_date__c as latest_state_financial_aid_app_date,
    latest_transcript__c as latest_transcript,
    legal_status__c as legal_status,
    linkedin_profile_url__c as linked_in_profile_url,
    maiden_name__c as maiden_name,
    marital_status__c as marital_status,
    mass_text_opt_in_status__c as mass_text_opt_in_status,
    matriculating_to_ambassador_college__c as matriculating_to_ambassador_college,
    matriculating_to_partner_college__c as matriculating_to_partner_college,
    media_release__c as media_release,
    metro_card_sites__c as metro_card_sites,
    middle_name__c as middle_name,
    middle_school_attended__c as middle_school_attended,
    middle_skilling_trade_military_interest__c
    as middle_skilling_trade_military_interest,
    military_enlistments__c as military_enlistments,
    military_status__c as military_status,
    most_advanced_app_status__c as most_advanced_app_status,
    most_advanced_hsp__c as most_advanced_hsp,
    most_recent__c as most_recent,
    most_recent_benchmark_status__c as most_recent_benchmark_status,
    most_recent_college_application__c as most_recent_college_application,
    most_recent_college_benchmark__c as most_recent_college_benchmark,
    most_recent_college_city__c as most_recent_college_city,
    most_recent_college_competitiveness__c as most_recent_college_competitiveness,
    most_recent_college_degree_type__c as most_recent_college_degree_type,
    most_recent_college_enrollment__c as most_recent_college_enrollment,
    most_recent_college_enrollment_id__c as most_recent_college_enrollment_id,
    most_recent_college_enrollment_name__c as most_recent_college_enrollment_name,
    most_recent_college_enrollment_status__c as most_recent_college_enrollment_status,
    most_recent_college_gpa__c as most_recent_college_gpa,
    most_recent_college_graduation_rate__c as most_recent_college_graduation_rate,
    most_recent_college_housing_from_app__c as most_recent_college_housing_from_app,
    most_recent_college_is_hbcu__c as most_recent_college_is_hbcu,
    most_recent_college_is_hsi__c as most_recent_college_is_hsi,
    most_recent_college_state__c as most_recent_college_state,
    most_recent_college_type__c as most_recent_college_type,
    most_recent_college_unmet_need_from_app__c
    as most_recent_college_unmet_need_from_app,
    most_recent_iep_date__c as most_recent_iep_date,
    ms_gpa__c as ms_gpa,
    ms_teacher_recommendation__c as ms_teacher_recommendation,
    nera_participant__c as nera_participant,
    non_cognitive__c as non_cognitive,
    non_cognitive_status__c as non_cognitive_status,
    non_custodial_parent_letter_submitted__c as non_custodial_parent_letter_submitted,
    not_pursuing_higher_ed_at_this_time__c as not_pursuing_higher_ed_at_this_time,
    nudge_texting_region__c as nudge_texting_region,
    number_in_household__c as number_in_household,
    number_of_current_kipp_enrollments__c as number_of_current_kipp_enrollments,
    old_system_id__c as old_system_id,
    opt_in_source__c as opt_in_source,
    opt_out_college_connections__c as opt_out_college_connections,
    opt_out_national_contact__c as opt_out_national_contact,
    opt_out_regional_contact__c as opt_out_regional_contact,
    other_gender__c as other_gender,
    out_of_country__c as out_of_country,
    outreach_student__c as outreach_student,
    overall_benchmark_status__c as overall_benchmark_status,
    overgrad_time_last_synched__c as overgrad_time_last_synched,
    parent_education_level__c as parent_education_level,
    partial_hs_class__c as partial_hs_class,
    passion_purpose_plan__c as passion_purpose_plan,
    pell_eligible__c as pell_eligible,
    personal_essay_completed__c as personal_essay_completed,
    picture__c as picture,
    picture_id__c as picture_id,
    post_hs_plan__c as post_hs_plan,
    post_hs_status__c as post_hs_status,
    postsec_advisor__c as postsec_advisor,
    postsecondary_status__c as postsecondary_status,
    prevent_overgrad_synch__c as prevent_overgrad_synch,
    primary_partnership_contact__c as primary_partnership_contact,
    profile_goals__c as profile_goals,
    qualified_asvab__c as qualified_asvab,
    qualified_physical_training__c as qualified_physical_training,
    reason_for_prevent_overgrad_synch__c as reason_for_prevent_overgrad_synch,
    salesforce_id__c as salesforce_id,
    sat_superscore__c as sat_superscore,
    school_sis_id__c as school_sis_id,
    secondary_email__c as secondary_email,
    socio_emotional__c as socio_emotional,
    socio_emotional_status__c as socio_emotional_status,
    student_disengagement_status__c as student_disengagement_status,
    student_level__c as student_level,
    student_s_school__c as student_s_school,
    student_segment_for_career_program__c as student_segment_for_career_program,
    tax_returns_submitted__c as tax_returns_submitted,
    transcript_release__c as transcript_release,
    undergrad_attended__c as undergrad_attended,
    working_papers__c as working_papers,
    x2year_college_enrollments__c as x2year_college_enrollments,
    x8th_grade_promotion_date__c as x8th_grade_promotion_date,
    ytd_gpa__c as ytd_gpa,

    safe_cast(kipp_hs_class__c as int) as kipp_hs_class,
    safe_cast(school_specific_id__c as int) as school_specific_id,
from {{ source("kippadb", "contact") }} as c
where not isdeleted