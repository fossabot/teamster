{{ config(materialized="view") }}

{% set relations = dbt_utils.get_relations_by_prefix(
    schema=model.schema,
    prefix="stg_illuminate__repository_",
    exclude="stg_illuminate__repository_%s",
) %}

{{ dbt_utils.union_relations(relations=relations) }}
