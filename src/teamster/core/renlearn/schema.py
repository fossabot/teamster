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
    {"name": "StudentIdentifier", "type": ["null", "long", "double"], "default": None},
    {"name": "StudentLastName", "type": ["null", "string"], "default": None},
    {"name": "StudentMiddleName", "type": ["null", "string"], "default": None},
    {"name": "StudentRenaissanceID", "type": ["null", "string"], "default": None},
    {"name": "StudentSourcedID", "type": ["null", "long", "double"], "default": None},
    {"name": "StudentStateID", "type": ["null", "double", "string"], "default": None},
    {"name": "StudentUserID", "type": ["null", "long", "float"], "default": None},
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

ACCELERATED_READER_FIELDS = [
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
    {"name": "Passed", "type": ["null", "boolean"], "default": None},
    {"name": "TWI", "type": ["null", "string"], "default": None},
    {"name": "BookRating", "type": ["null", "double"], "default": None},
    {"name": "AudioUsed", "type": ["null", "double", "string"], "default": None},
    {"name": "QuizDeleted", "type": ["null", "long"], "default": None},
    {"name": "WordCount", "type": ["null", "double"], "default": None},
    {"name": "QuizType", "type": ["null", "string"], "default": None},
    {"name": "LexileMeasure", "type": ["null", "string", "int"], "default": None},
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
    *CORE_FIELDS,
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
    {"name": "StudentDisplayID", "type": ["null", "long", "double"], "default": None},
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
        "type": ["null", "double"],
        "default": None,
    },
    {
        "name": "RenaissanceBenchmarkCategoryNumberOfLevels",
        "type": ["null", "long", "float"],
        "default": None,
    },
    {
        "name": "RenaissanceBenchmarkCategoryMinPercentileRank",
        "type": ["null", "double"],
        "default": None,
    },
    {
        "name": "RenaissanceBenchmarkCategoryMaxPercentileRank",
        "type": ["null", "double"],
        "default": None,
    },
    {
        "name": "StateBenchmarkAssessmentName",
        "type": ["null", "string"],
        "default": None,
    },
    {
        "name": "StateBenchmarkNumberOfCategoryLevels",
        "type": ["null", "double"],
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
    # Math
    {"name": "Audio", "type": ["null", "double", "string"], "default": None},
    {"name": "Quantile", "type": ["null", "string"], "default": None},
    # Reading
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
    # early literacy
    {"name": "LiteracyClassification", "type": ["null", "string"], "default": None},
    {"name": "LexileRange", "type": ["null", "string"], "default": None},
]

STAR_DASHBOARD_STANDARD_FIELDS = [
    {"name": "AssessmentID", "type": ["null", "string"], "default": None},
    {"name": "CompletedDate", "type": ["null", "string"], "default": None},
    {"name": "CompletedDateLocal", "type": ["null", "string"], "default": None},
    {"name": "DomainConfidenceLevel", "type": ["null", "double"], "default": None},
    {"name": "DomainGroup", "type": ["null", "string"], "default": None},
    {"name": "DomainMasteryLevel", "type": ["null", "double"], "default": None},
    {"name": "DomainName", "type": ["null", "string"], "default": None},
    {"name": "DomainPercentMastery", "type": ["null", "double"], "default": None},
    {"name": "LaunchDate", "type": ["null", "string"], "default": None},
    {"name": "RenaissanceClientID", "type": ["null", "long"], "default": None},
    {"name": "SchoolYear", "type": ["null", "string"], "default": None},
    {"name": "StandardConfidenceLevel", "type": ["null", "string"], "default": None},
    {"name": "StandardDescription", "type": ["null", "string"], "default": None},
    {"name": "StandardMasteryLevel", "type": ["null", "string"], "default": None},
    {"name": "StandardName", "type": ["null", "string"], "default": None},
    {"name": "StandardPercentMastery", "type": ["null", "long"], "default": None},
    {"name": "StudentIdentifier", "type": ["null", "long"], "default": None},
    {"name": "StudentRenaissanceID", "type": ["null", "string"], "default": None},
    {"name": "StudentSourcedID", "type": ["null", "long"], "default": None},
    {"name": "StudentStateID", "type": ["null", "string"], "default": None},
    {"name": "StudentUserID", "type": ["null", "long"], "default": None},
]

