import json
from typing import Union

import py_avro_schema
from pydantic import BaseModel


class URLVariable(BaseModel):
    key: str | None = None
    type: str | None = None
    value: str | None = None


class OpenText(BaseModel):
    onewordrequiredessay: dict[str, int | None] | None = None
    gibberish: list[str | None] | dict[str, int | None] | None = []


class DataQuality(BaseModel):
    opentext: OpenText | None = None


class Team(BaseModel):
    id: str | None = None
    name: str | None = None


class Statistics(BaseModel):
    Partial: int | None = None
    Disqualified: int | None = None
    Deleted: int | None = None
    Complete: int | None = None
    TestData: str | None = None


class PageProperties(BaseModel):
    hidden: bool | None = None
    piped_from: str | None = None


class Messages(BaseModel):
    center_label: list[str | None] | dict[str, str | None] | None = []
    configurator_button_text: list[str | None] | dict[str, str | None] | None = []
    configurator_complete: list[str | None] | dict[str, str | None] | None = []
    configurator_error: list[str | None] | dict[str, str | None] | None = []
    conjoint_best_label: list[str | None] | dict[str, str | None] | None = []
    conjoint_card_label: list[str | None] | dict[str, str | None] | None = []
    conjoint_error_label: list[str | None] | dict[str, str | None] | None = []
    conjoint_none_label: list[str | None] | dict[str, str | None] | None = []
    conjoint_worst_label: list[str | None] | dict[str, str | None] | None = []
    inputmask: list[str | None] | dict[str, str | None] | None = []
    l_extreme_label: list[str | None] | dict[str, str | None] | None = []
    left_label: list[str | None] | dict[str, str | None] | None = []
    maxdiff_attribute_label: list[str | None] | dict[str, str | None] | None = []
    maxdiff_best_label: list[str | None] | dict[str, str | None] | None = []
    maxdiff_of: list[str | None] | dict[str, str | None] | None = []
    maxdiff_sets_message: list[str | None] | dict[str, str | None] | None = []
    maxdiff_worst_label: list[str | None] | dict[str, str | None] | None = []
    na_text: list[str | None] | dict[str, str | None] | None = []
    payment_button_text: list[str | None] | dict[str, str | None] | None = []
    r_extreme_label: list[str | None] | dict[str, str | None] | None = []
    right_label: list[str | None] | dict[str, str | None] | None = []
    th_content: list[str | None] | dict[str, str | None] | None = []

    # payment_description: list[str | None] | dict[str, str | None] | None = Field(
    #     default=[], alias="payment-description"
    # )
    # payment_summary: list[str | None] | dict[str, str | None] | None = Field(
    #     default=[], alias="payment-summary"
    # )


class Atom(BaseModel):
    type: str | None = None
    value: str | None = None


class Atom2(BaseModel):
    type: str | None = None

    value: str | list[str | None] | None = []


class ShowRules(BaseModel):
    id: str | None = None
    operator: str | None = None

    atom: Atom | None = None
    atom2: Atom2 | None = None

    same_page_skus: list[str | None] | None = []


class QuestionProperties(BaseModel):
    break_after: bool | None = None
    custom_css: str | None = None
    disabled: bool | None = None
    exclude_number: str | None = None
    hidden: bool | None = None
    hide_after_response: bool | None = None
    labels_right: bool | None = None
    map_key: str | None = None
    option_sort: str | None = None
    orientation: str | None = None
    question_description_above: bool | None = None
    required: bool | None = None
    show_title: bool | None = None
    soft_required: bool | None = None
    subtype: str | None = None
    url: str | None = None
    # soft-required: bool | None = None

    messages: Messages | None = None
    show_rules: ShowRules | None = None

    defaulttext: dict[str, str | None] | None = None
    question_description: dict[str, str | None] | None = None

    inputmask: list[str | None] | dict[str, str | None] | None = []


class OptionProperties(BaseModel):
    disabled: bool | None = None
    piping_exclude: str | None = None
    # show_rules_logic_map: None = None

    show_rules: ShowRules | None = None


class SurveyOption(BaseModel):
    id: int | None = None
    value: str | None = None

    properties: OptionProperties | None = None

    title: dict[str, str | int | None] | None = None


class Answer(BaseModel):
    signature: str | None = None
    name: str | None = None


