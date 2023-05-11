import re
import zipfile

from dagster import (
    DagsterInvariantViolationError,
    MultiPartitionsDefinition,
    OpExecutionContext,
    Output,
    asset,
)
from dagster_ssh import SSHResource
from numpy import nan
from pandas import read_csv
from slugify import slugify

from teamster.core.utils.functions import get_avro_record_schema, regex_pattern_replace


def compose_remote_file_regex(remote_file_regex, context: OpExecutionContext):
    context.log.debug(remote_file_regex)
    try:
        partitions_def = context.asset_partitions_def_for_output()
        context.log.debug(partitions_def)
    except DagsterInvariantViolationError as e:
        context.log.error(e)
        return remote_file_regex

    if isinstance(partitions_def, MultiPartitionsDefinition):
        context.log.debug(context.partition_key.keys_by_dimension)
        for group_name, replacement in context.partition_key.keys_by_dimension.items():
            context.log.debug(group_name)
            context.log.debug(replacement)
        return regex_pattern_replace(
            pattern=remote_file_regex,
            replacements=context.partition_key.keys_by_dimension,
        )
    else:
        compiled_regex = re.compile(pattern=remote_file_regex)
        context.log.debug(compiled_regex)
        pattern_keys = compiled_regex.groupindex.keys()
        context.log.debug(pattern_keys)
        return regex_pattern_replace(
            pattern=remote_file_regex,
            replacements={key: context.partition_key for key in pattern_keys},
        )


def build_sftp_asset(
    asset_name,
    code_location,
    source_system,
    remote_filepath,
    remote_file_regex,
    asset_fields,
    archive_filepath=None,
    partitions_def=None,
    auto_materialize_policy=None,
    slugify_cols=False,
    op_tags={},
    **kwargs,
):
    @asset(
        name=asset_name,
        key_prefix=[code_location, source_system],
        metadata={
            "remote_filepath": remote_filepath,
            "remote_file_regex": remote_file_regex,
            "archive_filepath": archive_filepath,
        },
        required_resource_keys={f"sftp_{source_system}"},
        io_manager_key="gcs_avro_io",
        partitions_def=partitions_def,
        op_tags=op_tags,
        auto_materialize_policy=auto_materialize_policy,
    )
    def _asset(context: OpExecutionContext):
        ssh: SSHResource = getattr(context.resources, f"sftp_{source_system}")
        asset_metadata = context.assets_def.metadata_by_key[context.assets_def.key]

        remote_filepath = asset_metadata["remote_filepath"]
        archive_filepath = asset_metadata["archive_filepath"]
        remote_file_regex = compose_remote_file_regex(
            remote_file_regex=asset_metadata["remote_file_regex"], context=context
        )
        context.log.debug(remote_file_regex)

        # list files remote filepath
        conn = ssh.get_connection()
        with conn.open_sftp() as sftp_client:
            ls = sftp_client.listdir_attr(path=remote_filepath)
        conn.close()
        context.log.debug(ls)

        # find matching file for partition
        remote_filename = [
            f.filename
            for f in ls
            if re.match(pattern=remote_file_regex, string=f.filename) is not None
        ][0]

        # download file from sftp
        local_filepath = ssh.sftp_get(
            remote_filepath=f"{remote_filepath}/{remote_filename}",
            local_filepath=f"./data/{remote_filename}",
        )

        # unzip file, if necessary
        if archive_filepath is not None:
            with zipfile.ZipFile(file=local_filepath) as zf:
                zf.extract(member=archive_filepath, path="./data")

            local_filepath = f"./data/{archive_filepath}"

        # load file into pandas and prep for output
        df = read_csv(filepath_or_buffer=local_filepath, low_memory=False)
        df = df.replace({nan: None})
        if slugify_cols:
            df.rename(columns=lambda x: slugify(text=x, separator="_"), inplace=True)

        yield Output(
            value=(
                df.to_dict(orient="records"),
                get_avro_record_schema(
                    name=asset_name, fields=asset_fields[asset_name]
                ),
            ),
            metadata={"records": df.shape[0]},
        )

    return _asset