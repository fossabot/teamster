select
    _id as user_id,
    `name`,
    district,
    created,
    lastmodified,
    archivedat,
    accountingid,
    calendaremail,
    canvasid,
    cleverid,
    coach,
    email,
    endofyearvisible,
    evaluator,
    `first`,
    googleid,
    inactive,
    ispracticeuser,
    `last`,
    locked,
    noninstructional,
    oktaid,
    powerschoolid,
    `readonly`,
    showondashboards,
    sibmeid,
    sibmetoken,
    track,
    usertag1,
    usertag2,
    usertag3,
    usertag4,
    usertag5,
    usertag6,
    usertag7,
    usertag8,
    videolicense,
    lastactivity,
    safe_cast(internalid as int) as internalid,
    defaultinformation.course as defaultinformation_course,
    defaultinformation.gradelevel as defaultinformation_gradelevel,
    defaultinformation.period as defaultinformation_period,
    defaultinformation.school as defaultinformation_school,
    preferences.actionsdashtimeframe as preferences_actionsdashtimeframe,
    preferences.homepage as preferences_homepage,
    preferences.lastschoolselected as preferences_lastschoolselected,
    preferences.showactionstepmessage as preferences_showactionstepmessage,
    preferences.showdcpsmessage as preferences_showdcpsmessage,
    preferences.showsystemwidemessage as preferences_showsystemwidemessage,
    preferences.showtutorial as preferences_showtutorial,
    preferences.timezone as preferences_timezone,
    preferences.timezonetext as preferences_timezonetext,
    preferences.obspage.panelwidth as preferences_obspage_panelwidth,
    usertype.__v as usertype__v,
    usertype._id as usertype_id,
    usertype.abbreviation as usertype_abbreviation,
    usertype.archivedat as usertype_archivedat,
    usertype.creator as usertype_creator,
    usertype.district as usertype_district,
    usertype.name as usertype_name,
    usertype.created as usertype_created,
    usertype.lastmodified as usertype_lastmodified,
    usertype.expectations.meeting as usertype_expectations_meeting,
    usertype.expectations.exceeding as usertype_expectations_exceeding,
    usertype.expectations.meetingaggregate as usertype_expectations_meetingaggregate,
    usertype.expectations.exceedingaggregate
    as usertype_expectations_exceedingaggregate,
    usertype.expectations.summary as usertype_expectations_summary,
    pluconfig.required as pluconfig_required,
    pluconfig.startdate as pluconfig_startdate,
    pluconfig.enddate as pluconfig_enddate,
    districts,
    additionalemails,
    endofyearlog,
    pastusertypes,
    roles,
    regionaladminschools,
    externalintegrations,
    districtdata,
    preferences.unsubscribedto as preferences_unsubscribedto,
    preferences.navbar.shortcuts as preferences_navbar_shortcuts,
    preferences.admindashboard.`hidden` as preferences_admindashboard_hidden,
    preferences.obspage.collapsedpanes as preferences_obspage_collapsedpanes,
from {{ source("schoolmint_grow", "src_schoolmint_grow__users") }}
where _dagster_partition_key = 'f'