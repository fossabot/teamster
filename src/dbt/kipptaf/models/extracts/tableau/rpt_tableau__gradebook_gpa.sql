select distinct
    _dbt_source_relation,
    academic_year,
    region,
    school_level,
    schoolid,
    school,
    student_number,
    studentid,
    enroll_status,
    salesforce_id,
    ktc_cohort,
    lastfirst,
    gender,
    grade_level,
    ethnicity,
    cohort,
    year_in_school,
    lep_status,
    is_504,
    is_pathways,
    iep_status,
    lunch_status,
    is_counseling_services,
    is_student_athlete,
    year_in_network,
    is_retained_year,
    is_retained_ever,
    rn_undergrad,
    advisory,
    advisor_name,
    ada,
    ada_above_or_at_80,
    hos,
    roster_type,
    semester,
    quarter,
    tutoring_nj,
    nj_student_tier,
    course_name,
    course_number,
    sectionid,
    sections_dcid,
    section_number,
    external_expression,
    credit_type,
    teacher_number,
    teacher_name,
    exclude_from_gpa,
    is_current_quarter,
    quarter_start_date,
    quarter_end_date,
    category_name_code,
    category_quarter_code,
    category_quarter_percent_grade,
    category_y1_percent_grade_running,
    category_y1_percent_grade_current,
    category_quarter_average_all_courses,
    quarter_course_in_progress_percent_grade,
    quarter_course_in_progress_letter_grade,
    quarter_course_in_progress_grade_points,
    quarter_course_in_progress_percent_grade_adjusted,
    quarter_course_in_progress_letter_grade_adjusted,
    quarter_course_final_percent_grade,
    quarter_course_final_letter_grade,
    quarter_course_final_grade_points,
    quarter_course_percent_grade_that_matters,
    quarter_course_letter_grade_that_matters,
    quarter_course_grade_points_that_matters,
    need_60,
    need_70,
    need_80,
    need_90,
    quarter_citizenship,
    quarter_comment_value,
    y1_course_in_progress_percent_grade,
    y1_course_in_progress_percent_grade_adjusted,
    y1_course_in_progress_letter_grade,
    y1_course_in_progress_letter_grade_adjusted,
    y1_course_in_progress_grade_points,
    y1_course_in_progress_grade_points_unweighted,
    y1_course_final_percent_grade_adjusted,
    y1_course_final_letter_grade_adjusted,
    y1_course_final_earned_credits,
    y1_course_final_potential_credit_hours,
    y1_course_final_grade_points,
    gpa_for_quarter,
    gpa_semester,
    gpa_y1,
    gpa_y1_unweighted,
    gpa_total_credit_hours,
    gpa_n_failing_y1,
    gpa_cumulative_y1_gpa,
    gpa_cumulative_y1_gpa_unweighted,
    gpa_cumulative_y1_gpa_projected,
    gpa_cumulative_y1_gpa_projected_s1,
    gpa_cumulative_y1_gpa_projected_s1_unweighted,
    gpa_core_cumulative_y1_gpa,
    teacher_quarter,
    expected_teacher_assign_category_code,
    expected_teacher_assign_category_name,
    audit_yr_week_number,
    audit_qt_week_number,
    audit_start_date,
    audit_end_date,
    audit_due_date,
    audit_category_exp_audit_week_ytd,
    teacher_assign_id,
    teacher_assign_name,
    teacher_assign_score_type,
    teacher_assign_max_score,
    teacher_assign_due_date,
    teacher_assign_count,
    teacher_running_total_assign_by_cat,
    teacher_avg_score_for_assign_per_class_section_and_assign_id,
    total_expected_actual_graded_assignments_by_cat_qt_audit_week_all_courses,
    total_expected_graded_assignments_by_cat_qt_audit_week_all_courses,
    total_expected_actual_graded_assignments_by_course_cat_qt_audit_week,
    total_expected_graded_assignments_by_course_cat_qt_audit_week,
    total_expected_actual_graded_assignments_by_course_assign_id_qt_audit_week,
    total_expected_graded_assignments_by_course_assign_id_qt_audit_week,
    percent_graded_completion_by_cat_qt_audit_week_all_courses,
    percent_graded_completion_by_cat_qt_audit_week,
    percent_graded_completion_by_assign_id_qt_audit_week,
    student_course_entry_date,
    assign_category_code,
    assign_category,
    assign_category_quarter,
    assign_id,
    assign_name,
    assign_due_date,
    assign_score_type,
    assign_score_raw,
    assign_score_converted,
    assign_max_score,
    assign_is_exempt,
    assign_is_late,
    assign_is_missing,

    audit_flag_name,
    audit_flag_value,

