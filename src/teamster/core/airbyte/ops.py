from dagster import Config, OpExecutionContext, Output, op
from dagster_airbyte import AirbyteOutput
from dagster_airbyte.utils import generate_materializations


class AirbyteMaterializationOpConfig(Config):
    airbyte_outputs: list[dict]


@op
def airbyte_materialization_op(
    context: OpExecutionContext, config: AirbyteMaterializationOpConfig
):
    for output in config.airbyte_outputs:
        namespace_format = output["connection_details"]["namespaceFormat"].split("_")

        for materialization in generate_materializations(
            output=AirbyteOutput(**output),
            asset_key_prefix=[namespace_format[0], "_".join(namespace_format[1:])],
        ):
            yield Output(
                value=None,
                output_name=materialization.asset_key.path[-1],
                metadata=materialization.metadata,
            )


__all__ = [
    airbyte_materialization_op,
]
