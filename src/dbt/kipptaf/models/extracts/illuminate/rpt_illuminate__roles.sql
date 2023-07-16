/* KNJ specific departments = all CMO schools */
select
    df.powerschool_teacher_number as `01 Local User Id`,

    sch.school_number as `02 Site Id`,

    'School Leadership' as `03 Role Name`,
    concat(
        {{ var("current_academic_year") }}, '-', {{ var("current_fiscal_year") }}
    ) as `04 Academic Year`,
    1 as `05 Session Type Id`
from {{ ref("base_people__staff_roster") }} as df
inner join
    {{ ref("stg_powerschool__schools") }} as sch on sch.state_excludefromreporting = 0
where
    df.`Status` != 'TERMINATED'
    and df.department_home_name in ('Teaching and Learning', 'Data', 'Executive')
    and df.business_unit_home_name = 'KIPP TEAM and Family Schools Inc.'

union all

/* Campus-based staff = all schools at campus */
select
    df.powerschool_teacher_number as `01 Local User Id`,

    cc.powerschool_school_id as `02 Site Id`,

    'School Leadership' as `03 Role Name`,
    concat(
        {{ var("current_academic_year") }}, '-', {{ var("current_fiscal_year") }}
    ) as `04 Academic Year`,
    1 as `05 Session Type Id`
from {{ ref("base_people__staff_roster") }} as df
inner join
    {{ source("people", "src_people__campus_crosswalk") }} as cc
    on df.primary_site = cc.campus_name
    and cc.is_pathways = 0
    and cc._fivetran_deleted = 0
where
    df.`Status` != 'TERMINATED'
    and df.primary_on_site_department
    not in ('Teaching and Learning', 'Data', 'Executive')
    and df.is_campus_staff = 1

union all

/* School-based staff = only respective school */
select
    powerschool_teacher_number as `01 Local User Id`,
    primary_site_schoolid as `02 Site Id`,

    'School Leadership' as `03 Role Name`,
    concat(
        {{ var("current_academic_year") }}, '-', {{ var("current_fiscal_year") }}
    ) as `04 Academic Year`,
    1 as `05 Session Type Id`
from {{ ref("base_people__staff_roster") }}
where
    `Status` != 'TERMINATED'
    and department_home_name not in ('Teaching and Learning', 'Data', 'Executive')
    and is_campus_staff
