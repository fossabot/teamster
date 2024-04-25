from teamster.core.couchdrop.sensors import build_couchdrop_sftp_sensor

from .. import CODE_LOCATION, LOCAL_TIMEZONE
from ..fldoe.assets import _all

couchdrop_sftp_sensor = build_couchdrop_sftp_sensor(
    code_location=CODE_LOCATION, local_timezone=LOCAL_TIMEZONE, assets=_all
)

__all__ = [
    couchdrop_sftp_sensor,
]
