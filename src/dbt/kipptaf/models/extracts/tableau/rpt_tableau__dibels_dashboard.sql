{% set periods = ["BOY", "BOY->MOY", "MOY", "MOY->EOY", "EOY"] %}  -- Force expected assessments

with
    iready_roster as (
        select
            academic_year,
            region,
            school_abbreviation,
            student_id as student_number,
            student_grade,
            subject
        from {{ ref("base_iready__diagnostic_results") }}
        where
            test_round = 'BOY'
            and student_grade in ('3', '4')
            and rn_subj_round = 1
            and overall_relative_placement_int <= 2
            and left(academic_year, 4)
            = cast({{ var("current_academic_year") }} as string)
            and subject = 'Reading'
    ),

    student_k_2 as (
        select
            _dbt_source_relation,
            cast(academic_year as string) as academic_year,
            'KIPP NJ/MIAMI' as district,
            region,
            case
                when region in ('Camden', 'Newark')
                then 'NJ'
                when region = 'Miami'
                then 'FL'
            end as city,
            schoolid,
            school_abbreviation as school,
            studentid,
            student_number,
            lastfirst as student_name,
            first_name as student_first_name,
            last_name as student_last_name,
            case
                when cast(grade_level as string) = '0'
                then 'K'
                else cast(grade_level as string)
            end as grade_level,
            is_out_of_district as ood,
            gender,
            ethnicity,
            is_homeless,
            is_504,
            case when spedlep in ('No IEP', null) then 0 else 1 end as sped,
            lep_status,
            lunch_status
        from {{ ref("base_powerschool__student_enrollments") }}
        where
            academic_year = {{ var("current_academic_year") }}
            and enroll_status = 0
            and rn_year = 1
            and grade_level <= 2
            and not is_self_contained
    ),

    student_3_4 as (
        select
            e._dbt_source_relation,
            cast(e.academic_year as string) as academic_year,
            'KIPP NJ/MIAMI' as district,
            e.region as region,
            case
                when e.region in ('Camden', 'Newark')
                then 'NJ'
                when e.region = 'Miami'
                then 'FL'
            end as city,
            e.schoolid,
            e.school_abbreviation as school,
            e.studentid,
            e.student_number,
            e.lastfirst as student_name,
            e.first_name as student_first_name,
            e.last_name as student_last_name,
            cast(e.grade_level as string) as grade_level,
            is_out_of_district as ood,
            e.gender,
            e.ethnicity,
            e.is_homeless,
            e.is_504,
            case when e.spedlep in ('No IEP', null) then 0 else 1 end as sped,
            e.lep_status,
            e.lunch_status
        from {{ ref("base_powerschool__student_enrollments") }} as e
        left join iready_roster as i on e.student_number = i.student_number
        where
            e.academic_year = {{ var("current_academic_year") }}
            and e.enroll_status = 0
            and e.rn_year = 1
            and not is_self_contained
            and e.student_number
            in (select distinct i.student_number from iready_roster)
    ),

    students as (
        select
            _dbt_source_relation,
            academic_year,
            district,
            region,
            city,
            schoolid,
            school,
            studentid,
            student_number,
            student_name,
            student_first_name,
            student_last_name,
            grade_level,
            ood,
            gender,
            ethnicity,
            is_homeless,
            is_504,
            sped,
            lep_status,
            lunch_status
        from student_k_2
        union all
        select
            _dbt_source_relation,
            academic_year,
            district,
            region,
            city,
            schoolid,
            school,
            studentid,
            student_number,
            student_name,
            student_first_name,
            student_last_name,
            grade_level,
            ood,
            gender,
            ethnicity,
            is_homeless,
            is_504,
            sped,
            lep_status,
            lunch_status
        from student_3_4
    ),

    student_number as (
        select
            _dbt_source_relation,
            cast(academic_year as string) as academic_year,
            region,
            schoolid,
            school_abbreviation as school,
            studentid,
            student_number,
            enroll_status,
            advisory_name
        from {{ ref("base_powerschool__student_enrollments") }}
        where
            academic_year = {{ var("current_academic_year") }}
            and enroll_status = 0
            and rn_year = 1
            and grade_level <= 4
    ),

    schedules as (
        select distinct
            c._dbt_source_relation,
            cast(c.cc_academic_year as string) as schedule_academic_year,
            'KIPP NJ/MIAMI' as schedule_district,
            e.region as schedule_region,
            case
                when e.region in ('Camden', 'Newark')
                then 'NJ'
                when e.region = 'Miami'
                then 'FL'
            end as schedule_city,
            c.cc_schoolid as schedule_schoolid,
            c.cc_studentid as schedule_studentid,
            e.student_number as schedule_student_number,
            case
                when c.courses_course_name in ('ELA GrK', 'ELA K')
                then 'K'
                when c.courses_course_name = 'ELA Gr1'
                then '1'
                when c.courses_course_name = 'ELA Gr2'
                then '2'
                when c.courses_course_name = 'ELA Gr3'
                then '3'
                when c.courses_course_name = 'ELA Gr4'
                then '4'
            end as schedule_student_grade_level,
            c.cc_teacherid as teacherid,
            c.teacher_lastfirst as teacher_name,
            c.courses_course_name as course_name,
            c.cc_course_number as course_number,
            c.cc_section_number as section_number,
            e.advisory_name,
            period as expected_test,
            1 as scheduled
        from {{ ref("base_powerschool__course_enrollments") }} as c
        left join
            student_number as e
            on cast(c.cc_academic_year as string) = e.academic_year
            and c.cc_studentid = e.studentid
            and {{ union_dataset_join_clause(left_alias="c", right_alias="e") }}
        cross join unnest({{ periods }}) as period
        where
            c.cc_academic_year = {{ var("current_academic_year") }}
            and not c.is_dropped_course
            and not c.is_dropped_section
            and c.rn_course_number_year = 1
            and c.courses_course_name
            in ('ELA GrK', 'ELA K', 'ELA Gr1', 'ELA Gr2', 'ELA Gr3', 'ELA Gr4')
            and e.enroll_status = 0
    ),

    assessments_scores as (
        select
            left(bss.school_year, 4) as mclass_academic_year,  -- needed to extract the academic year format that matches NJ's syntax
            bss.student_primary_id as mclass_student_number,
            'benchmark' as assessment_type,
            bss.assessment_grade as mclass_assessment_grade,
            bss.benchmark_period as mclass_period,
            bss.client_date as mclass_client_date,
            bss.sync_date as mclass_sync_date,
            u.measure as mclass_measure,
            u.score as mclass_measure_score,
            u.level as mclass_measure_level,
            case
                when u.level = 'Above Benchmark'
                then 4
                when u.level = 'At Benchmark'
                then 3
                when u.level = 'Below Benchmark'
                then 2
                when u.level = 'Well Below Benchmark'
                then 1
                else null
            end as mclass_measure_level_int,
            u.national_norm_percentile as mclass_measure_percentile,
            u.semester_growth as mclass_measure_semester_growth,
            u.year_growth as mclass_measure_year_growth,
            null as mclass_probe_number,
            null as mclass_total_number_of_probes,
            null as mclass_score_change

        from {{ ref("stg_amplify__benchmark_student_summary") }} as bss
        inner join
            {{ ref("int_amplify__benchmark_student_summary_unpivot") }} as u
            on bss.surrogate_key = u.surrogate_key
        where left(bss.school_year, 4) = '2023'  -- Cannot use {{ var("current_academic_year") }} - errors out

        union all

        select
            left(school_year, 4) as mclass_academic_year,  -- needed to extract the academic year format that matches NJ's syntax
            student_primary_id as mclass_student_number,
            'pm' as assessment_type,
            cast(assessment_grade as string) as mclass_assessment_grade,
            pm_period as mclass_period,
            client_date as mclass_client_date,
            sync_date as mclass_sync_date,
            measure as mclass_measure,
            score as mclass_measure_score,
            null as mclass_measure_level,
            null mclass_measure_level_int,
            null as mclass_measure_percentile,
            null as mclass_measure_semester_growth,
            null as mclass_measure_year_growth,
            probe_number as mclass_probe_number,
            total_number_of_probes as mclass_total_number_of_probes,
            score_change as mclass_score_change
        from {{ ref("stg_amplify__pm_student_summary") }}
        where left(school_year, 4) = '2023'  -- Cannot use {{ var("current_academic_year") }} - errors out
    ),

    students_and_schedules as (
        select
            s.academic_year,
            s.district,
            s.region,
            s.city,
            s.schoolid,
            s.school,
            s.studentid,
            s.student_number,
            s.student_name,
            s.student_first_name,
            s.student_last_name,
            s.grade_level,
            s.ood,
            s.gender,
            s.ethnicity,
            s.is_homeless,
            s.is_504,
            s.sped,
            s.lep_status,
            s.lunch_status,
            m.schedule_academic_year,
            m.schedule_district,
            s.region as schedule_region,
            m.schedule_city,
            m.schedule_schoolid,
            m.schedule_studentid,
            m.schedule_student_number,
            m.schedule_student_grade_level,
            m.teacherid,
            m.teacher_name,
            m.course_name,
            m.course_number,
            m.section_number,
            m.advisory_name,
            m.expected_test,
            m.scheduled
        from students as s
        left join
            schedules as m
            on s.academic_year = m.schedule_academic_year
            and s.schoolid = m.schedule_schoolid
            and s.student_number = m.schedule_student_number
        where m.section_number not like '%SC%'
    ),

    students_schedules_and_assessments_scores as (
        select
            s.academic_year,
            s.district,
            s.region,
            s.city,
            s.schoolid,
            s.school,
            s.studentid,
            s.student_number,
            s.student_name,
            s.student_first_name,
            s.student_last_name,
            s.grade_level,
            s.ood,
            s.gender,
            s.ethnicity,
            s.is_homeless,
            s.is_504,
            s.sped,
            s.lep_status,
            s.lunch_status,
            s.schedule_academic_year,
            s.schedule_district,
            s.region as schedule_region,
            s.schedule_city,
            s.schedule_schoolid,
            s.schedule_studentid,
            s.schedule_student_number,
            s.schedule_student_grade_level,
            s.teacherid,
            s.teacher_name,
            s.course_name,
            s.course_number,
            s.section_number,
            s.advisory_name,
            s.expected_test,
            s.scheduled,
            a.mclass_academic_year,
            a.mclass_student_number,
            a.assessment_type,
            a.mclass_assessment_grade,
            a.mclass_period,
            a.mclass_client_date,
            a.mclass_sync_date,
            a.mclass_measure,
            a.mclass_measure_score,
            a.mclass_measure_level,
            a.mclass_measure_level_int,
            a.mclass_measure_percentile,
            a.mclass_measure_semester_growth,
            a.mclass_measure_year_growth,
            a.mclass_probe_number,
            a.mclass_total_number_of_probes,
            a.mclass_score_change
        from students_and_schedules as s
        left join
            assessments_scores as a
            on s.schedule_academic_year = a.mclass_academic_year
            and s.schedule_student_number = a.mclass_student_number
            and s.expected_test = a.mclass_period
    ),

    composite_only  -- Extract final composite by student per window
    as (
        select distinct
            academic_year, student_number, expected_test, mclass_measure_level
        from students_schedules_and_assessments_scores
        where mclass_measure = 'Composite'
    ),

    overall_composite_by_window  -- Pivot final composite by student per window
    as (
        select distinct academic_year, student_number, p.boy, p.moy, p.eoy
        from
            composite_only pivot (
                max(mclass_measure_level) for expected_test in ('BOY', 'MOY', 'EOY')
            ) as p
    ),

    probe_eligible_tag as (
        select distinct
            s.academic_year,
            s.student_number,
            c.boy,
            c.moy,
            c.eoy,
            case
                when boy in ('Below Benchmark', 'Well Below Benchmark')
                then 'Yes'
                when boy is null
                then 'No data'
                else 'No'
            end as boy_probe_eligible,
            case
                when moy in ('Below Benchmark', 'Well Below Benchmark')
                then 'Yes'
                when moy is null
                then 'No data'
                else 'No'
            end as moy_probe_eligible
        from students_schedules_and_assessments_scores as s
        left join
            overall_composite_by_window as c
            on s.academic_year = c.academic_year
            and s.student_number = c.student_number
    ),

    base_roster as (
        select
            s.academic_year,
            s.district,
            s.region,
            s.schoolid,
            s.school,
            s.student_number,
            s.student_name,
            s.student_last_name,
            s.student_first_name,
            s.grade_level,
            s.schedule_academic_year,
            s.schedule_district,
            s.schedule_region,
            s.schedule_schoolid,
            s.schedule_student_number,
            s.schedule_student_grade_level,
            s.ood,
            s.gender,
            s.ethnicity,
            s.is_homeless,
            s.is_504,
            s.sped,
            s.lep_status,
            s.lunch_status,
            s.teacherid,
            s.teacher_name,
            s.course_name,
            s.course_number,
            s.section_number,
            s.advisory_name,
            s.expected_test,
            coalesce(s.scheduled, 0) as scheduled,
            s.mclass_student_number,
            s.mclass_assessment_grade,
            s.mclass_period,
            s.mclass_client_date,
            s.mclass_sync_date,
            coalesce(p.boy, 'No data') as boy_composite,
            coalesce(p.moy, 'No data') as moy_composite,
            coalesce(p.eoy, 'No data') as eoy_composite,
            coalesce(s.mclass_probe_number, 0) as mclass_probe_number,
            coalesce(
                s.mclass_total_number_of_probes, 0
            ) as mclass_total_number_of_probes,
            p.boy_probe_eligible,
            p.moy_probe_eligible,
            case
                when p.boy_probe_eligible = 'Yes' and s.expected_test = 'BOY->MOY'
                then p.boy_probe_eligible
                when p.moy_probe_eligible = 'Yes' and s.expected_test = 'MOY->EOY'
                then p.moy_probe_eligible
                when p.boy_probe_eligible = 'No' and s.expected_test = 'BOY->MOY'
                then 'No'
                when p.moy_probe_eligible = 'No' and s.expected_test = 'MOY->EOY'
                then 'No'
                else 'Not applicable'
            end as pm_probe_eligible,
            case
                when
                    p.boy_probe_eligible = 'Yes'
                    and s.expected_test = 'BOY->MOY'
                    and s.mclass_total_number_of_probes is not null
                then 'Yes'
                when
                    p.moy_probe_eligible = 'Yes'
                    and s.expected_test = 'MOY->EOY'
                    and s.mclass_total_number_of_probes is not null
                then 'Yes'
                when
                    p.boy_probe_eligible = 'Yes'
                    and s.expected_test = 'BOY->MOY'
                    and s.mclass_total_number_of_probes is null
                then 'No'
                when
                    p.moy_probe_eligible = 'Yes'
                    and s.expected_test = 'MOY->EOY'
                    and s.mclass_total_number_of_probes is null
                then 'No'
                else 'Not applicable'
            end as pm_probe_tested,
            s.mclass_measure,
            s.mclass_measure_score,
            s.mclass_score_change,
            s.mclass_measure_level,
            s.mclass_measure_level_int,
            s.mclass_measure_percentile,
            s.mclass_measure_semester_growth,
            s.mclass_measure_year_growth,

        from students_schedules_and_assessments_scores as s
        left join
            probe_eligible_tag as p
            on s.academic_year = p.academic_year
            and s.student_number = p.student_number
    ),

    terms as (
        select
            name,
            start_date,
            end_date,
            academic_year as academic_year_term,
            region as region_term
        from {{ ref("stg_reporting__terms") }}
        where type = 'LIT' and academic_year = {{ var("current_academic_year") }}
    )

