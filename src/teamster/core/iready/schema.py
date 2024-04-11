import json

import py_avro_schema
from pydantic import BaseModel


class DiagnosticInstruction(BaseModel):
    academic_year: str | None = None
    annual_stretch_growth_measure: float | None = None
    annual_typical_growth_measure: float | None = None
    class_es: str | None = None
    class_teacher_s: str | None = None
    diagnostic_completion_date_1: str | None = None
    diagnostic_completion_date_2: str | None = None
    diagnostic_completion_date_3: str | None = None
    diagnostic_completion_date_4: str | None = None
    diagnostic_completion_date_5: str | None = None
    diagnostic_completion_date_most_recent: str | None = None
    diagnostic_gain_note_negative_gains_zero: str | None = None
    diagnostic_grouping_most_recent: float | None = None
    diagnostic_lexile_measure_most_recent: str | None = None
    diagnostic_lexile_range_most_recent: str | None = None
    diagnostic_overall_placement_1: str | None = None
    diagnostic_overall_placement_2: str | None = None
    diagnostic_overall_placement_3: str | None = None
    diagnostic_overall_placement_4: str | None = None
    diagnostic_overall_placement_5: str | None = None
    diagnostic_overall_placement_most_recent: str | None = None
    diagnostic_overall_relative_placement_1: str | None = None
    diagnostic_overall_relative_placement_2: str | None = None
    diagnostic_overall_relative_placement_3: str | None = None
    diagnostic_overall_relative_placement_4: str | None = None
    diagnostic_overall_relative_placement_5: str | None = None
    diagnostic_overall_relative_placement_most_recent: str | None = None
    diagnostic_overall_scale_score_1: float | None = None
    diagnostic_overall_scale_score_2: float | None = None
    diagnostic_overall_scale_score_3: float | None = None
    diagnostic_overall_scale_score_4: float | None = None
    diagnostic_overall_scale_score_5: float | None = None
    diagnostic_overall_scale_score_most_recent: float | None = None
    diagnostic_percentile_1: float | None = None
    diagnostic_percentile_2: float | None = None
    diagnostic_percentile_3: float | None = None
    diagnostic_percentile_4: float | None = None
    diagnostic_percentile_5: float | None = None
    diagnostic_percentile_most_recent: float | None = None
    diagnostic_quantile_measure_most_recent: str | None = None
    diagnostic_quantile_range_most_recent: str | None = None
    diagnostic_rush_flag_1: str | None = None
    diagnostic_rush_flag_2: str | None = None
    diagnostic_rush_flag_3: str | None = None
    diagnostic_rush_flag_4: str | None = None
    diagnostic_rush_flag_5: str | None = None
    diagnostic_rush_flag_most_recent: str | None = None
    diagnostic_start_date_1: str | None = None
    diagnostic_start_date_2: str | None = None
    diagnostic_start_date_3: str | None = None
    diagnostic_start_date_4: str | None = None
    diagnostic_start_date_5: str | None = None
    diagnostic_start_date_most_recent: str | None = None
    diagnostic_tier_1: str | None = None
    diagnostic_tier_2: str | None = None
    diagnostic_tier_3: str | None = None
    diagnostic_tier_4: str | None = None
    diagnostic_tier_5: str | None = None
    diagnostic_tier_most_recent: str | None = None
    diagnostic_time_on_task_min_1: float | None = None
    diagnostic_time_on_task_min_2: float | None = None
    diagnostic_time_on_task_min_3: float | None = None
    diagnostic_time_on_task_min_4: float | None = None
    diagnostic_time_on_task_min_5: float | None = None
    diagnostic_time_on_task_min_most_recent: float | None = None
    economically_disadvantaged: str | None = None
    english_language_learner: str | None = None
    enrolled: str | None = None
    first_name: str | None = None
    hispanic_or_latino: str | None = None
    instruction_overall_lessons_completed: float | None = None
    instruction_overall_lessons_not_passed: float | None = None
    instruction_overall_lessons_passed: float | None = None
    instruction_overall_pass_rate_percent: float | None = None
    instruction_overall_pass_rate: float | None = None
    instruction_overall_time_on_task_min: float | None = None
    last_name: str | None = None
    migrant: str | None = None
    number_of_completed_diagnostics_during_the_time_frame: int | None = None
    race: str | None = None
    report_group_s: str | None = None
    school: str | None = None
    sex: str | None = None
    special_education: str | None = None
    student_grade: str | None = None
    student_id: int | None = None
    subject: str | None = None
    user_name: str | None = None


