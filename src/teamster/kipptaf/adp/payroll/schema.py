GENERAL_LEDGER_FILE_FIELDS = [
    {"name": "journal", "type": ["null", "string"], "default": None},
    {"name": "date", "type": ["null", "string"], "default": None},
    {"name": "description", "type": ["null", "string"], "default": None},
    {"name": "reference_no", "type": ["null", "long"], "default": None},
    {"name": "state", "type": ["null", "string"], "default": None},
    {"name": "sourceentity", "type": ["null", "string"], "default": None},
    {"name": "line_no", "type": ["null", "long"], "default": None},
    {"name": "document", "type": ["null", "string"], "default": None},
    {"name": "acct_no", "type": ["null", "string", "long"], "default": None},
    {"name": "debit", "type": ["null", "double"], "default": None},
    {"name": "credit", "type": ["null", "double"], "default": None},
    {"name": "memo", "type": ["null", "string"], "default": None},
    {"name": "location_id", "type": ["null", "string", "long"], "default": None},
    {"name": "dept_id", "type": ["null", "long", "double"], "default": None},
    {"name": "glentry_classid", "type": ["null", "long"], "default": None},
    {"name": "glentry_projectid", "type": ["null", "long", "double"], "default": None},
    {"name": "file_number", "type": ["null", "long"], "default": None},
    {"name": "gldimfunction", "type": ["null", "string"], "default": None},
    {"name": "gldimdonor_restriction", "type": ["null", "string"], "default": None},
    {"name": "position_id", "type": ["null", "string"], "default": None},
    {"name": "employee_name", "type": ["null", "string"], "default": None},
    {"name": "job_title", "type": ["null", "long"], "default": None},
]

ASSET_FIELDS = {
    "general_ledger_file": GENERAL_LEDGER_FILE_FIELDS,
}
