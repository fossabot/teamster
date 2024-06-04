from dagster import build_schedule_context

from teamster.core.resources import DB_POWERSCHOOL, SSH_POWERSCHOOL
from teamster.kippnewark.powerschool.schedules import last_modified_schedule


def test_schedule():
    with build_schedule_context() as context:
        output = last_modified_schedule(
            context=context,
            ssh_powerschool=SSH_POWERSCHOOL,
            db_powerschool=DB_POWERSCHOOL,
        )

    assert output is not None
    for o in output:
        context.log.info(o)
