with
    form_responses as (
        select
            response_id,
            respondent_email,
            item_abbreviation,
            safe_cast(last_submitted_time as timestamp) as last_submitted_time,
            coalesce(text_value, file_upload_file_id) as pivot_column_value,
        from {{ ref("base_google_forms__form_responses") }}
        where form_id = '1jpeMof_oQ9NzTw85VFsA5A7G9VrH3XkSc_nZDFz07nA'
    ),

    response_pivot as (
        select
            response_id,
            respondent_email,
            last_submitted_time,

            /* pivot cols */
            additional_languages,
            cert_barriers,
            cert_out_of_state_details,
            cert_required,
            cert_status,
            cert_steps_taken,
            fl_additional_cert_1,
            fl_cert_endorsement_1,
            fl_cert_endorsement_2,
            fl_cert_endorsement_3,
            fl_cert_endorsement_4,
            fl_cert_endorsement_5,
            fl_cert_expiration_1,
            fl_cert_expiration_2,
            fl_cert_expiration_3,
            fl_cert_expiration_4,
            fl_cert_expiration_5,
            fl_open_to_student_teacher,
            gender_identity,
            languages_spoken,
            level_of_education,
            nj_cert_additional_1,
            nj_cert_document_link_1,
            nj_cert_document_link_2,
            nj_cert_document_link_3,
            nj_cert_document_link_4,
            nj_cert_document_link_5,
            nj_cert_endorsement_1,
            nj_cert_endorsement_2,
            nj_cert_endorsement_3,
            nj_cert_endorsement_4,
            nj_cert_endorsement_5,
            nj_cert_issue_date_1,
            nj_cert_issue_date_2,
            nj_cert_issue_date_3,
            nj_cert_issue_date_4,
            nj_cert_issue_date_5,
            nj_cert_type_1,
            nj_cert_type_2,
            nj_cert_type_3,
            nj_cert_type_4,
            nj_cert_type_5,
            race_ethnicity,
            respondent_name,
            undergraduate_school,
            updates_open_ended,
            praxis_document_link,
            safe_cast(years_teaching_in_njfl as numeric) as years_teaching_in_njfl,
            safe_cast(years_exp_outside_kipp as numeric) as years_exp_outside_kipp,
            safe_cast(
                years_teaching_outside_njfl as numeric
            ) as years_teaching_outside_njfl,
            safe_cast(
                regexp_extract(respondent_name, r'(\d{6})') as int
            ) as employee_number,
            replace(alumni_status, ',', '.') as alumni_status,
            replace(path_to_education, ',', '.') as path_to_education,
            replace(relay_status, ',', '.') as relay_status,
            replace(
                community_grew_up, 'Newark, Camden, and/or Miami', 'the cities we serve'
            ) as community_grew_up,
            replace(
                community_professional_exp,
                'Newark, Camden, and/or Miami',
                'the cities we serve'
            ) as community_professional_exp,
        from
            form_responses pivot (
                max(pivot_column_value) for item_abbreviation in (
                    'additional_languages',
                    'alumni_status',
                    'cert_barriers',
                    'cert_out_of_state_details',
                    'cert_required',
                    'cert_status',
                    'cert_steps_taken',
                    'community_grew_up',
                    'community_professional_exp',
                    'fl_additional_cert_1',
                    'fl_cert_endorsement_1',
                    'fl_cert_endorsement_2',
                    'fl_cert_endorsement_3',
                    'fl_cert_endorsement_4',
                    'fl_cert_endorsement_5',
                    'fl_cert_expiration_1',
                    'fl_cert_expiration_2',
                    'fl_cert_expiration_3',
                    'fl_cert_expiration_4',
                    'fl_cert_expiration_5',
                    'fl_open_to_student_teacher',
                    'gender_identity',
                    'languages_spoken',
                    'level_of_education',
                    'nj_cert_additional_1',
                    'nj_cert_document_link_1',
                    'nj_cert_document_link_2',
                    'nj_cert_document_link_3',
                    'nj_cert_document_link_4',
                    'nj_cert_document_link_5',
                    'nj_cert_endorsement_1',
                    'nj_cert_endorsement_2',
                    'nj_cert_endorsement_3',
                    'nj_cert_endorsement_4',
                    'nj_cert_endorsement_5',
                    'nj_cert_issue_date_1',
                    'nj_cert_issue_date_2',
                    'nj_cert_issue_date_3',
                    'nj_cert_issue_date_4',
                    'nj_cert_issue_date_5',
                    'nj_cert_type_1',
                    'nj_cert_type_2',
                    'nj_cert_type_3',
                    'nj_cert_type_4',
                    'nj_cert_type_5',
                    'path_to_education',
                    'race_ethnicity',
                    'relay_status',
                    'respondent_name',
                    'undergraduate_school',
                    'years_exp_outside_kipp',
                    'years_teaching_in_njfl',
                    'years_teaching_outside_njfl',
                    'updates_open_ended',
                    'praxis_document_link'
                )
            )
    ),

    multiselect_options as (
        select
            response_id,
            string_agg(alumni_status) as alumni_status,
            string_agg(community_grew_up) as community_grew_up,
            string_agg(community_professional_exp) as community_professional_exp,
            string_agg(languages_spoken) as languages_spoken,
            string_agg(path_to_education) as path_to_education,
            string_agg(race_ethnicity) as race_ethnicity,
            string_agg(relay_status) as relay_status,
        from response_pivot
        group by response_id
    ),

    response_union as (  -- noqa: ST03
        select
            rp.response_id,
            rp.respondent_email,
            rp.last_submitted_time,

            rp.employee_number,
            rp.respondent_name,

            rp.additional_languages,
            rp.cert_barriers,
            rp.cert_out_of_state_details,
            rp.cert_status,
            rp.cert_steps_taken,
            rp.fl_cert_endorsement_1,
            rp.fl_cert_endorsement_2,
            rp.fl_cert_endorsement_3,
            rp.fl_cert_endorsement_4,
            rp.fl_cert_endorsement_5,
            rp.fl_open_to_student_teacher,
            rp.gender_identity,
            rp.level_of_education,
            rp.nj_cert_document_link_1,
            rp.nj_cert_document_link_2,
            rp.nj_cert_document_link_3,
            rp.nj_cert_document_link_4,
            rp.nj_cert_document_link_5,
            rp.nj_cert_endorsement_1,
            rp.nj_cert_endorsement_2,
            rp.nj_cert_endorsement_3,
            rp.nj_cert_endorsement_4,
            rp.nj_cert_endorsement_5,
            rp.nj_cert_type_1,
            rp.nj_cert_type_2,
            rp.nj_cert_type_3,
            rp.nj_cert_type_4,
            rp.nj_cert_type_5,
            rp.undergraduate_school,
            rp.years_exp_outside_kipp,
            rp.years_teaching_in_njfl,
            rp.years_teaching_outside_njfl,
            rp.updates_open_ended,
            rp.praxis_document_link,
            safe_cast(rp.fl_cert_expiration_1 as date) as fl_cert_expiration_1,
            safe_cast(rp.fl_cert_expiration_2 as date) as fl_cert_expiration_2,
            safe_cast(rp.fl_cert_expiration_3 as date) as fl_cert_expiration_3,
            safe_cast(rp.fl_cert_expiration_4 as date) as fl_cert_expiration_4,
            safe_cast(rp.fl_cert_expiration_5 as date) as fl_cert_expiration_5,
            safe_cast(rp.nj_cert_issue_date_1 as date) as nj_cert_issue_date_1,
            safe_cast(rp.nj_cert_issue_date_2 as date) as nj_cert_issue_date_2,
            safe_cast(rp.nj_cert_issue_date_3 as date) as nj_cert_issue_date_3,
            safe_cast(rp.nj_cert_issue_date_4 as date) as nj_cert_issue_date_4,
            safe_cast(rp.nj_cert_issue_date_5 as date) as nj_cert_issue_date_5,
            if(rp.cert_required = 'Yes', true, false) as cert_required,
            if(rp.fl_additional_cert_1 = 'Yes', true, false) as fl_additional_cert_1,
            if(rp.nj_cert_additional_1 = 'Yes', true, false) as nj_cert_additional_1,

            mo.alumni_status,
            mo.community_grew_up,
            mo.community_professional_exp,
            mo.languages_spoken,
            mo.path_to_education,
            mo.race_ethnicity,
            mo.relay_status,
        from response_pivot as rp
        inner join multiselect_options as mo on rp.response_id = mo.response_id

        union all

        select
            null as response_id,
            respondent_email,
            `timestamp` as last_submitted_time,

            safe_cast(
                regexp_extract(respondent_name, r'(\d{6})') as int
            ) as employee_number,
            respondent_name,

            null as additional_languages,
            null as cert_barriers,
            null as cert_out_of_state_details,
            null as cert_status,
            null as cert_steps_taken,
            null as fl_cert_endorsement_1,
            null as fl_cert_endorsement_2,
            null as fl_cert_endorsement_3,
            null as fl_cert_endorsement_4,
            null as fl_cert_endorsement_5,
            null as fl_open_to_student_teacher,
            gender_identity,
            level_of_education,
            null as nj_cert_document_link_1,
            null as nj_cert_document_link_2,
            null as nj_cert_document_link_3,
            null as nj_cert_document_link_4,
            null as nj_cert_document_link_5,
            null as nj_cert_endorsement_1,
            null as nj_cert_endorsement_2,
            null as nj_cert_endorsement_3,
            null as nj_cert_endorsement_4,
            null as nj_cert_endorsement_5,
            null as nj_cert_type_1,
            null as nj_cert_type_2,
            null as nj_cert_type_3,
            null as nj_cert_type_4,
            null as nj_cert_type_5,
            undergraduate_school,
            years_exp_outside_kipp,
            years_teaching_in_njfl,
            years_teaching_outside_njfl,
            null as fl_cert_expiration_1,
            null as fl_cert_expiration_2,
            null as fl_cert_expiration_3,
            null as fl_cert_expiration_4,
            null as fl_cert_expiration_5,
            null as nj_cert_issue_date_1,
            null as nj_cert_issue_date_2,
            null as nj_cert_issue_date_3,
            null as nj_cert_issue_date_4,
            null as nj_cert_issue_date_5,
            null as cert_required,
            null as fl_additional_cert_1,
            null as nj_cert_additional_1,
            null as updates_open_ended,
            null as praxis_document_link,

            /* multiselect_options */
            alumni_status,
            community_grew_up,
            community_professional_experience as community_professional_exp,
            languages_spoken,
            path_to_education,
            race_ethnicity,
            relay_status,
        from {{ ref("stg_surveys__staff_info_archive") }}
    ),

    deduplicate as (
        {{
            dbt_utils.deduplicate(
                relation="response_union",
                partition_by="employee_number",
                order_by="last_submitted_time desc",
            )
        }}
    )

select  -- noqa: AM04
    *,
    case
        when regexp_contains(race_ethnicity, 'I decline to state')
        then 'Decline to State'
        when race_ethnicity = 'Latinx/Hispanic/Chicana(o)'
        then 'Latinx/Hispanic/Chicana(o)'
        when race_ethnicity = 'My racial/ethnic identity is not listed'
        then 'Race/Ethnicity Not Listed'
        when regexp_contains(race_ethnicity, 'Bi/Multiracial')
        then 'Bi/Multiracial'
        when regexp_contains(race_ethnicity, ',')
        then 'Bi/Multiracial'
        else race_ethnicity
    end as race_ethnicity_reporting,

    row_number() over (
        partition by employee_number order by last_submitted_time desc
    ) as rn_submission,
from deduplicate
