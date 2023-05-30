import json
import random

import pendulum
from dagster import EnvVar, build_resources
from fastavro import parse_schema, validation, writer

from teamster.core.alchemer.resources import AlchemerResource
from teamster.core.alchemer.schema import ASSET_FIELDS
from teamster.core.utils.functions import get_avro_record_schema

TEST_SURVEY_ID = 6734664
FILTER_SURVEY_IDS = []
PASSED_SURVEY_IDS = [
    # 2934233,
    # 3108476,
    # 3167842,
    # 3167903,
    # 3211265,
    # 3242248,
    # 3370039,
    # 3511436,
    # 3727563,
    # 3767678,
    # 3774202,
    # 3779180,
    # 3779180,
    # 3779230,
    # 3946606,
    # 4000821,
    # 4031194,
    # 4160102,
    # 4251844,
    # 4561288,
    # 4561325,
    # 4839791,
    # 4843086,
    # 4859726,
    # 5300913,
    # 5351760,
    # 5560557,
    # 5593585,
    # 6330385,
    # 6580731,
    # 6686058,
    # 6734664,
    # 6829997,
    # 6997086,
    # 7151740,
    # 7196293,
    # 7253288,
    # 7257383,
    # 7257415,
    7257431,
]


def check_schema(records, endpoint_name, key=None):
    print(f"\n{endpoint_name}")

    print("\tSAVING TO FILE...")
    with open(file=f"env/{endpoint_name.replace('/', '_')}.json", mode="w") as fp:
        json.dump(obj=records, fp=fp)
    print("\t\tPASS")

    schema = get_avro_record_schema(
        name=endpoint_name, fields=ASSET_FIELDS[endpoint_name]
    )
    # print(schema)

    print("\tPARSING SCHEMA...")
    parsed_schema = parse_schema(schema=schema)
    print("\t\tPASS")

    len_records = len(records)
    if key is not None:
        sample_record = [r for r in records if "" in json.dumps(obj=r)]
    elif len_records == 0:
        print("\tNO DATA")
        return
    else:
        sample_record = records[random.randint(a=0, b=(len_records - 1))]
    # print(f"\tSAMPLE RECORD:\n{sample_record}")

    print("\tVALIDATING SINGLE RECORD...")
    assert validation.validate(datum=sample_record, schema=parsed_schema, strict=True)
    print("\t\tPASS")

    print("\tVALIDATING ALL RECORDS...")
    assert validation.validate_many(records=records, schema=parsed_schema, strict=True)
    print("\t\tPASS")

    print("\tWRITING ALL RECORDS...")
    with open(file="/dev/null", mode="wb") as fo:
        writer(
            fo=fo,
            schema=parsed_schema,
            records=records,
            codec="snappy",
            strict_allow_default=True,
        )
    print("\t\tPASS")


def test_schema():
    with build_resources(
        resources={
            "alchemer": AlchemerResource(
                api_token=EnvVar("ALCHEMER_API_TOKEN"),
                api_token_secret=EnvVar("ALCHEMER_API_TOKEN_SECRET"),
                api_version="v5",
            )
        }
    ) as resources:
        alchemer: AlchemerResource = resources.alchemer

        all_surveys = alchemer._client.survey.list()

        test_survey_id = None
        for test_survey in all_surveys:
            if TEST_SURVEY_ID is not None:
                test_survey_id = TEST_SURVEY_ID
                break
            elif int(test_survey["id"]) in PASSED_SURVEY_IDS:
                print(f"PASSED: {test_survey['title']}")
            else:
                test_survey_id = test_survey["id"]
                break

        if test_survey_id is None:
            print("ALL SURVEYS PASSED")
            return

        survey = alchemer._client.survey.get(id=test_survey_id)
        print(f"\nSURVEY: {survey.title}")
        print(f"ID: {survey.id}")

        check_schema(records=[survey.data], endpoint_name="survey")

        check_schema(records=survey.question.list(), endpoint_name="survey_question")

        check_schema(records=survey.campaign.list(), endpoint_name="survey_campaign")

        if int(survey.id) in FILTER_SURVEY_IDS:
            start_date = pendulum.now(tz="US/Eastern").subtract(days=1)

            survey_response = survey.response.filter(
                "date_submitted", ">=", start_date.to_datetime_string()
            ).list(params={"resultsperpage": 500})
        else:
            survey_response = survey.response.list()

        check_schema(records=survey_response, endpoint_name="survey_response")
