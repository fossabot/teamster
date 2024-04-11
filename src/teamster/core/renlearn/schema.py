import json

import py_avro_schema
from pydantic import BaseModel


class RenLearningCore(BaseModel):
    Asian: str | None = None
    BlackOrAfricanAmerican: str | None = None
    ClassCode: str | None = None
    ClassRenaissanceID: str | None = None
    ClassSourcedID: str | None = None
    CourseCode: str | None = None
    CourseName: str | None = None
    CourseRenaissanceID: str | None = None
    CourseSourcedID: str | None = None
    DistrictIdentifier: float | None = None
    DistrictName: str | None = None
    DistrictRenaissanceID: str | None = None
    DistrictSourcedID: str | None = None
    EnrollmentStatus: str | None = None
    Gender: str | None = None
    GroupID: str | None = None
    GroupOrClassName: str | None = None
    HispanicOrLatino: str | None = None
    MultiRace: str | None = None
    RenaissanceClientID: int | None = None
    SchoolIdentifier: int | None = None
    SchoolName: str | None = None
    SchoolRenaissanceID: str | None = None
    SchoolSourcedID: str | None = None
    SchoolYear: str | None = None
    StudentEmail: float | None = None
    StudentFirstName: str | None = None
    StudentLastName: str | None = None
    StudentMiddleName: str | None = None
    StudentRenaissanceID: str | None = None
    TeacherEmail: str | None = None
    TeacherFirstName: str | None = None
    TeacherIdentifier: str | None = None
    TeacherLastName: str | None = None
    TeacherMiddleName: float | None = None
    TeacherRenaissanceID: str | None = None
    TeacherSourcedID: str | None = None
    TeacherUserID: str | None = None
    White: str | None = None
    AmericanIndianOrAlaskaNative: str | None = None
    NativeHawaiianOrOtherPacificIslander: str | None = None
    SchoolYearStartDate: str | None = None
    SchoolYearEndDate: str | None = None
    BirthDate: str | None = None

    CurrentGrade: int | str | None = None
    DistrictStateID: float | int | None = None
    SchoolStateID: float | int | None = None
    StudentIdentifier: int | float | None = None
    StudentSourcedID: int | float | None = None
    StudentStateID: float | str | None = None
    StudentUserID: int | float | None = None
    TeacherStateID: float | int | None = None


class AcceleratedReader(RenLearningCore):
    QuizNumber: float | None = None
    ContentLanguage: str | None = None
    ContentTitle: str | None = None
    Author: str | None = None
    FictionNonFiction: str | None = None
    InterestLevel: str | None = None
    BookLevel: float | None = None
    QuestionsPresented: float | None = None
    QuestionsCorrect: float | None = None
    PercentCorrect: float | None = None
    PointsPossible: float | None = None
    PointsEarned: float | None = None
    Passed: bool | None = None
    TWI: str | None = None
    BookRating: float | None = None
    QuizDeleted: int | None = None
    WordCount: float | None = None
    QuizType: str | None = None
    LexileLevel: float | None = None
    DateQuizCompleted: str | None = None
    DateQuizCompletedLocal: str | None = None

    AudioUsed: float | str | None = None
    LexileMeasure: str | int | None = None


