import pathlib

import pendulum
from dagster import (
    AssetExecutionContext,
    MonthlyPartitionsDefinition,
    ResourceParam,
    asset,
)
from fastavro import writer
from zenpy import Zenpy
from zenpy.lib.exception import RecordNotFoundException

from teamster.core.utils.functions import get_avro_record_schema

from .. import CODE_LOCATION, LOCAL_TIMEZONE
from .schema import ASSET_FIELDS


@asset(
    key=[CODE_LOCATION, "zendesk", "ticket_metrics_archive"],
    io_manager_key="io_manager_gcs_file",
    partitions_def=MonthlyPartitionsDefinition(
        start_date=pendulum.datetime(2011, 7, 1),
        end_date=pendulum.datetime(2023, 6, 30),
        timezone=LOCAL_TIMEZONE.name,
    ),
)
def ticket_metrics_archive(
    context: AssetExecutionContext, zendesk: ResourceParam[Zenpy]
):
    data_filepath = pathlib.Path("env/ticket_metrics_archive/data.avro")
    schema = get_avro_record_schema(
        name="ticket_metrics", fields=ASSET_FIELDS["ticket_metrics"]
    )

    partition_key = pendulum.parser.parse(context.partition_key)

    start_date = partition_key.subtract(seconds=1)
    end_date = partition_key.add(months=1)

    context.log.info(
        f"Searching closed tickets: updated>{start_date} updated<{end_date}"
    )
    archived_tickets = zendesk.search_export(
        type="ticket", status="closed", updated_between=[start_date, end_date]
    )

    context.log.info(f"Saving results to {data_filepath}")
    data_filepath.parent.mkdir(parents=True, exist_ok=True)

    writer(
        fo=data_filepath.open("wb"),
        schema=schema,
        records=[],
        codec="snappy",
        strict_allow_default=True,
    )

    fo = data_filepath.open("a+b")

    try:
        for ticket in archived_tickets:
            ticket_id = ticket.id

            context.log.info(f"Getting metrics for ticket #{ticket_id}")

            try:
                writer(
                    fo=fo,
                    schema=schema,
                    records=[zendesk.tickets.metrics(ticket_id).to_dict()],
                    codec="snappy",
                    strict_allow_default=True,
                )
            except RecordNotFoundException as e:
                context.log.exception(e)
                pass

    except IndexError as e:
        context.log.exception(e)
        pass

    fo.close()

    return data_filepath


__all__ = [
    ticket_metrics_archive,
]