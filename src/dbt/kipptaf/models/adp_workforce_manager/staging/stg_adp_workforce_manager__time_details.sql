select
    _dagster_partition_fiscal_year,
    _dagster_partition_date,
    _dagster_partition_symbolic_id,
    employee_payrule,
    location,
    job,
    days,
    hours,
    money,
    transaction_type,
    transaction_apply_to,
    transaction_in_exceptions,
    transaction_out_exceptions,
    regexp_extract(employee_name, r'\((\w+)\)') as worker_id,
    parse_date('%b %d, %Y', transaction_apply_date) as transaction_apply_date,
    parse_datetime(
        '%b %d, %Y %I:%M %p', transaction_start_date_time
    ) as transaction_start_date_time,
    parse_datetime(
        '%b %d, %Y %I:%M %p', transaction_end_date_time
    ) as transaction_end_date_time,
from {{ source("adp_workforce_manager", "src_adp_workforce_manager__time_details") }}
