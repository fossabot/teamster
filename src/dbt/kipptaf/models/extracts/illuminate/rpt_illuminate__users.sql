select
    ps_teachernumber as `01 User Id`,
    preferred_last_name as `02 User Last Name`,
    preferred_first_name as `03 User First Name`,
    null as `04 User Middle Name`,
    null as `05 Birth Date`,
    null as `06 Gender`,
    userprincipalname as `07 Email Address`,
    samaccountname as `08 Username`,
    null as `09 Password`,
    df_employee_number as `10 State User Or Employee Id`,
    null as `11 Name Suffix`,
    null as `12 Former First Name`,
    null as `13 Former Middle Name`,
    null as `14 Former Last Name`,
    null as `15 Primary Race`,
    null as `16 User Is Hispanic`,
    null as `17 Address`,
    legal_entity_name as `18 City`,
    null as `19 State`,
    null as `20 Zip`,
    primary_job as `21 Job Title`,
    null as `22 Education Level`,
    null as `23 Hire Date`,
    null as `24 Exit Date`,
    coalesce(is_active_ad, 0) as `25 Active`,
    null as `26 Position Status`,
    null as `27 Total Years Edu Service`,
    null as `28 Total Year In District`,
    null as `29 Email2`,
    null as `30 Phone1`,
    null as `31 Phone2`
from {{ ref("base_people__staff_roster") }}