select
    b.academic_year,
    b.district,
    b.region,
    b.schoolid,
    b.school,
    b.student_number,
    b.student_name,
    b.student_last_name,
    b.student_first_name,
    b.grade_level,
    b.schedule_academic_year,
    b.schedule_district,
    b.schedule_region,
    b.schedule_schoolid,
    b.schedule_student_number,
    b.schedule_student_grade_level,
    b.ood,
    b.gender,
    b.ethnicity,
    b.is_homeless,
    b.is_504,
    b.sped,
    b.lep_status,
    b.lunch_status,
    b.teacherid,
    b.teacher_name,
    b.course_name,
    b.course_number,
    b.section_number,
    b.advisory_name,
    b.expected_test,
    b.scheduled,
    b.mclass_student_number,
    b.mclass_assessment_grade,
    b.mclass_period,
    b.mclass_client_date,
    b.mclass_sync_date,
    b.boy_composite,
    b.moy_composite,
    b.eoy_composite,
    b.mclass_probe_number,
    b.mclass_total_number_of_probes,
    b.boy_probe_eligible,
    b.moy_probe_eligible,
    b.pm_probe_eligible,
    b.pm_probe_tested,
    b.mclass_measure,
    b.mclass_measure_score,
    b.mclass_score_change,
    b.mclass_measure_level,
    b.mclass_measure_level_int,
    b.mclass_measure_percentile,
    b.mclass_measure_semester_growth,
    b.mclass_measure_year_growth,
    t.name,
    t.start_date,
    t.end_date,
from base_roster as b
left join
    terms as t
    on cast(b.academic_year as int) = t.academic_year_term
    and b.expected_test = t.name
    and b.region = t.region_term
