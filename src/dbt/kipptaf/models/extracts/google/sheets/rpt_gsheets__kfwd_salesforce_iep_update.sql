select
    'TO ADD' as action,
    c.contact_id,
    coalesce(
        co.parent_consent_intial_iep_date, current_date('America/New_York')
    ) as most_recent_iep_date__c,
from {{ ref("base_powerschool__student_enrollments") }} as co
inner join
    {{ ref("int_kippadb__roster") }} as c
    on co.student_number = c.student_number
    and c.contact_most_recent_iep_date is null
where
    co.spedlep like 'SPED%'
    and co.academic_year = {{ var("current_academic_year") }}
    and co.rn_year = 1
    and co.grade_level >= 8
    and co.enroll_status = 0
    and c.contact_id is not null

union all

select 'TO DELETE' as action, c.contact_id, null as most_recent_iep_date__c,
from {{ ref("int_kippadb__roster") }} as c

inner join
    {{ ref("base_powerschool__student_enrollments") }} as co
    on c.student_number = co.student_number
    and co.spedlep not like 'SPED%'
    and co.academic_year = {{ var("current_academic_year") }}
    and co.rn_year = 1
    and co.grade_level >= 8
    and co.enroll_status = 0
where c.contact_most_recent_iep_date is not null
