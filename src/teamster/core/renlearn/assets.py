import zipfile

from dagster import OpExecutionContext, Output, ResourceParam, asset
from dagster_ssh import SSHResource
from numpy import nan
from pandas import read_csv

from teamster.core.renlearn.schema import ASSET_FIELDS
from teamster.core.utils.classes import FiscalYearPartitionsDefinition
from teamster.core.utils.functions import get_avro_record_schema


def build_sftp_asset(
    asset_name,
    code_location,
    source_system,
    remote_filepath,
    remote_file_regex,
    partition_start_date,
    archive_filepath=None,
    op_tags={},
):
    @asset(
        name=asset_name,
        key_prefix=[code_location, source_system],
        metadata={
            "remote_filepath": remote_filepath,
            "remote_file_regex": remote_file_regex,
            "archive_filepath": archive_filepath,
        },
        io_manager_key="gcs_avro_io",
        partitions_def=FiscalYearPartitionsDefinition(
            start_date=partition_start_date, start_month=7, fmt="%Y-%m-%d"
        ),
        op_tags=op_tags,
    )
    def _asset(context: OpExecutionContext, sftp_renlearn: ResourceParam[SSHResource]):
        asset_metadata = context.assets_def.metadata_by_key[context.assets_def.key]

        remote_filepath = asset_metadata["remote_filepath"]
        remote_filename = asset_metadata["remote_file_regex"]
        archive_filepath = asset_metadata["archive_filepath"]

        local_filepath = sftp_renlearn.sftp_get(
            remote_filepath=f"{remote_filepath}/{remote_filename}",
            local_filepath=f"./data/{remote_filename}",
        )

        if archive_filepath is not None:
            with zipfile.ZipFile(file=local_filepath) as zf:
                zf.extract(member=archive_filepath, path="./data")

            local_filepath = f"./data/{archive_filepath}"

        df = read_csv(filepath_or_buffer=local_filepath, low_memory=False)
        df = df.replace({nan: None})

        yield Output(
            value=(
                df.to_dict(orient="records"),
                get_avro_record_schema(
                    name=asset_name, fields=ASSET_FIELDS[asset_name]
                ),
            ),
            metadata={"records": df.shape[0]},
        )

    return _asset
