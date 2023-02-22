def get_date_record_schema(name):
    return {
        "name": f"{name}-record",
        "type": "record",
        "fields": [
            {"name": "date", "type": "string", "logicalType": "timestamp-micros"},
            {"name": "timezone_type", "type": "int"},
            {"name": "timezone", "type": "string"},
        ],
    }


ENROLLMENT_RECORD_SCHEMA = {
    "name": "enrollment-record",
    "type": "record",
    "fields": [
        {"name": "EnrollmentID", "type": ["null", "string"]},
        {"name": "AcademicYearID", "type": ["null", "string"]},
        {"name": "YearName", "type": ["null", "string"]},
        {"name": "StartDate", "type": ["null", get_date_record_schema("StartDate")]},
        {"name": "EndDate", "type": ["null", get_date_record_schema("EndDate")]},
        {"name": "GradeLevelID", "type": ["null", "string"]},
        {"name": "GradeLevelName", "type": ["null", "string"]},
        {"name": "DepartmentID", "type": ["null", "string"]},
        {"name": "DepartmentName", "type": ["null", "string"]},
        {"name": "BehaviorPlanID", "type": ["null", "string"]},
        {"name": "BehaviorPlanName", "type": ["null", "string"]},
        {"name": "CreateByName", "type": ["null", "string"]},
        {"name": "CreateDate", "type": ["null", get_date_record_schema("CreateDate")]},
        {"name": "TermByName", "type": ["null", "string"]},
        {"name": "TermDate", "type": ["null", get_date_record_schema("TermDate")]},
        {"name": "GradeLevelKey", "type": ["null", "string"]},
    ],
}

