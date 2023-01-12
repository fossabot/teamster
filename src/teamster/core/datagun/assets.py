import gzip
import json
import pathlib

import pandas as pd
from dagster import asset
from sqlalchemy import literal_column, select, table, text

from teamster.core.utils.classes import CustomJSONEncoder
from teamster.core.utils.variables import NOW, TODAY


def construct_sql(context, query_type, query_value):
    if query_type == "text":
        return text(query_value)
    elif query_type == "file":
        sql_file = pathlib.Path(query_value).absolute()
        with sql_file.open(mode="r") as f:
            return text(f.read())
    elif query_type == "schema":
        return (
            select(*[literal_column(col) for col in query_value.get("select", ["*"])])
            .select_from(table(**query_value["table"]))
            .where(text(query_value.get("where", "")))
        )


def extract(context, sql, partition_size):
    if hasattr(sql, "whereclause"):
        sql.whereclause.text = sql.whereclause.text.format(today=TODAY.isoformat())

    return context.resources.warehouse.execute_query(
        query=sql, partition_size=partition_size, output_fmt="dict"
    )


def transform(context, data, file_suffix, file_encoding=None, file_format=None):
    context.log.info(f"Transforming data to {file_suffix}")
    if file_suffix == "gsheet":
        df = pd.DataFrame(data=data)

        df_json = df.to_json(orient="split", date_format="iso", index=False)

        df_dict = json.loads(df_json)
        df_dict["shape"] = df.shape

        return df_dict
    elif file_suffix == "json":
        return json.dumps(obj=data, cls=CustomJSONEncoder).encode(file_encoding)
    elif file_suffix == "json.gz":
        return gzip.compress(
            json.dumps(obj=data, cls=CustomJSONEncoder).encode(file_encoding)
        )
    elif file_suffix in ["csv", "txt", "tsv"]:
        df = pd.DataFrame(data=data)
        return df.to_csv(index=False, encoding=file_encoding, **file_format).encode(
            file_encoding
        )


def load_sftp(context, data, file_name, destination_config):
    destination_name = destination_config.get("name")
    destination_path = destination_config.get("path")

    if destination_name == "pythonanywhere":
        sftp = context.resources.sftp_pythonanywhere

    sftp_conn = sftp.get_connection()
    with sftp_conn.open_sftp() as sftp:
        sftp.chdir(".")

        if destination_path != "":
            destination_filepath = (
                pathlib.Path(sftp.getcwd()) / destination_path / file_name
            )
        else:
            destination_filepath = pathlib.Path(sftp.getcwd()) / file_name

        # confirm destination_filepath dir exists or create it
        try:
            sftp.stat(str(destination_filepath.parent))
        except IOError:
            dir_path = pathlib.Path("/")
            for dir in destination_filepath.parent.parts:
                dir_path = dir_path / dir
                try:
                    sftp.stat(str(dir_path))
                except IOError:
                    context.log.info(f"Creating directory: {dir_path}")
                    sftp.mkdir(str(dir_path))

        # if destination_path given, chdir after confirming
        if destination_path:
            sftp.chdir(str(destination_filepath.parent))

        context.log.info(f"Saving file to {destination_filepath}")
        with sftp.file(file_name, "w") as f:
            f.write(data)


def load_gsheet(context, data, file_stem):
    if file_stem[0].isnumeric():
        file_stem = "GS" + file_stem

    context.resources.gsheet.update_named_range(
        data=data, spreadsheet_name=file_stem, range_name=file_stem
    )


def sftp_extract_asset_factory(
    asset_name, key_prefix, query_config, file_config, destination_config
):
    @asset(
        name=asset_name,
        key_prefix=key_prefix,
        required_resource_keys={"warehouse", f"sftp_{destination_config['name']}"},
    )
    def sftp_extract(context):
        file_suffix = file_config["suffix"]
        file_stem = file_config["stem"].format(
            today=TODAY.date().isoformat(), now=str(NOW.timestamp()).replace(".", "_")
        )
        file_name = f"{file_stem}.{file_suffix}"

        sql = construct_sql(
            context=context,
            query_type=query_config["type"],
            query_value=query_config["value"],
        )

        extract_data = extract(
            context=context,
            sql=sql,
            partition_size=query_config.get("partition_size", 100000),
        )

        if extract_data:
            transformed_data = transform(
                context=context,
                data=extract_data,
                file_suffix=file_suffix,
                file_encoding=file_config.get("encoding", "utf-8"),
                file_format=file_config.get("format", {}),
            )

            load_sftp(
                context=context,
                data=transformed_data,
                file_name=file_name,
                destination_config=destination_config,
            )

    return sftp_extract


def gsheet_extract_asset_factory(asset_name, query_config, file_config):
    @asset(
        name=asset_name,
        key_prefix="gsheets",
        required_resource_keys={"warehouse", "gsheet"},
    )
    def gsheet_extract(context):
        file_stem = file_config["stem"].format(
            today=TODAY.date().isoformat(), now=str(NOW.timestamp()).replace(".", "_")
        )

        sql = construct_sql(
            context=context,
            query_type=query_config["type"],
            query_value=query_config["value"],
        )

        extract_data = extract(
            context=context,
            sql=sql,
            partition_size=query_config.get("partition_size", 100000),
        )

        if extract_data:
            transformed_data = transform(
                context=context, data=extract_data, file_suffix="gsheet"
            )

            load_gsheet(context=context, data=transformed_data, file_stem=file_stem)

    return gsheet_extract
