select
    nullif(rosterid, '') as `roster_id`,
    nullif(active, '') as `active`,
    nullif(collecthw, '') as `collect_hw`,
    nullif(coursenumber, '') as `course_number`,
    nullif(gradelevels, '') as `grade_levels`,
    nullif(lastsynced, '') as `last_synced`,
    nullif(markercolor, '') as `marker_color`,
    nullif(masterid, '') as `master_id`,
    nullif(mastername, '') as `master_name`,
    nullif(meetingdays, '') as `meeting_days`,
    nullif(`period`, '') as `period`,
    nullif(room, '') as `room`,
    nullif(rostername, '') as `roster_name`,
    nullif(rostertype, '') as `roster_type`,
    nullif(rostertypeid, '') as `roster_type_id`,
    nullif(rtifocusid, '') as `rti_focus_id`,
    nullif(rtitier, '') as `rti_tier`,
    nullif(schoolid, '') as `school_id`,
    nullif(screensetid, '') as `screen_set_id`,
    nullif(screensetname, '') as `screen_set_name`,
    nullif(secondaryintegrationid, '') as `secondary_integration_id`,
    nullif(sectionnumber, '') as `section_number`,
    nullif(showroster, '') as `show_roster`,
    nullif(sisexpression, '') as `sis_expression`,
    nullif(sisgradebookname, '') as `sis_gradebook_name`,
    nullif(siskey, '') as `sis_key`,
    nullif(studentcount, '') as `student_count`,
    nullif(subjectid, '') as `subject_id`,
    nullif(subjectname, '') as `subject_name`,
    nullif(takeattendance, '') as `take_attendance`,
    nullif(takeclassattendance, '') as `take_class_attendance`,
from {{ source("deanslist", "src_deanslist__rosters") }}
