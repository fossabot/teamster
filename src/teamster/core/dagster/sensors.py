from dagster import (
    RunFailureSensorContext,
    RunRequest,
    SensorResult,
    run_failure_sensor,
)
from dagster._core.execution.plan.objects import ErrorSource


@run_failure_sensor
def run_execution_interrupted_sensor(context: RunFailureSensorContext):
    run_requests = []
    for event in context.get_step_failure_events():
        if event.event_specific_data.error_source == ErrorSource.INTERRUPT:
            ...
            run_requests.append(RunRequest(...))

    return SensorResult(run_requests=run_requests)


# DagsterEvent(
#     event_type_value='STEP_FAILURE',
#     job_name='__ASSET_JOB_2',
#     step_handle=StepHandle(
#         node_handle=NodeHandle(
#             name='kipptaf__dbt__alchemer__src_alchemer__survey_response',
#             parent=None
#         ),
#         key='kipptaf__dbt__alchemer__src_alchemer__survey_response'
#     ),
#     node_handle=NodeHandle(
#         name='kipptaf__dbt__alchemer__src_alchemer__survey_response',
#         parent=None
#     ),
#     step_kind_value='COMPUTE',
#     logging_tags={
#         'job_name': '__ASSET_JOB_2',
#         'op_name': 'kipptaf__dbt__alchemer__src_alchemer__survey_response',
#         'resource_fn_name': 'None',
#         'resource_name': 'None',
#         'run_id': '35b4f2b7-77fe-4a26-9087-9818f2f237a1',
#         'step_key': 'kipptaf__dbt__alchemer__src_alchemer__survey_response'
#     },
#     event_specific_data=StepFailureData(
#         error=SerializableErrorInfo(
#             message='dagster._core.errors.DagsterExecutionInterruptedError\n',
#             stack=[
#                 '  File "/usr/local/lib/python3.10/site-packages/dagster/_core/...',
#                 '  File "/usr/local/lib/python3.10/site-packages/dagster/_core/...',
#                 '  File "/usr/local/lib/python3.10/site-packages/dagster/_core/...',
#                 '  File "/usr/local/lib/python3.10/site-packages/dagster/_core/...',
#                 '  File "/usr/local/lib/python3.10/contextlib.py", line 135, in ...',
#                 '  File "/usr/local/lib/python3.10/site-packages/dagster/_core/...',
#                 '  File "/usr/local/lib/python3.10/contextlib.py", line 135, in ...',
#                 '  File "/usr/local/lib/python3.10/site-packages/dagster/_core/er...',
#                 '  File "/usr/local/lib/python3.10/contextlib.py", line 135, in ...',
#                 '  File "/usr/local/lib/python3.10/site-packages/dagster/_utils/...'
#             ],
#             cls_name='DagsterExecutionInterruptedError',
#             cause=None,
#             context=None
#         ),
#         user_failure_data=None,
#         error_source=<ErrorSource.INTERRUPT: 'INTERRUPT'>
#     ),
#     message='Execution of step "kipptaf__dbt__alchemer__src_alchemer__survey_resp...',
#     pid=1,
#     step_key='kipptaf__dbt__alchemer__src_alchemer__survey_response'
# )