class SurveyData(BaseModel):
    answer_id: int | str | None = None
    id: int | None = None
    original_answer: str | None = None
    parent: int | None = None
    question: str | None = None
    section_id: int | None = None
    shown: bool | None = None
    type: str | None = None

    answer: str | Answer | None = None

    subquestions: (
        dict[str, Union["SurveyData", dict[str, "SurveyData"], None]] | None
    ) = None


class SurveyQuestion(BaseModel):
    base_type: str | None = None
    comment: bool | None = None
    has_showhide_deps: bool | None = None
    id: int | None = None
    shortname: str | None = None
    type: str | None = None

    properties: QuestionProperties | None = None

    description: list[str | None] | None = []
    options: list[SurveyOption | None] | None = None
    sub_questions: list["SurveyQuestion"] | None = None

    title: dict[str, str | None] | None = None

    varname: list[str | None] | dict[str, str | None] | None = []


class SurveyPage(BaseModel):
    id: int | None = None

    title: list[str | None] | dict[str, str | None] | None = []
    description: list[str | None] | dict[str, str | None] | None = []

    properties: list[str | None] | PageProperties | None = []
    questions: list[SurveyQuestion | None] | None = None


class SurveyCampaign(BaseModel):
    close_message: str | None = None
    date_created: str | None = None
    date_modified: str | None = None
    id: str | None = None
    invite_id: str | None = None
    language: str | None = None
    limit_responses: str | None = None
    link_close_date: str | None = None
    link_open_date: str | None = None
    link_type: str | None = None
    name: str | None = None
    primary_theme_content: str | None = None
    primary_theme_options: str | None = None
    SSL: str | None = None
    status: str | None = None
    subtype: str | None = None
    token_variables: str | None = None
    type: str | None = None
    uri: str | None = None


class SurveyResponse(BaseModel):
    city: str | None = None
    comments: str | None = None
    contact_id: str | None = None
    country: str | None = None
    date_started: str | None = None
    date_submitted: str | None = None
    dma: str | None = None
    id: str | None = None
    ip_address: str | None = None
    is_test_data: str | None = None
    language: str | None = None
    latitude: str | None = None
    link_id: str | None = None
    longitude: str | None = None
    postal: str | None = None
    referer: str | None = None
    region: str | None = None
    response_time: int | None = None
    session_id: str | None = None
    status: str | None = None
    user_agent: str | None = None

    url_variables: list[str | None] | dict[str, str | URLVariable | None] | None = []
    data_quality: list[str | None] | DataQuality | None = []

    survey_data: list[str | None] | dict[str, SurveyData | None] | None = []


class Survey(BaseModel):
    auto_close: str | None = None
    blockby: str | None = None
    created_on: str | None = None
    forward_only: bool | None = None
    id: str | None = None
    internal_title: str | None = None
    modified_on: str | None = None
    overall_quota: str | None = None
    status: str | None = None
    theme: str | None = None
    title: str | None = None
    type: str | None = None

    statistics: Statistics | None = None

    languages: list[str | None] | None = None
    pages: list[SurveyPage | None] | None = None
    team: list[Team | None] | None = None

    links: dict[str, str | None] | None = None
    title_ml: dict[str, str | None] | None = None


class answer_record(Answer):
    """helper class for backwards compatibility"""


class survey_data_record(SurveyData):
    """helper class for backwards compatibility"""

    answer: str | answer_record | None = None
    subquestions: (
        dict[str, Union["survey_data_record", dict[str, "survey_data_record"], None]]
        | None
    ) = None


class survey_response_record(SurveyResponse):
    """helper class for backwards compatibility"""

    survey_data: list[str | None] | dict[str, survey_data_record | None] | None = []


SURVEY_SCHEMA = json.loads(py_avro_schema.generate(py_type=Survey, namespace="survey"))

SURVEY_CAMPAIGN_SCHEMA = json.loads(
    py_avro_schema.generate(py_type=SurveyCampaign, namespace="survey_campaign")
)

SURVEY_QUESTION_SCHEMA = json.loads(
    py_avro_schema.generate(py_type=SurveyQuestion, namespace="survey_question")
)

SURVEY_RESPONSE_DQ_SCHEMA = json.loads(
    py_avro_schema.generate(
        py_type=SurveyResponse, namespace="survey_response_disqualified"
    )
)

SURVEY_RESPONSE_SCHEMA = json.loads(
    py_avro_schema.generate(
        py_type=survey_response_record,
        options=py_avro_schema.Option.NO_DOC | py_avro_schema.Option.NO_AUTO_NAMESPACE,
    )
)
