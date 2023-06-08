import gzip
import json
import pathlib

import pendulum
from dagster import OpExecutionContext, asset, config_from_files
from pandas import DataFrame
from sqlalchemy import literal_column, select, table, text

from teamster.core.google.resources.sheets import GoogleSheetsResource
from teamster.core.sqlalchemy.resources import MSSQLResource
from teamster.core.ssh.resources import SSHConfigurableResource
from teamster.core.utils.classes import CustomJSONEncoder


def construct_sql(query_type, query_value, now):
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
            .where(
                text(query_value.get("where", "").format(today=now.to_date_string()))
            )
        )


def transform(data, file_suffix, file_encoding=None, file_format=None):
    if file_suffix == "json":
        return json.dumps(obj=data, cls=CustomJSONEncoder).encode(file_encoding)
    elif file_suffix == "json.gz":
        return gzip.compress(
            json.dumps(obj=data, cls=CustomJSONEncoder).encode(file_encoding)
        )
    elif file_suffix in ["csv", "txt", "tsv"]:
        return (
            DataFrame(data=data)
            .to_csv(index=False, encoding=file_encoding, **file_format)
            .encode(file_encoding)
        )
    elif file_suffix == "gsheet":
        df = DataFrame(data=data)

        df_json = df.to_json(orient="split", date_format="iso", index=False)

        df_dict = json.loads(df_json)

        df_dict["shape"] = df.shape

        return df_dict


def load_sftp(context: OpExecutionContext, data, file_name, destination_config):
    destination_name = destination_config.get("name")
    destination_path = destination_config.get("path", "")

    # context.resources is a namedtuple
    ssh: SSHConfigurableResource = getattr(context.resources, f"ssh_{destination_name}")

    conn = ssh.get_connection()
    with conn.open_sftp() as sftp:
        sftp.chdir(".")

        if destination_path != "":
            destination_filepath = (
                pathlib.Path(sftp.getcwd()) / destination_path / file_name
            )
        else:
            destination_filepath = pathlib.Path(sftp.getcwd()) / file_name

        # confirm destination_filepath dir exists or create it
        context.log.debug(destination_filepath)

        destination_dir = destination_filepath.parent
        if str(destination_dir) != "/":
            try:
                sftp.stat(str(destination_dir))
            except IOError:
                path = pathlib.Path("/")
                for dir_parts in destination_dir.parts:
                    path = path / dir_parts
                    try:
                        sftp.stat(str(path))
                    except IOError:
                        context.log.info(f"Creating directory: {path}")
                        sftp.mkdir(path=str(path))

        # if destination_path given, chdir after confirming
        if destination_path:
            sftp.chdir(str(destination_dir))

        context.log.info(f"Saving file to {destination_filepath}")
        with sftp.file(filename=file_name, mode="w") as f:
            f.write(data)


def sftp_extract_asset_factory(
    asset_name,
    key_prefix,
    query_config,
    file_config,
    destination_config,
    timezone,
    op_tags={},
):
    now = pendulum.now(tz=timezone)

    @asset(
        name=asset_name,
        key_prefix=key_prefix,
        required_resource_keys={"db_mssql", f"ssh_{destination_config['name']}"},
        op_tags=op_tags,
    )
    def sftp_extract(context):
        file_suffix = file_config["suffix"]
        file_stem = file_config["stem"].format(
            today=now.to_date_string(), now=str(now.timestamp()).replace(".", "_")
        )

        sql = construct_sql(
            query_type=query_config["type"], query_value=query_config["value"], now=now
        )

        data = context.resources.db_mssql.engine.execute_query(
            query=sql,
            partition_size=query_config.get("partition_size", 100000),
            output_format="dict",
        )

        if data:
            context.log.info(f"Transforming data to {file_suffix}")
            transformed_data = transform(
                data=data,
                file_suffix=file_suffix,
                file_encoding=file_config.get("encoding", "utf-8"),
                file_format=file_config.get("format", {}),
            )

            load_sftp(
                context=context,
                data=transformed_data,
                file_name=f"{file_stem}.{file_suffix}",
                destination_config=destination_config,
            )

    return sftp_extract


