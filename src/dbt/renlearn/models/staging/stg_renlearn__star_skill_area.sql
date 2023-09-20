select
    assessmentid as `assessment_id`,
    completeddate as `completed_date`,
    completeddatelocal as `completed_date_local`,
    domainname as `domain_name`,
    domainscore as `domain_score`,
    familyname as `family_name`,
    launchdate as `launch_date`,
    renaissanceclientid as `renaissance_client_id`,
    schoolyear as `school_year`,
    skillareaname as `skill_area_name`,
    studentidentifier as `student_identifier`,
    studentrenaissanceid as `student_renaissance_id`,
    studentsourcedid as `student_sourced_id`,
    studentstateid as `student_state_id`,
    studentuserid as `student_user_id`,
    skillareamasteryscore as `skill_area_mastery_score`,
    _dagster_partition_fiscal_year as `_dagster_partition_fiscal_year`,
    _dagster_partition_subject as `_dagster_partition_subject`,
from {{ source("renlearn", "src_renlearn__star_skill_area") }}