from
    {{ ref("int_powerschool__gradebook_gpa") }} unpivot (
        audit_flag_value for audit_flag_name in (
            qt_teacher_no_missing_assignments,
            qt_teacher_s_total_less_200,
            qt_teacher_s_total_greater_200,
            w_assign_max_score_not_10,
            f_assign_max_score_not_10,
            s_max_score_greater_100,
            w_expected_assign_count_not_met,
            f_expected_assign_count_not_met,
            s_expected_assign_count_not_met,
            assign_null_score,
            assign_score_above_max,
            assign_exempt_with_score,
            assign_w_score_less_5,
            assign_f_score_less_5,
            assign_w_missing_score_not_5,
            assign_f_missing_score_not_5,
            assign_s_score_less_50p,
            qt_assign_no_course_assignments,
            qt_kg_conduct_code_missing,
            qt_kg_conduct_code_not_hr,
            qt_g1_g8_conduct_code_missing,
            qt_kg_conduct_code_incorrect,
            qt_g1_g8_conduct_code_incorrect,
            qt_grade_70_comment_missing,
            qt_es_comment_missing,
            qt_comment_missing,
            qt_percent_grade_greater_100,
            w_percent_graded_completion_by_qt_audit_week_not_100,
            f_percent_graded_completion_by_qt_audit_week_not_100,
            s_percent_graded_completion_by_qt_audit_week_not_100,
            qt_student_is_ada_80_plus_gpa_less_2,
            w_grade_inflation
        )
    )
where audit_flag_value = 1

union all

