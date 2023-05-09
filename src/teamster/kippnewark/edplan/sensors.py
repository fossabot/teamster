from teamster.core.edplan.sensors import build_sftp_sensor

from .. import CODE_LOCATION
from . import assets

sftp_sensor = build_sftp_sensor(
    code_location=CODE_LOCATION, source_system="edplan", asset_defs=assets
)

__all__ = [
    sftp_sensor,
]
