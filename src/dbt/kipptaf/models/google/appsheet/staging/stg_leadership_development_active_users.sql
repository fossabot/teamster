select *,
from {{ source("google_appsheet", "src_leadership_development_active_users") }}
