{% set quarter = ["Q1", "Q2", "Q3", "Q4"] %}

with
    student_roster as (
        select
            enr._dbt_source_relation,
            enr.academic_year,
            enr.yearid,
            enr.region,
            enr.school_level,
            enr.schoolid,
            enr.school_abbreviation as school,
            enr.studentid,
            enr.student_number,
            enr.lastfirst,
            enr.gender,
            enr.enroll_status,
            enr.grade_level,
            enr.ethnicity,
            enr.cohort,
            enr.year_in_school,
            enr.advisor_lastfirst as advisor_name,
            enr.is_out_of_district,
            enr.lep_status,
            enr.is_504,
            enr.is_self_contained as is_pathways,
            enr.lunch_status,
            enr.year_in_network,
            enr.is_retained_year,
            enr.is_retained_ever,
            enr.rn_undergrad,

            ktc.id as salesforce_id,

            hos.head_of_school_preferred_name_lastfirst as hos,
            case
                when enr.school_level in ('ES', 'MS')
                then advisory_name
                when enr.school_level = 'HS'
                then advisor_lastfirst
            end as advisory,
            case
                when enr.spedlep like 'SPED%' then 'Has IEP' else 'No IEP'
            end as iep_status,
            case when sp.studentid is not null then 1 end as is_counselingservices,
            case when sa.studentid is not null then 1 end as is_studentathlete,

            quarter,
            round(ada.ada, 3) as ada,
        from {{ ref("base_powerschool__student_enrollments") }} as enr
        left join
            {{ ref("stg_kippadb__contact") }} as ktc
            on enr.student_number = ktc.school_specific_id
        left join
            {{ ref("int_powerschool__spenrollments") }} as sp
            on enr.studentid = sp.studentid
            and current_date('America/New_York') between sp.enter_date and sp.exit_date
            and sp.specprog_name = 'Counseling Services'
            and {{ union_dataset_join_clause(left_alias="enr", right_alias="sp") }}
        left join
            {{ ref("int_powerschool__spenrollments") }} as sa
            on enr.studentid = sa.studentid
            and current_date('America/New_York') between sa.enter_date and sa.exit_date
            and sa.specprog_name = 'Student Athlete'
            and {{ union_dataset_join_clause(left_alias="enr", right_alias="sa") }}
        left join
            {{ ref("int_powerschool__ada") }} as ada
            on enr.yearid = ada.yearid
            and enr.studentid = ada.studentid
            and {{ union_dataset_join_clause(left_alias="enr", right_alias="ada") }}
        left join
            {{ ref("int_people__leadership_crosswalk") }} as hos
            on enr.schoolid = hos.home_work_location_powerschool_school_id
        cross join unnest({{ quarter }}) as quarter
        where
            enr.rn_year = 1
            and enr.grade_level != 99
            and enr.academic_year >= {{ var("current_academic_year") }} - 4
    ),

    transfer_roster as (
        select distinct
            tr._dbt_source_relation,
            tr.academic_year,
            tr.yearid,
            tr.studentid,

            coalesce(co.region, e1.region) as region,
            coalesce(co.school_level, e1.school_level) as school_level,
            coalesce(co.schoolid, e1.schoolid) as schoolid,
            coalesce(co.school, e1.school) as school,
            coalesce(co.student_number, e1.student_number) as student_number,
            coalesce(co.lastfirst, e1.lastfirst) as lastfirst,
            coalesce(co.gender, e1.gender) as gender,
            coalesce(co.enroll_status, e1.enroll_status) as enroll_status,
            coalesce(co.grade_level, e1.grade_level) as grade_level,
            coalesce(co.ethnicity, e1.ethnicity) as ethnicity,
            coalesce(co.cohort, e1.cohort) as cohort,
            coalesce(co.year_in_school, e1.year_in_school) as year_in_school,
            coalesce(co.advisor_name, e1.advisor_name) as advisor_name,
            coalesce(
                co.is_out_of_district, e1.is_out_of_district
            ) as is_out_of_district,
            coalesce(co.lep_status, e1.lep_status) as lep_status,
            coalesce(co.is_504, e1.is_504) as is_504,
            coalesce(co.is_pathways, e1.is_pathways) as is_pathways,
            coalesce(co.lunch_status, e1.lunch_status) as lunch_status,
            coalesce(co.year_in_network, e1.year_in_network) as year_in_network,
            coalesce(co.is_retained_year, e1.is_retained_year) as is_retained_year,
            coalesce(co.is_retained_ever, e1.is_retained_ever) as is_retained_ever,
            coalesce(co.rn_undergrad, e1.rn_undergrad) as rn_undergrad,
            coalesce(co.salesforce_id, e1.salesforce_id) as salesforce_id,
            coalesce(co.hos, e1.hos) as hos,
            coalesce(co.advisory, e1.advisory) as advisory,
            coalesce(co.iep_status, e1.iep_status) as iep_status,
            coalesce(co.is_counselingservices, 0) as is_counselingservices,
            coalesce(co.is_studentathlete, 0) as is_studentathlete,
            coalesce(co.ada, e1.ada) as ada,

            quarter,
        from {{ ref("stg_powerschool__storedgrades") }} as tr
        left join
            student_roster as co
            on tr.studentid = co.studentid
            and tr.schoolid = co.schoolid
            and {{ union_dataset_join_clause(left_alias="tr", right_alias="co") }}
        left join
            student_roster as e1
            on tr.studentid = e1.studentid
            and tr.schoolid = e1.schoolid
            and {{ union_dataset_join_clause(left_alias="tr", right_alias="e1") }}
            and e1.year_in_school = 1
        cross join unnest({{ quarter }}) as quarter
        where tr.storecode = 'Y1' and tr.schoolname not like '%KIPP%'
    ),

    students as (
        select
            _dbt_source_relation,
            academic_year,
            yearid,
            region,
            school_level,
            schoolid,
            school,
            studentid,
            student_number,
            lastfirst,
            gender,
            enroll_status,
            grade_level,
            ethnicity,
            cohort,
            year_in_school,
            advisor_name,
            is_out_of_district,
            lep_status,
            is_504,
            is_pathways,
            lunch_status,
            year_in_network,
            is_retained_year,
            is_retained_ever,
            rn_undergrad,
            salesforce_id,
            hos,
            advisory,
            iep_status,
            is_counselingservices,
            is_studentathlete,
            ada,
            quarter,

            if(quarter in ('Q1', 'Q2'), 'S1', 'S2') as semester,
        from student_roster

        union all

        select
            _dbt_source_relation,
            academic_year,
            yearid,
            region,
            school_level,
            schoolid,
            school,
            studentid,
            student_number,
            lastfirst,
            gender,
            enroll_status,
            grade_level,
            ethnicity,
            cohort,
            year_in_school,
            advisor_name,
            is_out_of_district,
            lep_status,
            is_504,
            is_pathways,
            lunch_status,
            year_in_network,
            is_retained_year,
            is_retained_ever,
            rn_undergrad,
            salesforce_id,
            hos,
            advisory,
            iep_status,
            is_counselingservices,
            is_studentathlete,
            ada,
            quarter,

            if(quarter in ('Q1', 'Q2'), 'S1', 'S2') as semester,
        from transfer_roster
    ),

    section_teacher as (
        select
            m._dbt_source_relation,
            m.cc_yearid as yearid,
            m.cc_academic_year,
            m.cc_studentid as studentid,
            m.cc_course_number as course_number,
            m.cc_sectionid as sectionid,
            m.cc_section_number,
            m.sections_section_number as section_number,
            m.sections_external_expression as external_expression,
            m.sections_termid as termid,
            m.courses_credittype as credit_type,
            m.courses_course_name as course_name,
            m.teacher_lastfirst as teacher_name,

            f.tutoring_nj,
            f.nj_student_tier,
        from {{ ref("base_powerschool__course_enrollments") }} as m
        left join
            {{ ref("int_reporting__student_filters") }} as f
            on m.cc_studentid = f.studentid
            and m.cc_academic_year = f.academic_year
            and m.courses_credittype = f.powerschool_credittype
            and {{ union_dataset_join_clause(left_alias="m", right_alias="f") }}
        where
            not m.is_dropped_course
            and not m.is_dropped_section
            and m.rn_course_number_year = 1
            and m.cc_academic_year >= {{ var("current_academic_year") }} - 4
    ),

    transfer_teacher as (
        select
            t._dbt_source_relation,
            t.yearid,
            t.academic_year,
            t.studentid,

            g.course_name,
            g.sectionid,

            'TRANSFER' as section_number,
            'TRANSFER' as external_expression,
            g.termid,
            'TRANSFER' as credit_type,
            'TRANSFER' as teacher_name,

            false as tutoring_nj,
            'NA' as nj_student_tier,

            concat(
                'T',
                upper(regexp_extract(t._dbt_source_relation, r'(kipp\w+)_')),
                g.dcid
            ) as course_number,
        from transfer_roster as t
        left join
            {{ ref("stg_powerschool__storedgrades") }} as g
            on t.yearid = g.yearid
            and t.studentid = g.studentid
            and t.schoolid = g.schoolid
            and t.academic_year = g.academic_year
            and {{ union_dataset_join_clause(left_alias="t", right_alias="g") }}
    ),

    sections as (
        select
            _dbt_source_relation,
            yearid,
            cc_academic_year,
            studentid,
            course_number,
            sectionid,
            cc_section_number,
            section_number,
            external_expression,
            termid,
            credit_type,
            course_name,
            teacher_name,
            tutoring_nj,
            nj_student_tier,
        from section_teacher

        union all

        select
            _dbt_source_relation,
            yearid,
            academic_year,
            studentid,
            course_number,
            sectionid,
            null as cc_section_number,
            section_number,
            external_expression,
            termid,
            credit_type,
            course_name,
            teacher_name,
            tutoring_nj,
            nj_student_tier,
        from transfer_teacher

    ),

    schedules as (
        select
            r._dbt_source_relation,
            r.academic_year,
            r.yearid,
            r.region,
            r.school_level,
            r.schoolid,
            r.school,
            r.studentid,
            r.student_number,
            r.salesforce_id,
            r.lastfirst,
            r.gender,
            r.enroll_status,
            r.grade_level,
            r.ethnicity,
            r.cohort,
            r.year_in_school,
            r.is_out_of_district,
            r.lep_status,
            r.is_504,
            r.is_pathways,
            r.iep_status,
            r.lunch_status,
            r.year_in_network,
            r.is_retained_year,
            r.is_retained_ever,
            r.rn_undergrad,
            r.advisory,
            r.advisor_name,
            r.ada,
            r.hos,
            r.quarter,
            r.semester,

            m.course_number,
            m.sectionid,
            m.section_number,
            m.cc_section_number,
            m.external_expression,
            m.termid,
            m.credit_type,
            m.course_name,
            m.teacher_name,
            m.tutoring_nj,
            m.nj_student_tier,
        from students as r
        left join
            sections as m
            on r.academic_year = m.cc_academic_year
            and r.studentid = m.studentid
            and {{ union_dataset_join_clause(left_alias="r", right_alias="m") }}
    )

select *
from schedules
