{% set expected_teacher_assign_category_code = ["W", "F", "S"] %}

with
    assign_1 as (
        select distinct
            t.academic_year,
            t.grade_band as school_level,
            t.name as teacher_quarter,

            s._dbt_source_relation,
            s.terms_yearid as yearid,
            s.sections_schoolid as schoolid,
            s.teachernumber as teacher_number,
            s.teacher_lastfirst as teacher_name,
            s.courses_course_number as course_number,
            s.sections_schedulesectionid as sectionid,
            s.sections_dcid,

            expected_teacher_assign_category_code,

            1 as counter,

            case
                when t.grade_band in ('ES', 'MS')
                then s.sections_section_number
                else s.sections_external_expression
            end as section,

            case
                regexp_extract(s._dbt_source_relation, r'(kipp\w+)_')
                when 'kippcamden'
                then 'Camden'
                when 'kippnewark'
                then 'Newark'
                when 'kippmiami'
                then 'Miami'
            end as region,

        from {{ ref("stg_reporting__terms") }} as t
        left join
            {{ ref("base_powerschool__sections") }} as s
            on t.powerschool_year_id = s.terms_yearid
            and t.school_id = s.sections_schoolid
            and t.type = 'RT'
            and t.grade_band is not null
        cross join
            unnest(
                {{ expected_teacher_assign_category_code }}
            ) as expected_teacher_assign_category_code
        where
            t.academic_year = {{ var("current_academic_year") }}
            and s.courses_schoolid != 999999
            and current_date('America/New_York')
            between s.terms_firstday and s.terms_lastday
    ),

    assign_2 as (
        select distinct
            t._dbt_source_relation,
            t.yearid,
            t.academic_year,
            t.region,
            t.schoolid,
            t.school_level,
            t.teacher_number,
            t.teacher_name,
            t.course_number,
            t.`section`,
            t.sectionid,
            t.sections_dcid,
            t.expected_teacher_assign_category_code,
            t.teacher_quarter,
            t.counter,

            aud.year_week_number,
            aud.quarter_week_number,
            aud.audit_start_date,
            aud.audit_end_date,
            aud.audit_due_date,

            case
                t.expected_teacher_assign_category_code
                when 'W'
                then 'Work Habits'
                when 'F'
                then 'Formative Mastery'
                when 'S'
                then 'Summative Mastery'
            end as expected_teacher_assign_category_name,

            case
                t.expected_teacher_assign_category_code
                when 'W'
                then aud.w_expected_quarter
                when 'F'
                then aud.f_expected_quarter
                when 'S'
                then aud.s_expected_quarter
            end as audit_category_exp_audit_week_ytd,

        from assign_1 as t
        left join
            {{ ref("stg_reporting__gradebook_expectations") }} as aud
            on t.academic_year = aud.academic_year
            and t.teacher_quarter = aud.quarter
            and t.region = aud.region
    ),

    assign_3 as (
        select distinct
            t._dbt_source_relation,
            t.yearid,
            t.academic_year,
            t.region,
            t.schoolid,
            t.school_level,
            t.teacher_number,
            t.teacher_name,
            t.course_number,
            t.`section`,
            t.sectionid,
            t.sections_dcid,
            t.teacher_quarter,
            t.year_week_number,
            t.quarter_week_number,
            t.audit_start_date,
            t.audit_end_date,
            t.audit_due_date,
            t.expected_teacher_assign_category_code,
            t.expected_teacher_assign_category_name,
            t.audit_category_exp_audit_week_ytd,
            t.counter,
            a.assignmentid as teacher_assign_id,
            a.name as teacher_assign_name,
            a.scoretype as teacher_assign_score_type,
            a.totalpointvalue as teacher_assign_max_score,
            a.duedate as teacher_assign_due_date,

            if(a.assignmentid is null, 0, 1) as teacher_assign_count,

        from assign_2 as t
        inner join
            {{ ref("int_powerschool__section_grade_config") }} as gb
            on t.sections_dcid = gb.sections_dcid
            and t.expected_teacher_assign_category_name = gb.category_name
            and gb.grading_formula_weighting_type != 'Total_Points'
            and {{ union_dataset_join_clause(left_alias="t", right_alias="gb") }}
        left join
            {{ ref("int_powerschool__gradebook_assignments") }} as a
            on gb.sections_dcid = a.sectionsdcid
            and gb.category_id = a.category_id
            and a.duedate between t.audit_start_date and t.audit_end_date
            and a.category_name = t.expected_teacher_assign_category_name
            and a.iscountedinfinalgrade = 1
            and {{ union_dataset_join_clause(left_alias="gb", right_alias="a") }}
    ),

    assign_4 as (
        select
            _dbt_source_relation,
            yearid,
            academic_year,
            region,
            schoolid,
            school_level,
            teacher_number,
            teacher_name,
            course_number,
            `section`,
            sectionid,
            sections_dcid,
            teacher_quarter,
            year_week_number,
            quarter_week_number,
            audit_start_date,
            audit_end_date,
            audit_due_date,
            expected_teacher_assign_category_code,
            expected_teacher_assign_category_name,
            audit_category_exp_audit_week_ytd,
            counter,
            teacher_assign_id,
            teacher_assign_name,
            teacher_assign_score_type,
            teacher_assign_max_score,
            teacher_assign_due_date,
            teacher_assign_count,

            if(
                sum(teacher_assign_count) over (
                    partition by
                        schoolid,
                        teacher_name,
                        course_number,
                        section,
                        teacher_quarter,
                        expected_teacher_assign_category_code
                    order by teacher_quarter, quarter_week_number
                )
                >= audit_category_exp_audit_week_ytd,
                0,
                1
            ) as teacher_category_assign_count_expected_not_met,

            sum(teacher_assign_count) over (
                partition by
                    schoolid,
                    teacher_name,
                    course_number,
                    section,
                    teacher_quarter,
                    expected_teacher_assign_category_code
                order by teacher_quarter, quarter_week_number
            ) as teacher_running_total_assign_by_cat,

        from assign_3
    ),

    assign_5 as (
        select distinct
            t._dbt_source_relation,
            t.yearid,
            t.academic_year,
            t.region,
            t.schoolid,
            t.school_level,
            t.teacher_number,
            t.teacher_name,
            t.course_number,
            t.`section`,
            t.sectionid,
            t.sections_dcid,
            t.teacher_quarter,
            t.year_week_number,
            t.quarter_week_number,
            t.audit_start_date,
            t.audit_end_date,
            t.audit_due_date,
            t.expected_teacher_assign_category_code,
            t.expected_teacher_assign_category_name,
            t.audit_category_exp_audit_week_ytd,
            t.counter,
            t.teacher_assign_id,
            t.teacher_assign_name,
            t.teacher_assign_score_type,
            t.teacher_assign_max_score,
            t.teacher_assign_due_date,
            t.teacher_assign_count,
            t.teacher_running_total_assign_by_cat,
            t.teacher_category_assign_count_expected_not_met,

            if(t.teacher_quarter in ('Q1', 'Q2'), 'S1', 'S2') as teacher_semester_code,

            avg(
                if(
                    asg.assign_expected_with_score = 1,
                    asg.assign_final_score_percent,
                    null
                )
            ) over (
                partition by
                    t.schoolid,
                    t.teacher_quarter,
                    t.teacher_name,
                    t.course_number,
                    t.section,
                    t.teacher_assign_id
            ) as teacher_avg_score_for_assign_per_class_section_and_assign_id,

            sum(asg.assign_expected_with_score) over (
                partition by
                    t.schoolid,
                    t.teacher_name,
                    t.teacher_quarter,
                    t.quarter_week_number,
                    asg.assign_category_code
            ) as
            total_expected_actual_graded_assignments_by_cat_qt_audit_week_all_courses,

            sum(asg.assign_expected_to_be_scored) over (
                partition by
                    t.schoolid,
                    t.teacher_name,
                    t.teacher_quarter,
                    t.quarter_week_number,
                    asg.assign_category_code
            ) as total_expected_graded_assignments_by_cat_qt_audit_week_all_courses,

            sum(asg.assign_expected_with_score) over (
                partition by
                    t.schoolid,
                    t.teacher_quarter,
                    t.quarter_week_number,
                    t.course_number,
                    t.section,
                    asg.assign_category_code
            ) as total_expected_actual_graded_assignments_by_course_cat_qt_audit_week,

            sum(asg.assign_expected_to_be_scored) over (
                partition by
                    t.schoolid,
                    t.teacher_quarter,
                    t.quarter_week_number,
                    t.course_number,
                    t.section,
                    asg.assign_category_code
            ) as total_expected_graded_assignments_by_course_cat_qt_audit_week,

            sum(asg.assign_expected_with_score) over (
                partition by
                    t.schoolid,
                    t.course_number,
                    t.sectionid,
                    t.teacher_quarter,
                    t.quarter_week_number,
                    asg.assign_category,
                    asg.assign_id
            ) as
            total_expected_actual_graded_assignments_by_course_assign_id_qt_audit_week,

            sum(asg.assign_expected_to_be_scored) over (
                partition by
                    t.schoolid,
                    t.course_number,
                    t.sectionid,
                    t.teacher_quarter,
                    t.quarter_week_number,
                    asg.assign_category,
                    asg.assign_id
            ) as total_expected_graded_assignments_by_course_assign_id_qt_audit_week,

            -- flags
            if(
                sum(asg.assign_is_missing) over (
                    partition by
                        t.schoolid,
                        t.teacher_quarter,
                        t.teacher_name,
                        t.course_number,
                        t.section
                )
                = 0,
                1,
                0
            ) as qt_teacher_no_missing_assignments,

            if(
                sum(
                    if(
                        asg.assign_category_code = 'S'
                        and asg.assign_expected_to_be_scored = 1,
                        t.teacher_assign_max_score,
                        0
                    )
                ) over (
                    partition by
                        t.schoolid,
                        t.teacher_quarter,
                        t.teacher_name,
                        t.course_number,
                        t.section
                )
                < 200,
                1,
                0
            ) as qt_teacher_s_total_less_200,

            if(
                sum(
                    if(asg.assign_category_code = 'S', t.teacher_assign_max_score, 0)
                ) over (
                    partition by
                        t.schoolid,
                        t.teacher_quarter,
                        t.teacher_name,
                        t.course_number,
                        t.section
                )
                > 200,
                1,
                0
            ) as qt_teacher_s_total_greater_200,

        from assign_4 as t
        left join
            {{ ref("int_powerschool__student_assignments") }} as asg
            on t.academic_year = asg.academic_year
            and t.schoolid = asg.schoolid
            and t.course_number = asg.course_number
            and t.sections_dcid = asg.sections_dcid
            and t.expected_teacher_assign_category_code = asg.assign_category_code
            and t.teacher_assign_id = asg.assign_id
            and {{ union_dataset_join_clause(left_alias="t", right_alias="asg") }}
    )

