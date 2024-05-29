select
    employee_number,
    job_title,
    home_work_location_name,
    home_work_location_abbreviation,
    business_unit_home_name,
    case
        /* All Access*/
        when department_home_name in ('Data', 'Human Resources')
        then 6
        /* Regional */
        when
            job_title in (
                'Managing Director Operations',
                'Managing Director School Operations',
                'Head of Schools',
                'Head of Schools in Residence'
            )
        then 5
        /* Location */
        when
            job_title in (
                'School Leader',
                'School Leaders in Residence',
                'Director School Operations',
                'Director Campus Operatons'
            )
        then 4
        when job_title like '%Director%' and department_home_name = 'Operations'
        then 3
        when job_title like '%Assistant School Leader%'
        then 2
        else 1
    end as permissions_level,
from {{ ref("base_people__staff_roster") }}
where
    assignment_status in ('Active', 'Leave') and business_unit_home_name = 'KIPP Miami'
