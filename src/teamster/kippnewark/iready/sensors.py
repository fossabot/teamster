from teamster.core.iready.sensors import build_sftp_sensor

from .. import CODE_LOCATION, LOCAL_TIMEZONE
from . import assets

sftp_sensor = build_sftp_sensor(
    code_location=CODE_LOCATION,
    source_system="iready",
    asset_defs=assets,
    timezone=LOCAL_TIMEZONE,
    minimum_interval_seconds=(60 * 10),
)

__all__ = [
    sftp_sensor,
]