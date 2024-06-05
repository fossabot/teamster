with
    student_unpivot_flags as (
        select distinct
            _dbt_source_relation,
            yearid,
            academic_year,
            region,
            schoolid,
            school_level,
            studentid,
            student_number,
            student_course_entry_date,
            grade_level,
            course_number,
            section_or_period,
            sectionid,
            sections_dcid,
            assign_quarter,
            assign_category_code,
            assign_category,
            assign_category_quarter,
            assign_id,
            assign_name,
            assign_due_date,
            assign_score_type,
            assign_is_exempt,
            assign_is_late,
            assign_is_missing,
            assign_score_raw,
            assign_score_converted,
            assign_final_score_percent,
            assign_max_score,
            audit_qt_week_number,

            student_flag_name,
            student_flag_value,

        from
            {{ ref("int_powerschool__student_assignments") }} unpivot (
                student_flag_value for student_flag_name in (
                    assign_null_score,
                    assign_score_above_max,
                    assign_exempt_with_score,
                    assign_w_score_less_5,
                    assign_f_score_less_5,
                    assign_w_missing_score_not_5,
                    assign_f_missing_score_not_5,
                    assign_s_score_less_50p,
                    assign_s_ms_score_not_conversion_chart_options,
                    assign_s_hs_score_not_conversion_chart_options
                )
            )
        where student_flag_value = 1
    )

select distinct
    _dbt_source_relation,
    yearid,
    academic_year,
    region,
    schoolid,
    school_level,
    studentid,
    student_number,
    student_course_entry_date,
    grade_level,
    course_number,
    section_or_period,
    sectionid,
    sections_dcid,
    assign_quarter,
    assign_category_code,
    assign_category,
    assign_category_quarter,
    assign_id,
    assign_name,
    assign_due_date,
    assign_score_type,
    assign_is_exempt,
    assign_is_late,
    assign_is_missing,
    assign_score_raw,
    assign_score_converted,
    assign_final_score_percent,
    assign_max_score,
    audit_qt_week_number,

    assign_null_score,
    assign_score_above_max,
    assign_exempt_with_score,
    assign_w_score_less_5,
    assign_f_score_less_5,
    assign_w_missing_score_not_5,
    assign_f_missing_score_not_5,
    assign_s_score_less_50p,
    assign_s_ms_score_not_conversion_chart_options,
    assign_s_hs_score_not_conversion_chart_options,

from
    student_unpivot_flags pivot (
        max(student_flag_value) for student_flag_name in (
            'assign_null_score',
            'assign_score_above_max',
            'assign_exempt_with_score',
            'assign_w_score_less_5',
            'assign_f_score_less_5',
            'assign_w_missing_score_not_5',
            'assign_f_missing_score_not_5',
            'assign_s_score_less_50p',
            'assign_s_ms_score_not_conversion_chart_options',
            'assign_s_hs_score_not_conversion_chart_options'
        )
    )