import json

import py_avro_schema

from teamster.google.forms.schema import Form, Responses

FORM_SCHEMA = json.loads(py_avro_schema.generate(py_type=Form, namespace="form"))

RESPONSES_SCHEMA = json.loads(
    py_avro_schema.generate(py_type=Responses, namespace="response")
)