class DiagnosticResults(BaseModel):
    academic_year: str | None = None
    algebra_and_algebraic_thinking_placement: str | None = None
    algebra_and_algebraic_thinking_relative_placement: str | None = None
    algebra_and_algebraic_thinking_scale_score: int | None = None
    annual_stretch_growth_measure: int | None = None
    annual_typical_growth_measure: int | None = None
    baseline_diagnostic_y_n: str | None = None
    class_es: str | None = None
    class_teacher_s: str | None = None
    completion_date: str | None = None
    comprehension_informational_text_placement: str | None = None
    comprehension_informational_text_relative_placement: str | None = None
    comprehension_informational_text_scale_score: int | None = None
    comprehension_literature_placement: str | None = None
    comprehension_literature_relative_placement: str | None = None
    comprehension_literature_scale_score: int | None = None
    comprehension_overall_placement: str | None = None
    comprehension_overall_relative_placement: str | None = None
    comprehension_overall_scale_score: int | None = None
    diagnostic_gain: float | None = None
    duration_min: int | None = None
    economically_disadvantaged: str | None = None
    english_language_learner: str | None = None
    enrolled: str | None = None
    first_name: str | None = None
    geometry_placement: str | None = None
    geometry_relative_placement: str | None = None
    geometry_scale_score: int | None = None
    grouping: int | None = None
    high_frequency_words_placement: str | None = None
    high_frequency_words_relative_placement: str | None = None
    high_frequency_words_scale_score: float | None = None
    hispanic_or_latino: str | None = None
    last_name: str | None = None
    lexile_measure: str | None = None
    lexile_range: str | None = None
    measurement_and_data_placement: str | None = None
    measurement_and_data_relative_placement: str | None = None
    measurement_and_data_scale_score: int | None = None
    mid_on_grade_level_scale_score: int | None = None
    migrant: str | None = None
    most_recent_diagnostic_y_n: str | None = None
    most_recent_diagnostic_ytd_y_n: str | None = None
    number_and_operations_placement: str | None = None
    number_and_operations_relative_placement: str | None = None
    number_and_operations_scale_score: int | None = None
    overall_placement: str | None = None
    overall_relative_placement: str | None = None
    overall_scale_score: int | None = None
    percent_progress_to_annual_stretch_growth_percent: float | None = None
    percent_progress_to_annual_typical_growth_percent: float | None = None
    percentile: int | None = None
    phonics_placement: str | None = None
    phonics_relative_placement: str | None = None
    phonics_scale_score: float | None = None
    phonological_awareness_placement: str | None = None
    phonological_awareness_relative_placement: str | None = None
    phonological_awareness_scale_score: float | None = None
    quantile_measure: str | None = None
    quantile_range: str | None = None
    race: str | None = None
    reading_comprehension_informational_text_placement: str | None = None
    reading_comprehension_informational_text_relative_placement: str | None = None
    reading_comprehension_informational_text_scale_score: float | None = None
    reading_comprehension_literature_placement: str | None = None
    reading_comprehension_literature_relative_placement: str | None = None
    reading_comprehension_literature_scale_score: float | None = None
    reading_comprehension_overall_placement: str | None = None
    reading_comprehension_overall_relative_placement: str | None = None
    reading_comprehension_overall_scale_score: float | None = None
    reading_difficulty_indicator_y_n: str | None = None
    report_group_s: str | None = None
    rush_flag: str | None = None
    school: str | None = None
    sex: str | None = None
    special_education: str | None = None
    start_date: str | None = None
    student_id: int | None = None
    user_name: str | None = None
    vocabulary_placement: str | None = None
    vocabulary_relative_placement: str | None = None
    vocabulary_scale_score: int | None = None
    # percent_progress_to_annual_stretch_growth: float | None = None
    # percent_progress_to_annual_typical_growth: float | None = None

    student_grade: str | int | None = None