def gsheet_extract_asset_factory(
    asset_name, key_prefix, query_config, file_config, timezone, folder_id, op_tags={}
):
    now = pendulum.now(tz=timezone)

    @asset(name=asset_name, key_prefix=key_prefix, op_tags=op_tags)
    def gsheet_extract(
        context: OpExecutionContext,
        db_mssql: MSSQLResource,
        gsheets: GoogleSheetsResource,
    ):
        file_stem: str = file_config["stem"].format(
            today=now.to_date_string(), now=str(now.timestamp()).replace(".", "_")
        )

        # gsheet title first character must be alpha
        if file_stem[0].isnumeric():
            file_stem = "GS" + file_stem

        data = db_mssql.engine.execute_query(
            query=construct_sql(
                query_type=query_config["type"],
                query_value=query_config["value"],
                now=now,
            ),
            partition_size=query_config.get("partition_size", 100000),
            output_format="dict",
        )

        if not data:
            return None

        context.log.info("Transforming data to gsheet")
        transformed_data = transform(data=data, file_suffix="gsheet")

        context.log.info(f"Opening: {file_stem}")
        spreadsheet = gsheets.open_or_create_sheet(title=file_stem, folder_id=folder_id)

        context.log.debug(spreadsheet.url)

        named_range_match = [
            nr for nr in spreadsheet.list_named_ranges() if nr["name"] == file_stem
        ]

        if named_range_match:
            named_range = named_range_match[0]["range"]
            named_range_id = named_range_match["namedRangeId"]

            named_range_sheet_id = named_range.get("sheetId", 0)
            end_row_ix = named_range.get("endRowIndex", 0)
            end_col_ix = named_range.get("endColumnIndex", 0)

            range_area = (end_row_ix + 1) * (end_col_ix + 1)
        else:
            named_range_id = None
            range_area = 0

        worksheet = (
            spreadsheet.get_worksheet_by_id(id=named_range_sheet_id)
            if named_range_id
            else spreadsheet.sheet1
        )

        nrows, ncols = transformed_data["shape"]
        nrows = nrows + 1  # header row
        transformed_data_area = nrows * ncols

        # resize worksheet
        worksheet_area = worksheet.row_count * worksheet.col_count
        if worksheet_area != transformed_data_area:
            context.log.debug(f"Resizing worksheet area to {nrows}x{ncols}.")
            worksheet.resize(rows=nrows, cols=ncols)

        # resize named range
        if range_area != transformed_data_area:
            start_cell = gsheets.rowcol_to_a1(1, 1)
            end_cell = gsheets.rowcol_to_a1(nrows, ncols)

            context.log.debug(
                f"Resizing named range '{file_stem}' to {start_cell}:{end_cell}."
            )

            worksheet.delete_named_range(named_range_id=named_range_id)
            worksheet.define_named_range(
                name=f"{start_cell}:{end_cell}", range_name=file_stem
            )

        context.log.debug(f"Clearing '{file_stem}' values.")
        worksheet.batch_clear([file_stem])

        context.log.info(f"Updating '{file_stem}': {transformed_data_area} cells.")
        worksheet.update(
            file_stem, [transformed_data["columns"]] + transformed_data["data"]
        )

    return gsheet_extract


def generate_extract_assets(code_location, name, extract_type, timezone):
    cfg = config_from_files(
        [f"src/teamster/{code_location}/datagun/config/{name}.yaml"]
    )

    assets = []
    for ac in cfg["assets"]:
        if extract_type == "sftp":
            assets.append(
                sftp_extract_asset_factory(
                    key_prefix=cfg["key_prefix"], timezone=timezone, **ac
                )
            )
        elif extract_type == "gsheet":
            assets.append(
                gsheet_extract_asset_factory(
                    key_prefix=cfg["key_prefix"],
                    folder_id=cfg["folder_id"],
                    timezone=timezone,
                    **ac,
                )
            )

    return assets