class STAR(RenLearningCore):
    ACTBenchmarkCategory: float | None = None
    AssessmentID: str | None = None
    AssessmentNumber: int | None = None
    AssessmentStatus: str | None = None
    AssessmentType: str | None = None
    CurrentSGP: float | None = None
    DeactivationReason: float | None = None
    ExtraTime: str | None = None
    GradePlacement: float | None = None
    NormalCurveEquivalent: float | None = None
    OpenGrowthScore: float | None = None
    PercentileRank: int | None = None
    RaschScore: float | None = None
    SATBenchmarkCategory: float | None = None
    ScaledScore: int | None = None
    SchoolBenchmarkCategoryLevel: int | None = None
    SchoolBenchmarkProficient: str | None = None
    ScreeningPeriodWindowName: str | None = None
    StandardErrorOfMeasurement: float | None = None
    StateBenchmarkCategoryName: str | None = None
    StateBenchmarkProficient: str | None = None
    TakenAt: str | None = None
    TakenAtByIPAddress: float | None = None
    TeacherDisplayID: str | None = None
    TotalCorrect: float | None = None
    TotalPossible: float | None = None
    TotalTimeInSeconds: int | None = None
    UnifiedScore: int | None = None
    LaunchDate: str | None = None
    CompletedDate: str | None = None
    CompletedDateLocal: str | None = None
    PartnershipForAssessmentOfReadinessForCollegeAndCareers: float | None = None
    ScreeningWindowStartDate: str | None = None
    ScreeningWindowEndDate: str | None = None
    StateBenchmarkCategoryLevel: float | None = None
    StateBenchmarkMinScaledScore: float | None = None
    StateBenchmarkMaxScaledScore: float | None = None
    SmarterBalancedAssessmentConsortium: float | None = None
    StudentGrowthPercentileFallFall: float | None = None
    StudentGrowthPercentileFallSpring: float | None = None
    StudentGrowthPercentileFallWinter: float | None = None
    StudentGrowthPercentileSpringFall: float | None = None
    StudentGrowthPercentileSpringSpring: float | None = None
    StudentGrowthPercentileWinterSpring: float | None = None
    RenaissanceBenchmarkCategoryName: str | None = None
    RenaissanceBenchmarkCategoryLevel: float | None = None
    RenaissanceBenchmarkCategoryMinPercentileRank: float | None = None
    RenaissanceBenchmarkCategoryMaxPercentileRank: float | None = None
    StateBenchmarkAssessmentName: str | None = None
    StateBenchmarkNumberOfCategoryLevels: float | None = None
    DistrictBenchmarkCategoryName: str | None = None
    DistrictBenchmarkProficient: str | None = None
    DistrictBenchmarkCategoryLevel: int | None = None
    DistrictBenchmarkNumberOfCategoryLevels: int | None = None
    DistrictBenchmarkMinPercentileRank: int | None = None
    DistrictBenchmarkMaxPercentileRank: int | None = None
    SchoolBenchmarkCategoryName: str | None = None
    SchoolBenchmarkNumberOfCategoryLevels: int | None = None
    SchoolBenchmarkMinPercentileRank: int | None = None
    SchoolBenchmarkMaxPercentileRank: int | None = None
    # Math
    Quantile: str | None = None
    # Reading
    InstructionalReadingLevel: str | None = None
    Lexile: str | None = None
    Grade3_AssessmentAttempts: int | None = None
    Grade3_PassingStatus: float | None = None
    Grade3_PassingScore: float | None = None
    EstimatedOralReadingFluency: float | None = None
    LowerZoneOfProximalDevelopment: float | None = None
    UpperZoneOfProximalDevelopment: float | None = None
    LowerLexileZoneOfProximalDevelopment: float | None = None
    UpperLexileZoneOfProximalDevelopment: float | None = None
    # early literacy
    LiteracyClassification: str | None = None
    LexileRange: str | None = None

    Grade: int | str | None = None
    GradeEquivalent: float | str | None
    StudentDisplayID: int | float | None
    RenaissanceBenchmarkCategoryNumberOfLevels: int | float | None = None
    Audio: float | str | None = None


class StarDashboardStandard(BaseModel):
    AssessmentID: str | None = None
    CompletedDate: str | None = None
    CompletedDateLocal: str | None = None
    DomainConfidenceLevel: float | None = None
    DomainGroup: str | None = None
    DomainMasteryLevel: float | None = None
    DomainName: str | None = None
    DomainPercentMastery: float | None = None
    LaunchDate: str | None = None
    RenaissanceClientID: int | None = None
    SchoolYear: str | None = None
    StandardConfidenceLevel: str | None = None
    StandardDescription: str | None = None
    StandardMasteryLevel: str | None = None
    StandardName: str | None = None
    StandardPercentMastery: int | None = None
    StudentIdentifier: int | None = None
    StudentRenaissanceID: str | None = None
    StudentSourcedID: int | None = None
    StudentStateID: str | None = None
    StudentUserID: int | None = None


class StarSkillArea(BaseModel):
    AssessmentID: str | None = None
    CompletedDate: str | None = None
    CompletedDateLocal: str | None = None
    DomainName: str | None = None
    DomainScore: int | None = None
    FamilyName: str | None = None
    LaunchDate: str | None = None
    RenaissanceClientID: int | None = None
    SchoolYear: str | None = None
    SkillAreaName: str | None = None
    StudentIdentifier: int | None = None
    StudentRenaissanceID: str | None = None
    StudentSourcedID: int | None = None
    StudentStateID: str | None = None
    StudentUserID: int | None = None
    SkillAreaMasteryScore: int | None = None


