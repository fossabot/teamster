from dagster import Definitions, load_assets_from_modules

from teamster.core.resources import get_dbt_cli_resource, get_io_manager_gcs_avro
from teamster.staging import CODE_LOCATION, dbt

defs = Definitions(
    assets=load_assets_from_modules(
        modules=[
            dbt,
        ]
    ),
    resources={
        "io_manager_gcs_avro": get_io_manager_gcs_avro("staging"),
        "dbt_cli": get_dbt_cli_resource(CODE_LOCATION),
    },
)