class InstructionalUsage(BaseModel):
    academic_year: str | None = None
    april_lessons_completed: int | None = None
    april_lessons_passed: float | None = None
    april_percent_lessons_passed: float | None = None
    april_total_time_on_task_min: int | None = None
    april_weekly_average_time_on_task_min: int | None = None
    august_lessons_completed: int | None = None
    august_lessons_passed: float | None = None
    august_percent_lessons_passed: float | None = None
    august_total_time_on_task_min: int | None = None
    august_weekly_average_time_on_task_min: int | None = None
    class_es: str | None = None
    class_teacher_s: str | None = None
    december_lessons_completed: int | None = None
    december_lessons_passed: float | None = None
    december_percent_lessons_passed: float | None = None
    december_total_time_on_task_min: int | None = None
    december_weekly_average_time_on_task_min: int | None = None
    economically_disadvantaged: str | None = None
    english_language_learner: str | None = None
    enrolled: str | None = None
    february_lessons_completed: int | None = None
    february_lessons_passed: float | None = None
    february_percent_lessons_passed: float | None = None
    february_total_time_on_task_min: int | None = None
    february_weekly_average_time_on_task_min: int | None = None
    first_lesson_completion_date: str | None = None
    first_name: str | None = None
    hispanic_or_latino: str | None = None
    january_lessons_completed: int | None = None
    january_lessons_passed: float | None = None
    january_percent_lessons_passed: float | None = None
    january_total_time_on_task_min: int | None = None
    january_weekly_average_time_on_task_min: int | None = None
    july_lessons_completed: int | None = None
    july_lessons_passed: float | None = None
    july_percent_lessons_passed: float | None = None
    july_total_time_on_task_min: int | None = None
    july_weekly_average_time_on_task_min: int | None = None
    june_lessons_completed: int | None = None
    june_lessons_passed: float | None = None
    june_percent_lessons_passed: float | None = None
    june_total_time_on_task_min: int | None = None
    june_weekly_average_time_on_task_min: int | None = None
    last_name: str | None = None
    last_week_end_date: str | None = None
    last_week_lessons_completed: int | None = None
    last_week_lessons_passed: float | None = None
    last_week_percent_lessons_passed: float | None = None
    last_week_start_date: str | None = None
    last_week_time_on_task_min: int | None = None
    march_lessons_completed: int | None = None
    march_lessons_passed: float | None = None
    march_percent_lessons_passed: float | None = None
    march_total_time_on_task_min: int | None = None
    march_weekly_average_time_on_task_min: int | None = None
    may_lessons_completed: int | None = None
    may_lessons_passed: float | None = None
    may_percent_lessons_passed: float | None = None
    may_total_time_on_task_min: int | None = None
    may_weekly_average_time_on_task_min: int | None = None
    migrant: str | None = None
    most_recent_lesson_completion_date: str | None = None
    november_lessons_completed: int | None = None
    november_lessons_passed: float | None = None
    november_percent_lessons_passed: float | None = None
    november_total_time_on_task_min: int | None = None
    november_weekly_average_time_on_task_min: int | None = None
    october_lessons_completed: int | None = None
    october_lessons_passed: float | None = None
    october_percent_lessons_passed: float | None = None
    october_total_time_on_task_min: int | None = None
    october_weekly_average_time_on_task_min: int | None = None
    race: str | None = None
    report_group_s: str | None = None
    school: str | None = None
    september_lessons_completed: int | None = None
    september_lessons_passed: float | None = None
    september_percent_lessons_passed: float | None = None
    september_total_time_on_task_min: int | None = None
    september_weekly_average_time_on_task_min: int | None = None
    sex: str | None = None
    special_education: str | None = None
    student_grade: str | None = None
    student_id: int | None = None
    subject: str | None = None
    user_name: str | None = None
    year_to_date_algebra_and_algebraic_thinking_lessons_completed: int | None = None
    year_to_date_algebra_and_algebraic_thinking_lessons_passed: float | None = None
    year_to_date_algebra_and_algebraic_thinking_percent_lessons_passed: float | None = (
        None
    )
    year_to_date_algebra_and_algebraic_thinking_time_on_task_min: int | None = None
    year_to_date_comprehension_close_reading_lessons_completed: int | None = None
    year_to_date_comprehension_close_reading_lessons_passed: float | None = None
    year_to_date_comprehension_close_reading_percent_lessons_passed: float | None = None
    year_to_date_comprehension_close_reading_time_on_task_min: int | None = None
    year_to_date_comprehension_lessons_completed: int | None = None
    year_to_date_comprehension_lessons_passed: float | None = None
    year_to_date_comprehension_percent_lessons_passed: float | None = None
    year_to_date_comprehension_time_on_task_min: int | None = None
    year_to_date_geometry_lessons_completed: int | None = None
    year_to_date_geometry_lessons_passed: float | None = None
    year_to_date_geometry_percent_lessons_passed: float | None = None
    year_to_date_geometry_time_on_task_min: int | None = None
    year_to_date_high_frequency_words_lessons_completed: int | None = None
    year_to_date_high_frequency_words_lessons_passed: float | None = None
    year_to_date_high_frequency_words_percent_lessons_passed: float | None = None
    year_to_date_high_frequency_words_time_on_task_min: int | None = None
    year_to_date_measurement_and_data_lessons_completed: int | None = None
    year_to_date_measurement_and_data_lessons_passed: float | None = None
    year_to_date_measurement_and_data_percent_lessons_passed: float | None = None
    year_to_date_measurement_and_data_time_on_task_min: int | None = None
    year_to_date_number_and_operations_lessons_completed: int | None = None
    year_to_date_number_and_operations_lessons_passed: float | None = None
    year_to_date_number_and_operations_percent_lessons_passed: float | None = None
    year_to_date_number_and_operations_time_on_task_min: int | None = None
    year_to_date_overall_lessons_completed: int | None = None
    year_to_date_overall_lessons_passed: float | None = None
    year_to_date_overall_percent_lessons_passed: float | None = None
    year_to_date_overall_time_on_task_min: int | None = None
    year_to_date_phonics_lessons_completed: int | None = None
    year_to_date_phonics_lessons_passed: float | None = None
    year_to_date_phonics_percent_lessons_passed: float | None = None
    year_to_date_phonics_time_on_task_min: int | None = None
    year_to_date_phonological_awareness_lessons_completed: int | None = None
    year_to_date_phonological_awareness_lessons_passed: float | None = None
    year_to_date_phonological_awareness_percent_lessons_passed: float | None = None
    year_to_date_phonological_awareness_time_on_task_min: int | None = None
    year_to_date_vocabulary_lessons_completed: int | None = None
    year_to_date_vocabulary_lessons_passed: float | None = None
    year_to_date_vocabulary_percent_lessons_passed: float | None = None
    year_to_date_vocabulary_time_on_task_min: int | None = None


