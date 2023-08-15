select
    id as `id`,
    name as `name`,

    contact__c as `contact`,
    date__c as `date`,
    test_type__c as `test_type`,
    source__c as `source`,
    subject__c as `subject`,
    test_location__c as `test_location`,

    act_composite__c as `act_composite`,
    act_ela__c as `act_ela`,
    act_english__c as `act_english`,
    act_math__c as `act_math`,
    act_reading__c as `act_reading`,
    act_science__c as `act_science`,
    act_stem__c as `act_stem`,
    act_writing__c as `act_writing`,

    sat_total_score__c as `sat_total_score`,
    sat_ebrw__c as `sat_ebrw`,
    sat_essay_analysis__c as `sat_essay_analysis`,
    sat_essay_reading__c as `sat_essay_reading`,
    sat_essay_writing__c as `sat_essay_writing`,
    sat_math__c as `sat_math`,
    sat_math_test_score__c as `sat_math_test_score`,
    sat_reading_test_score__c as `sat_reading_test_score`,
    sat_verbal__c as `sat_verbal`,
    sat_writing__c as `sat_writing`,
    sat_critical_reading_pre_2016__c as `sat_critical_reading_pre_2016`,
    sat_math_pre_2016__c as `sat_math_pre_2016`,
    sat_writing_and_language_test_score__c as `sat_writing_and_language_test_score`,
    sat_writing_pre_2016__c as `sat_writing_pre_2016`,

    ssat_overall_percentile__c as `ssat_overall_percentile`,
    ssat_math__c as `ssat_math`,
    ssat_math_percentile__c as `ssat_math_percentile`,
    ssat_reading_comp__c as `ssat_reading_comp`,
    ssat_reading_comp_percentile__c as `ssat_reading_comp_percentile`,
    ssat_verbal__c as `ssat_verbal`,
    ssat_verbal_percentile__c as `ssat_verbal_percentile`,

    ap__c as `ap`,

    ib_course_grade__c as `ib_course_grade`,

    psat_total_score__c as `psat_total_score`,
    psat_ebrw__c as `psat_ebrw`,
    psat_math__c as `psat_math`,
    psat_math_test_score__c as `psat_math_test_score`,
    psat_reading_test_score__c as `psat_reading_test_score`,
    psat_verbal__c as `psat_verbal`,
    psat_writing__c as `psat_writing`,
    psat_writing_and_language_test_score__c as `psat_writing_and_language_test_score`,
    psat_critical_reading_pre_2016__c as `psat_critical_reading_pre_2016`,
    psat_math_pre_2016__c as `psat_math_pre_2016`,
    psat_writing_pre_2016__c as `psat_writing_pre_2016`,

    arithmetic_reasoning_ar__c as `arithmetic_reasoning_ar`,
    assembling_objects_ao__c as `assembling_objects_ao`,
    auto_and_shop_information_as__c as `auto_and_shop_information_as`,
    clerical_cl__c as `clerical_cl`,
    combat_co__c as `combat_co`,
    electronics_el__c as `electronics_el`,
    electronics_information_ei__c as `electronics_information_ei`,
    field_artillery_fa__c as `field_artillery_fa`,
    general_maintenance_gm__c as `general_maintenance_gm`,
    general_science_gs__c as `general_science_gs`,
    general_technical_gt__c as `general_technical_gt`,
    mathematics_knowledge_mk__c as `mathematics_knowledge_mk`,
    mechanical_comprehension_mc__c as `mechanical_comprehension_mc`,
    mechanical_maintenance_mm__c as `mechanical_maintenance_mm`,
    operators_and_food_of__c as `operators_and_food_of`,
    paragraph_comprehension_pc__c as `paragraph_comprehension_pc`,
    skilled_technical_st__c as `skilled_technical_st`,
    surveillance_and_communications_sc__c as `surveillance_and_communications_sc`,
    word_knowledge_wk__c as `word_knowledge_wk`,
    school_ability_index_sai__c as `school_ability_index_sai`,
    corrected_age_ca_months__c as `corrected_age_ca_months`,
    corrected_age_ca_years__c as `corrected_age_ca_years`,
    physical_training_requirement_passed__c as `physical_training_requirement_passed`,
    asvab_minimum_score_requirement__c as `asvab_minimum_score_requirement`,
    raw_score_rs__c as `raw_score_rs`,
    raw_score_rs_denominator__c as `raw_score_rs_denominator`,
    raw_score_rs_numerator__c as `raw_score_rs_numerator`,
    scaled_score_ss__c as `scaled_score_ss`,
    qualified_air_force__c as `qualified_air_force`,
    qualified_army__c as `qualified_army`,
    qualified_coast_guard__c as `qualified_coast_guard`,
    qualified_marine_corps__c as `qualified_marine_corps`,
    qualified_navy__c as `qualified_navy`,
    total_qualified_military_branches__c as `total_qualified_military_branches`,

    afqt_score__c as `afqt_score`,

    bcpss_magnet__c as `bcpss_magnet`,
    bcpss_poly__c as `bcpss_poly`,

    csq__c as `csq`,

    dc_cas_math__c as `dc_cas_math`,
    dc_cas_reading__c as `dc_cas_reading`,

    estimated_act_high__c as `estimated_act_high`,
    estimated_act_low__c as `estimated_act_low`,

    explore_composite__c as `explore_composite`,
    explore_english__c as `explore_english`,
    explore_est_plan_high__c as `explore_est_plan_high`,
    explore_est_plan_low__c as `explore_est_plan_low`,
    explore_math__c as `explore_math`,
    explore_reading__c as `explore_reading`,
    explore_science__c as `explore_science`,

    ged_language_arts_reading__c as `ged_language_arts_reading`,
    ged_language_arts_writing__c as `ged_language_arts_writing`,
    ged_mathematics__c as `ged_mathematics`,
    ged_science__c as `ged_science`,
    ged_social_studies__c as `ged_social_studies`,
    ged_total_score__c as `ged_total_score`,

    hspt_language__c as `hspt_language`,
    hspt_math__c as `hspt_math`,
    hspt_quantitative__c as `hspt_quantitative`,
    hspt_reading__c as `hspt_reading`,
    hspt_vb__c as `hspt_vb`,
    hspt_verbal__c as `hspt_verbal`,

    isee_mathematics_achievement_stanine__c as `isee_mathematics_achievement_stanine`,
    isee_percentile__c as `isee_percentile`,
    isee_quantitative_reasoning_stanine__c as `isee_quantitative_reasoning_stanine`,
    isee_reading_comprehension_stanine__c as `isee_reading_comprehension_stanine`,
    isee_verbal_reasoning_stanine__c as `isee_verbal_reasoning_stanine`,

    nwea_percentile__c as `nwea_percentile`,

    nyc_level__c as `nyc_level`,

    plan_composite__c as `plan_composite`,
    plan_english__c as `plan_english`,
    plan_geometry__c as `plan_geometry`,
    plan_math__c as `plan_math`,
    plan_pre_alg_algebra__c as `plan_pre_alg_algebra`,
    plan_reading__c as `plan_reading`,
    plan_rhetorical_skills__c as `plan_rhetorical_skills`,
    plan_science__c as `plan_science`,
    plan_usage_mechanics__c as `plan_usage_mechanics`,

    grade_level__c as `grade_level`,
    overall_score__c as `overall_score`,
    scoring_irregularity__c as `scoring_irregularity`,
    standardized_test_count__c as `standardized_test_count`,

    stanford_language_nce__c as `stanford_language_nce`,
    stanford_language_pr__c as `stanford_language_pr`,
    stanford_language_stanine__c as `stanford_language_stanine`,
    stanford_math_nce__c as `stanford_math_nce`,
    stanford_math_pr__c as `stanford_math_pr`,
    stanford_math_stanine__c as `stanford_math_stanine`,
    stanford_overall_nce__c as `stanford_overall_nce`,
    stanford_reading_nce__c as `stanford_reading_nce`,
    stanford_reading_pr__c as `stanford_reading_pr`,
    stanford_reading_s__c as `stanford_reading_s`,

    recordtypeid as `record_type_id`,
    createdbyid as `created_by_id`,
    createddate as `created_date`,
    lastactivitydate as `last_activity_date`,
    lastmodifiedbyid as `last_modified_by_id`,
    lastmodifieddate as `last_modified_date`,
    lastreferenceddate as `last_referenced_date`,
    lastvieweddate as `last_viewed_date`,
    systemmodstamp as `system_modstamp`,
from {{ source("kippadb", "standardized_test") }}
where not isdeleted