select
    _dbt_source_relation,
    yearid,
    academic_year,
    region,
    schoolid,
    school_level,
    teacher_number,
    teacher_name,
    course_number,
    `section`,
    sectionid,
    sections_dcid,
    teacher_quarter,
    year_week_number,
    quarter_week_number,
    audit_start_date,
    audit_end_date,
    audit_due_date,
    expected_teacher_assign_category_code,
    expected_teacher_assign_category_name,
    audit_category_exp_audit_week_ytd,
    counter,
    teacher_assign_id,
    teacher_assign_name,
    teacher_assign_score_type,
    teacher_assign_max_score,
    teacher_assign_due_date,
    teacher_assign_count,
    teacher_running_total_assign_by_cat,
    teacher_semester_code,
    teacher_avg_score_for_assign_per_class_section_and_assign_id,
    total_expected_actual_graded_assignments_by_cat_qt_audit_week_all_courses,
    total_expected_graded_assignments_by_cat_qt_audit_week_all_courses,
    total_expected_actual_graded_assignments_by_course_cat_qt_audit_week,
    total_expected_graded_assignments_by_course_cat_qt_audit_week,
    total_expected_actual_graded_assignments_by_course_assign_id_qt_audit_week,
    total_expected_graded_assignments_by_course_assign_id_qt_audit_week,

    qt_teacher_no_missing_assignments,
    qt_teacher_s_total_less_200,
    qt_teacher_s_total_greater_200,

    if(
        expected_teacher_assign_category_code = 'W'
        and teacher_category_assign_count_expected_not_met = 1,
        1,
        0
    ) as w_expected_assign_count_not_met,

    if(
        expected_teacher_assign_category_code = 'F'
        and teacher_category_assign_count_expected_not_met = 1,
        1,
        0
    ) as f_expected_assign_count_not_met,

    if(
        expected_teacher_assign_category_code = 'S'
        and teacher_category_assign_count_expected_not_met = 1,
        1,
        0
    ) as s_expected_assign_count_not_met,

    if(
        expected_teacher_assign_category_code = 'W' and teacher_assign_max_score != 10,
        1,
        0
    ) as w_assign_max_score_not_10,

    if(
        expected_teacher_assign_category_code = 'F' and teacher_assign_max_score != 10,
        1,
        0
    ) as f_assign_max_score_not_10,

    if(
        region = 'FL'
        and expected_teacher_assign_category_code = 'S'
        and teacher_assign_max_score > 100,
        1,
        0
    ) as s_max_score_greater_100,

    round(
        safe_divide(
            total_expected_actual_graded_assignments_by_cat_qt_audit_week_all_courses,
            total_expected_graded_assignments_by_cat_qt_audit_week_all_courses
        ),
        2
    ) as percent_graded_completion_by_cat_qt_audit_week_all_courses,

    round(
        safe_divide(
            total_expected_actual_graded_assignments_by_course_cat_qt_audit_week,
            total_expected_graded_assignments_by_course_cat_qt_audit_week
        ),
        2
    ) as percent_graded_completion_by_cat_qt_audit_week,

    round(
        safe_divide(
            total_expected_actual_graded_assignments_by_course_assign_id_qt_audit_week,
            total_expected_graded_assignments_by_course_assign_id_qt_audit_week
        ),
        2
    ) as percent_graded_completion_by_assign_id_qt_audit_week,

from assign_5