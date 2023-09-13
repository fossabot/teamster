{{ config(materialized="view") }}

with
    union_relations as (
        {{
            dbt_utils.union_relations(
                relations=[
                    ref("stg_illuminate__repository_1"),
                    ref("stg_illuminate__repository_10"),
                    ref("stg_illuminate__repository_100"),
                    ref("stg_illuminate__repository_101"),
                    ref("stg_illuminate__repository_102"),
                    ref("stg_illuminate__repository_103"),
                    ref("stg_illuminate__repository_104"),
                    ref("stg_illuminate__repository_105"),
                    ref("stg_illuminate__repository_11"),
                    ref("stg_illuminate__repository_110"),
                    ref("stg_illuminate__repository_111"),
                    ref("stg_illuminate__repository_113"),
                    ref("stg_illuminate__repository_114"),
                    ref("stg_illuminate__repository_115"),
                    ref("stg_illuminate__repository_116"),
                    ref("stg_illuminate__repository_117"),
                    ref("stg_illuminate__repository_118"),
                    ref("stg_illuminate__repository_119"),
                    ref("stg_illuminate__repository_12"),
                    ref("stg_illuminate__repository_120"),
                    ref("stg_illuminate__repository_121"),
                    ref("stg_illuminate__repository_122"),
                    ref("stg_illuminate__repository_123"),
                    ref("stg_illuminate__repository_124"),
                    ref("stg_illuminate__repository_125"),
                    ref("stg_illuminate__repository_126"),
                    ref("stg_illuminate__repository_127"),
                    ref("stg_illuminate__repository_128"),
                    ref("stg_illuminate__repository_129"),
                    ref("stg_illuminate__repository_13"),
                    ref("stg_illuminate__repository_130"),
                    ref("stg_illuminate__repository_131"),
                    ref("stg_illuminate__repository_132"),
                    ref("stg_illuminate__repository_133"),
                    ref("stg_illuminate__repository_134"),
                    ref("stg_illuminate__repository_135"),
                    ref("stg_illuminate__repository_136"),
                    ref("stg_illuminate__repository_137"),
                    ref("stg_illuminate__repository_138"),
                    ref("stg_illuminate__repository_139"),
                    ref("stg_illuminate__repository_14"),
                    ref("stg_illuminate__repository_140"),
                    ref("stg_illuminate__repository_141"),
                    ref("stg_illuminate__repository_142"),
                    ref("stg_illuminate__repository_143"),
                    ref("stg_illuminate__repository_144"),
                    ref("stg_illuminate__repository_145"),
                    ref("stg_illuminate__repository_146"),
                    ref("stg_illuminate__repository_147"),
                    ref("stg_illuminate__repository_148"),
                    ref("stg_illuminate__repository_149"),
                    ref("stg_illuminate__repository_15"),
                    ref("stg_illuminate__repository_150"),
                    ref("stg_illuminate__repository_151"),
                    ref("stg_illuminate__repository_152"),
                    ref("stg_illuminate__repository_153"),
                    ref("stg_illuminate__repository_154"),
                    ref("stg_illuminate__repository_155"),
                    ref("stg_illuminate__repository_156"),
                    ref("stg_illuminate__repository_157"),
                    ref("stg_illuminate__repository_158"),
                    ref("stg_illuminate__repository_159"),
                    ref("stg_illuminate__repository_16"),
                    ref("stg_illuminate__repository_160"),
                    ref("stg_illuminate__repository_161"),
                    ref("stg_illuminate__repository_162"),
                    ref("stg_illuminate__repository_163"),
                    ref("stg_illuminate__repository_168"),
                    ref("stg_illuminate__repository_169"),
                    ref("stg_illuminate__repository_17"),
                    ref("stg_illuminate__repository_170"),
                    ref("stg_illuminate__repository_172"),
                    ref("stg_illuminate__repository_174"),
                    ref("stg_illuminate__repository_175"),
                    ref("stg_illuminate__repository_176"),
                    ref("stg_illuminate__repository_177"),
                    ref("stg_illuminate__repository_178"),
                    ref("stg_illuminate__repository_179"),
                    ref("stg_illuminate__repository_180"),
                    ref("stg_illuminate__repository_181"),
                    ref("stg_illuminate__repository_182"),
                    ref("stg_illuminate__repository_184"),
                    ref("stg_illuminate__repository_188"),
                    ref("stg_illuminate__repository_189"),
                    ref("stg_illuminate__repository_19"),
                    ref("stg_illuminate__repository_190"),
                    ref("stg_illuminate__repository_191"),
                    ref("stg_illuminate__repository_192"),
                    ref("stg_illuminate__repository_193"),
                    ref("stg_illuminate__repository_194"),
                    ref("stg_illuminate__repository_195"),
                    ref("stg_illuminate__repository_196"),
                    ref("stg_illuminate__repository_197"),
                    ref("stg_illuminate__repository_198"),
                    ref("stg_illuminate__repository_199"),
                    ref("stg_illuminate__repository_2"),
                    ref("stg_illuminate__repository_20"),
                    ref("stg_illuminate__repository_200"),
                    ref("stg_illuminate__repository_201"),
                    ref("stg_illuminate__repository_202"),
                    ref("stg_illuminate__repository_203"),
                    ref("stg_illuminate__repository_204"),
                    ref("stg_illuminate__repository_206"),
                    ref("stg_illuminate__repository_207"),
                    ref("stg_illuminate__repository_208"),
                    ref("stg_illuminate__repository_209"),
                    ref("stg_illuminate__repository_21"),
                    ref("stg_illuminate__repository_213"),
                    ref("stg_illuminate__repository_214"),
                    ref("stg_illuminate__repository_215"),
                    ref("stg_illuminate__repository_216"),
                    ref("stg_illuminate__repository_217"),
                    ref("stg_illuminate__repository_22"),
                    ref("stg_illuminate__repository_221"),
                    ref("stg_illuminate__repository_222"),
                    ref("stg_illuminate__repository_223"),
                    ref("stg_illuminate__repository_224"),
                    ref("stg_illuminate__repository_225"),
                    ref("stg_illuminate__repository_226"),
                    ref("stg_illuminate__repository_227"),
                    ref("stg_illuminate__repository_228"),
                    ref("stg_illuminate__repository_229"),
                    ref("stg_illuminate__repository_23"),
                    ref("stg_illuminate__repository_230"),
                    ref("stg_illuminate__repository_231"),
                    ref("stg_illuminate__repository_232"),
                    ref("stg_illuminate__repository_233"),
                    ref("stg_illuminate__repository_234"),
                    ref("stg_illuminate__repository_235"),
                    ref("stg_illuminate__repository_236"),
                    ref("stg_illuminate__repository_237"),
                    ref("stg_illuminate__repository_238"),
                    ref("stg_illuminate__repository_239"),
                    ref("stg_illuminate__repository_24"),
                    ref("stg_illuminate__repository_240"),
                    ref("stg_illuminate__repository_241"),
                    ref("stg_illuminate__repository_242"),
                    ref("stg_illuminate__repository_243"),
                    ref("stg_illuminate__repository_244"),
                    ref("stg_illuminate__repository_245"),
                    ref("stg_illuminate__repository_246"),
                    ref("stg_illuminate__repository_247"),
                    ref("stg_illuminate__repository_248"),
                    ref("stg_illuminate__repository_249"),
                    ref("stg_illuminate__repository_25"),
                    ref("stg_illuminate__repository_250"),
                    ref("stg_illuminate__repository_251"),
                    ref("stg_illuminate__repository_252"),
                    ref("stg_illuminate__repository_253"),
                    ref("stg_illuminate__repository_254"),
                    ref("stg_illuminate__repository_255"),
                    ref("stg_illuminate__repository_256"),
                    ref("stg_illuminate__repository_257"),
                    ref("stg_illuminate__repository_258"),
                    ref("stg_illuminate__repository_259"),
                    ref("stg_illuminate__repository_26"),
                    ref("stg_illuminate__repository_260"),
                    ref("stg_illuminate__repository_261"),
                    ref("stg_illuminate__repository_262"),
                    ref("stg_illuminate__repository_263"),
                    ref("stg_illuminate__repository_264"),
                    ref("stg_illuminate__repository_265"),
                    ref("stg_illuminate__repository_266"),
                    ref("stg_illuminate__repository_267"),
                    ref("stg_illuminate__repository_268"),
                    ref("stg_illuminate__repository_269"),
                    ref("stg_illuminate__repository_27"),
                    ref("stg_illuminate__repository_270"),
                    ref("stg_illuminate__repository_271"),
                    ref("stg_illuminate__repository_272"),
                    ref("stg_illuminate__repository_273"),
                    ref("stg_illuminate__repository_274"),
                    ref("stg_illuminate__repository_275"),
                    ref("stg_illuminate__repository_276"),
                    ref("stg_illuminate__repository_277"),
                    ref("stg_illuminate__repository_278"),
                    ref("stg_illuminate__repository_279"),
                    ref("stg_illuminate__repository_280"),
                    ref("stg_illuminate__repository_281"),
                    ref("stg_illuminate__repository_282"),
                    ref("stg_illuminate__repository_283"),
                    ref("stg_illuminate__repository_284"),
                    ref("stg_illuminate__repository_285"),
                    ref("stg_illuminate__repository_286"),
                    ref("stg_illuminate__repository_287"),
                    ref("stg_illuminate__repository_288"),
                    ref("stg_illuminate__repository_289"),
                    ref("stg_illuminate__repository_29"),
                    ref("stg_illuminate__repository_290"),
                    ref("stg_illuminate__repository_291"),
                    ref("stg_illuminate__repository_292"),
                    ref("stg_illuminate__repository_293"),
                    ref("stg_illuminate__repository_295"),
                    ref("stg_illuminate__repository_299"),
                    ref("stg_illuminate__repository_3"),
                    ref("stg_illuminate__repository_300"),
                    ref("stg_illuminate__repository_301"),
                    ref("stg_illuminate__repository_302"),
                    ref("stg_illuminate__repository_303"),
                    ref("stg_illuminate__repository_304"),
                    ref("stg_illuminate__repository_305"),
                    ref("stg_illuminate__repository_306"),
                    ref("stg_illuminate__repository_307"),
                    ref("stg_illuminate__repository_308"),
                    ref("stg_illuminate__repository_309"),
                    ref("stg_illuminate__repository_31"),
                    ref("stg_illuminate__repository_310"),
                    ref("stg_illuminate__repository_311"),
                    ref("stg_illuminate__repository_312"),
                    ref("stg_illuminate__repository_313"),
                    ref("stg_illuminate__repository_314"),
                    ref("stg_illuminate__repository_315"),
                    ref("stg_illuminate__repository_316"),
                    ref("stg_illuminate__repository_317"),
                    ref("stg_illuminate__repository_319"),
                    ref("stg_illuminate__repository_32"),
                    ref("stg_illuminate__repository_320"),
                    ref("stg_illuminate__repository_321"),
                    ref("stg_illuminate__repository_322"),
                    ref("stg_illuminate__repository_323"),
                    ref("stg_illuminate__repository_324"),
                    ref("stg_illuminate__repository_325"),
                    ref("stg_illuminate__repository_326"),
                    ref("stg_illuminate__repository_327"),
                    ref("stg_illuminate__repository_328"),
                    ref("stg_illuminate__repository_329"),
                    ref("stg_illuminate__repository_33"),
                    ref("stg_illuminate__repository_330"),
                    ref("stg_illuminate__repository_331"),
                    ref("stg_illuminate__repository_332"),
                    ref("stg_illuminate__repository_333"),
                    ref("stg_illuminate__repository_336"),
                    ref("stg_illuminate__repository_337"),
                    ref("stg_illuminate__repository_338"),
                    ref("stg_illuminate__repository_339"),
                    ref("stg_illuminate__repository_34"),
                    ref("stg_illuminate__repository_340"),
                    ref("stg_illuminate__repository_341"),
                    ref("stg_illuminate__repository_342"),
                    ref("stg_illuminate__repository_343"),
                    ref("stg_illuminate__repository_344"),
                    ref("stg_illuminate__repository_345"),
                    ref("stg_illuminate__repository_346"),
                    ref("stg_illuminate__repository_347"),
                    ref("stg_illuminate__repository_348"),
                    ref("stg_illuminate__repository_349"),
                    ref("stg_illuminate__repository_35"),
                    ref("stg_illuminate__repository_350"),
                    ref("stg_illuminate__repository_351"),
                    ref("stg_illuminate__repository_352"),
                    ref("stg_illuminate__repository_353"),
                    ref("stg_illuminate__repository_354"),
                    ref("stg_illuminate__repository_355"),
                    ref("stg_illuminate__repository_356"),
                    ref("stg_illuminate__repository_359"),
                    ref("stg_illuminate__repository_360"),
                    ref("stg_illuminate__repository_361"),
                    ref("stg_illuminate__repository_362"),
                    ref("stg_illuminate__repository_363"),
                    ref("stg_illuminate__repository_364"),
                    ref("stg_illuminate__repository_365"),
                    ref("stg_illuminate__repository_366"),
                    ref("stg_illuminate__repository_367"),
                    ref("stg_illuminate__repository_368"),
                    ref("stg_illuminate__repository_369"),
                    ref("stg_illuminate__repository_37"),
                    ref("stg_illuminate__repository_370"),
                    ref("stg_illuminate__repository_371"),
                    ref("stg_illuminate__repository_372"),
                    ref("stg_illuminate__repository_373"),
                    ref("stg_illuminate__repository_374"),
                    ref("stg_illuminate__repository_375"),
                    ref("stg_illuminate__repository_376"),
                    ref("stg_illuminate__repository_377"),
                    ref("stg_illuminate__repository_378"),
                    ref("stg_illuminate__repository_379"),
                    ref("stg_illuminate__repository_38"),
                    ref("stg_illuminate__repository_380"),
                    ref("stg_illuminate__repository_381"),
                    ref("stg_illuminate__repository_382"),
                    ref("stg_illuminate__repository_383"),
                    ref("stg_illuminate__repository_384"),
                    ref("stg_illuminate__repository_385"),
                    ref("stg_illuminate__repository_386"),
                    ref("stg_illuminate__repository_387"),
                    ref("stg_illuminate__repository_388"),
                    ref("stg_illuminate__repository_389"),
                    ref("stg_illuminate__repository_39"),
                    ref("stg_illuminate__repository_390"),
                    ref("stg_illuminate__repository_391"),
                    ref("stg_illuminate__repository_392"),
                    ref("stg_illuminate__repository_393"),
                    ref("stg_illuminate__repository_394"),
                    ref("stg_illuminate__repository_395"),
                    ref("stg_illuminate__repository_396"),
                    ref("stg_illuminate__repository_397"),
                    ref("stg_illuminate__repository_398"),
                    ref("stg_illuminate__repository_399"),
                    ref("stg_illuminate__repository_4"),
                    ref("stg_illuminate__repository_40"),
                    ref("stg_illuminate__repository_400"),
                    ref("stg_illuminate__repository_401"),
                    ref("stg_illuminate__repository_402"),
                    ref("stg_illuminate__repository_403"),
                    ref("stg_illuminate__repository_404"),
                    ref("stg_illuminate__repository_405"),
                    ref("stg_illuminate__repository_406"),
                    ref("stg_illuminate__repository_407"),
                    ref("stg_illuminate__repository_408"),
                    ref("stg_illuminate__repository_409"),
                    ref("stg_illuminate__repository_41"),
                    ref("stg_illuminate__repository_410"),
                    ref("stg_illuminate__repository_411"),
                    ref("stg_illuminate__repository_412"),
                    ref("stg_illuminate__repository_413"),
                    ref("stg_illuminate__repository_414"),
                    ref("stg_illuminate__repository_415"),
                    ref("stg_illuminate__repository_416"),
                    ref("stg_illuminate__repository_417"),
                    ref("stg_illuminate__repository_418"),
                    ref("stg_illuminate__repository_419"),
                    ref("stg_illuminate__repository_42"),
                    ref("stg_illuminate__repository_420"),
                    ref("stg_illuminate__repository_421"),
                    ref("stg_illuminate__repository_422"),
                    ref("stg_illuminate__repository_423"),
                    ref("stg_illuminate__repository_425"),
                    ref("stg_illuminate__repository_43"),
                    ref("stg_illuminate__repository_45"),
                    ref("stg_illuminate__repository_46"),
                    ref("stg_illuminate__repository_47"),
                    ref("stg_illuminate__repository_48"),
                    ref("stg_illuminate__repository_49"),
                    ref("stg_illuminate__repository_5"),
                    ref("stg_illuminate__repository_50"),
                    ref("stg_illuminate__repository_51"),
                    ref("stg_illuminate__repository_52"),
                    ref("stg_illuminate__repository_53"),
                    ref("stg_illuminate__repository_54"),
                    ref("stg_illuminate__repository_55"),
                    ref("stg_illuminate__repository_56"),
                    ref("stg_illuminate__repository_57"),
                    ref("stg_illuminate__repository_58"),
                    ref("stg_illuminate__repository_59"),
                    ref("stg_illuminate__repository_6"),
                    ref("stg_illuminate__repository_60"),
                    ref("stg_illuminate__repository_61"),
                    ref("stg_illuminate__repository_62"),
                    ref("stg_illuminate__repository_63"),
                    ref("stg_illuminate__repository_64"),
                    ref("stg_illuminate__repository_65"),
                    ref("stg_illuminate__repository_66"),
                    ref("stg_illuminate__repository_67"),
                    ref("stg_illuminate__repository_68"),
                    ref("stg_illuminate__repository_69"),
                    ref("stg_illuminate__repository_7"),
                    ref("stg_illuminate__repository_70"),
                    ref("stg_illuminate__repository_71"),
                    ref("stg_illuminate__repository_72"),
                    ref("stg_illuminate__repository_73"),
                    ref("stg_illuminate__repository_74"),
                    ref("stg_illuminate__repository_75"),
                    ref("stg_illuminate__repository_76"),
                    ref("stg_illuminate__repository_77"),
                    ref("stg_illuminate__repository_78"),
                    ref("stg_illuminate__repository_79"),
                    ref("stg_illuminate__repository_8"),
                    ref("stg_illuminate__repository_80"),
                    ref("stg_illuminate__repository_81"),
                    ref("stg_illuminate__repository_82"),
                    ref("stg_illuminate__repository_84"),
                    ref("stg_illuminate__repository_85"),
                    ref("stg_illuminate__repository_86"),
                    ref("stg_illuminate__repository_89"),
                    ref("stg_illuminate__repository_9"),
                    ref("stg_illuminate__repository_90"),
                    ref("stg_illuminate__repository_91"),
                    ref("stg_illuminate__repository_92"),
                    ref("stg_illuminate__repository_93"),
                    ref("stg_illuminate__repository_94"),
                    ref("stg_illuminate__repository_95"),
                    ref("stg_illuminate__repository_96"),
                    ref("stg_illuminate__repository_97"),
                    ref("stg_illuminate__repository_98"),
                    ref("stg_illuminate__repository_99"),
                ]
            )
        }}
    )

select
    ur.*,

    r.title,
    r.scope,
    r.subject_area,
    r.date_administered,

    s.local_student_id,

    rf.label as field_label,
from union_relations as ur
inner join
    {{ ref("base_illuminate__repositories") }} as r
    on ur.repository_id = r.repository_id
inner join {{ ref("stg_illuminate__students") }} as s on ur.student_id = s.student_id
inner join
    {{ ref("stg_illuminate__repository_fields") }} as rf
    on ur.repository_id = rf.repository_id
    and ur.field_name = rf.name
