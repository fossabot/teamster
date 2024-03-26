with
    students as (
        select
            e._dbt_source_relation,
            e.academic_year,
            e.student_number,
            e.studentid,
            e.students_dcid,
            e.state_studentnumber,
            e.grade_level,
            e.enroll_status,

            adb.contact_id as kippadb_contact_id,

            discipline,
        from {{ ref("base_powerschool__student_enrollments") }} as e
        left join
            {{ ref("int_kippadb__roster") }} as adb
            on e.student_number = adb.student_number
        cross join unnest(['Math', 'ELA']) as discipline
        where
            e.academic_year = {{ var("current_academic_year") }}
            and e.grade_level = 12
            and e.rn_year = 1
    ),

    pathway_code_unpivot as (
        select
            _dbt_source_relation,
            studentsdcid,
            values_column as code,
            case
                regexp_extract(name_column, r'_([a-z]+)$')
                when 'ela'
                then 'ELA'
                when 'math'
                then 'Math'
            end as discipline,
        from
            {{ ref("stg_powerschool__s_nj_stu_x") }} unpivot (
                values_column for name_column
                in (graduation_pathway_ela, graduation_pathway_math)
            )
    ),

    transfer_scores as (
        select
            b._dbt_source_relation,
            b.name as test_name,

            s.studentid,
            s.grade_level as assessment_grade_level,

            t.numscore as testscalescore,
            t.alphascore as testperformancelevel,

            r.name as testcode,
            case
                r.name when 'ELAGP' then 'ELA' when 'MATGP' then 'Math'
            end as discipline,
            case
                r.name
                when 'ELAGP'
                then 'English Language Arts'
                when 'MATGP'
                then 'Mathematics'
            end as subject,
        from {{ ref("stg_powerschool__test") }} as b
        left join
            {{ ref("stg_powerschool__studenttest") }} as s
            on b.id = s.testid
            and {{ union_dataset_join_clause(left_alias="b", right_alias="s") }}
        left join
            {{ ref("stg_powerschool__studenttestscore") }} as t
            on s.studentid = t.studentid
            and s.id = t.studenttestid
            and {{ union_dataset_join_clause(left_alias="s", right_alias="t") }}
        left join
            {{ ref("stg_powerschool__testscore") }} as r
            on s.testid = r.testid
            and t.testscoreid = r.id
            and {{ union_dataset_join_clause(left_alias="s", right_alias="r") }}
        where b.name = 'NJGPA'
    ),

    psat10_unpivot as (
        select local_student_id, score_type, score,
        from
            {{ ref("stg_illuminate__psat") }} unpivot (
                score for score_type in (
                    eb_read_write_section_score,
                    math_test_score,
                    math_section_score,
                    reading_test_score
                )
            )
        where score_type not in ('total_score', 'writing_test_score')
    ),

    act_sat_psat10_official as (
        select
            contact,
            test_type,
            case
                when score_type in ('act_reading', 'sat_reading_test_score', 'sat_ebrw')
                then 'ELA'
                when score_type in ('act_math', 'sat_math_test_score', 'sat_math')
                then 'Math'
            end as discipline,
            case
                when score_type in ('act_reading', 'act_math') and score >= 17
                then true
                when score_type = 'sat_reading_test_score' and score >= 23
                then true
                when score_type = 'sat_math_test_score' and score >= 22
                then true
                when score_type = 'sat_math' and score >= 440
                then true
                when score_type = 'sat_ebrw' and score >= 450
                then true
                else false
            end as met_pathway_requirement,
        from {{ ref("int_kippadb__standardized_test_unpivot") }}
        where
            rn_highest = 1
            and score_type in (
                'act_reading',
                'act_math',
                'sat_math_test_score',
                'sat_math',
                'sat_reading_test_score',
                'sat_ebrw'
            )

        union all

        select
            local_student_id as contact,
            'PSAT10' as test_type,
            case
                when score_type in ('eb_read_write_section_score', 'reading_test_score')
                then 'ELA'
                else 'Math'
            end as discipline,
            case
                when
                    score_type in ('reading_test_score', 'math_test_score')
                    and score >= 21
                then true
                when
                    score_type in ('math_section_score', 'eb_read_write_section_score')
                    and score >= 420
                then true
                else false
            end as met_pathway_requirement,
        from psat10_unpivot
    ),

    act_sat_psat10_pivot as (
        select
            contact,
            discipline,
            if(act is null, false, act) as act,
            if(sat is null, false, sat) as sat,
            if(psat10 is null, false, psat10) as psat10,
        from
            act_sat_psat10_official pivot (
                max(met_pathway_requirement) for test_type in ('ACT', 'SAT', 'PSAT10')
            )
    ),

    njgpa as (
        select
            s.student_number,
            s.state_studentnumber,

            x.subject,
            x.testcode,
            x.testscalescore,
            x.discipline,
        from students as s
        left join
            transfer_scores as x
            on s.studentid = x.studentid
            and {{ union_dataset_join_clause(left_alias="s", right_alias="x") }}
        where x.studentid is not null

        union all

        select
            localstudentidentifier as student_number,
            safe_cast(statestudentidentifier as string) as state_studentnumber,
            subject,
            testcode,
            testscalescore,
            case
                when testcode = 'ELAGP' then 'ELA' when testcode = 'MATGP' then 'Math'
            end as discipline,
        from {{ ref("stg_pearson__njgpa") }}
        where testscorecomplete = 1 and testcode in ('ELAGP', 'MATGP')
    ),

    njgpa_rollup as (
        select
            student_number,
            state_studentnumber,
            testcode,
            subject,
            discipline,
            max(testscalescore) as testscalescore,
        from njgpa
        group by student_number, state_studentnumber, testcode, subject, discipline
    ),

    roster as (
        select
            s._dbt_source_relation,
            s.academic_year,
            s.student_number,
            s.students_dcid,
            s.state_studentnumber,
            s.kippadb_contact_id,
            s.grade_level,
            s.enroll_status,
            s.discipline,

            c.code,

            if(n.testscalescore is null, false, true) as njgpa_attempt,
            if(n.testscalescore >= 725, true, false) as njgpa_pass,
        from students as s
        left join
            pathway_code_unpivot as c
            on s.students_dcid = c.studentsdcid
            and s.discipline = c.discipline
            and {{ union_dataset_join_clause(left_alias="s", right_alias="c") }}
        left join
            njgpa_rollup as n
            on s.state_studentnumber = n.state_studentnumber
            and s.discipline = n.discipline
    )

select
    r._dbt_source_relation,
    r.academic_year,
    r.student_number,
    r.grade_level,
    r.enroll_status,
    r.discipline,
    r.code,
    r.njgpa_attempt,
    r.njgpa_pass,

    if(o1.act is null, false, o1.act) as act,
    if(o1.sat is null, false, o1.sat) as sat,
    if(o2.psat10 is null, false, o2.psat10) as psat10,

    case
        when r.code in ('M', 'N', 'O', 'P')
        then r.code
        when r.njgpa_pass
        then 'S'
        when r.njgpa_attempt and not r.njgpa_pass and o1.act
        then 'E'
        when r.njgpa_attempt and not r.njgpa_pass and o1.act in (false, null) and o1.sat
        then 'D'
        when
            r.njgpa_attempt
            and not r.njgpa_pass
            and o1.act in (false, null)
            and o1.sat in (false, null)
            and o2.psat10
        then 'J'
        else 'R'
    end as final_grad_path,
from roster as r
left join
    act_sat_psat10_pivot as o1
    on r.kippadb_contact_id = o1.contact
    and r.discipline = o1.discipline
left join
    act_sat_psat10_pivot as o2
    on cast(r.student_number as string) = o2.contact
    and r.discipline = o2.discipline
