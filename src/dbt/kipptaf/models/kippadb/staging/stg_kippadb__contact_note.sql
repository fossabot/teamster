select
    id,
    `name`,
    academic_color__c as academic_color,
    advisor_activity__c as advisor_activity,
    category__c as category,
    college_connection_event_type__c as college_connection_event_type,
    college_connections_contact__c as college_connections_contact,
    comments__c as comments,
    contact__c as contact,
    contact_note_count__c as contact_note_count,
    createdbyid as created_by_id,
    createddate as created_date,
    current_category_ranking__c as current_category_ranking,
    date__c as `date`,
    financial_color__c as financial_color,
    initiated_by_student__c as initiated_by_student,
    kipp_sf_user_id__c as kipp_sf_user_id,
    lastactivitydate as last_activity_date,
    lastmodifiedbyid as last_modified_by_id,
    lastmodifieddate as last_modified_date,
    lastreferenceddate as last_referenced_date,
    lastvieweddate as last_viewed_date,
    meaningful_contact__c as meaningful_contact,
    next_steps__c as next_steps,
    note_count__c as note_count,
    overall_benchmark_color__c as overall_benchmark_color,
    passion_purpose_plan_color__c as passion_purpose_plan_color,
    related_college_benchmark__c as related_college_benchmark,
    socio_emotional_color__c as socio_emotional_color,
    status__c as `status`,
    subject__c as `subject`,
    systemmodstamp as system_modstamp,
    type__c as `type`,

    {{
        teamster_utils.date_to_fiscal_year(
            date_field="date__c", start_month=7, year_source="start"
        )
    }} as academic_year,
from {{ source("kippadb", "contact_note") }}
where not isdeleted