STAR_SKILL_AREA_FIELDS = [
    {"name": "AssessmentID", "type": ["null", "string"], "default": None},
    {"name": "CompletedDate", "type": ["null", "string"], "default": None},
    {"name": "CompletedDateLocal", "type": ["null", "string"], "default": None},
    {"name": "DomainName", "type": ["null", "string"], "default": None},
    {"name": "DomainScore", "type": ["null", "long"], "default": None},
    {"name": "FamilyName", "type": ["null", "string"], "default": None},
    {"name": "LaunchDate", "type": ["null", "string"], "default": None},
    {"name": "RenaissanceClientID", "type": ["null", "long"], "default": None},
    {"name": "SchoolYear", "type": ["null", "string"], "default": None},
    {"name": "SkillAreaName", "type": ["null", "string"], "default": None},
    {"name": "StudentIdentifier", "type": ["null", "long"], "default": None},
    {"name": "StudentRenaissanceID", "type": ["null", "string"], "default": None},
    {"name": "StudentSourcedID", "type": ["null", "long"], "default": None},
    {"name": "StudentStateID", "type": ["null", "string"], "default": None},
    {"name": "StudentUserID", "type": ["null", "long"], "default": None},
    {
        "name": "SkillAreaMasteryScore",
        "type": ["null", "long"],
        "default": None,
    },
]

