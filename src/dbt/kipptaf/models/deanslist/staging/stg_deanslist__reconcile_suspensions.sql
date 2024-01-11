select
    dlincidentid as dl_incident_id,
    studentid as student_id,
    schoolname as school_name,
    studentfirst as student_first_name,
    studentlast as student_last_name,
    consequence as consequence,
    attendancebehavior as attendance_behavior,
    submittedfn as submitted_first_name,
    submittedln as submitted_last_name,
    safe_cast(submittedat as datetime) as submitted_at,
    safe_cast(constart as date) as consequence_start_date,
    safe_cast(conend as date) as consequence_end_date,
    safe_cast(attendancedate as date) as attendance_date,
from {{ source("deanslist", "src_deanslist__reconcile_suspensions") }}