class FastStarCore(BaseModel):
    AchievementLevel: str | None = None
    AssessmentName: str | None = None
    FAST_Equivalent_Score: int | None = None
    FAST_ES_Max: float | None = None
    FAST_ES_Min: float | None = None
    FAST_NOL: float | None = None
    FileDate: str | None = None
    Level3_or_Above: str | None = None
    SchoolType: str | None = None
    Assess_Num: int | None = None
    Assess_Status: str | None = None
    CBTFlag: str | None = None
    CID: str | None = None
    ClassCode: str | None = None
    ClientID: int | None = None
    Cname: str | None = None
    CompletedDate: str | None = None
    CompletedDateLocal: str | None = None
    CurrentSGP: float | None = None
    DBM_Level: int | None = None
    DBMC_NOL: int | None = None
    DBMC_PR_Max: int | None = None
    DBMC_PR_Min: int | None = None
    DBMC: str | None = None
    DBMP: str | None = None
    DIS: int | None = None
    DisName: str | None = None
    DOB: int | None = None
    Email_S: str | None = None
    Email_T: str | None = None
    Enrolled: str | None = None
    EstORF: float | None = None
    EthHisp: str | None = None
    Exempted_Absence: str | None = None
    Exempted_FailedPrac: str | None = None
    Exempted_NonEngSpeaker: str | None = None
    Exempted_WrongTest: str | None = None
    ExtraTime: str | None = None
    FirstName_T: str | None = None
    FirstName: str | None = None
    FLEID: str | None = None
    Gender: str | None = None
    GID_RID: str | None = None
    Gname: str | None = None
    Grade_P: float | None = None
    Grade_T: str | None = None
    GUID: str | None = None
    LastName_T: str | None = None
    LastName: str | None = None
    LaunchDate: str | None = None
    MI_T: str | None = None
    MI: str | None = None
    MultiRace: str | None = None
    NCE: float | None = None
    PaperAccommodations: str | None = None
    PNP_Answer_Eliminator: str | None = None
    PNP_Audio_Options: str | None = None
    PNP_Calculator: str | None = None
    PNP_Color_Scheme: str | None = None
    PNP_Contrast_Overlay: str | None = None
    PNP_Enlarge_Text: str | None = None
    PNP_Highlighter: str | None = None
    PNP_Line_Reader: str | None = None
    PNP_Other_Assistive_Technology: str | None = None
    PNP_Screen_Reader: str | None = None
    PNP_Unlimited_Time: str | None = None
    PR: int | None = None
    RaceA: str | None = None
    RaceB: str | None = None
    RaceI: str | None = None
    RaceP: str | None = None
    RaceW: str | None = None
    RBM_Level: int | None = None
    RBMC_NOL: int | None = None
    RBMC_PR_Max: int | None = None
    RBMC_PR_Min: int | None = None
    RBMC: str | None = None
    Reported: str | None = None
    SBM_Level: int | None = None
    SBM: str | None = None
    SBMC_NOL: int | None = None
    SBMC_SS_Max: int | None = None
    SBMC_SS_Min: int | None = None
    SBMC: str | None = None
    SBMP: str | None = None
    SCH: int | None = None
    SchBM_Level: int | None = None
    SchBMC_NOL: int | None = None
    SchBMC_PR_Max: int | None = None
    SchBMC_PR_Min: int | None = None
    SchBMC: str | None = None
    SchBMP: str | None = None
    SchName: str | None = None
    SchoolYear_ED: str | None = None
    SchoolYear_SD: str | None = None
    SchoolYear: str | None = None
    SEM: float | None = None
    SGP_FF: float | None = None
    SGP_FS: float | None = None
    SGP_FW: float | None = None
    SGP_SF: float | None = None
    SGP_SS: float | None = None
    SGP_WS: float | None = None
    Sgrade: str | None = None
    SID_SID: int | None = None
    SW_ED: str | None = None
    SW_Name: str | None = None
    SW_SD: str | None = None
    TestingIP: str | None = None
    TestingSite: str | None = None
    TestName: str | None = None
    TID_RID: str | None = None
    TID: int | None = None
    TotalCorrect: float | None = None
    TotalPossible: float | None = None
    TotalTime: int | None = None
    UnifiedScore: int | None = None

    Grade_E: float | str | None = None


