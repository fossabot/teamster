with
    deduplicate as (
        {{
            dbt_utils.deduplicate(
                relation=source(
                    "schoolmint_grow", "src_schoolmint_grow__assignments"
                ),
                partition_by="_id",
                order_by="_file_name desc",
            )
        }}
    )

select
    _id as assignment_id,
    `name`,
    district,
    created,
    lastmodified,
    archivedat,
    coachingactivity,
    excludefrombank,
    goaltype,
    locked,
    parent,
    `private`,
    `type`,
    observation,
    user._id as user_id,
    user.name as user_name,
    user.email as user_email,
    creator._id as creator_id,
    creator.name as creator_name,
    creator.email as creator_email,
    progress._id as progress_id,
    progress.assigner as progress_assigner,
    progress.justification as progress_justification,
    progress.percent as progress_percent,
    progress.date as progress_date,
    school._id as school_id,
    school.name as school_name,
    grade._id as grade_id,
    grade.name as grade_name,
    course._id as course_id,
    course.name as course_name,
    tags,
from deduplicate
where _dagster_partition_archived = 'f'
