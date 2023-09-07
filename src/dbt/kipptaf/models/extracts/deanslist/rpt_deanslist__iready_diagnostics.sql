SELECT
    'Test Rounds' AS DOMAIN,
    LEFT(IR.ACADEMIC_YEAR, 4) AS ACADEMIC_YEAR,
    IR.STUDENT_ID AS STUDENT_NUMBER,
    IR.SUBJECT,
    CAST(IR.COMPLETION_DATE AS DATE) AS COMPLETION_DATE,
    IR.TEST_ROUND,
    IR.TEST_ROUND_DATE,
    IR.PERCENTILE,
    IR.OVERALL_SCALE_SCORE,
    IR.PERCENT_PROGRESS_TO_ANNUAL_TYPICAL_GROWTH AS PCT_PROGRESS_TYPICAL,
    IR.PERCENT_PROGRESS_TO_ANNUAL_STRETCH_GROWTH AS PCT_PROGRESS_STRETCH
FROM
    {{ ref('base_iready__diagnostic_results') }} AS IR
WHERE
    IR.RN_SUBJ_ROUND = 1
    AND IR.TEST_ROUND != 'Outside Round'
UNION ALL
SELECT
    'YTD Growth' AS DOMAIN,
    LEFT(IR.ACADEMIC_YEAR, 4) AS ACADEMIC_YEAR,
    IR.STUDENT_ID AS STUDENT_NUMBER,
    IR.SUBJECT,
    CAST(IR.COMPLETION_DATE AS DATE) AS COMPLETION_DATE,
    IR.TEST_ROUND,
    IR.TEST_ROUND_DATE,
    IR.PERCENTILE,
    IR.OVERALL_SCALE_SCORE,
    IR.PERCENT_PROGRESS_TO_ANNUAL_TYPICAL_GROWTH AS PCT_PROGRESS_TYPICAL,
    IR.PERCENT_PROGRESS_TO_ANNUAL_STRETCH_GROWTH AS PCT_PROGRESS_STRETCH
FROM
    {{ ref('base_iready__diagnostic_results') }} AS IR
INNER JOIN (
    SELECT
        ACADEMIC_YEAR,
        SUBJECT,
        STUDENT_ID,
        MAX(COMPLETION_DATE) AS MAX_COMPLETION_DATE
    FROM
        {{ ref('base_iready__diagnostic_results') }}
    GROUP BY
        ACADEMIC_YEAR,
        SUBJECT,
        STUDENT_ID
) AS SUB
    ON
        IR.ACADEMIC_YEAR = SUB.ACADEMIC_YEAR
        AND IR.STUDENT_ID = SUB.STUDENT_ID
        AND IR.SUBJECT = SUB.SUBJECT
        AND IR.COMPLETION_DATE = SUB.MAX_COMPLETION_DATE
WHERE
    CAST(LEFT(IR.ACADEMIC_YEAR, 4) AS INT)
    = {{ var("current_academic_year") }}
