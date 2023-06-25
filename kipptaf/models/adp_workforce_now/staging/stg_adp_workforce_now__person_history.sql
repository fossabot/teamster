with
    deduplicate as (
        {{
            dbt_utils.deduplicate(
                relation=source(
                    "adp_workforce_now", "src_adp_workforce_now__person_history"
                ),
                partition_by="worker_id",
                order_by="_fivetran_synced",
            )
        }}
    )

select *
from deduplicate
