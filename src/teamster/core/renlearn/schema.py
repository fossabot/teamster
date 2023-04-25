CORE_FIELDS = [
    {"name": "Asian", "type": ["null", "string"], "default": None},
    {"name": "BlackOrAfricanAmerican", "type": ["null", "string"], "default": None},
    {"name": "ClassCode", "type": ["null", "string"], "default": None},
    {"name": "ClassRenaissanceID", "type": ["null", "string"], "default": None},
    {"name": "ClassSourcedID", "type": ["null", "string"], "default": None},
    {"name": "CourseCode", "type": ["null", "string"], "default": None},
    {"name": "CourseName", "type": ["null", "string"], "default": None},
    {"name": "CourseRenaissanceID", "type": ["null", "string"], "default": None},
    {"name": "CourseSourcedID", "type": ["null", "string"], "default": None},
    {"name": "CurrentGrade", "type": ["null", "long", "string"], "default": None},
    {"name": "DistrictIdentifier", "type": ["null", "double"], "default": None},
    {"name": "DistrictName", "type": ["null", "string"], "default": None},
    {"name": "DistrictRenaissanceID", "type": ["null", "string"], "default": None},
    {"name": "DistrictSourcedID", "type": ["null", "string"], "default": None},
    {"name": "DistrictStateID", "type": ["null", "double", "long"], "default": None},
    {"name": "EnrollmentStatus", "type": ["null", "string"], "default": None},
    {"name": "Gender", "type": ["null", "string"], "default": None},
    {"name": "GroupID", "type": ["null", "string"], "default": None},
    {"name": "GroupOrClassName", "type": ["null", "string"], "default": None},
    {"name": "HispanicOrLatino", "type": ["null", "string"], "default": None},
    {"name": "MultiRace", "type": ["null", "string"], "default": None},
    {"name": "RenaissanceClientID", "type": ["null", "long"], "default": None},
    {"name": "SchoolIdentifier", "type": ["null", "long"], "default": None},
    {"name": "SchoolName", "type": ["null", "string"], "default": None},
    {"name": "SchoolRenaissanceID", "type": ["null", "string"], "default": None},
    {"name": "SchoolSourcedID", "type": ["null", "string"], "default": None},
    {"name": "SchoolStateID", "type": ["null", "double", "long"], "default": None},
    {"name": "SchoolYear", "type": ["null", "string"], "default": None},
    {"name": "StudentEmail", "type": ["null", "double"], "default": None},
    {"name": "StudentFirstName", "type": ["null", "string"], "default": None},
    {"name": "StudentIdentifier", "type": ["null", "long"], "default": None},
    {"name": "StudentLastName", "type": ["null", "string"], "default": None},
    {"name": "StudentMiddleName", "type": ["null", "string"], "default": None},
    {"name": "StudentRenaissanceID", "type": ["null", "string"], "default": None},
    {"name": "StudentSourcedID", "type": ["null", "long"], "default": None},
    {"name": "StudentStateID", "type": ["null", "double", "string"], "default": None},
    {"name": "StudentUserID", "type": ["null", "long"], "default": None},
    {"name": "TeacherEmail", "type": ["null", "string"], "default": None},
    {"name": "TeacherFirstName", "type": ["null", "string"], "default": None},
    {"name": "TeacherIdentifier", "type": ["null", "string"], "default": None},
    {"name": "TeacherLastName", "type": ["null", "string"], "default": None},
    {"name": "TeacherMiddleName", "type": ["null", "double"], "default": None},
    {"name": "TeacherRenaissanceID", "type": ["null", "string"], "default": None},
    {"name": "TeacherSourcedID", "type": ["null", "string"], "default": None},
    {"name": "TeacherStateID", "type": ["null", "double", "long"], "default": None},
    {"name": "TeacherUserID", "type": ["null", "string"], "default": None},
    {"name": "White", "type": ["null", "string"], "default": None},
    {
        "name": "AmericanIndianOrAlaskaNative",
        "type": ["null", "string"],
        "default": None,
    },
    {
        "name": "NativeHawaiianOrOtherPacificIslander",
        "type": ["null", "string"],
        "default": None,
    },
    {
        "name": "SchoolYearStartDate",
        "type": ["null", "string"],
        "logicalType": "timestamp-millis",
        "default": None,
    },
    {
        "name": "SchoolYearEndDate",
        "type": ["null", "string"],
        "logicalType": "timestamp-millis",
        "default": None,
    },
    {
        "name": "BirthDate",
        "type": ["null", "string"],
        "logicalType": "timestamp-millis",
        "default": None,
    },
]