AVRO_SCHEMA = {
    "users": [
        {"name": "DLSchoolID", "type": ["null", "string"]},
        {"name": "SchoolName", "type": ["null", "string"]},
        {"name": "DLUserID", "type": ["null", "string"]},
        {"name": "FirstName", "type": ["null", "string"]},
        {"name": "MiddleName", "type": ["null", "string"]},
        {"name": "LastName", "type": ["null", "string"]},
        {"name": "Title", "type": ["null", "string"]},
        {"name": "UserSchoolID", "type": ["null", "string"]},
        {"name": "UserRole", "type": ["null", "string"]},
        {"name": "Username", "type": ["null", "string"]},
        {"name": "Email", "type": ["null", "string"]},
        {"name": "GroupName", "type": ["null", "string"]},
    ],
    "students": [
        {"name": "StudentID", "type": ["null", "string"]},
        {"name": "DepartmentID", "type": ["null", "string"]},
        {"name": "Department", "type": ["null", "string"]},
        {"name": "GradeLevelID", "type": ["null", "string"]},
        {"name": "GradeLevel", "type": ["null", "string"]},
        {"name": "GradeLevelKey", "type": ["null", "string"]},
        {"name": "FirstName", "type": ["null", "string"]},
        {"name": "MiddleName", "type": ["null", "string"]},
        {"name": "LastName", "type": ["null", "string"]},
        {"name": "StudentSchoolID", "type": ["null", "string"]},
        {"name": "IntegrationID", "type": ["null", "string"]},
        {"name": "EnrollmentStatus", "type": ["null", "string"]},
        {"name": "BehaviorPlan", "type": ["null", "string"]},
        {
            "name": "BirthDate",
            "type": ["string", {"type": "long", "logicalType": "timestamp-micros"}],
        },
        {"name": "Enrollment", "type": ["null", ENROLLMENT_RECORD_SCHEMA]},
        {"name": "HomeLanguageID", "type": ["null", "string"]},
        {"name": "HomeLanguage", "type": ["null", "string"]},
        {"name": "HomeroomID", "type": ["null", "string"]},
        {"name": "Homeroom", "type": ["null", "string"]},
        {"name": "IsNSLP", "type": ["null", "string"]},
        {"name": "Gender", "type": ["null", "string"]},
        {"name": "StreetAddress1", "type": ["null", "string"]},
        {"name": "StreetAddress2", "type": ["null", "string"]},
        {"name": "City", "type": ["null", "string"]},
        {"name": "State", "type": ["null", "string"]},
        {"name": "ZipCode", "type": ["null", "string"]},
        {"name": "PhotoFile", "type": ["null", "string"]},
        {"name": "DLPS_ValidationCode", "type": ["null", "string"]},
        {"name": "Parents", "type": ["null", {"type": "array", "items": "string"}]},
        {"name": "Notes", "type": ["null", {"type": "array", "items": "string"}]},
    ],
    "lists": [
        {"name": "ListID", "type": ["null", "string"]},
        {"name": "ListName", "type": ["null", "string"]},
        {"name": "IsDated", "type": ["null", "boolean"]},
    ],
    "terms": [
        {"name": "TermID", "type": ["null", "string"]},
        {"name": "AcademicYearID", "type": ["null", "string"]},
        {"name": "AcademicYearName", "type": ["null", "string"]},
        {"name": "SchoolID", "type": ["null", "string"]},
        {"name": "TermTypeID", "type": ["null", "string"]},
        {"name": "TermType", "type": ["null", "string"]},
        {"name": "TermName", "type": ["null", "string"]},
        {"name": "StartDate", "type": ["null", get_date_record_schema("StartDate")]},
        {"name": "EndDate", "type": ["null", get_date_record_schema("EndDate")]},
    ],
    "rosters": [
        {"name": "RosterID", "type": ["null", "string"]},
        {"name": "RosterName", "type": ["null", "string"]},
        {"name": "RosterTypeID", "type": ["null", "string"]},
        {"name": "RosterType", "type": ["null", "string"]},
        {"name": "MasterID", "type": ["null", "string"]},
        {"name": "MasterName", "type": ["null", "string"]},
        {"name": "TakeAttendance", "type": ["null", "string"]},
        {"name": "TakeClassAttendance", "type": ["null", "string"]},
        {"name": "CollectHW", "type": ["null", "string"]},
        {"name": "MarkerColor", "type": ["null", "string"]},
        {"name": "SISKey", "type": ["null", "string"]},
        {"name": "SecondaryIntegrationID", "type": ["null", "string"]},
        {"name": "ScreenSetID", "type": ["null", "string"]},
        {"name": "StudentCount", "type": ["null", "string"]},
    ],
    "behavior": [
        {"name": "DLOrganizationID", "type": ["string", "null"]},
        {"name": "DLSchoolID", "type": ["string", "null"]},
        {"name": "SchoolName", "type": ["string", "null"]},
        {"name": "DLStudentID", "type": ["string", "null"]},
        {"name": "StudentSchoolID", "type": ["string", "null"]},
        {"name": "SecondaryStudentID", "type": ["string", "null"]},
        {"name": "StudentFirstName", "type": ["string", "null"]},
        {"name": "StudentMiddleName", "type": ["string", "null"]},
        {"name": "StudentLastName", "type": ["string", "null"]},
        {"name": "DLSAID", "type": ["string", "null"]},
        {
            "name": "BehaviorDate",
            "type": ["null", {"type": "string", "logicalType": "date"}],
        },
        {"name": "Behavior", "type": ["string", "null"]},
        {"name": "BehaviorCategory", "type": ["string", "null"]},
        {"name": "PointValue", "type": ["string", "null"]},
        {"name": "DLUserID", "type": ["string", "null"]},
        {"name": "StaffSchoolID", "type": ["string", "null"]},
        {"name": "StaffTitle", "type": ["string", "null"]},
        {"name": "StaffFirstName", "type": ["string", "null"]},
        {"name": "StaffMiddleName", "type": ["string", "null"]},
        {"name": "StaffLastName", "type": ["string", "null"]},
        {"name": "Roster", "type": ["string", "null"]},
        {"name": "RosterID", "type": ["string", "null"]},
        {"name": "SourceType", "type": ["string", "null"]},
        {"name": "SourceID", "type": ["string", "null"]},
        {"name": "SourceProcedure", "type": ["string", "null"]},
        {"name": "Notes", "type": ["string", "null"]},
        {"name": "Assignment", "type": ["string", "null"]},
        {
            "name": "DL_LASTUPDATE",
            "type": ["null", {"type": "string", "logicalType": "timestamp-micros"}],
        },
        {"name": "is_deleted", "type": ["null", "int"]},
    ],
}


def get_avro_schema(name):
    return {"type": "record", "name": name, "fields": AVRO_SCHEMA[name]}
