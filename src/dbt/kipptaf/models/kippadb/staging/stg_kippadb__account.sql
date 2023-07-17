select
    id as id,
    `name`,
    `description`,
    `type`,
    annualrevenue as annual_revenue,
    billingaddress as billing_address,
    billingcity as billing_city,
    billingcountry as billing_country,
    billinggeocodeaccuracy as billing_geocode_accuracy,
    billinglatitude as billing_latitude,
    billinglongitude as billing_longitude,
    billingpostalcode as billing_postal_code,
    billingstate as billing_state,
    billingstreet as billing_street,
    createdbyid as created_by_id,
    createddate as created_date,
    fax,
    industry,
    jigsaw,
    jigsawcompanyid as jigsaw_company_id,
    lastactivitydate as last_activity_date,
    lastmodifiedbyid as last_modified_by_id,
    lastmodifieddate as last_modified_date,
    lastreferenceddate as last_referenced_date,
    lastvieweddate as last_viewed_date,
    masterrecordid as master_record_id,
    numberofemployees as number_of_employees,
    ownerid as owner_id,
    parentid as parent_id,
    phone,
    photourl as photo_url,
    recordtypeid as record_type_id,
    shippingaddress as shipping_address,
    shippingcity as shipping_city,
    shippingcountry as shipping_country,
    shippinggeocodeaccuracy as shipping_geocode_accuracy,
    shippinglatitude as shipping_latitude,
    shippinglongitude as shipping_longitude,
    shippingpostalcode as shipping_postal_code,
    shippingstate as shipping_state,
    shippingstreet as shipping_street,
    sicdesc as sic_desc,
    systemmodstamp as system_modstamp,
    website,

    academic_rigor__c as academic_rigor,
    account_count__c as account_count,
    accountsource as account_source,
    act_composite_25_75__c as act_composite_25_75,
    act25__c as act25,
    act75__c as act75,
    adjusted_6_year_graduation_rate__c as adjusted_6_year_graduation_rate,
    adjusted_6_year_minority_graduation_rate__c
    as adjusted_6_year_minority_graduation_rate,
    admission_term__c as admission_term,
    admission_type__c as admission_type,
    admissionscompletion_data_last_updated__c
    as admissions_completion_data_last_updated,
    african_american__c as african_american,
    african_american_hispanic_retention_rate__c
    as african_american_hispanic_retention_rate,
    alternate_names__c as alternate_names,
    ambassador_college__c as ambassador_college,
    annual_matriculation_target_max__c as annual_matriculation_target_max,
    annual_matriculation_target_min__c as annual_matriculation_target_min,
    campus_locale__c as campus_locale,
    cdu_external_id__c as cdu_external_id,
    ceeb__c as ceeb,
    closest_kipp_school__c as closest_kipp_school,
    college_connections_college__c as college_connections_college,
    college_navigator_link__c as college_navigator_link,
    college_powerranking__c as college_power_ranking,
    college_prep__c as college_prep,
    community_school_program__c as community_school_program,
    community_service_hours__c as community_service_hours,
    competitiveness_index__c as competitiveness_index,
    competitiveness_ranking__c as competitiveness_ranking,
    completion_compared_to_peers__c as completion_compared_to_peers,
    completion_within_competitiveness_rank__c as completion_within_competitiveness_rank,
    credits_required__c as credits_required,
    dep_total_applications_current_cycle__c as dep_total_applications_current_cycle,
    distance_from_nearest_kipp_school_mi__c as distance_from_nearest_kipp_school_mi,
    diversity__c as diversity,
    early_action_due_date__c as early_action_due_date,
    early_decision_due_date__c as early_decision_due_date,
    female__c as female,
    financial_aid_priority_due_date__c as financial_aid_priority_due_date,
    freshman_class_size__c as freshman_class_size,
    gender_specific__c as gender_specific,
    general_fee__c as general_fee,
    geographic_region__c as geographic_region,
    gpa_type__c as gpa_type,
    hbcu__c as hbcu,
    hispanic__c as hispanic,
    hsi__c as hsi,
    kipp_acceptance_rate_all_time__c as kipp_acceptance_rate_all_time,
    kipp_acceptance_rate_seniors__c as kipp_acceptance_rate_seniors,
    kipp_ambassador_college_end_date__c as kipp_ambassador_college_end_date,
    kipp_ambassador_college_start_date__c as kipp_ambassador_college_start_date,
    kipp_college_partner_end_date__c as kipp_college_partner_end_date,
    kipp_college_partner_start_date__c as kipp_college_partner_start_date,
    kipp_enrollment_rate_all_time__c as kipp_enrollment_rate_all_time,
    kipp_graduation_and_persistence_rate__c as kipp_graduation_and_persistence_rate,
    kipp_partnership_owner__c as kipp_partnership_owner,
    kipp_specific_graduation_rate__c as kipp_specific_graduation_rate,
    male__c as male,
    matriculation_target_progress_max__c as matriculation_target_progress_max,
    matriculation_target_progress_min__c as matriculation_target_progress_min,
    metro_area__c as metro_area,
    ncesid__c as nces_id,
    net_price__c as net_price,
    net_price_0_30k_income__c as net_price_0_30k_income,
    net_price_30_48k_income__c as net_price_30_48k_income,
    net_price_48_75k_income__c as net_price_48_75k_income,
    number_of_marking_periods__c as number_of_marking_periods,
    of_accepted_students_that_enroll__c as of_accepted_students_that_enroll,
    of_applicants_admitted__c as of_applicants_admitted,
    of_freshmen_receiving_pell_grants__c as of_freshmen_receiving_pell_grants,
    of_overall_students_receiving_pell__c as of_overall_students_receiving_pell,
    of_undergrads__c as of_undergrads,
    old_system_id__c as old_system_id,
    open_admissions__c as open_admissions,
    other_fee_amount__c as other_fee_amount,
    other_fees__c as other_fees,
    partner_college__c as partner_college,
    partner_graduation_and_persistence_rate__c
    as partner_graduation_and_persistence_rate,
    partnership_persistence_target__c as partnership_persistence_target,
    percent_in_state__c as percent_in_state,
    percent_out_of_state__c as percent_out_of_state,
    period_for_admissions_stats__c as period_for_admissions_stats,
    pr_regionalrank__c as pr_regional_rank,
    priority_application_due_date__c as priority_application_due_date,
    public_with_entrance_criteria__c as public_with_entrance_criteria,
    region__c as region,
    region_prefix__c as region_prefix,
    registration_fee__c as registration_fee,
    regular_decision_due_date__c as regular_decision_due_date,
    required_forms__c as required_forms,
    room_board__c as room_board,
    sat_math_25_75__c as sat_math_25_75,
    sat_reading_25_75__c as sat_reading_25_75,
    sat_writing_25_75__c as sat_writing_25_75,
    satmath25__c as sa_tmath25,
    satmath75__c as sa_tmath75,
    satread25__c as sa_tread25,
    satread75__c as sa_tread75,
    satwriting25__c as sa_twriting25,
    satwriting75__c as sa_twriting75,
    short_name__c as short_name,
    students_currently_enrolled__c as students_currently_enrolled,
    students_graduated__c as students_graduated,
    submitting_act__c as submitting_act,
    submitting_sat__c as submitting_sat,
    system_batch_sync_old_school_name__c as system_batch_sync_old_school_name,
    system_batch_sync_school_name__c as system_batch_sync_school_name,
    system_rollback_account_name__c as system_rollback_account_name,
    total_applications_current_cycle__c as total_applications_current_cycle,
    total_attending_or_graduated_enrollments__c
    as total_attending_or_graduated_enrollments,
    total_kipp_acceptances__c as total_kipp_acceptances,
    total_kipp_acceptances_all_time__c as total_kipp_acceptances_all_time,
    total_kipp_acceptances_seniors__c as total_kipp_acceptances_seniors,
    total_kipp_applications__c as total_kipp_applications,
    total_kipp_enrollments_all_time__c as total_kipp_enrollments_all_time,
    total_kipp_matric_enrollments_seniors__c as total_kipp_matric_enrollments_seniors,
    total_kipp_matriculations__c as total_kipp_matriculations,
    total_kipp_submitted_apps_all_time__c as total_kipp_submitted_apps_all_time,
    total_kipp_submitted_apps_seniors__c as total_kipp_submitted_apps_seniors,
    tuition__c as tuition,
    undergrad_size_range__c as undergrad_size_range,
    x1st_year_retention_rate__c as x1st_year_retention_rate,
    x6_yr_completion_rate__c as x6_yr_completion_rate,
    x6_yr_minority_completion_rate__c as x6_yr_minority_completion_rate,
    x6_yr_minority_transfer_rate__c as x6_yr_minority_transfer_rate,
    x6_yr_transfer_rate__c as x6_yr_transfer_rate,
from {{ source("kippadb", "account") }}
where not isdeleted