GENERIC_AR_EXTRACT_FIELDS = [
    *CORE_FIELDS,
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
    {"name": "QuizDeleted", "type": ["null", "long"], "default": None},
    {"name": "WordCount", "type": ["null", "double"], "default": None},
    {"name": "QuizType", "type": ["null", "string"], "default": None},
    {"name": "LexileMeasure", "type": ["null", "string"], "default": None},
    {"name": "LexileLevel", "type": ["null", "double"], "default": None},
    {
        "name": "DateQuizCompleted",
        "type": ["null", "string"],
        "logicalType": "timestamp-millis",
        "default": None,
    },
    {
        "name": "DateQuizCompletedLocal",
        "type": ["null", "string"],
        "logicalType": "timestamp-millis",
        "default": None,
    },
]

STAR_FIELDS = [
    {"name": "ACTBenchmarkCategory", "type": ["null", "double"], "default": None},
    {"name": "AssessmentID", "type": ["null", "string"], "default": None},
    {"name": "AssessmentNumber", "type": ["null", "long"], "default": None},
    {"name": "AssessmentStatus", "type": ["null", "string"], "default": None},
    {"name": "AssessmentType", "type": ["null", "string"], "default": None},
    {"name": "CurrentSGP", "type": ["null", "double"], "default": None},
    {"name": "DeactivationReason", "type": ["null", "double"], "default": None},
    {"name": "ExtraTime", "type": ["null", "string"], "default": None},
    {"name": "Grade", "type": ["null", "long", "string"], "default": None},
    {"name": "GradeEquivalent", "type": ["null", "double", "string"], "default": None},
    {"name": "GradePlacement", "type": ["null", "double"], "default": None},
    {"name": "NormalCurveEquivalent", "type": ["null", "double"], "default": None},
    {"name": "OpenGrowthScore", "type": ["null", "double"], "default": None},
    {"name": "PercentileRank", "type": ["null", "long"], "default": None},
    {"name": "RaschScore", "type": ["null", "double"], "default": None},
    {"name": "SATBenchmarkCategory", "type": ["null", "double"], "default": None},
    {"name": "ScaledScore", "type": ["null", "long"], "default": None},
    {"name": "SchoolBenchmarkCategoryLevel", "type": ["null", "long"], "default": None},
    {"name": "SchoolBenchmarkProficient", "type": ["null", "string"], "default": None},
    {"name": "ScreeningPeriodWindowName", "type": ["null", "string"], "default": None},
    {"name": "StandardErrorOfMeasurement", "type": ["null", "double"], "default": None},
    {"name": "StateBenchmarkCategoryName", "type": ["null", "string"], "default": None},
    {"name": "StateBenchmarkProficient", "type": ["null", "string"], "default": None},
    {"name": "StudentDisplayID", "type": ["null", "long"], "default": None},
    {"name": "TakenAt", "type": ["null", "string"], "default": None},
    {"name": "TakenAtByIPAddress", "type": ["null", "double"], "default": None},
    {"name": "TeacherDisplayID", "type": ["null", "string"], "default": None},
    {"name": "TotalCorrect", "type": ["null", "double"], "default": None},
    {"name": "TotalPossible", "type": ["null", "double"], "default": None},
    {"name": "TotalTimeInSeconds", "type": ["null", "long"], "default": None},
    {"name": "UnifiedScore", "type": ["null", "long"], "default": None},
    {
        "name": "LaunchDate",
        "type": ["null", "string"],
        "logicalType": "timestamp-millis",
        "default": None,
    },
    {
        "name": "CompletedDate",
        "type": ["null", "string"],
        "logicalType": "timestamp-millis",
        "default": None,
    },
    {
        "name": "CompletedDateLocal",
        "type": ["null", "string"],
        "logicalType": "timestamp-millis",
        "default": None,
    },
    {
        "name": "PartnershipForAssessmentOfReadinessForCollegeAndCareers",
        "type": ["null", "double"],
        "default": None,
    },
    {
        "name": "ScreeningWindowStartDate",
        "type": ["null", "string"],
        "logicalType": "timestamp-millis",
        "default": None,
    },
    {
        "name": "ScreeningWindowEndDate",
        "type": ["null", "string"],
        "logicalType": "timestamp-millis",
        "default": None,
    },
    {
        "name": "StateBenchmarkCategoryLevel",
        "type": ["null", "double"],
        "default": None,
    },
    {
        "name": "StateBenchmarkMinScaledScore",
        "type": ["null", "double"],
        "default": None,
    },
    {
        "name": "StateBenchmarkMaxScaledScore",
        "type": ["null", "double"],
        "default": None,
    },
    {
        "name": "SmarterBalancedAssessmentConsortium",
        "type": ["null", "double"],
        "default": None,
    },
    {
        "name": "StudentGrowthPercentileFallFall",
        "type": ["null", "double"],
        "default": None,
    },
    {
        "name": "StudentGrowthPercentileFallSpring",
        "type": ["null", "double"],
        "default": None,
    },
    {
        "name": "StudentGrowthPercentileFallWinter",
        "type": ["null", "double"],
        "default": None,
    },
    {
        "name": "StudentGrowthPercentileSpringFall",
        "type": ["null", "double"],
        "default": None,
    },
    {
        "name": "StudentGrowthPercentileSpringSpring",
        "type": ["null", "double"],
        "default": None,
    },
    {
        "name": "StudentGrowthPercentileWinterSpring",
        "type": ["null", "double"],
        "default": None,
    },
    {
        "name": "RenaissanceBenchmarkCategoryName",
        "type": ["null", "string"],
        "default": None,
    },
    {
        "name": "RenaissanceBenchmarkCategoryLevel",
        "type": ["null", "long"],
        "default": None,
    },
    {
        "name": "RenaissanceBenchmarkCategoryNumberOfLevels",
        "type": ["null", "long"],
        "default": None,
    },
    {
        "name": "RenaissanceBenchmarkCategoryMinPercentileRank",
        "type": ["null", "long"],
        "default": None,
    },
    {
        "name": "RenaissanceBenchmarkCategoryMaxPercentileRank",
        "type": ["null", "long"],
        "default": None,
    },
    {
        "name": "StateBenchmarkAssessmentName",
        "type": ["null", "string"],
        "default": None,
    },
    {
        "name": "StateBenchmarkNumberOfCategoryLevels",
        "type": ["null", "long"],
        "default": None,
    },
    {
        "name": "DistrictBenchmarkCategoryName",
        "type": ["null", "string"],
        "default": None,
    },
    {
        "name": "DistrictBenchmarkProficient",
        "type": ["null", "string"],
        "default": None,
    },
    {
        "name": "DistrictBenchmarkCategoryLevel",
        "type": ["null", "long"],
        "default": None,
    },
    {
        "name": "DistrictBenchmarkNumberOfCategoryLevels",
        "type": ["null", "long"],
        "default": None,
    },
    {
        "name": "DistrictBenchmarkMinPercentileRank",
        "type": ["null", "long"],
        "default": None,
    },
    {
        "name": "DistrictBenchmarkMaxPercentileRank",
        "type": ["null", "long"],
        "default": None,
    },
    {
        "name": "SchoolBenchmarkCategoryName",
        "type": ["null", "string"],
        "default": None,
    },
    {
        "name": "SchoolBenchmarkNumberOfCategoryLevels",
        "type": ["null", "long"],
        "default": None,
    },
    {
        "name": "SchoolBenchmarkMinPercentileRank",
        "type": ["null", "long"],
        "default": None,
    },
    {
        "name": "SchoolBenchmarkMaxPercentileRank",
        "type": ["null", "long"],
        "default": None,
    },
]

