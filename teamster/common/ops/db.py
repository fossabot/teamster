import gzip
import json
import pathlib
import re

import pandas as pd
from dagster import Dict, DynamicOut, DynamicOutput, In, List, Out, Output, Tuple, op

from teamster.common.config.db import QUERY_CONFIG
from teamster.common.utils import TODAY, CustomJSONEncoder


@op(
    config_schema=QUERY_CONFIG,
    out={"dynamic_query": DynamicOut(dagster_type=Tuple)},
    tags={"dagster/priority": 1},
)
def compose_queries(context):
    dest_config = context.op_config["destination"]

    queries = context.op_config["queries"]
    for i, q in enumerate(queries):
        [(query_type, value)] = q["sql"].items()
        if query_type == "text":
            query = value
        elif query_type == "file":
            with pathlib.Path(value).absolute().open() as f:
                query = f.read()
        elif query_type == "schema":
            table_name = value["table"]
            where = value.get("where", "")
            query = " ".join(
                [
                    f"SELECT {value['columns']}",
                    f"FROM {table_name}",
                    f"WHERE {where}" if where else "",
                ]
            )

        file_config = q.get("file", {})

        file_stem = file_config.get("stem")
        if not file_stem:
            context.log.info("No file stem specified, using default: table + where")
            file_stem = table_name + re.sub(
                r"[^a-zA-Z0-9=;]", "", where.replace(" AND ", ";").replace(" OR ", ",")
            )
        file_config["stem"] = file_stem.format(TODAY.date().isoformat())
        file_config["table_name"] = table_name

        file_suffix = file_config.get("suffix")
        if not file_suffix:
            context.log.info("No file suffix specified, using default: json.gz")
            file_config["suffix"] = "json.gz"

        yield DynamicOutput(
            value=(query, file_config, dest_config),
            output_name="dynamic_query",
            mapping_key="_".join(
                [
                    f"{query_type}",
                    f"{re.sub(r'[^A-Za-z0-9_]+', '', file_stem)}",
                    f"{file_suffix}",
                    f"{i}",
                ]
            ),
        )


@op(
    ins={"dynamic_query": In(dagster_type=Tuple)},
    out={
        "data": Out(dagster_type=List[Dict], is_required=False),
        "file_config": Out(dagster_type=Dict, is_required=False),
        "dest_config": Out(dagster_type=Dict, is_required=False),
    },
    required_resource_keys={"db"},
    tags={"dagster/priority": 2},
)
def extract(context, dynamic_query):
    query, file_config, dest_config = dynamic_query

    data = context.resources.db.execute_text_query(query)
    if data:
        yield Output(value=data, output_name="data")
        yield Output(value=file_config, output_name="file_config")
        yield Output(value=dest_config, output_name="dest_config")


@op(
    ins={
        "data": In(dagster_type=List[Dict]),
        "file_config": In(dagster_type=Dict),
        "dest_config": In(dagster_type=Dict),
    },
    out={"transformed": Out(dagster_type=Tuple, is_required=False)},
    required_resource_keys={"file_manager"},
    tags={"dagster/priority": 3},
)
def transform(context, data, file_config, dest_config):
    table_name = file_config["table_name"]
    file_stem = file_config["stem"]
    file_suffix = file_config["suffix"]
    file_format = file_config.get("format", {})

    file_encoding = file_format.get("encoding", "utf-8")

    dest_type = dest_config["type"]
    dest_name = dest_config.get("name", table_name)
    dest_path = dest_config.get("path")

    context.log.info(f"Transforming data to {file_suffix}")
    if file_suffix == "json":
        data_bytes = json.dumps(obj=data, cls=CustomJSONEncoder).encode(file_encoding)
    elif file_suffix == "json.gz":
        data_bytes = gzip.compress(
            json.dumps(obj=data, cls=CustomJSONEncoder).encode(file_encoding)
        )
    elif file_suffix == "gsheet":
        df = pd.DataFrame(data=data)
        df_json = df.to_json(orient="split", date_format="iso", index=False)
        df_dict = json.loads(df_json)
        df_dict["shape"] = df.shape
    elif file_suffix in ["csv", "txt", "tsv"]:
        df = pd.DataFrame(data=data)
        data_bytes = df.to_csv(index=False, **file_format).encode(file_encoding)

    if dest_type == "gsheet":
        yield Output(value=(dest_type, (df_dict, file_stem)), output_name="transformed")
    elif dest_type in ["gcs", "sftp"]:
        file_handle = context.resources.file_manager.upload_from_string(
            obj=data_bytes,
            file_key=(f"{dest_name}/{file_stem}.{file_suffix}"),
        )
        context.log.info(f"Saved to {file_handle.path_desc}.")

        if dest_type == "sftp":
            yield Output(
                value=(dest_type, (file_handle, dest_path)), output_name="transformed"
            )
