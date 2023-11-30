from dagster import AssetExecutionContext, Output, asset

from teamster.core.google.forms.resources import GoogleFormsResource
from teamster.core.google.forms.schema import ASSET_FIELDS
from teamster.core.utils.functions import get_avro_record_schema


def build_google_forms_assets(partitions_def):
    @asset(
        key=["google", "forms", "form"],
        io_manager_key="io_manager_gcs_avro",
        partitions_def=partitions_def,
        group_name="google_forms",
    )
    def form(context: AssetExecutionContext, google_forms: GoogleFormsResource):
        data = google_forms.get_form(form_id=context.partition_key)
        schema = get_avro_record_schema(name="form", fields=ASSET_FIELDS["form"])

        yield Output(value=([data], schema), metadata={"record_count": len(data)})

    @asset(
        key=["google", "forms", "responses"],
        io_manager_key="io_manager_gcs_avro",
        partitions_def=partitions_def,
        group_name="google_forms",
    )
    def responses(context: AssetExecutionContext, google_forms: GoogleFormsResource):
        data = google_forms.list_responses(form_id=context.partition_key)
        schema = get_avro_record_schema(
            name="responses", fields=ASSET_FIELDS["responses"]
        )

        yield Output(
            value=([data], schema),
            metadata={"record_count": len(data.get("responses"))},
        )

    return [form, responses]