STAR_MATH_FIELDS = [
    *CORE_FIELDS,
    *STAR_FIELDS,
    {"name": "Audio", "type": ["null", "double"], "default": None},
    {"name": "Quantile", "type": ["null", "string"], "default": None},
]

STAR_READING_FIELDS = [
    *CORE_FIELDS,
    *STAR_FIELDS,
    {"name": "InstructionalReadingLevel", "type": ["null", "string"], "default": None},
    {"name": "Lexile", "type": ["null", "string"], "default": None},
    {"name": "Grade3_AssessmentAttempts", "type": ["null", "long"], "default": None},
    {"name": "Grade3_PassingStatus", "type": ["null", "double"], "default": None},
    {"name": "Grade3_PassingScore", "type": ["null", "double"], "default": None},
    {
        "name": "EstimatedOralReadingFluency",
        "type": ["null", "double"],
        "default": None,
    },
    {
        "name": "LowerZoneOfProximalDevelopment",
        "type": ["null", "double"],
        "default": None,
    },
    {
        "name": "UpperZoneOfProximalDevelopment",
        "type": ["null", "double"],
        "default": None,
    },
    {
        "name": "LowerLexileZoneOfProximalDevelopment",
        "type": ["null", "double"],
        "default": None,
    },
    {
        "name": "UpperLexileZoneOfProximalDevelopment",
        "type": ["null", "double"],
        "default": None,
    },
]

ENDPOINT_FIELDS = {
    "generic_ar_extract": GENERIC_AR_EXTRACT_FIELDS,
    "star_math": STAR_MATH_FIELDS,
    "star_reading": STAR_READING_FIELDS,
}