class PersonalizedInstruction(BaseModel):
    academic_year: str | None = None
    class_es: str | None = None
    class_teacher_s: str | None = None
    completion_date: str | None = None
    domain: str | None = None
    economically_disadvantaged: str | None = None
    english_language_learner: str | None = None
    first_name: str | None = None
    hispanic_or_latino: str | None = None
    last_name: str | None = None
    lesson_grade: str | None = None
    lesson_id: str | None = None
    lesson_language: str | None = None
    lesson_level: str | None = None
    lesson_name: str | None = None
    lesson_objective: str | None = None
    migrant: str | None = None
    passed_or_not_passed: str | None = None
    race: str | None = None
    report_group_s: str | None = None
    school: str | None = None
    score: int | None = None
    sex: str | None = None
    special_education: str | None = None
    student_grade: str | None = None
    student_id: int | None = None
    subject: str | None = None
    teacher_assigned_lesson: str | None = None
    total_time_on_lesson_min: int | None = None
    user_name: str | None = None


"""
helper classes for backwards compatibility
"""


class diagnostic_and_instruction_record(DiagnosticInstruction): ...


class diagnostic_results_record(DiagnosticResults): ...


class instructional_usage_data_record(InstructionalUsage): ...


class personalized_instruction_by_lesson_record(PersonalizedInstruction): ...


ASSET_SCHEMA = {
    "diagnostic_and_instruction": json.loads(
        py_avro_schema.generate(
            py_type=diagnostic_and_instruction_record,
            namespace="diagnostic_and_instruction",
        )
    ),
    "diagnostic_results": json.loads(
        py_avro_schema.generate(
            py_type=diagnostic_results_record, namespace="diagnostic_results"
        )
    ),
    "instructional_usage_data": json.loads(
        py_avro_schema.generate(
            py_type=instructional_usage_data_record,
            namespace="instructional_usage_data",
        )
    ),
    "personalized_instruction_by_lesson": json.loads(
        py_avro_schema.generate(
            py_type=personalized_instruction_by_lesson_record,
            namespace="personalized_instruction_by_lesson",
        )
    ),
}
