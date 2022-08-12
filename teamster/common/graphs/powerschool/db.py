from dagster import graph

from teamster.common.ops.db import compose_queries, extract, transform


@graph
def execute_query(dynamic_query):
    data, file_config, dest_config = extract(dynamic_query=dynamic_query)

    transform(data=data, file_config=file_config, dest_config=dest_config)


@graph
def run_queries():
    # parse queries from run config file
    dynamic_query = compose_queries()

    # execute composed queries and transform to configured file type
    dynamic_query.map(execute_query)
