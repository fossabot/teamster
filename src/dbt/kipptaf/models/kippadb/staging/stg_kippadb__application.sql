select
    id,
    `name`,
    recordtypeid as record_type_id,
    createdbyid as created_by_id,
    createddate as created_date,
    lastactivitydate as last_activity_date,
    lastmodifiedbyid as last_modified_by_id,
    lastmodifieddate as last_modified_date,
    lastreferenceddate as last_referenced_date,
    lastvieweddate as last_viewed_date,
    systemmodstamp as system_modstamp,

    abc_referral__c as abc_referral,
    admission_term__c as admission_term,
    advisor_rank__c as advisor_rank,
    anticipated_housing_situation__c as anticipated_housing_situation,
    applicant__c as applicant,
    application_admission_type__c as application_admission_type,
    application_count__c as application_count,
    application_source__c as application_source,
    application_status__c as application_status,
    application_submission_status__c as application_submission_status,
    archived_application__c as archived_application,
    books_and_supplies__c as books_and_supplies,
    calculated_due_date__c as calculated_due_date,
    commitment_form_sent__c as commitment_form_sent,
    css_profile_submitted_to_college__c as css_profile_submitted_to_college,
    date_of_initial_interest__c as date_of_initial_interest,
    days_until_due_date__c as days_until_due_date,
    due_date__c as due_date,
    due_date_status__c as due_date_status,
    due_date_status_color__c as due_date_status_color,
    early_action_due_date__c as early_action_due_date,
    early_decision_due_date__c as early_decision_due_date,
    efc_from_fafsa__c as efc_from_fafsa,
    english_teacher_recommendation_submitted__c
    as english_teacher_recommendation_submitted,
    expected_hs_graduation_date__c as expected_hs_graduation_date,
    fafsa_submitted_to_college__c as fafsa_submitted_to_college,
    financial_aid_eligibility__c as financial_aid_eligibility,
    financial_aid_entered__c as financial_aid_entered,
    financial_aid_priority_due_date__c as financial_aid_priority_due_date,
    gpa__c as gpa,
    gpa_type__c as gpa_type,
    honors_special_program_name__c as honors_special_program_name,
    honors_special_program_status__c as honors_special_program_status,
    intended_degree_type__c as intended_degree_type,
    intended_major__c as intended_major,
    intended_major_area__c as intended_major_area,
    interview_date__c as interview_date,
    interview_status__c as interview_status,
    match_type__c as match_type,
    math_teacher_recommendation_submitted__c as math_teacher_recommendation_submitted,
    matriculation_decision__c as matriculation_decision,
    miscellaneous_expenses__c as miscellaneous_expenses,
    net_cost_out_of_pocket__c as net_cost_out_of_pocket,
    odds_of_admission__c as odds_of_admission,
    other_intended_major__c as other_intended_major,
    other_reason_for_not_attending__c as other_reason_for_not_attending,
    parent_section_due_date__c as parent_section_due_date,
    parent_section_submitted__c as parent_section_submitted,
    primary_reason_for_not_attending__c as primary_reason_for_not_attending,
    principal_recommenation_submitted__c as principal_recommenation_submitted,
    priority_application_due_date__c as priority_application_due_date,
    recruitment_activity_participation__c as recruitment_activity_participation,
    regular_decision_due_date__c as regular_decision_due_date,
    required_forms__c as required_forms,
    required_forms_completed__c as required_forms_completed,
    room_board__c as room_board,
    school__c as school,
    school_section_due_date__c as school_section_due_date,
    school_section_submitted__c as school_section_submitted,
    starting_application_status__c as starting_application_status,
    student_rank__c as student_rank,
    student_section_due_date__c as student_section_due_date,
    student_section_submitted__c as student_section_submitted,
    total_aid_accepted__c as total_aid_accepted,
    total_aid_available__c as total_aid_available,
    total_cost_of_attendance__c as total_cost_of_attendance,
    total_federal_loans__c as total_federal_loans,
    total_gift_aid__c as total_gift_aid,
    total_work_study__c as total_work_study,
    transfer_application__c as transfer_application,
    transportation__c as transportation,
    tuition_and_fees__c as tuition_and_fees,
    type__c as `type`,
    type_for_roll_ups__c as type_for_roll_ups,
    unmet_need__c as unmet_need,
    waitlist_placement__c as waitlist_placement,
    year_aid_package_received__c as year_aid_package_received,
from {{ source("kippadb", "application") }}
where not isdeleted