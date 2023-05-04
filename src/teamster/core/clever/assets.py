import pathlib

from dagster import (
    DynamicPartitionsDefinition,
    MultiPartitionsDefinition,
    OpExecutionContext,
    Output,
    ResourceParam,
    StaticPartitionsDefinition,
    asset,
)
from dagster_ssh import SSHResource
from numpy import nan
from pandas import read_csv

from teamster.core.clever.schema import ASSET_FIELDS
from teamster.core.utils.functions import get_avro_record_schema


def build_sftp_asset(
    asset_name, code_location, source_system, remote_filepath, op_tags={}
):
    @asset(
        name=asset_name,
        key_prefix=[code_location, source_system],
        metadata={
            "remote_filepath": remote_filepath,
            "remote_file_regex": (
                r"(?P<date>\d{4}-\d{2}-\d{2})[-\w+]+-(?P<type>\w+).csv"
            ),
        },
        io_manager_key="gcs_avro_io",
        partitions_def=MultiPartitionsDefinition(
            {
                "date": DynamicPartitionsDefinition(
                    name=f"{code_location}_{source_system}_{asset_name}_date"
                ),
                "type": StaticPartitionsDefinition(["staff", "students", "teachers"]),
            }
        ),
        op_tags=op_tags,
    )
    def _asset(
        context: OpExecutionContext, sftp_clever_reports: ResourceParam[SSHResource]
    ):
        remote_filepath = context.assets_def.metadata_by_key[context.assets_def.key][
            "remote_filepath"
        ]

        local_filepath = sftp_clever_reports.sftp_get(
            remote_filepath=(
                f"{remote_filepath}/"
                + context.partition_key.keys_by_dimension["date"]
                + f"-{remote_filepath}-"
                + context.partition_key.keys_by_dimension["type"]
                + ".csv"
            ),
            local_filepath=f"./data/{pathlib.Path(remote_filepath).name}",
        )

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
