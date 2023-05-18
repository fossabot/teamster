import pendulum
from dagster import StaticPartitionsDefinition, config_from_files

from teamster.core.sftp.assets import build_sftp_asset
from teamster.core.titan.schema import ASSET_FIELDS
from teamster.core.utils.classes import FiscalYear


def build_titan_sftp_assets(config_dir, code_location, fiscal_year, timezone):
    sftp_assets = []

    for a in config_from_files([f"{config_dir}/assets.yaml"])["assets"]:
        start_fy = FiscalYear(
            datetime=pendulum.from_format(
                string=a["partition_start_date"], fmt="YYYY-MM-DD", tz=timezone
            ),
            start_month=7,
        )

        partitions_def = StaticPartitionsDefinition(
            [
                str(fy - 1)
                for fy in range(start_fy.fiscal_year, (fiscal_year.fiscal_year + 1))
            ]
        )

        asset = build_sftp_asset(
            code_location=code_location,
            source_system="titan",
            asset_fields=ASSET_FIELDS,
            partitions_def=partitions_def,
            **a,
        )

        sftp_assets.append(asset)

    return sftp_assets