FAST_STAR_CORE_FIELDS = [
    {"name": "AchievementLevel", "type": ["null", "string"], "default": None},
    {"name": "AssessmentName", "type": ["null", "string"], "default": None},
    {"name": "FAST_Equivalent_Score", "type": ["null", "long"], "default": None},
    {"name": "FAST_ES_Max", "type": ["null", "double"], "default": None},
    {"name": "FAST_ES_Min", "type": ["null", "double"], "default": None},
    {"name": "FAST_NOL", "type": ["null", "double"], "default": None},
    {"name": "FileDate", "type": ["null", "string"], "default": None},
    {"name": "Level3_or_Above", "type": ["null", "string"], "default": None},
    {"name": "SchoolType", "type": ["null", "string"], "default": None},
    {"name": "Assess_Num", "type": ["null", "long"], "default": None},
    {"name": "Assess_Status", "type": ["null", "string"], "default": None},
    {"name": "CBTFlag", "type": ["null", "string"], "default": None},
    {"name": "CID", "type": ["null", "string"], "default": None},
    {"name": "ClassCode", "type": ["null", "string"], "default": None},
    {"name": "ClientID", "type": ["null", "long"], "default": None},
    {"name": "Cname", "type": ["null", "string"], "default": None},
    {"name": "CompletedDate", "type": ["null", "string"], "default": None},
    {"name": "CompletedDateLocal", "type": ["null", "string"], "default": None},
    {"name": "CurrentSGP", "type": ["null", "double"], "default": None},
    {"name": "DBM_Level", "type": ["null", "long"], "default": None},
    {"name": "DBMC_NOL", "type": ["null", "long"], "default": None},
    {"name": "DBMC_PR_Max", "type": ["null", "long"], "default": None},
    {"name": "DBMC_PR_Min", "type": ["null", "long"], "default": None},
    {"name": "DBMC", "type": ["null", "string"], "default": None},
    {"name": "DBMP", "type": ["null", "string"], "default": None},
    {"name": "DIS", "type": ["null", "long"], "default": None},
    {"name": "DisName", "type": ["null", "string"], "default": None},
    {"name": "DOB", "type": ["null", "long"], "default": None},
    {"name": "Email_S", "type": ["null", "string"], "default": None},
    {"name": "Email_T", "type": ["null", "string"], "default": None},
    {"name": "Enrolled", "type": ["null", "string"], "default": None},
    {"name": "EstORF", "type": ["null", "double"], "default": None},
    {"name": "EthHisp", "type": ["null", "string"], "default": None},
    {"name": "Exempted_Absence", "type": ["null", "string"], "default": None},
    {"name": "Exempted_FailedPrac", "type": ["null", "string"], "default": None},
    {"name": "Exempted_NonEngSpeaker", "type": ["null", "string"], "default": None},
    {"name": "Exempted_WrongTest", "type": ["null", "string"], "default": None},
    {"name": "ExtraTime", "type": ["null", "string"], "default": None},
    {"name": "FirstName_T", "type": ["null", "string"], "default": None},
    {"name": "FirstName", "type": ["null", "string"], "default": None},
    {"name": "FLEID", "type": ["null", "string"], "default": None},
    {"name": "Gender", "type": ["null", "string"], "default": None},
    {"name": "GID_RID", "type": ["null", "string"], "default": None},
    {"name": "Gname", "type": ["null", "string"], "default": None},
    {"name": "Grade_E", "type": ["null", "double", "string"], "default": None},
    {"name": "Grade_P", "type": ["null", "double"], "default": None},
    {"name": "Grade_T", "type": ["null", "string"], "default": None},
    {"name": "GUID", "type": ["null", "string"], "default": None},
    {"name": "LastName_T", "type": ["null", "string"], "default": None},
    {"name": "LastName", "type": ["null", "string"], "default": None},
    {"name": "LaunchDate", "type": ["null", "string"], "default": None},
    {"name": "MI_T", "type": ["null", "string"], "default": None},
    {"name": "MI", "type": ["null", "string"], "default": None},
    {"name": "MultiRace", "type": ["null", "string"], "default": None},
    {"name": "NCE", "type": ["null", "double"], "default": None},
    {"name": "PaperAccommodations", "type": ["null", "string"], "default": None},
    {"name": "PNP_Answer_Eliminator", "type": ["null", "string"], "default": None},
    {"name": "PNP_Audio_Options", "type": ["null", "string"], "default": None},
    {"name": "PNP_Calculator", "type": ["null", "string"], "default": None},
    {"name": "PNP_Color_Scheme", "type": ["null", "string"], "default": None},
    {"name": "PNP_Contrast_Overlay", "type": ["null", "string"], "default": None},
    {"name": "PNP_Enlarge_Text", "type": ["null", "string"], "default": None},
    {"name": "PNP_Highlighter", "type": ["null", "string"], "default": None},
    {"name": "PNP_Line_Reader", "type": ["null", "string"], "default": None},
    {
        "name": "PNP_Other_Assistive_Technology",
        "type": ["null", "string"],
        "default": None,
    },
    {"name": "PNP_Screen_Reader", "type": ["null", "string"], "default": None},
    {"name": "PNP_Unlimited_Time", "type": ["null", "string"], "default": None},
    {"name": "PR", "type": ["null", "long"], "default": None},
    {"name": "RaceA", "type": ["null", "string"], "default": None},
    {"name": "RaceB", "type": ["null", "string"], "default": None},
    {"name": "RaceI", "type": ["null", "string"], "default": None},
    {"name": "RaceP", "type": ["null", "string"], "default": None},
    {"name": "RaceW", "type": ["null", "string"], "default": None},
    {"name": "RBM_Level", "type": ["null", "long"], "default": None},
    {"name": "RBMC_NOL", "type": ["null", "long"], "default": None},
    {"name": "RBMC_PR_Max", "type": ["null", "long"], "default": None},
    {"name": "RBMC_PR_Min", "type": ["null", "long"], "default": None},
    {"name": "RBMC", "type": ["null", "string"], "default": None},
    {"name": "Reported", "type": ["null", "string"], "default": None},
    {"name": "SBM_Level", "type": ["null", "long"], "default": None},
    {"name": "SBM", "type": ["null", "string"], "default": None},
    {"name": "SBMC_NOL", "type": ["null", "long"], "default": None},
    {"name": "SBMC_SS_Max", "type": ["null", "long"], "default": None},
    {"name": "SBMC_SS_Min", "type": ["null", "long"], "default": None},
    {"name": "SBMC", "type": ["null", "string"], "default": None},
    {"name": "SBMP", "type": ["null", "string"], "default": None},
    {"name": "SCH", "type": ["null", "long"], "default": None},
    {"name": "SchBM_Level", "type": ["null", "long"], "default": None},
    {"name": "SchBMC_NOL", "type": ["null", "long"], "default": None},
    {"name": "SchBMC_PR_Max", "type": ["null", "long"], "default": None},
    {"name": "SchBMC_PR_Min", "type": ["null", "long"], "default": None},
    {"name": "SchBMC", "type": ["null", "string"], "default": None},
    {"name": "SchBMP", "type": ["null", "string"], "default": None},
    {"name": "SchName", "type": ["null", "string"], "default": None},
    {"name": "SchoolYear_ED", "type": ["null", "string"], "default": None},
    {"name": "SchoolYear_SD", "type": ["null", "string"], "default": None},
    {"name": "SchoolYear", "type": ["null", "string"], "default": None},
    {"name": "SEM", "type": ["null", "double"], "default": None},
    {"name": "SGP_FF", "type": ["null", "double"], "default": None},
    {"name": "SGP_FS", "type": ["null", "double"], "default": None},
    {"name": "SGP_FW", "type": ["null", "double"], "default": None},
    {"name": "SGP_SF", "type": ["null", "double"], "default": None},
    {"name": "SGP_SS", "type": ["null", "double"], "default": None},
    {"name": "SGP_WS", "type": ["null", "double"], "default": None},
    {"name": "Sgrade", "type": ["null", "string"], "default": None},
    {"name": "SID_SID", "type": ["null", "long"], "default": None},
    {"name": "SW_ED", "type": ["null", "string"], "default": None},
    {"name": "SW_Name", "type": ["null", "string"], "default": None},
    {"name": "SW_SD", "type": ["null", "string"], "default": None},
    {"name": "TestingIP", "type": ["null", "string"], "default": None},
    {"name": "TestingSite", "type": ["null", "string"], "default": None},
    {"name": "TestName", "type": ["null", "string"], "default": None},
    {"name": "TID_RID", "type": ["null", "string"], "default": None},
    {"name": "TID", "type": ["null", "long"], "default": None},
    {"name": "TotalCorrect", "type": ["null", "double"], "default": None},
    {"name": "TotalPossible", "type": ["null", "double"], "default": None},
    {"name": "TotalTime", "type": ["null", "long"], "default": None},
    {"name": "UnifiedScore", "type": ["null", "long"], "default": None},
]

