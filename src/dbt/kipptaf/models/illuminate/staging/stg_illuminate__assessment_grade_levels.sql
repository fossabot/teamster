select
    assessment_grade_level_id,
    assessment_id,
    grade_level_id,
    grade_level_id - 1 as grade_level,
from {{ source("illuminate", "assessment_grade_levels") }}
where not _fivetran_deleted
