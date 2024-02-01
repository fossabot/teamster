NJSMART_POWERSCHOOL_FIELDS = [
    {"name": "dob", "type": ["null", "string"], "default": None},
    {"name": "first_name", "type": ["null", "string"], "default": None},
    {"name": "last_name", "type": ["null", "string"], "default": None},
    {"name": "nj_se_delayreason", "type": ["null", "double"], "default": None},
    {"name": "nj_se_earlyintervention", "type": ["null", "string"], "default": None},
    {"name": "nj_se_eligibilityddate", "type": ["null", "string"], "default": None},
    {"name": "nj_se_lastiepmeetingdate", "type": ["null", "string"], "default": None},
    {"name": "nj_se_parentalconsentdate", "type": ["null", "string"], "default": None},
    {"name": "nj_se_placement", "type": ["null", "double"], "default": None},
    {"name": "nj_se_reevaluationdate", "type": ["null", "string"], "default": None},
    {"name": "nj_se_referraldate", "type": ["null", "string"], "default": None},
    {"name": "nj_timeinregularprogram", "type": ["null", "string"], "default": None},
    {"name": "special_education", "type": ["null", "double"], "default": None},
    {
        "name": "state_studentnumber",
        "type": ["null", "long", "double"],
        "default": None,
    },
    {"name": "student_number", "type": ["null", "long"], "default": None},
    {"name": "ti_serv_counseling", "type": ["null", "string"], "default": None},
    {"name": "ti_serv_occup", "type": ["null", "string"], "default": None},
    {"name": "ti_serv_other", "type": ["null", "string"], "default": None},
    {"name": "ti_serv_physical", "type": ["null", "string"], "default": None},
    {"name": "ti_serv_speech", "type": ["null", "string"], "default": None},
    {
        "name": "nj_se_initialiepmeetingdate",
        "type": ["null", "string"],
        "default": None,
    },
    {
        "name": "nj_se_parentalconsentobtained",
        "type": ["null", "string"],
        "default": None,
    },
    {
        "name": "nj_se_consenttoimplementdate",
        "type": ["null", "string"],
        "default": None,
    },
    {"name": "declassificationspeddate", "type": ["null", "string"], "default": None},
    {"name": "mddisabling_condition1", "type": ["null", "string"], "default": None},
    {"name": "mddisabling_condition2", "type": ["null", "string"], "default": None},
    {"name": "mddisabling_condition3", "type": ["null", "string"], "default": None},
    {"name": "mddisabling_condition4", "type": ["null", "string"], "default": None},
    {"name": "mddisabling_condition5", "type": ["null", "string"], "default": None},
]

NJSMART_POWERSCHOOL_ARCHIVE_FIELDS = [
    {"name": "file", "type": ["null", "string"], "default": None},
    {"name": "line", "type": ["null", "long"], "default": None},
    {"name": "student_number", "type": ["null", "double"], "default": None},
    {"name": "effective_date", "type": ["null", "string"], "default": None},
    {"name": "special_education", "type": ["null", "double"], "default": None},
    {"name": "case_manager", "type": ["null", "string"], "default": None},
    {"name": "iepbegin_date", "type": ["null", "string"], "default": None},
    {"name": "iepend_date", "type": ["null", "string"], "default": None},
    {"name": "iepgraduation_attendance", "type": ["null", "string"], "default": None},
    {
        "name": "iepgraduation_course_requirement",
        "type": ["null", "string"],
        "default": None,
    },
    {
        "name": "nj_se_consenttoimplementdate",
        "type": ["null", "string"],
        "default": None,
    },
    {"name": "nj_se_delayreason", "type": ["null", "double"], "default": None},
    {"name": "nj_se_eligibilityddate", "type": ["null", "string"], "default": None},
    {
        "name": "nj_se_initialiepmeetingdate",
        "type": ["null", "string"],
        "default": None,
    },
    {"name": "nj_se_lastiepmeetingdate", "type": ["null", "string"], "default": None},
    {
        "name": "nj_se_parental_consentobtained",
        "type": ["null", "string"],
        "default": None,
    },
    {
        "name": "nj_se_parentalconsentdate",
        "type": ["null", "string"],
        "default": None,
    },
    {"name": "nj_se_placement", "type": ["null", "double"], "default": None},
    {"name": "nj_se_reevaluationdate", "type": ["null", "string"], "default": None},
    {"name": "nj_se_referraldate", "type": ["null", "string"], "default": None},
    {"name": "nj_timeinregularprogram", "type": ["null", "string"], "default": None},
    {"name": "ti_serv_counseling", "type": ["null", "string"], "default": None},
    {"name": "ti_serv_occup", "type": ["null", "string"], "default": None},
    {"name": "ti_serv_other", "type": ["null", "string"], "default": None},
    {"name": "ti_serv_physical", "type": ["null", "string"], "default": None},
    {"name": "ti_serv_speech", "type": ["null", "string"], "default": None},
    {"name": "state_studentnumber", "type": ["null", "double"], "default": None},
    {"name": "academic_year", "type": ["null", "long"], "default": None},
    {"name": "spedlep", "type": ["null", "string"], "default": None},
    {"name": "special_education_code", "type": ["null", "string"], "default": None},
    {"name": "row_hash", "type": ["null", "string"], "default": None},
    {"name": "effective_end_date", "type": ["null", "string"], "default": None},
    {"name": "rn_stu_yr", "type": ["null", "long"], "default": None},
]

ASSET_FIELDS = {
    "njsmart_powerschool": NJSMART_POWERSCHOOL_FIELDS,
    "njsmart_powerschool_archive": NJSMART_POWERSCHOOL_ARCHIVE_FIELDS,
}
