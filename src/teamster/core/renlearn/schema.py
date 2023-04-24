GENERIC_AR_EXTRACT_FIELDS = [
    {"name": "RenaissanceClientID", "type": ["null", "long"], "default": None},
    {"name": "SchoolYear", "type": ["null", "string"], "default": None},
    {"name": "SchoolYearStartDate", "type": ["null", "string"], "default": None},
    {"name": "SchoolYearEndDate", "type": ["null", "string"], "default": None},
    {"name": "StudentRenaissanceID", "type": ["null", "string"], "default": None},
    {"name": "StudentSourcedID", "type": ["null", "long"], "default": None},
    {"name": "StudentIdentifier", "type": ["null", "long"], "default": None},
    {"name": "StudentUserID", "type": ["null", "long"], "default": None},
    {"name": "StudentStateID", "type": ["null", "double"], "default": None},
    {"name": "StudentEmail", "type": ["null", "double"], "default": None},
    {"name": "StudentFirstName", "type": ["null", "string"], "default": None},
    {"name": "StudentMiddleName", "type": ["null", "string"], "default": None},
    {"name": "StudentLastName", "type": ["null", "string"], "default": None},
    {"name": "Gender", "type": ["null", "string"], "default": None},
    {"name": "BirthDate", "type": ["null", "string"], "default": None},
    {"name": "MultiRace", "type": ["null", "string"], "default": None},
    {"name": "HispanicOrLatino", "type": ["null", "string"], "default": None},
    {
        "name": "AmericanIndianOrAlaskaNative",
        "type": ["null", "string"],
        "default": None,
    },
    {"name": "Asian", "type": ["null", "string"], "default": None},
    {"name": "BlackOrAfricanAmerican", "type": ["null", "string"], "default": None},
    {
        "name": "NativeHawaiianOrOtherPacificIslander",
        "type": ["null", "string"],
        "default": None,
    },
    {"name": "White", "type": ["null", "string"], "default": None},
    {"name": "CurrentGrade", "type": ["null", "string"], "default": None},
    {"name": "EnrollmentStatus", "type": ["null", "string"], "default": None},
    {"name": "DistrictRenaissanceID", "type": ["null", "string"], "default": None},
    {"name": "DistrictSourcedID", "type": ["null", "string"], "default": None},
    {"name": "DistrictIdentifier", "type": ["null", "double"], "default": None},
    {"name": "DistrictStateID", "type": ["null", "double"], "default": None},
    {"name": "DistrictName", "type": ["null", "string"], "default": None},
    {"name": "SchoolRenaissanceID", "type": ["null", "string"], "default": None},
    {"name": "SchoolSourcedID", "type": ["null", "string"], "default": None},
    {"name": "SchoolIdentifier", "type": ["null", "long"], "default": None},
    {"name": "SchoolStateID", "type": ["null", "double"], "default": None},
    {"name": "SchoolName", "type": ["null", "string"], "default": None},
    {"name": "CourseRenaissanceID", "type": ["null", "string"], "default": None},
    {"name": "CourseSourcedID", "type": ["null", "string"], "default": None},
    {"name": "CourseCode", "type": ["null", "string"], "default": None},
    {"name": "CourseName", "type": ["null", "string"], "default": None},
    {"name": "ClassRenaissanceID", "type": ["null", "string"], "default": None},
    {"name": "ClassSourcedID", "type": ["null", "string"], "default": None},
    {"name": "ClassCode", "type": ["null", "string"], "default": None},
    {"name": "GroupID", "type": ["null", "string"], "default": None},
    {"name": "GroupOrClassName", "type": ["null", "string"], "default": None},
    {"name": "TeacherRenaissanceID", "type": ["null", "string"], "default": None},
    {"name": "TeacherSourcedID", "type": ["null", "string"], "default": None},
    {"name": "TeacherIdentifier", "type": ["null", "string"], "default": None},
    {"name": "TeacherUserID", "type": ["null", "string"], "default": None},
    {"name": "TeacherStateID", "type": ["null", "double"], "default": None},
    {"name": "TeacherEmail", "type": ["null", "string"], "default": None},
    {"name": "TeacherFirstName", "type": ["null", "string"], "default": None},
    {"name": "TeacherMiddleName", "type": ["null", "double"], "default": None},
    {"name": "TeacherLastName", "type": ["null", "string"], "default": None},
    {"name": "QuizNumber", "type": ["null", "double"], "default": None},
    {"name": "ContentLanguage", "type": ["null", "string"], "default": None},
    {"name": "ContentTitle", "type": ["null", "string"], "default": None},
    {"name": "Author", "type": ["null", "string"], "default": None},
    {"name": "FictionNonFiction", "type": ["null", "string"], "default": None},
    {"name": "InterestLevel", "type": ["null", "string"], "default": None},
    {"name": "BookLevel", "type": ["null", "double"], "default": None},
    {"name": "QuestionsPresented", "type": ["null", "double"], "default": None},
    {"name": "QuestionsCorrect", "type": ["null", "double"], "default": None},
    {"name": "PercentCorrect", "type": ["null", "double"], "default": None},
    {"name": "PointsPossible", "type": ["null", "double"], "default": None},
    {"name": "PointsEarned", "type": ["null", "double"], "default": None},
    {"name": "Passed", "type": ["null", "string"], "default": None},
    {"name": "TWI", "type": ["null", "string"], "default": None},
    {"name": "BookRating", "type": ["null", "double"], "default": None},
    {"name": "AudioUsed", "type": ["null", "double"], "default": None},
    {"name": "DateQuizCompleted", "type": ["null", "string"], "default": None},
    {"name": "DateQuizCompletedLocal", "type": ["null", "string"], "default": None},
    {"name": "QuizDeleted", "type": ["null", "long"], "default": None},
    {"name": "WordCount", "type": ["null", "double"], "default": None},
    {"name": "QuizType", "type": ["null", "string"], "default": None},
    {"name": "LexileMeasure", "type": ["null", "string"], "default": None},
    {"name": "LexileLevel", "type": ["null", "double"], "default": None},
]

ENDPOINT_FIELDS = {
    "generic_ar_extract": GENERIC_AR_EXTRACT_FIELDS,
}
