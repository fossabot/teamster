{{-
    config(
        materialized="incremental",
        incremental_strategy="merge",
        unique_key="student_number",
        merge_update_columns=["default_password"],
    )
-}}

{%- if execute -%}
    {%- if flags.FULL_REFRESH -%}
        {{
            exceptions.raise_compiler_error(
                (
                    "Full refresh is not allowed for this model. "
                    "Exclude it from the run via the argument '--exclude model_name'."
                )
            )
        }}
    {%- endif -%}
{%- endif -%}

with
    components as (
        select
            student_number,
            format_date('%m', dob) as dob_month,
            format_date('%d', dob) as dob_day,
            format_date('%y', dob) as dob_year,
            regexp_replace(
                normalize(lower(first_name), nfd), r"[\pM\W]", ''
            ) as first_name_clean,
            regexp_replace(
                normalize(
                    lower(regexp_replace(last_name, r'\s[IiVvXxJjRr\.]*$', '')), nfd
                ),
                r"[\pM\W]",
                ''
            ) as last_name_clean,
        from {{ ref("stg_powerschool__students") }}
        where
            student_number not in (select student_number from {{ this }})
            and dob is not null
            and first_name is not null
            and last_name is not null
            and enroll_status = 0
    ),

    username_options as (
        select
            student_number,
            concat(last_name_clean, dob_month, dob_day) as username,
            1 as priority_order,
        from components

        union all

        select
            student_number,
            concat(first_name_clean, dob_month, dob_day) as username,
            2 as priority_order,
        from components

        union all

        select
            student_number,
            concat(
                left(first_name_clean, 1), last_name_clean, dob_month, dob_day
            ) as username,
            3 as priority_order,
        from components
    ),

    username_filter as (
        select
            student_number,
            username,
            row_number() over (
                partition by student_number order by priority_order asc
            ) as priority_order,
            row_number() over (
                partition by username order by priority_order asc, student_number asc
            ) as rn_username,
        from username_options
        where username not in (select username from {{ this }})
    )

{% if is_incremental() %}
    select
        c.student_number,
        coalesce(u1.username, u2.username, u3.username) as username,
        if(
            length(concat(c.last_name_clean, c.dob_year)) < 8,
            left(concat(c.last_name_clean, c.dob_year, c.student_number), 8),
            concat(c.last_name_clean, c.dob_year)
        ) as default_password,
        coalesce(u1.username, u2.username, u3.username)
        || '@teamstudents.org' as google_email,
    from components as c
    left join
        username_filter as u1
        on c.student_number = u1.student_number
        and u1.priority_order = 1
        and u1.rn_username = 1
    left join
        username_filter as u2
        on c.student_number = u2.student_number
        and u2.priority_order = 2
        and u2.rn_username = 1
    left join
        username_filter as u3
        on c.student_number = u3.student_number
        and u3.priority_order = 3
        and u3.rn_username = 1
{% else %}
    select
        student_number,
        username,
        default_password,
        username || '@teamstudents.org' as google_email,
    from {{ source("people", "src_people__student_logins_archive") }}
{% endif %}