class FastStar(FastStarCore):
    # Math
    Quantile: str | None = None
    # Reading
    IRL: str | None = None
    Lexile: str | None = None
    PassingScore_G3: str | None = None
    PassingStatus_G3: str | None = None
    ZPD_Lexile_Lower: float | None = None
    ZPD_Lexile_Upper: float | None = None
    ZPD_Lower: float | None = None
    ZPD_Upper: float | None = None
    # Early Literacy
    LexileRange: str | None = None
    LitClassification: str | None = None
    # Early Literacy - Domains
    SubDomain_AP: int | None = None
    SubDomain_AP_SkillSet_A: int | None = None
    SubDomain_AP_SkillSet_B: int | None = None
    SubDomain_AP_SkillSet_C: int | None = None
    SubDomain_CW: int | None = None
    SubDomain_CW_SkillSet_A: int | None = None
    SubDomain_CW_SkillSet_B: int | None = None
    SubDomain_CW_SkillSet_C: int | None = None
    SubDomain_CW_SkillSet_D: int | None = None
    SubDomain_EN: int | None = None
    SubDomain_EN_SkillSet_A: int | None = None
    SubDomain_EN_SkillSet_B: int | None = None
    SubDomain_EN_SkillSet_C: int | None = None
    SubDomain_EN_SkillSet_D: int | None = None
    SubDomain_EN_SkillSet_E: int | None = None
    SubDomain_PA: int | None = None
    SubDomain_PA_SkillSet_A: int | None = None
    SubDomain_PA_SkillSet_B: int | None = None
    SubDomain_PA_SkillSet_C: int | None = None
    SubDomain_PA_SkillSet_D: int | None = None
    SubDomain_PA_SkillSet_E: int | None = None
    SubDomain_PA_SkillSet_F: int | None = None
    SubDomain_PA_SkillSet_G: int | None = None
    SubDomain_PA_SkillSet_H: int | None = None
    SubDomain_PC: int | None = None
    SubDomain_PC_SkillSet_A: int | None = None
    SubDomain_PH: int | None = None
    SubDomain_PH_SkillSet_A: int | None = None
    SubDomain_PH_SkillSet_B: int | None = None
    SubDomain_PH_SkillSet_C: int | None = None
    SubDomain_PH_SkillSet_D: int | None = None
    SubDomain_PH_SkillSet_E: int | None = None
    SubDomain_PH_SkillSet_F: int | None = None
    SubDomain_PH_SkillSet_G: int | None = None
    SubDomain_PH_SkillSet_H: int | None = None
    SubDomain_PH_SkillSet_I: int | None = None
    SubDomain_PH_SkillSet_J: int | None = None
    SubDomain_PH_SkillSet_K: int | None = None
    SubDomain_PH_SkillSet_L: int | None = None
    SubDomain_SA: int | None = None
    SubDomain_SA_SkillSet_A: int | None = None
    SubDomain_SA_SkillSet_B: int | None = None
    SubDomain_SA_SkillSet_C: int | None = None
    SubDomain_SA_SkillSet_D: int | None = None
    SubDomain_SC: int | None = None
    SubDomain_SC_SkillSet_A: int | None = None
    SubDomain_VO: int | None = None
    SubDomain_VO_SkillSet_A: int | None = None
    SubDomain_VO_SkillSet_B: int | None = None
    SubDomain_VO_SkillSet_C: int | None = None
    SubDomain_VS: int | None = None
    SubDomain_VS_SkillSet_A: int | None = None
    SubDomain_VS_SkillSet_B: int | None = None

    Attempts_G3: str | int | None = None


"""
helper classes for backwards compatibility
"""


class accelerated_reader_record(AcceleratedReader): ...


class fast_star_record(FastStar): ...


class star_dashboard_standards_record(StarDashboardStandard): ...


class star_record(STAR): ...


class star_skill_area_record(StarSkillArea): ...


ASSET_SCHEMA = {
    "accelerated_reader": json.loads(
        py_avro_schema.generate(
            py_type=accelerated_reader_record, namespace="accelerated_reader"
        )
    ),
    "fast_star": json.loads(
        py_avro_schema.generate(py_type=fast_star_record, namespace="fast_star")
    ),
    "star_dashboard_standards": json.loads(
        py_avro_schema.generate(
            py_type=star_dashboard_standards_record,
            namespace="star_dashboard_standards",
        )
    ),
    "star": json.loads(py_avro_schema.generate(py_type=star_record, namespace="star")),
    "star_skill_area": json.loads(
        py_avro_schema.generate(
            py_type=star_skill_area_record, namespace="star_skill_area"
        )
    ),
}
