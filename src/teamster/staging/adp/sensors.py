from teamster.core.adp.sensors import build_sftp_sensor

from .. import CODE_LOCATION, LOCAL_TIMEZONE
from .assets import sftp_assets

sftp_sensor = build_sftp_sensor(
    code_location=CODE_LOCATION,
    source_system="adp",
    asset_defs=sftp_assets,
    timezone=LOCAL_TIMEZONE,
    minimum_interval_seconds=600,
)

__all__ = [
    sftp_sensor,
]