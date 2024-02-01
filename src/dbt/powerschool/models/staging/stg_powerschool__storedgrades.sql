with
    -- trunk-ignore(sqlfluff/ST03)
    dcid_filter as (
        select *, _file_name,
        from {{ source("powerschool", "src_powerschool__storedgrades") }}
        where
            dcid.int_value in (
                select dcid.int_value,
                from {{ source("powerschool", "src_powerschool__storedgrades_dcid") }}
            )
    ),

    deduplicate as (
        {{
            dbt_utils.deduplicate(
                relation="dcid_filter",
                partition_by="dcid.int_value",
                order_by="_file_name desc",
            )
        }}
    ),

    staging as (
        select
            /* column transformations */
            dcid.int_value as dcid,
            studentid.int_value as studentid,
            sectionid.int_value as sectionid,
            termid.int_value as termid,
            percent.double_value as `percent`,
            absences.double_value as absences,
            tardies.double_value as tardies,
            potentialcrhrs.double_value as potentialcrhrs,
            earnedcrhrs.double_value as earnedcrhrs,
            grade_level.int_value as grade_level,
            schoolid.int_value as schoolid,
            excludefromgpa.int_value as excludefromgpa,
            gpa_points.double_value as gpa_points,
            gpa_addedvalue.double_value as gpa_addedvalue,
            gpa_custom2.double_value as gpa_custom2,
            excludefromclassrank.int_value as excludefromclassrank,
            excludefromhonorroll.int_value as excludefromhonorroll,
            isearnedcrhrsfromgb.int_value as isearnedcrhrsfromgb,
            ispotentialcrhrsfromgb.int_value as ispotentialcrhrsfromgb,
            excludefromtranscripts.int_value as excludefromtranscripts,
            replaced_dcid.int_value as replaced_dcid,
            excludefromgraduation.int_value as excludefromgraduation,
            excludefromgradesuppression.int_value as excludefromgradesuppression,
            gradereplacementpolicy_id.int_value as gradereplacementpolicy_id,
            whomodifiedid.int_value as whomodifiedid,

            /* remaining columns */
            storecode as storecode,
            datestored as datestored,
            grade as grade,
            behavior as behavior,
            comment_value as comment_value,
            course_name as course_name,
            course_number as course_number,
            credit_type as credit_type,
            `log` as `log`,
            course_equiv as course_equiv,
            schoolname as schoolname,
            gradescale_name as gradescale_name,
            teacher_name as teacher_name,
            gpa_custom1 as gpa_custom1,
            custom as custom,
            ab_course_cmp_fun_flg as ab_course_cmp_fun_flg,
            ab_course_cmp_ext_crd as ab_course_cmp_ext_crd,
            ab_course_cmp_fun_sch as ab_course_cmp_fun_sch,
            ab_course_cmp_met_cd as ab_course_cmp_met_cd,
            ab_course_eva_pro_cd as ab_course_eva_pro_cd,
            ab_course_cmp_sta_cd as ab_course_cmp_sta_cd,
            ab_pri_del_met_cd as ab_pri_del_met_cd,
            ab_lng_cd as ab_lng_cd,
            ab_dipl_exam_mark as ab_dipl_exam_mark,
            ab_final_mark as ab_final_mark,
            termbinsname as termbinsname,
            psguid as psguid,
            replaced_grade as replaced_grade,
            replaced_equivalent_course as replaced_equivalent_course,
            ip_address as ip_address,
            whomodifiedtype as whomodifiedtype,
            transaction_date as transaction_date,
            executionid as executionid,

            percent.double_value / 100.000 as percent_decimal,
            left(storecode, 2) as storecode_type,
            safe_cast(left(safe_cast(termid.int_value as string), 2) as int) as yearid,
        from deduplicate
    ),

    with_years as (
        select *, yearid + 1990 as academic_year, yearid + 1991 as fiscal_year,
        from staging
    )

select
    *,
    case
        /* unweighted pre-2016 */
        when academic_year < 2016 and gradescale_name = 'NCA Honors'
        then 'NCA 2011'
        /* unweighted 2016-2018 */
        when academic_year >= 2016 and gradescale_name = 'NCA Honors'
        then 'KIPP NJ 2016 (5-12)'
        /* unweighted 2019+ */
        when academic_year >= 0 and gradescale_name = 'KIPP NJ 2019 (5-12) Weighted'
        then 'KIPP NJ 2019 (5-12) Unweighted'
        /* MISSING GRADESCALE - default pre-2016 */
        when
            academic_year < 2016
            and (coalesce(gradescale_name, '') = '' or gradescale_name = 'NULL')
        then 'NCA 2011'
        /* MISSING GRADESCALE - default 2016+ */
        when
            academic_year >= 2016
            and (coalesce(gradescale_name, '') = '' or gradescale_name = 'NULL')
        then 'KIPP NJ 2016 (5-12)'
        /* return original grade scale */
        else gradescale_name
    end as gradescale_name_unweighted,
from with_years