select distinct
    _dbt_source_relation,
    academic_year,
    region,
    school_level,
    schoolid,
    school,
    student_number,
    studentid,
    enroll_status,
    salesforce_id,
    ktc_cohort,
    lastfirst,
    gender,
    grade_level,
    ethnicity,
    cohort,
    year_in_school,
    lep_status,
    is_504,
    is_pathways,
    iep_status,
    lunch_status,
    is_counseling_services,
    is_student_athlete,
    year_in_network,
    is_retained_year,
    is_retained_ever,
    rn_undergrad,
    advisory,
    advisor_name,
    ada,
    ada_above_or_at_80,
    hos,
    roster_type,
    semester,
    quarter,
    tutoring_nj,
    nj_student_tier,
    course_name,
    course_number,
    sectionid,
    sections_dcid,
    section_number,
    external_expression,
    credit_type,
    teacher_number,
    teacher_name,
    exclude_from_gpa,
    is_current_quarter,
    quarter_start_date,
    quarter_end_date,
    category_name_code,
    category_quarter_code,
    category_quarter_percent_grade,
    category_y1_percent_grade_running,
    category_y1_percent_grade_current,
    category_quarter_average_all_courses,
    quarter_course_in_progress_percent_grade,
    quarter_course_in_progress_letter_grade,
    quarter_course_in_progress_grade_points,
    quarter_course_in_progress_percent_grade_adjusted,
    quarter_course_in_progress_letter_grade_adjusted,
    quarter_course_final_percent_grade,
    quarter_course_final_letter_grade,
    quarter_course_final_grade_points,
    quarter_course_percent_grade_that_matters,
    quarter_course_letter_grade_that_matters,
    quarter_course_grade_points_that_matters,
    need_60,
    need_70,
    need_80,
    need_90,
    quarter_citizenship,
    quarter_comment_value,
    y1_course_in_progress_percent_grade,
    y1_course_in_progress_percent_grade_adjusted,
    y1_course_in_progress_letter_grade,
    y1_course_in_progress_letter_grade_adjusted,
    y1_course_in_progress_grade_points,
    y1_course_in_progress_grade_points_unweighted,
    y1_course_final_percent_grade_adjusted,
    y1_course_final_letter_grade_adjusted,
    y1_course_final_earned_credits,
    y1_course_final_potential_credit_hours,
    y1_course_final_grade_points,
    gpa_for_quarter,
    gpa_semester,
    gpa_y1,
    gpa_y1_unweighted,
    gpa_total_credit_hours,
    gpa_n_failing_y1,
    gpa_cumulative_y1_gpa,
    gpa_cumulative_y1_gpa_unweighted,
    gpa_cumulative_y1_gpa_projected,
    gpa_cumulative_y1_gpa_projected_s1,
    gpa_cumulative_y1_gpa_projected_s1_unweighted,
    gpa_core_cumulative_y1_gpa,
    teacher_quarter,
    expected_teacher_assign_category_code,
    expected_teacher_assign_category_name,
    audit_yr_week_number,
    audit_qt_week_number,
    audit_start_date,
    audit_end_date,
    audit_due_date,
    audit_category_exp_audit_week_ytd,
    teacher_assign_id,
    teacher_assign_name,
    teacher_assign_score_type,
    teacher_assign_max_score,
    teacher_assign_due_date,
    teacher_assign_count,
    teacher_running_total_assign_by_cat,
    teacher_avg_score_for_assign_per_class_section_and_assign_id,
    total_expected_actual_graded_assignments_by_cat_qt_audit_week_all_courses,
    total_expected_graded_assignments_by_cat_qt_audit_week_all_courses,
    total_expected_actual_graded_assignments_by_course_cat_qt_audit_week,
    total_expected_graded_assignments_by_course_cat_qt_audit_week,
    total_expected_actual_graded_assignments_by_course_assign_id_qt_audit_week,
    total_expected_graded_assignments_by_course_assign_id_qt_audit_week,
    percent_graded_completion_by_cat_qt_audit_week_all_courses,
    percent_graded_completion_by_cat_qt_audit_week,
    percent_graded_completion_by_assign_id_qt_audit_week,
    student_course_entry_date,
    assign_category_code,
    assign_category,
    assign_category_quarter,
    assign_id,
    assign_name,
    assign_due_date,
    assign_score_type,
    assign_score_raw,
    assign_score_converted,
    assign_max_score,
    assign_is_exempt,
    assign_is_late,
    assign_is_missing,

    'No Issues' as audit_flag_name,
    null as audit_flag_value,

from
    {{ ref("int_powerschool__gradebook_gpa") }} unpivot (
        audit_flag_value for audit_flag_name in (
            qt_teacher_no_missing_assignments,
            qt_teacher_s_total_less_200,
            qt_teacher_s_total_greater_200,
            w_assign_max_score_not_10,
            f_assign_max_score_not_10,
            s_max_score_greater_100,
            w_expected_assign_count_not_met,
            f_expected_assign_count_not_met,
            s_expected_assign_count_not_met,
            assign_null_score,
            assign_score_above_max,
            assign_exempt_with_score,
            assign_w_score_less_5,
            assign_f_score_less_5,
            assign_w_missing_score_not_5,
            assign_f_missing_score_not_5,
            assign_s_score_less_50p,
            qt_assign_no_course_assignments,
            qt_kg_conduct_code_missing,
            qt_kg_conduct_code_not_hr,
            qt_g1_g8_conduct_code_missing,
            qt_kg_conduct_code_incorrect,
            qt_g1_g8_conduct_code_incorrect,
            qt_grade_70_comment_missing,
            qt_es_comment_missing,
            qt_comment_missing,
            qt_percent_grade_greater_100,
            w_percent_graded_completion_by_qt_audit_week_not_100,
            f_percent_graded_completion_by_qt_audit_week_not_100,
            s_percent_graded_completion_by_qt_audit_week_not_100,
            qt_student_is_ada_80_plus_gpa_less_2,
            w_grade_inflation
        )
    )
where audit_flag_value = 0
