-- IMPORT CTEs
with
    adb_official_tests as (  -- ADB table with official ACT and SAT scores
        select *
        from {{ ref("int_kippadb__standardized_test_unpivot") }}
        where
            score_type in (
                'act_composite',
                'act_reading',
                'act_math',
                'act_english',
                'act_science',
                'sat_total_score',
                'sat_reading_test_score',
                'sat_math_test_score',
                'sat_math',
                'sat_ebrw'
            )
    ),

    adb_roster as (  -- ADB to student_number crosswalk
        select * from {{ ref("int_kippadb__roster") }}
    ),

    illum_assessments_list as (  -- List of Illum assessments
        select *
        from {{ ref("base_illuminate__assessments") }}
        where scope in ('ACT Prep', 'SAT')
    ),

    illum_students as (select * from {{ ref("stg_illuminate__students") }}),  -- Crosswalk for Illum student IDs and student_number

    illum_students_questions_groups as (  -- Student total answers by groups
        select * from {{ ref("stg_illuminate__agg_student_responses_group") }}
    ),

    illum_reporting_groups as (  -- Illu crossswalk of reporting group ID to its name
        select * from {{ ref("stg_illuminate__reporting_groups") }}
    ),

    rpt_terms as (select * from {{ ref("stg_reporting__terms") }}),  -- Google-Sheet with reporting terms to tag BOY

    scale_score_key as (  -- Google-Sheet with scale score conversions from raw ranges
        select * from {{ ref("stg_assessments__act_scale_score_key") }}
    ),

    student_enrollments as (
        select *
        from {{ ref("base_powerschool__student_enrollments") }}  -- PowerSchool enrollment table for GL and school info
        where rn_year = 1
    ),

    -- LOGICAL CTEs
    ms_grad as (  -- Brings the name of the middle school the student graduated it from (to identify the latest MS in the district the student attended)
        select sub.student_number, sub.ms_attended
        from
            (
                select
                    student_number,
                    school_name as ms_attended,
                    row_number() over (
                        partition by student_number order by exitdate desc
                    ) as rn
                from student_enrollments
                where school_level = 'MS'
            ) as sub
        where rn = 1
    ),

    act_official as (  -- All types of ACT scores from ADB
        select
            ktc.student_number,
            stl.contact,  -- ID from ADB for the student
            'Official' as test_type,
            test_type as scope,
            concat(
                format_date('%b', stl.date), ' ', format_date('%g', stl.date)
            ) as administration_round,
            stl.date as test_date,
            case
                when stl.score_type = 'act_composite'
                then 'Composite'
                when stl.score_type = 'act_reading'
                then 'Reading'
                when stl.score_type = 'act_math'
                then 'Math'
                when stl.score_type = 'act_english'
                then 'English'
                when stl.score_type = 'act_science'
                then 'Science'
            end as subject_area,
            stl.score as scale_score,
            row_number() over (
                partition by stl.contact, stl.score_type order by stl.score desc
            ) as rn_highest  -- Sorts the table in desc order to calculate the highest score per score_type per student
        from adb_official_tests as stl  -- ADB scores data
        inner join adb_roster as ktc on stl.contact = ktc.contact_id
        where
            stl.score_type in (
                'act_composite', 'act_reading', 'act_math', 'act_english', 'act_science'
            )
    ),

    sat_official  -- All types of SAT scores from ADB
    as (
        select
            ktc.student_number,
            stl.contact,  -- ID from ADB for the student
            'Official' as test_type,
            test_type as scope,
            concat(
                format_date('%b', stl.date), ' ', format_date('%g', stl.date)
            ) as administration_round,
            stl.date as test_date,
            case
                when stl.score_type = 'sat_total_score'  -- Need to verify all of these are accurately tagged to match NJ's grad requirements
                then 'Composite'
                when stl.score_type = 'sat_reading_test_score'
                then 'Reading Test'
                when stl.score_type = 'sat_math_test_score'
                then 'Math Test'
                when stl.score_type = 'sat_math'
                then 'Math'
                when stl.score_type = 'sat_ebrw'
                then 'EBRW'
            end as subject_area,
            stl.score as scale_score,
            row_number() over (
                partition by stl.contact, stl.score_type order by stl.score desc
            ) as rn_highest  -- sorts the table in desc order to calculate the highest score per score_type per student
        from adb_official_tests as stl  -- ADB scores data
        inner join
            adb_roster as ktc  -- ADB to student_number crosswalk
            on stl.contact = ktc.contact_id
        where
            stl.score_type in (
                'sat_total_score',
                'sat_reading_test_score',
                'sat_math_test_score',
                'sat_math',
                'sat_ebrw'
            )
    ),

    act_sat_official as (
        select *
        from act_official
        union all
        select *
        from sat_official
    ),

    practice_tests  -- Foundation ACT/SAT Prep Practice Test data from Illuminate
    as (
        select
            ais.academic_year_clean as academic_year,  -- Fall SY
            co.schoolid,
            asr.student_id as illuminate_student_id,
            co.student_number,
            co.grade_level,
            concat(
                format_date('%b', ais.administered_at),
                ' ',
                format_date('%g', ais.administered_at)
            ) as administration_round,
            ais.administered_at as test_date,
            safe_cast(rt.code as string) as scope_round,
            safe_cast(rt.name as string) as test_type,
            ais.assessment_id,
            safe_cast(ais.title as string) as assessment_title,
            ais.scope,  -- To differentiate between ACT/SAT preps
            safe_cast(ais.subject_area as string) as subject_area,
            asr.performance_band_level as overall_performance_band_for_group,
            asr.reporting_group_id,
            rg.label as reporting_group_label,
            asr.points as points_earned_for_group_subject,
            asr.points_possible as points_possible_for_group_subject,
            sum(asr.points) over (
                partition by
                    ais.assessment_id, rt.code, ais.subject_area, asr.student_id
            ) as overall_number_correct_for_scope_round_per_subject,  -- Calculate total earned raw score for all groups combined per scope and subject
            sum(asr.points_possible) over (
                partition by
                    ais.assessment_id, rt.code, ais.subject_area, asr.student_id
            ) as overall_number_possible_for_scope_round_per_subject  -- Calc max eligible raw score for all groups combined
        from illum_assessments_list as ais
        inner join
            illum_students_questions_groups as asr
            on ais.assessment_id = asr.assessment_id
        inner join illum_students as s on asr.student_id = s.student_id
        inner join
            rpt_terms as rt
            on (ais.administered_at between rt.start_date and rt.end_date)
            and rt.type = ais.scope
        inner join
            student_enrollments as co
            on s.local_student_id = co.student_number
            and ais.academic_year_clean = co.academic_year
            and co.rn_year = 1
        inner join
            illum_reporting_groups as rg
            on asr.reporting_group_id = rg.reporting_group_id
    ),

    practice_tests_with_scale_score_and_composite  -- Convert the number of correct questions (raw) to the scale score for ACT/SAT Prep
    as (
        select
            l.academic_year,
            l.schoolid,
            l.illuminate_student_id,
            l.student_number,
            l.grade_level,
            l.administration_round,
            l.test_date,
            l.scope_round,
            l.assessment_id,
            l.assessment_title,
            l.scope,
            case
                when l.subject_area = 'Mathematics' then 'Math' else l.subject_area
            end as subject_area,
            count(distinct l.subject_area) over (
                partition by
                    l.student_number,
                    l.academic_year,
                    l.grade_level,
                    l.administration_round
            ) as total_subjects_tested_per_scope_round,
            l.overall_performance_band_for_group,
            l.reporting_group_id,
            l.reporting_group_label,
            l.points_earned_for_group_subject,
            l.points_possible_for_group_subject,
            l.overall_number_correct_for_scope_round_per_subject,
            l.overall_number_possible_for_scope_round_per_subject,
            cast(ssk.scale_score as int64) as scale_score_for_scope_round_per_subject,  -- Uses the approx raw score to bring a scale score from the G-Sheet
            case
                when
                    count(distinct l.subject_area) over (  -- If the total number of subject areas tested matches the total count needed per scope
                        partition by
                            l.student_number,
                            l.academic_year,
                            l.grade_level,
                            l.administration_round
                    )
                    = 4
                then
                    sum(distinct ssk.scale_score) over (  -- Then add all of the distinct scale scores for all subjects to create the composite score
                        partition by
                            l.student_number,
                            l.academic_year,
                            l.grade_level,
                            l.administration_round,
                            l.scope_round,
                            l.subject_area
                    )
            end as overall_composite_score  -- Otherwise NULL it
        from practice_tests as l
        left join
            scale_score_key as ssk
            on l.academic_year = ssk.academic_year
            and l.scope = ssk.test_type
            and l.grade_level = ssk.grade_level
            and l.scope_round = ssk.administration_round
            and (  -- Simplify later when updates/fixes get loaded
                case
                    when l.subject_area = 'Mathematics'
                    then 'Math'
                    when l.subject_area is null
                    then 'Writing'
                    else l.subject_area
                end
            )
            = ssk.subject
            and (
                l.overall_number_correct_for_scope_round_per_subject
                between ssk.raw_score_low and ssk.raw_score_high
            )
    ),

    final_official as (
        select
            e.academic_year,
            e.region,
            e.schoolid,
            e.school_abbreviation,
            e.student_number,
            e.lastfirst,
            e.grade_level,
            e.enroll_status,
            e.advisor_lastfirst,
            e.cohort,
            case when e.spedlep in ('No IEP', null) then 0 else 1 end as sped,
            m.ms_attended,
            o.test_type,
            null as assessment_id,
            '' as assessment_title,
            o.administration_round,
            o.test_type as scope,
            o.test_date,
            o.subject_area,
            '' as overall_performance_band_for_group,
            'NA' as reporting_group_label,
            null as points_earned_for_group_subject,
            null as points_possible_for_group_subject,
            null as overall_number_correct_for_scope_round_per_subject,
            null as overall_number_possible_for_scope_round_per_subject,
            o.scale_score as scale_score_for_scope_round_per_subject,
            o.rn_highest,
            avg(case when subject_area = 'Composite' then o.scale_score end) over (
                partition by
                    o.student_number, o.test_type, o.administration_round, o.test_date
            ) as overall_composite_score
        from student_enrollments as e
        inner join
            act_sat_official as o
            on e.student_number = o.student_number
            and (o.test_date between e.entrydate and e.exitdate)
        left join ms_grad as m on e.student_number = m.student_number
    ),

    final_practice_tests as (
        select
            e.academic_year,
            e.region,
            e.schoolid,
            e.school_abbreviation,
            e.student_number,
            e.lastfirst,
            e.grade_level,
            e.enroll_status,
            e.advisor_lastfirst,
            e.cohort,
            case when e.spedlep in ('No IEP', null) then 0 else 1 end as sped,
            m.ms_attended,
            concat('Practice', ' ', p.scope) as test_type,
            p.assessment_id,
            p.assessment_title,
            p.administration_round,
            p.scope,
            p.test_date,
            p.subject_area,
            cast(
                p.overall_performance_band_for_group as string
            ) as overall_performance_band_for_group,
            p.reporting_group_label,
            p.points_earned_for_group_subject,
            p.points_possible_for_group_subject,
            p.overall_number_correct_for_scope_round_per_subject,
            p.overall_number_possible_for_scope_round_per_subject,
            p.scale_score_for_scope_round_per_subject,
            null as rn_highest,
            p.overall_composite_score
        from student_enrollments as e
        inner join
            practice_tests_with_scale_score_and_composite as p
            on e.student_number = p.student_number
            and e.academic_year = p.academic_year
        left join ms_grad as m on e.student_number = m.student_number
    )

select *
from final_official
union all
select *
from final_practice_tests