import random
import shutil

from dagster import EnvVar, config_from_files, materialize
from dagster_gcp import GCSResource

from teamster.core.google.io.resources import gcs_io_manager
from teamster.core.ssh.resources import SSHConfigurableResource
from teamster.staging import GCS_PROJECT_NAME


def _test_assets(asset, ssh_resource):
    partition_keys = asset.partitions_def.get_partition_keys()

    partition_key = partition_keys[random.randint(a=0, b=(len(partition_keys) - 1))]

    result = materialize(
        assets=[asset],
        partition_key=partition_key,
        resources={
            "gcs": GCSResource(project=GCS_PROJECT_NAME),
            "io_manager_gcs_avro": gcs_io_manager.configured(
                config_from_files(
                    ["src/teamster/staging/config/resources/io_avro.yaml"]
                )
            ),
            **ssh_resource,
        },
    )

    assert result.success

    shutil.rmtree("/workspaces/teamster/dagster")


def test_assets_renlearn():
    from teamster.kippmiami.renlearn import assets

    for asset in assets:
        _test_assets(
            asset=asset,
            ssh_resource={
                "ssh_renlearn": SSHConfigurableResource(
                    remote_host="sftp.renaissance.com",
                    username=EnvVar("KIPPMIAMI_RENLEARN_SFTP_USERNAME"),
                    password=EnvVar("KIPPMIAMI_RENLEARN_SFTP_PASSWORD"),
                )
            },
        )

    from teamster.kippnewark.renlearn import assets

    for asset in assets:
        _test_assets(
            asset=asset,
            ssh_resource={
                "ssh_renlearn": SSHConfigurableResource(
                    remote_host="sftp.renaissance.com",
                    username=EnvVar("KIPPNJ_RENLEARN_SFTP_USERNAME"),
                    password=EnvVar("KIPPNJ_RENLEARN_SFTP_PASSWORD"),
                )
            },
        )


def test_assets_fldoe():
    from teamster.kippmiami.fldoe import assets

    for asset in assets:
        _test_assets(
            asset=asset,
            ssh_resource={
                "ssh_couchdrop": SSHConfigurableResource(
                    remote_host="kipptaf.couchdrop.io",
                    username=EnvVar("COUCHDROP_SFTP_USERNAME"),
                    password=EnvVar("COUCHDROP_SFTP_PASSWORD"),
                ),
            },
        )


def test_assets_iready():
    from teamster.kippmiami.iready import assets

    ssh_iready = SSHConfigurableResource(
        remote_host="prod-sftp-1.aws.cainc.com",
        username=EnvVar("IREADY_SFTP_USERNAME"),
        password=EnvVar("IREADY_SFTP_PASSWORD"),
    )

    for asset in assets:
        _test_assets(asset=asset, ssh_resource={"ssh_iready": ssh_iready})

    from teamster.kippnewark.iready import assets

    for asset in assets:
        _test_assets(asset=asset, ssh_resource={"ssh_iready": ssh_iready})


def test_assets_edplan():
    from teamster.kippcamden.edplan import assets

    for asset in assets:
        _test_assets(
            asset=asset,
            ssh_resource={
                "ssh_edplan": SSHConfigurableResource(
                    remote_host="secureftp.easyiep.com",
                    username=EnvVar("KIPPCAMDEN_EDPLAN_SFTP_USERNAME"),
                    password=EnvVar("KIPPCAMDEN_EDPLAN_SFTP_PASSWORD"),
                )
            },
        )

    from teamster.kippnewark.edplan import assets

    for asset in assets:
        _test_assets(
            asset=asset,
            ssh_resource={
                "ssh_edplan": SSHConfigurableResource(
                    remote_host="secureftp.easyiep.com",
                    username=EnvVar("KIPPNEWARK_EDPLAN_SFTP_USERNAME"),
                    password=EnvVar("KIPPNEWARK_EDPLAN_SFTP_PASSWORD"),
                )
            },
        )


def test_assets_titan():
    from teamster.kippcamden.titan import assets

    for asset in assets:
        _test_assets(
            asset=asset,
            ssh_resource={
                "ssh_titan": SSHConfigurableResource(
                    remote_host="sftp.titank12.com",
                    username=EnvVar("KIPPCAMDEN_TITAN_SFTP_USERNAME"),
                    password=EnvVar("KIPPCAMDEN_TITAN_SFTP_PASSWORD"),
                )
            },
        )

    from teamster.kippnewark.titan import assets

    for asset in assets:
        _test_assets(
            asset=asset,
            ssh_resource={
                "ssh_titan": SSHConfigurableResource(
                    remote_host="sftp.titank12.com",
                    username=EnvVar("KIPPNEWARK_TITAN_SFTP_USERNAME"),
                    password=EnvVar("KIPPNEWARK_TITAN_SFTP_PASSWORD"),
                )
            },
        )


""" can't test dynamic partitions
def test_assets_achieve3k():
    from teamster.kipptaf.achieve3k import assets

    _test_assets(
        asset=assets,
        ssh_resource={
            "ssh_achieve3k": SSHConfigurableResource(
                remote_host="xfer.achieve3000.com",
                username=EnvVar("ACHIEVE3K_SFTP_USERNAME"),
                password=EnvVar("ACHIEVE3K_SFTP_PASSWORD"),
            )
        },
    )


def test_assets_clever():
    from teamster.kipptaf.clever import assets

    _test_assets(
        asset=assets,
        ssh_resource={
            "ssh_clever_reports": SSHConfigurableResource(
                remote_host="reports-sftp.clever.com",
                username=EnvVar("CLEVER_REPORTS_SFTP_USERNAME"),
                password=EnvVar("CLEVER_REPORTS_SFTP_PASSWORD"),
            )
        },
        partition_key="",
    )
"""