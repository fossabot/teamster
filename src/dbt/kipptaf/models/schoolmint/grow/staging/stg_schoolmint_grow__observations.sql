with
    deduplicate as (
        {{
            dbt_utils.deduplicate(
                relation=source(
                    "schoolmint_grow", "src_schoolmint_grow__observations"
                ),
                partition_by="_id",
                order_by="_file_name desc",
            )
        }}
    )

select
    observation_id,
    `name`,
    district,
    created,
    lastmodified,
    archivedat,
    assignactionstepwidgettext,
    isprivate,
    ispublished,
    locked,
    observationmodule,
    observationtag1,
    observationtag2,
    observationtag3,
    observationtype,
    privatenotes1,
    privatenotes2,
    privatenotes3,
    privatenotes4,
    quickhits,
    requiresignature,
    score,
    scoreaveragedbystrand,
    sendemail,
    sharednotes1,
    sharednotes2,
    sharednotes3,
    signed,
    observedat,
    firstpublished,
    observeduntil,
    viewedbyteacher,
    signedat,
    lastpublished,
    rubric._id as rubric_id,
    rubric.name as rubric_name,
    observer._id as observer_id,
    observer.name as observer_name,
    observer.email as observer_email,
    teacher._id as teacher_id,
    teacher.name as teacher_name,
    teacher.email as teacher_email,
    teachingassignment._id as teachingassignment_id,
    teachingassignment.school as teachingassignment_school,
    teachingassignment.course as teachingassignment_course,
    teachingassignment.grade as teachingassignment_grade,
    teachingassignment.gradelevel as teachingassignment_gradelevel,
    teachingassignment.period as teachingassignment_period,
    tagnotes1.notes as tagnotes1_notes,
    tagnotes2.notes as tagnotes2_notes,
    tagnotes3.notes as tagnotes3_notes,
    tagnotes4.notes as tagnotes4_notes,

    attachments,
    comments,
    eventlog,
    files,
    listtwocolumna,
    listtwocolumnapaired,
    listtwocolumnb,
    listtwocolumnbpaired,
    magicnotes,
    meetings,
    observationscores,
    tags,
    videonotes,
    videos,
from deduplicate
where _dagster_partition_archived = 'f'