FAST_STAR_FIELDS = [
    *FAST_STAR_CORE_FIELDS,
    # Math
    {"name": "Quantile", "type": ["null", "string"], "default": None},
    # Reading
    {"name": "Attempts_G3", "type": ["null", "string", "long"], "default": None},
    {"name": "IRL", "type": ["null", "string"], "default": None},
    {"name": "Lexile", "type": ["null", "string"], "default": None},
    {"name": "PassingScore_G3", "type": ["null", "string"], "default": None},
    {"name": "PassingStatus_G3", "type": ["null", "string"], "default": None},
    {"name": "ZPD_Lexile_Lower", "type": ["null", "double"], "default": None},
    {"name": "ZPD_Lexile_Upper", "type": ["null", "double"], "default": None},
    {"name": "ZPD_Lower", "type": ["null", "double"], "default": None},
    {"name": "ZPD_Upper", "type": ["null", "double"], "default": None},
    # Early Literacy
    {"name": "LexileRange", "type": ["null", "string"], "default": None},
    {"name": "LitClassification", "type": ["null", "string"], "default": None},
    # Early Literacy - Domains
    {"name": "SubDomain_AP", "type": ["null", "long"], "default": None},
    {"name": "SubDomain_AP_SkillSet_A", "type": ["null", "long"], "default": None},
    {"name": "SubDomain_AP_SkillSet_B", "type": ["null", "long"], "default": None},
    {"name": "SubDomain_AP_SkillSet_C", "type": ["null", "long"], "default": None},
    {"name": "SubDomain_CW", "type": ["null", "long"], "default": None},
    {"name": "SubDomain_CW_SkillSet_A", "type": ["null", "long"], "default": None},
    {"name": "SubDomain_CW_SkillSet_B", "type": ["null", "long"], "default": None},
    {"name": "SubDomain_CW_SkillSet_C", "type": ["null", "long"], "default": None},
    {"name": "SubDomain_CW_SkillSet_D", "type": ["null", "long"], "default": None},
    {"name": "SubDomain_EN", "type": ["null", "long"], "default": None},
    {"name": "SubDomain_EN_SkillSet_A", "type": ["null", "long"], "default": None},
    {"name": "SubDomain_EN_SkillSet_B", "type": ["null", "long"], "default": None},
    {"name": "SubDomain_EN_SkillSet_C", "type": ["null", "long"], "default": None},
    {"name": "SubDomain_EN_SkillSet_D", "type": ["null", "long"], "default": None},
    {"name": "SubDomain_EN_SkillSet_E", "type": ["null", "long"], "default": None},
    {"name": "SubDomain_PA", "type": ["null", "long"], "default": None},
    {"name": "SubDomain_PA_SkillSet_A", "type": ["null", "long"], "default": None},
    {"name": "SubDomain_PA_SkillSet_B", "type": ["null", "long"], "default": None},
    {"name": "SubDomain_PA_SkillSet_C", "type": ["null", "long"], "default": None},
    {"name": "SubDomain_PA_SkillSet_D", "type": ["null", "long"], "default": None},
    {"name": "SubDomain_PA_SkillSet_E", "type": ["null", "long"], "default": None},
    {"name": "SubDomain_PA_SkillSet_F", "type": ["null", "long"], "default": None},
    {"name": "SubDomain_PA_SkillSet_G", "type": ["null", "long"], "default": None},
    {"name": "SubDomain_PA_SkillSet_H", "type": ["null", "long"], "default": None},
    {"name": "SubDomain_PC", "type": ["null", "long"], "default": None},
    {"name": "SubDomain_PC_SkillSet_A", "type": ["null", "long"], "default": None},
    {"name": "SubDomain_PH", "type": ["null", "long"], "default": None},
    {"name": "SubDomain_PH_SkillSet_A", "type": ["null", "long"], "default": None},
    {"name": "SubDomain_PH_SkillSet_B", "type": ["null", "long"], "default": None},
    {"name": "SubDomain_PH_SkillSet_C", "type": ["null", "long"], "default": None},
    {"name": "SubDomain_PH_SkillSet_D", "type": ["null", "long"], "default": None},
    {"name": "SubDomain_PH_SkillSet_E", "type": ["null", "long"], "default": None},
    {"name": "SubDomain_PH_SkillSet_F", "type": ["null", "long"], "default": None},
    {"name": "SubDomain_PH_SkillSet_G", "type": ["null", "long"], "default": None},
    {"name": "SubDomain_PH_SkillSet_H", "type": ["null", "long"], "default": None},
    {"name": "SubDomain_PH_SkillSet_I", "type": ["null", "long"], "default": None},
    {"name": "SubDomain_PH_SkillSet_J", "type": ["null", "long"], "default": None},
    {"name": "SubDomain_PH_SkillSet_K", "type": ["null", "long"], "default": None},
    {"name": "SubDomain_PH_SkillSet_L", "type": ["null", "long"], "default": None},
    {"name": "SubDomain_SA", "type": ["null", "long"], "default": None},
    {"name": "SubDomain_SA_SkillSet_A", "type": ["null", "long"], "default": None},
    {"name": "SubDomain_SA_SkillSet_B", "type": ["null", "long"], "default": None},
    {"name": "SubDomain_SA_SkillSet_C", "type": ["null", "long"], "default": None},
    {"name": "SubDomain_SA_SkillSet_D", "type": ["null", "long"], "default": None},
    {"name": "SubDomain_SC", "type": ["null", "long"], "default": None},
    {"name": "SubDomain_SC_SkillSet_A", "type": ["null", "long"], "default": None},
    {"name": "SubDomain_VO", "type": ["null", "long"], "default": None},
    {"name": "SubDomain_VO_SkillSet_A", "type": ["null", "long"], "default": None},
    {"name": "SubDomain_VO_SkillSet_B", "type": ["null", "long"], "default": None},
    {"name": "SubDomain_VO_SkillSet_C", "type": ["null", "long"], "default": None},
    {"name": "SubDomain_VS", "type": ["null", "long"], "default": None},
    {"name": "SubDomain_VS_SkillSet_A", "type": ["null", "long"], "default": None},
    {"name": "SubDomain_VS_SkillSet_B", "type": ["null", "long"], "default": None},
]

FAST_STAR_DOMAIN_FIELDS = [
    *FAST_STAR_CORE_FIELDS,
]

ASSET_FIELDS = {
    "accelerated_reader": ACCELERATED_READER_FIELDS,
    "star": STAR_FIELDS,
    "star_dashboard_standards": STAR_DASHBOARD_STANDARD_FIELDS,
    "star_skill_area": STAR_SKILL_AREA_FIELDS,
    "fast_star": FAST_STAR_FIELDS,
}
