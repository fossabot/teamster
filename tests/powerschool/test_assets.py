from dagster import build_op_context, config_from_files, with_resources

from teamster.core.powerschool.db.assets import table_asset_factory
from teamster.core.resources.sqlalchemy import oracle
from teamster.core.resources.ssh import ssh_resource

CODE_LOCATION = "test"
PARTITIONS_START_DATE = "2002-07-01T00:00:00.000000-0400"

powerschool_table_asset = with_resources(
    definitions=[table_asset_factory(asset_name="schools")],
    resource_defs={
        "ps_db": oracle.configured(
            config_from_files(["src/teamster/core/powerschool/db/config/db.yaml"])
        ),
        "ps_ssh": ssh_resource.configured(
            config_from_files(["src/teamster/core/powerschool/db/config/ssh.yaml"])
        ),
    },
)[0]


def test_powerschool_table_asset():
    result = powerschool_table_asset(build_op_context())
    assert result
