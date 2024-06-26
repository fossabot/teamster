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
    coachingactivity as coaching_activity,
    excludefrombank as exclude_from_bank,
    goaltype as goal_type,
    locked,
    `private`,
    `type`,
    observation,

    {# records #}
    user._id as user_id,
    user.name as user_name,
    user.email as user_email,
    creator._id as creator_id,
    creator.name as creator_name,
    creator.email as creator_email,
    parent._id as parent_id,
    parent.name as parent_name,
    progress._id as progress_id,
    progress.assigner as progress_assigner,
    progress.justification as progress_justification,
    progress.percent as progress_percent,
    progress.date as progress_date,

    {# repeated records #}
    tags,

    timestamp(created) as created,
    timestamp(lastmodified) as last_modified,
    timestamp(archivedat) as archived_at,

    date(timestamp(created), '{{ var("local_timezone") }}') as created_date_local,
from deduplicate
where _dagster_partition_archived = 'f'
