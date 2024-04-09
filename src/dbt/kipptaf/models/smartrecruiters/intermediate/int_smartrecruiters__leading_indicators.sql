with
    applications as (
        select
            application_id,
            application_state,
            application_status,
            candidate_id,
            department_internal,
            job_city,
            job_title,
            recruiters,
            source_subtype,
            source_type,
            `source`,
            application_reason_for_rejection,
            application_reason_for_withdrawal,
            application_status_before_rejection,
            application_status_before_withdrawal,
            application_state_new_date as application_date,
            application_state_hired_date as hired_date,
            application_state_in_review_date as review_date,
            application_state_interview_date as interview_date,
            application_state_lead_date as lead_date,
            application_state_offer_date as offer_date,
            application_state_rejected_date as rejected_date,
            application_state_transferred_date as transferred_date,
            application_state_withdrawn_date as withdrawn_date,
            application_status_in_review_resume_review_date
            as in_review_resume_review_date,
            application_status_interview_demo_date as interview_demo_date,
            application_status_interview_phone_screen_complete_date
            as phone_screen_complete_date,
            application_status_interview_phone_screen_requested_date
            as phone_screen_requested_date,
            application_status_interview_performance_task_date
            as interview_performance_task_date,
            application_status_in_review_performance_task_date
            as in_review_performance_task_date

        from {{ source("smartrecruiters", "src_smartrecruiters__applications") }}
    ),

    applications_unpivot as (
        select
            application_id,
            application_state,
            application_status,
            candidate_id,
            department_internal,
            job_city,
            job_title,
            recruiters,
            source_subtype,
            source_type,
            `source`,
            name_column,
            values_column,
        from
            applications unpivot (
                values_column for name_column in (
                    application_date,
                    hired_date,
                    review_date,
                    interview_date,
                    lead_date,
                    offer_date,
                    rejected_date,
                    transferred_date,
                    withdrawn_date,
                    in_review_resume_review_date,
                    interview_demo_date,
                    phone_screen_complete_date,
                    phone_screen_requested_date,
                    interview_performance_task_date,
                    in_review_performance_task_date
                )
            ) as u
    )

select
    au.application_id,
    au.application_state,
    au.application_status,
    au.candidate_id,
    au.department_internal,
    au.job_city,
    au.job_title,
    au.recruiters,
    au.source_subtype,
    au.source_type,
    au.source,
    au.name_column as status_type,
    au.values_column as date_val,

    a.candidate_last_name,
    a.candidate_first_name,
    a.candidate_email,
    a.current_employer,
    a.candidate_tags_values,
    a.screening_question_answer_new_jersey_miami_affiliated_orgs as taf_affiliated_orgs,
    a.screening_question_answer_new_jersey_miami_other_orgs as taf_other_orgs,
    a.screening_question_answer_new_jersey_miami_current_or_former_kipp_employee
    as taf_current_or_former_kipp_employee,
    a.screening_question_answer_new_jersey_miami_expected_salary as taf_expected_salary,
    a.screening_question_answer_national_race as kf_race,
    a.screening_question_answer_national_gender as kf_gender,
    a.screening_question_answer_national_are_you_alumnus as kf_are_you_alumnus,
    a.screening_question_answer_national_in_which_regions_alumnus
    as kf_in_which_regions_alumnus,
    a.screening_question_answer_new_jersey_out_of_state_sped_credits as nj_sped_credits,
    -- trunk-ignore(sqlfluff/LT05)
    a.screening_question_answer_new_jersey_miami_current_or_former_kipp_nj_miami_employee
    as former_kippnjmia,
    concat(a.candidate_last_name, ', ', a.candidate_first_name) as candidate_last_first,
    coalesce(
        a.application_field_school_shared_with_new_jersey,
        a.application_field_school_shared_with_miami
    ) as school_shared_with,
    coalesce(
        a.screening_question_answer_new_jersey_undergrad_gpa,
        a.screening_question_answer_miami_undergrad_gpa
    ) as undergrad_gpa,
    coalesce(
        a.screening_question_answer_new_jersey_grad_gpa,
        a.screening_question_answer_miami_grad_gpa
    ) as grad_gpa,
    coalesce(
        a.screening_question_answer_new_jersey_teacher_certification_question,
        a.screening_question_answer_miami_teacher_certification_question
    ) as certification_instate,
    coalesce(
        -- trunk-ignore(sqlfluff/LT05)
        a.screening_question_answer_new_jersey_out_of_state_teacher_certification_details,
        a.screening_question_answer_miami_out_of_state_teaching_certification_details
    ) as certification_outstate,
from applications_unpivot as au
left join
    {{ source("smartrecruiters", "src_smartrecruiters__applicants") }} as a
    on au.application_id = a.application_id
