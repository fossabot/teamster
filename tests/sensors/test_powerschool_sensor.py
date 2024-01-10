from dagster import build_sensor_context

from teamster.core.powerschool.sensors import build_powerschool_sensor
from teamster.core.resources import (
    get_oracle_resource_powerschool,
    get_ssh_resource_powerschool,
)
from teamster.core.utils.functions import get_dagster_cloud_instance
from teamster.kippnewark.powerschool.assets import partition_assets


def test_powerschool_sensor():
    context = build_sensor_context(
        instance=get_dagster_cloud_instance("/workspaces/teamster/.dagster/home")
    )

    dynamic_partition_sensor = build_powerschool_sensor(
        name="test", asset_defs=partition_assets
    )

    sensor_results = dynamic_partition_sensor(
        context=context,
        ssh_powerschool=get_ssh_resource_powerschool("KIPPNEWARK"),
        db_powerschool=get_oracle_resource_powerschool("KIPPNEWARK"),
    )

    for result in sensor_results:
        context.log.info(result)
