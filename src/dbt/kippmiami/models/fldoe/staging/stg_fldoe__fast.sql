with
    fast_data as (
        select
            student_id,
            local_id,
            _dagster_partition_school_year_term as academic_year,

            `1_reading_prose_and_poetry_performance` as reading_prose_and_poetry,
            `2_reading_informational_text_performance` as reading_informational_text,
            `3_reading_across_genres_vocabulary_performance`
            as reading_across_genres_vocabulary,
            `1_number_sense_and_additive_reasoning_performance`
            as number_sense_and_additive_reasoning,
            `1_number_sense_and_operations_and_algebraic_reasoning_performance`
            as number_sense_and_operations_and_algebraic_reasoning,
            `1_number_sense_and_operations_and_probability_performance`
            as number_sense_and_operations_and_probability,
            `1_number_sense_and_operations_performance` as number_sense_and_operations,
            `1_number_sense_and_operations_with_whole_numbers_performance`
            as number_sense_and_operations_with_whole_numbers,
            `2_number_sense_and_multiplicative_reasoning_performance`
            as number_sense_and_multiplicative_reasoning,
            `2_number_sense_and_operations_with_fractions_and_decimals_performance`
            as number_sense_and_operations_with_fractions_and_decimals,
            `2_proportional_reasoning_and_relationships_performance`
            as proportional_reasoning_and_relationships,
            `3_fractional_reasoning_performance` as fractional_reasoning,
            `3_geometric_reasoning_data_analysis_and_probability_performance`
            as geometric_reasoning_data_analysis_and_probability,
            `3_linear_relationships_data_analysis_and_functions_performance`
            as linear_relationships_data_analysis_and_functions,
            `4_data_analysis_and_probability_performance`
            as data_analysis_and_probability,

            parse_date('%m/%d/%Y', date_taken) as date_taken,
            parse_date('%m/%d/%Y', test_completion_date) as test_completion_date,
            regexp_extract(test_reason, r'\w+\d') as administration_window,
            safe_cast(
                regexp_extract(_dagster_partition_grade_level_subject, r'^(\d)') as int
            ) as assessment_grade,
            regexp_extract(
                _dagster_partition_grade_level_subject, r'(\w+)$'
            ) as assessment_subject,

            coalesce(
                fast_grade_3_ela_reading_achievement_level,
                grade_3_fast_ela_reading_achievement_level,
                fast_grade_4_ela_reading_achievement_level,
                grade_4_fast_ela_reading_achievement_level,
                fast_grade_5_ela_reading_achievement_level,
                grade_5_fast_ela_reading_achievement_level,
                fast_grade_6_ela_reading_achievement_level,
                grade_6_fast_ela_reading_achievement_level,
                fast_grade_7_ela_reading_achievement_level,
                grade_7_fast_ela_reading_achievement_level,
                fast_grade_8_ela_reading_achievement_level,
                grade_8_fast_ela_reading_achievement_level,
                fast_grade_3_mathematics_achievement_level,
                grade_3_fast_mathematics_achievement_level,
                fast_grade_4_mathematics_achievement_level,
                grade_4_fast_mathematics_achievement_level,
                fast_grade_5_mathematics_achievement_level,
                grade_5_fast_mathematics_achievement_level,
                fast_grade_6_mathematics_achievement_level,
                grade_6_fast_mathematics_achievement_level,
                fast_grade_7_mathematics_achievement_level,
                grade_7_fast_mathematics_achievement_level,
                fast_grade_8_mathematics_achievement_level,
                grade_8_fast_mathematics_achievement_level
            ) as achievement_level,

            coalesce(
                fast_grade_3_ela_reading_percentile_rank.string_value,
                grade_3_fast_ela_reading_percentile_rank.string_value,
                fast_grade_4_ela_reading_percentile_rank.string_value,
                grade_4_fast_ela_reading_percentile_rank.string_value,
                fast_grade_5_ela_reading_percentile_rank.string_value,
                grade_5_fast_ela_reading_percentile_rank.string_value,
                fast_grade_6_ela_reading_percentile_rank.string_value,
                grade_6_fast_ela_reading_percentile_rank.string_value,
                fast_grade_7_ela_reading_percentile_rank.string_value,
                grade_7_fast_ela_reading_percentile_rank.string_value,
                fast_grade_8_ela_reading_percentile_rank.string_value,
                grade_8_fast_ela_reading_percentile_rank.string_value,
                fast_grade_3_mathematics_percentile_rank.string_value,
                grade_3_fast_mathematics_percentile_rank.string_value,
                fast_grade_4_mathematics_percentile_rank.string_value,
                grade_4_fast_mathematics_percentile_rank.string_value,
                fast_grade_5_mathematics_percentile_rank.string_value,
                grade_5_fast_mathematics_percentile_rank.string_value,
                fast_grade_6_mathematics_percentile_rank.string_value,
                grade_6_fast_mathematics_percentile_rank.string_value,
                fast_grade_7_mathematics_percentile_rank.string_value,
                grade_7_fast_mathematics_percentile_rank.string_value,
                fast_grade_8_mathematics_percentile_rank.string_value,
                grade_8_fast_mathematics_percentile_rank.string_value,
                safe_cast(
                    fast_grade_3_ela_reading_percentile_rank.long_value as string
                ),
                safe_cast(
                    fast_grade_3_mathematics_percentile_rank.long_value as string
                ),
                safe_cast(
                    fast_grade_4_ela_reading_percentile_rank.long_value as string
                ),
                safe_cast(
                    fast_grade_4_mathematics_percentile_rank.long_value as string
                ),
                safe_cast(
                    fast_grade_5_ela_reading_percentile_rank.long_value as string
                ),
                safe_cast(
                    fast_grade_5_mathematics_percentile_rank.long_value as string
                ),
                safe_cast(
                    fast_grade_6_ela_reading_percentile_rank.long_value as string
                ),
                safe_cast(
                    fast_grade_6_mathematics_percentile_rank.long_value as string
                ),
                safe_cast(
                    fast_grade_7_ela_reading_percentile_rank.long_value as string
                ),
                safe_cast(
                    fast_grade_7_mathematics_percentile_rank.long_value as string
                ),
                safe_cast(
                    fast_grade_8_ela_reading_percentile_rank.long_value as string
                ),
                safe_cast(
                    fast_grade_8_mathematics_percentile_rank.long_value as string
                ),
                safe_cast(
                    grade_3_fast_ela_reading_percentile_rank.long_value as string
                ),
                safe_cast(
                    grade_3_fast_mathematics_percentile_rank.long_value as string
                ),
                safe_cast(
                    grade_4_fast_ela_reading_percentile_rank.long_value as string
                ),
                safe_cast(
                    grade_4_fast_mathematics_percentile_rank.long_value as string
                ),
                safe_cast(
                    grade_5_fast_ela_reading_percentile_rank.long_value as string
                ),
                safe_cast(
                    grade_5_fast_mathematics_percentile_rank.long_value as string
                ),
                safe_cast(
                    grade_6_fast_ela_reading_percentile_rank.long_value as string
                ),
                safe_cast(
                    grade_6_fast_mathematics_percentile_rank.long_value as string
                ),
                safe_cast(
                    grade_7_fast_ela_reading_percentile_rank.long_value as string
                ),
                safe_cast(
                    grade_7_fast_mathematics_percentile_rank.long_value as string
                ),
                safe_cast(
                    grade_8_fast_ela_reading_percentile_rank.long_value as string
                ),
                safe_cast(
                    grade_8_fast_mathematics_percentile_rank.long_value as string
                ),
            ) as percentile_rank,

            coalesce(
                fast_grade_3_ela_reading_scale_score.long_value,
                fast_grade_3_mathematics_scale_score.long_value,
                fast_grade_4_ela_reading_scale_score.long_value,
                fast_grade_4_mathematics_scale_score.long_value,
                fast_grade_5_ela_reading_scale_score.long_value,
                fast_grade_5_mathematics_scale_score.long_value,
                fast_grade_6_ela_reading_scale_score.long_value,
                fast_grade_6_mathematics_scale_score.long_value,
                fast_grade_7_ela_reading_scale_score.long_value,
                fast_grade_7_mathematics_scale_score.long_value,
                fast_grade_8_ela_reading_scale_score.long_value,
                fast_grade_8_mathematics_scale_score.long_value,
                grade_3_fast_ela_reading_scale_score.long_value,
                grade_3_fast_mathematics_scale_score.long_value,
                grade_4_fast_ela_reading_scale_score.long_value,
                grade_4_fast_mathematics_scale_score.long_value,
                grade_5_fast_ela_reading_scale_score.long_value,
                grade_5_fast_mathematics_scale_score.long_value,
                grade_6_fast_ela_reading_scale_score.long_value,
                grade_6_fast_mathematics_scale_score.long_value,
                grade_7_fast_ela_reading_scale_score.long_value,
                grade_7_fast_mathematics_scale_score.long_value,
                grade_8_fast_ela_reading_scale_score.long_value,
                grade_8_fast_mathematics_scale_score.long_value,
                safe_cast(fast_grade_3_ela_reading_scale_score.string_value as int),
                safe_cast(fast_grade_3_mathematics_scale_score.string_value as int),
                safe_cast(fast_grade_4_ela_reading_scale_score.string_value as int),
                safe_cast(fast_grade_4_mathematics_scale_score.string_value as int),
                safe_cast(fast_grade_5_ela_reading_scale_score.string_value as int),
                safe_cast(fast_grade_5_mathematics_scale_score.string_value as int),
                safe_cast(fast_grade_6_ela_reading_scale_score.string_value as int),
                safe_cast(fast_grade_6_mathematics_scale_score.string_value as int),
                safe_cast(fast_grade_7_ela_reading_scale_score.string_value as int),
                safe_cast(fast_grade_7_mathematics_scale_score.string_value as int),
                safe_cast(fast_grade_8_ela_reading_scale_score.string_value as int),
                safe_cast(fast_grade_8_mathematics_scale_score.string_value as int),
                safe_cast(grade_3_fast_ela_reading_scale_score.string_value as int),
                safe_cast(grade_3_fast_mathematics_scale_score.string_value as int),
                safe_cast(grade_4_fast_ela_reading_scale_score.string_value as int),
                safe_cast(grade_4_fast_mathematics_scale_score.string_value as int),
                safe_cast(grade_5_fast_ela_reading_scale_score.string_value as int),
                safe_cast(grade_5_fast_mathematics_scale_score.string_value as int),
                safe_cast(grade_6_fast_ela_reading_scale_score.string_value as int),
                safe_cast(grade_6_fast_mathematics_scale_score.string_value as int),
                safe_cast(grade_7_fast_ela_reading_scale_score.string_value as int),
                safe_cast(grade_7_fast_mathematics_scale_score.string_value as int),
                safe_cast(grade_8_fast_ela_reading_scale_score.string_value as int),
                safe_cast(grade_8_fast_mathematics_scale_score.string_value as int)
            ) as scale_score,

            coalesce(
                `2_algebraic_reasoning_performance`, `3_algebraic_reasoning_performance`
            ) as algebraic_reasoning,
            coalesce(
                `3_geometric_reasoning_performance`, `4_geometric_reasoning_performance`
            ) as geometric_reasoning,
            coalesce(
                -- noqa: disable=LT05
                `3_geometric_reasoning_measurement_and_data_analysis_and_probability_performance`,
                `4_geometric_reasoning_measurement_and_data_analysis_and_probability_performance`
            -- noqa: enable=LT05
            ) as geometric_reasoning_measurement_and_data_analysis_and_probability,
        from {{ source("fldoe", "src_fldoe__fast") }}
    ),

    with_calcs as (
        select
            * except (percentile_rank),
            safe_cast(
                regexp_extract(percentile_rank, r'\d+') as numeric
            ) as percentile_rank,
            safe_cast(
                regexp_extract(achievement_level, r'\d+') as int
            ) as achievement_level_int,
            lag(scale_score, 1) over (
                partition by student_id, academic_year, assessment_subject
                order by administration_window asc
            ) as scale_score_prev,
        from fast_data
    )

select
    *,
    case
        when achievement_level_int >= 3
        then true
        when achievement_level_int < 3
        then false
    end as is_proficient,
from with_calcs
