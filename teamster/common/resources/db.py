import json
import sys

import oracledb
from dagster import Field, IntSource, StringSource, resource
from dagster._utils import merge_dicts
from sqlalchemy import text
from sqlalchemy.engine import URL, create_engine
from sshtunnel import SSHTunnelForwarder

from teamster.common.utils import CustomJSONEncoder

sys.modules["cx_Oracle"] = oracledb  # patched until sqlalchemy supports oracledb (v2)


class SqlAlchemyEngine(object):
    def __init__(self, dialect, driver, logger, **kwargs):
        self.ssh_config = {}
        self.ssh_tunnel = None
        self.log = logger
        self.connection_url = URL.create(drivername=f"{dialect}+{driver}", **kwargs)
        self.engine = create_engine(url=self.connection_url)

        ssh_config = kwargs.get("ssh_config")
        if ssh_config:
            for k, v in ssh_config.items():
                if k not in ["remote_bind_host", "remote_bind_port"]:
                    self.ssh_config[k] = v

            self.ssh_config["remote_bind_address"] = (
                ssh_config.get("remote_bind_host"),
                ssh_config.get("remote_bind_port"),
            )

            self.ssh_config["local_bind_address"] = (kwargs["host"], kwargs["port"])

            self.ssh_tunnel = SSHTunnelForwarder(**self.ssh_config)

    def execute_text_query(self, query, output="dict"):
        self.log.info(f"Executing query:\n{query}")

        if self.ssh_tunnel:
            if not self.ssh_tunnel.is_active:
                self.ssh_tunnel.start()

        with self.engine.connect() as conn:
            result = conn.execute(statement=text(query))

            if output in ["dict", "json"]:
                output_obj = [dict(row) for row in result.mappings()]
            else:
                output_obj = [row for row in result]

        # if self.ssh_config:
        #     tunnel.stop()

        self.log.info(f"Retrieved {len(output_obj)} rows.")
        if output == "json":
            return json.dumps(obj=output_obj, cls=CustomJSONEncoder)
        else:
            return output_obj


class MssqlEngine(SqlAlchemyEngine):
    def __init__(self, dialect, driver, logger, mssql_driver, **kwargs):
        super().__init__(
            dialect, driver, logger, query={"driver": mssql_driver}, **kwargs
        )


class OracleEngine(SqlAlchemyEngine):
    def __init__(
        self,
        dialect,
        driver,
        logger,
        version,
        prefetchrows=oracledb.defaults.prefetchrows,
        **kwargs,
    ):
        oracledb.version = version
        oracledb.defaults.prefetchrows = prefetchrows
        super().__init__(dialect, driver, logger, **kwargs)


SQLALCHEMY_ENGINE_CONFIG = {
    "dialect": Field(StringSource),
    "driver": Field(StringSource),
    "username": Field(StringSource, is_required=False),
    "password": Field(StringSource, is_required=False),
    "host": Field(StringSource, is_required=False),
    "port": Field(IntSource, is_required=False),
    "database": Field(StringSource, is_required=False),
    "ssh_config": Field(dict, is_required=False),  # TODO: add ssh_config shape
}


@resource(
    config_schema=merge_dicts(
        SQLALCHEMY_ENGINE_CONFIG,
        {"mssql_driver": Field(StringSource, is_required=True)},
    )
)
def mssql(context):
    return MssqlEngine(logger=context.log, **context.resource_config)


@resource(
    config_schema=merge_dicts(
        SQLALCHEMY_ENGINE_CONFIG,
        {
            "version": Field(StringSource, is_required=True),
            "prefetchrows": Field(IntSource, is_required=False),
        },
    )
)
def oracle(context):
    return OracleEngine(logger=context.log, **context.resource_config)
