from teamster.core.alchemer.assets import build_partition_assets
from teamster.kipptaf import CODE_LOCATION

(
    survey,
    survey_question,
    survey_campaign,
    survey_response_disqualified,
    survey_response,
) = build_partition_assets(code_location=CODE_LOCATION)

survey_metadata_assets = [survey, survey_campaign, survey_question]

__all__ = [
    *survey_metadata_assets,
    survey_response_disqualified,
    survey_response,
]
