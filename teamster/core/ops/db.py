import gzip
import json
import pathlib
import re

import pandas as pd
from dagster import Dict, DynamicOut, DynamicOutput, In, List, Out, Output, Tuple, op
from sqlalchemy import literal_column, select, table, text

from teamster.core.config.db import QUERY_CONFIG, SSH_TUNNEL_CONFIG
from teamster.core.utils import NOW, TODAY, CustomJSONEncoder, get_last_schedule_run


@op(
    config_schema=QUERY_CONFIG,
    out={"dynamic_query": DynamicOut(dagster_type=Tuple)},
    tags={"dagster/priority": 1},
)
def compose_queries(context):
    dest_config = context.op_config["destination"]

    queries = context.op_config["queries"]
    for i, q in enumerate(queries):
        file_config = {**q.get("file", {})}

        [(query_type, value)] = q["sql"].items()
        if query_type == "text":
            query = text(value)
        elif query_type == "file":
            with pathlib.Path(value).absolute().open() as f:
                query = text(f.read())
        elif query_type == "schema":
            where_fmt = value.get("where", "").format(
                TODAY=TODAY, LAST_RUN=get_last_schedule_run(context=context)
            )
            query = (
                select(*[literal_column(col) for col in value["select"]])
                .select_from(table(**value["table"]))
                .where(text(where_fmt))
            )

            query_where = re.sub(r"\s+AND\s+", ";", where_fmt, flags=re.IGNORECASE)
            query_where = re.sub(r"\s+OR\s+", ",", query_where, flags=re.IGNORECASE)
            query_where = re.sub(r"\s+", "_", query_where)

            file_config["query_where"] = re.sub(r"[^a-zA-Z0-9_=;,]", "", query_where)
            file_config["table_name"] = value["table"]["name"]

        file_suffix = file_config.get("suffix")
        if file_suffix is None:
            context.log.info("No file suffix specified, using default: json.gz")
            file_config["suffix"] = "json.gz"

        yield DynamicOutput(
            value=(query, file_config, dest_config),
            output_name="dynamic_query",
            mapping_key="_".join(
                [
                    query_type,
                    re.sub(
                        r"[^A-Za-z0-9_]+",
                        "",
                        file_config.get("stem", file_config.get("table_name", "")),
                    ),
                    file_config["suffix"].replace(".", ""),
                    str(i),
                ]
            ),
        )


@op(
    config_schema=SSH_TUNNEL_CONFIG,
    ins={"dynamic_query": In(dagster_type=Tuple)},
    out={
        "data": Out(dagster_type=List[Dict], is_required=False),
        "file_config": Out(dagster_type=Dict, is_required=False),
        "dest_config": Out(dagster_type=Dict, is_required=False),
    },
    required_resource_keys={"db", "ssh"},
    tags={"dagster/priority": 2},
)
def extract(context, dynamic_query):
    query, file_config, dest_config = dynamic_query

    if hasattr(context.resources.ssh, "get_tunnel"):
        context.log.info("Starting SSH tunnel.")
        ssh_tunnel = context.resources.ssh.get_tunnel(**context.op_config)
        ssh_tunnel.start()
    else:
        ssh_tunnel = None

    data = context.resources.db.execute_query(query)

    if ssh_tunnel is not None:
        context.log.info("Stopping SSH tunnel.")
        ssh_tunnel.stop()

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
    file_suffix = file_config["suffix"]
    file_format = file_config.get("format", {})
    table_name = file_config.get("table_name")
    file_encoding = file_format.get("encoding", "utf-8")
    file_stem = file_config.get("stem", f"{table_name}_{NOW.timestamp()}").format(
        TODAY=TODAY.date().isoformat()
    )

    dest_type = dest_config["type"]
    dest_name = dest_config.get("name")

    if dest_name:
        gcs_folder = dest_name
    elif table_name:
        gcs_folder = table_name
    else:
        gcs_folder = "data"

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
        yield Output(value=(dest_config, file_stem, df_dict), output_name="transformed")
    elif dest_type in ["gcs", "sftp"]:
        file_handle = context.resources.file_manager.write_data(
            data=data_bytes, key=f"{gcs_folder}/{file_stem}", ext=file_suffix
        )
        context.log.info(f"Saved to {file_handle.path_desc}.")

        if dest_type == "sftp":
            yield Output(value=(dest_config, file_handle), output_name="transformed")
