from teamster.core.datagun.assets import (
    gsheet_extract_asset_factory,
    sftp_extract_asset_factory,
)

sftp_extract_assets = []
gsheet_extract_assets = []

for sftp_extract_config in [
    # pythonanywhere
    {
        "asset_name": "workers_json",
        "key_prefix": "adp",
        "query_config": {
            "query_type": "schema",
            "query_value": {"table": {"name": "adp_workers", "schema": "extracts"}},
        },
        "file_config": {"stem": "workers", "suffix": "json"},
        "destination_config": {"name": "pythonanywhere", "path": "sftp/adp"},
    },
    {
        "asset_name": "contacts_json",
        "key_prefix": "alchemer",
        "query_config": {
            "query_type": "schema",
            "query_value": {
                "table": {"name": "alchemer_contacts", "schema": "extracts"}
            },
        },
        "file_config": {"stem": "contacts", "suffix": "json"},
        "destination_config": {"name": "pythonanywhere", "path": "sftp/alchemer"},
    },
    {
        "asset_name": "students_json",
        "key_prefix": "fpodms",
        "query_config": {
            "query_type": "schema",
            "query_value": {"table": {"name": "fpodms_students", "schema": "extracts"}},
        },
        "file_config": {"stem": "students", "suffix": "json"},
        "destination_config": {"name": "pythonanywhere", "path": "sftp/fpodms"},
    },
    {
        "asset_name": "users_students_json",
        "key_prefix": "gam",
        "query_config": {
            "query_type": "schema",
            "query_value": {
                "table": {"name": "gam_users_students", "schema": "extracts"}
            },
        },
        "file_config": {"stem": "users_students", "suffix": "json"},
        "destination_config": {"name": "pythonanywhere", "path": "sftp/gam"},
    },
    {
        "asset_name": "users_admins_json",
        "key_prefix": "gam",
        "query_config": {
            "query_type": "schema",
            "query_value": {
                "table": {"name": "gam_users_admins", "schema": "extracts"}
            },
        },
        "file_config": {"stem": "users_admins", "suffix": "json"},
        "destination_config": {"name": "pythonanywhere", "path": "sftp/gam"},
    },
    {
        "asset_name": "bgcheck_audit_json",
        "key_prefix": "njdoe",
        "query_config": {
            "query_type": "schema",
            "query_value": {
                "table": {
                    "name": "njdoe_bgcheck_audit",
                    "schema": "extracts",
                    "where": "(is_approved = 0 OR is_approved_district = 0)",
                }
            },
        },
        "file_config": {"stem": "bgcheck_audit", "suffix": "json"},
        "destination_config": {"name": "pythonanywhere", "path": "sftp/njdoe"},
    },
    {
        "asset_name": "users_json",
        "key_prefix": "whetstone",
        "query_config": {
            "query_type": "file",
            "query_value": "src/teamster/kipptaf/datagun/config/sql/whetstone_users.sql",
        },
        "file_config": {"stem": "users", "suffix": "json"},
        "destination_config": {"name": "pythonanywhere", "path": "sftp/whetstone"},
    },
    # blissbook
    {
        "asset_name": "members_csv",
        "key_prefix": "blissbook",
        "query_config": {
            "query_type": "schema",
            "query_value": {
                "table": {"name": "blissbook_employee_list", "schema": "extracts"}
            },
        },
        "file_config": {"stem": "members", "suffix": "csv"},
        "destination_config": {"name": "blissbook"},
    },
    # clever
    {
        "asset_name": "enrollments_csv",
        "key_prefix": "clever",
        "query_config": {
            "query_type": "schema",
            "query_value": {
                "table": {"name": "clever_enrollments", "schema": "extracts"}
            },
        },
        "file_config": {"stem": "enrollments", "suffix": "csv"},
        "destination_config": {"name": "clever"},
    },
    {
        "asset_name": "teachers_csv",
        "key_prefix": "clever",
        "query_config": {
            "query_type": "schema",
            "query_value": {"table": {"name": "clever_teachers", "schema": "extracts"}},
        },
        "file_config": {"stem": "teachers", "suffix": "csv"},
        "destination_config": {"name": "clever"},
    },
    {
        "asset_name": "students_csv",
        "key_prefix": "clever",
        "query_config": {
            "query_type": "schema",
            "query_value": {"table": {"name": "clever_students", "schema": "extracts"}},
        },
        "file_config": {"stem": "students", "suffix": "csv"},
        "destination_config": {"name": "clever"},
    },
    {
        "asset_name": "staff_csv",
        "key_prefix": "clever",
        "query_config": {
            "query_type": "schema",
            "query_value": {"table": {"name": "clever_staff", "schema": "extracts"}},
        },
        "file_config": {"stem": "staff", "suffix": "csv"},
        "destination_config": {"name": "clever"},
    },
    {
        "asset_name": "sections_csv",
        "key_prefix": "clever",
        "query_config": {
            "query_type": "schema",
            "query_value": {"table": {"name": "clever_sections", "schema": "extracts"}},
        },
        "file_config": {"stem": "sections", "suffix": "csv"},
        "destination_config": {"name": "clever"},
    },
    {
        "asset_name": "schools_csv",
        "key_prefix": "clever",
        "query_config": {
            "query_type": "schema",
            "query_value": {"table": {"name": "clever_schools", "schema": "extracts"}},
        },
        "file_config": {"stem": "schools", "suffix": "csv"},
        "destination_config": {"name": "clever"},
    },
    # coupa
    {
        "asset_name": "users_csv",
        "key_prefix": "coupa",
        "query_config": {
            "query_type": "schema",
            "query_value": {"table": {"name": "coupa_users", "schema": "extracts"}},
        },
        "file_config": {"stem": "users_{today}", "suffix": "csv"},
        "destination_config": {"name": "coupa", "path": "/Incoming/Users"},
    },
    # egencia
    {
        "asset_name": "users_csv",
        "key_prefix": "egencia",
        "query_config": {
            "query_type": "file",
            "query_value": "src/teamster/kipptaf/datagun/config/sql/egencia_users.sql",
        },
        "file_config": {"stem": "users_{today}", "suffix": "csv"},
        "destination_config": {"name": "egencia", "path": "/global/50323/USERS"},
    },
    # kipptaf
    {
        "asset_name": "AD_csv",
        "key_prefix": "idauto",
        "query_config": {
            "query_type": "schema",
            "query_value": {
                "table": {"name": "idauto_staff_roster", "schema": "extracts"}
            },
        },
        "file_config": {
            "stem": "AD",
            "suffix": "csv",
            "encoding": "latin1",
            "format": {"quoting": 1},  # csv.QUOTE_ALL
        },
        "destination_config": {"name": "kipptaf"},
    },
    # littlesis
    {
        "asset_name": "littlesis_extract_csv",
        "key_prefix": "littlesis",
        "query_config": {
            "query_type": "schema",
            "query_value": {
                "table": {"name": "littlesis_enrollments", "schema": "extracts"}
            },
        },
        "file_config": {"stem": "littlesis_extract", "suffix": "csv"},
        "destination_config": {"name": "littlesis"},
    },
    # read180
    {
        "asset_name": "teachers_csv",
        "key_prefix": "read180",
        "query_config": {
            "query_type": "schema",
            "query_value": {
                "table": {"name": "read180_teachers", "schema": "extracts"}
            },
        },
        "file_config": {"stem": "teachers", "suffix": "csv"},
        "destination_config": {"name": "read180", "path": "/uploads"},
    },
    {
        "asset_name": "students_csv",
        "key_prefix": "read180",
        "query_config": {
            "query_type": "schema",
            "query_value": {
                "table": {"name": "read180_students", "schema": "extracts"}
            },
        },
        "file_config": {"stem": "students", "suffix": "csv"},
        "destination_config": {"name": "read180", "path": "/uploads"},
    },
    # razkids
    {
        "asset_name": "teachers_csv",
        "key_prefix": "razkids",
        "query_config": {
            "query_type": "schema",
            "query_value": {
                "table": {"name": "razkids_teachers", "schema": "extracts"}
            },
        },
        "file_config": {"stem": "teachers", "suffix": "csv"},
        "destination_config": {"name": "razkids"},
    },
    {
        "asset_name": "students_csv",
        "key_prefix": "razkids",
        "query_config": {
            "query_type": "schema",
            "query_value": {
                "table": {"name": "razkids_students", "schema": "extracts"}
            },
        },
        "file_config": {"stem": "students", "suffix": "csv"},
        "destination_config": {"name": "razkids"},
    },
    # illuminate
    {
        "asset_name": "courses_txt",
        "key_prefix": "illuminate",
        "query_config": {
            "query_type": "schema",
            "query_value": {
                "table": {"name": "illuminate_courses", "schema": "extracts"}
            },
        },
        "file_config": {"stem": "courses", "suffix": "txt", "format": {"sep": "\t"}},
        "destination_config": {"name": "illuminate"},
    },
    {
        "asset_name": "enrollment_txt",
        "key_prefix": "illuminate",
        "query_config": {
            "query_type": "schema",
            "query_value": {
                "table": {"name": "illuminate_enrollment", "schema": "extracts"}
            },
        },
        "file_config": {
            "stem": "enrollment",
            "suffix": "txt",
            "format": {"sep": "\t"},
        },
        "destination_config": {"name": "illuminate"},
    },
    {
        "asset_name": "mastschd_txt",
        "key_prefix": "illuminate",
        "query_config": {
            "query_type": "schema",
            "query_value": {
                "table": {"name": "illuminate_mastschd", "schema": "extracts"}
            },
        },
        "file_config": {"stem": "mastschd", "suffix": "txt", "format": {"sep": "\t"}},
        "destination_config": {"name": "illuminate"},
    },
    {
        "asset_name": "roles_txt",
        "key_prefix": "illuminate",
        "query_config": {
            "query_type": "schema",
            "query_value": {
                "table": {"name": "illuminate_roles", "schema": "extracts"}
            },
        },
        "file_config": {"stem": "roles", "suffix": "txt", "format": {"sep": "\t"}},
        "destination_config": {"name": "illuminate"},
    },
    {
        "asset_name": "roster_txt",
        "key_prefix": "illuminate",
        "query_config": {
            "query_type": "schema",
            "query_value": {
                "table": {"name": "illuminate_roster", "schema": "extracts"}
            },
        },
        "file_config": {"stem": "roster", "suffix": "txt", "format": {"sep": "\t"}},
        "destination_config": {"name": "illuminate"},
    },
    {
        "asset_name": "users_txt",
        "key_prefix": "illuminate",
        "query_config": {
            "query_type": "schema",
            "query_value": {
                "table": {"name": "illuminate_users", "schema": "extracts"}
            },
        },
        "file_config": {"stem": "users", "suffix": "txt", "format": {"sep": "\t"}},
        "destination_config": {"name": "illuminate"},
    },
    {
        "asset_name": "terms_txt",
        "key_prefix": "illuminate",
        "query_config": {
            "query_type": "schema",
            "query_value": {
                "table": {"name": "illuminate_terms", "schema": "extracts"}
            },
        },
        "file_config": {"stem": "terms", "suffix": "txt", "format": {"sep": "\t"}},
        "destination_config": {"name": "illuminate"},
    },
    {
        "asset_name": "student_portal_accounts_txt",
        "key_prefix": "illuminate",
        "query_config": {
            "query_type": "schema",
            "query_value": {
                "table": {
                    "name": "illuminate_student_portal_accounts",
                    "schema": "extracts",
                }
            },
        },
        "file_config": {
            "stem": "student_portal_accounts",
            "suffix": "txt",
            "format": {"sep": "\t"},
        },
        "destination_config": {"name": "illuminate"},
    },
    {
        "asset_name": "studemo_txt",
        "key_prefix": "illuminate",
        "query_config": {
            "query_type": "schema",
            "query_value": {
                "table": {"name": "illuminate_studemo", "schema": "extracts"}
            },
        },
        "file_config": {"stem": "studemo", "suffix": "txt", "format": {"sep": "\t"}},
        "destination_config": {"name": "illuminate"},
    },
    {
        "asset_name": "sites_txt",
        "key_prefix": "illuminate",
        "query_config": {
            "query_type": "schema",
            "query_value": {
                "table": {"name": "illuminate_sites", "schema": "extracts"}
            },
        },
        "file_config": {"stem": "sites", "suffix": "txt", "format": {"sep": "\t"}},
        "destination_config": {"name": "illuminate"},
    },
    # deanslist
    {
        "asset_name": "deanslist_college_admission_tests_json",
        "key_prefix": "deanslist",
        "query_config": {
            "query_type": "schema",
            "query_value": {
                "table": {
                    "name": "deanslist_college_admission_tests",
                    "schema": "extracts",
                }
            },
        },
        "file_config": {"stem": "deanslist_college_admission_tests", "suffix": "json"},
        "destination_config": {"name": "deanslist"},
    },
    {
        "asset_name": "deanslist_designations_json",
        "key_prefix": "deanslist",
        "query_config": {
            "query_type": "schema",
            "query_value": {
                "table": {
                    "name": "deanslist_designations",
                    "schema": "extracts",
                }
            },
        },
        "file_config": {"stem": "deanslist_designations", "suffix": "json"},
        "destination_config": {"name": "deanslist"},
    },
    {
        "asset_name": "deanslist_transcript_grades_json",
        "key_prefix": "deanslist",
        "query_config": {
            "query_type": "schema",
            "query_value": {
                "table": {
                    "name": "deanslist_transcript_grades",
                    "schema": "extracts",
                }
            },
        },
        "file_config": {"stem": "deanslist_transcript_grades", "suffix": "json"},
        "destination_config": {"name": "deanslist"},
    },
    {
        "asset_name": "deanslist_finalgrades_json",
        "key_prefix": "deanslist",
        "query_config": {
            "query_type": "schema",
            "query_value": {
                "table": {
                    "name": "deanslist_finalgrades",
                    "schema": "extracts",
                }
            },
        },
        "file_config": {"stem": "deanslist_finalgrades", "suffix": "json"},
        "destination_config": {"name": "deanslist"},
    },
    {
        "asset_name": "deanslist_instructional_tech_json",
        "key_prefix": "deanslist",
        "query_config": {
            "query_type": "schema",
            "query_value": {
                "table": {
                    "name": "deanslist_instructional_tech",
                    "schema": "extracts",
                }
            },
        },
        "file_config": {"stem": "deanslist_instructional_tech", "suffix": "json"},
        "destination_config": {"name": "deanslist"},
    },
    {
        "asset_name": "deanslist_iready_diagnostics_json",
        "key_prefix": "deanslist",
        "query_config": {
            "query_type": "schema",
            "query_value": {
                "table": {
                    "name": "deanslist_iready_diagnostics",
                    "schema": "extracts",
                }
            },
        },
        "file_config": {"stem": "deanslist_iready_diagnostics", "suffix": "json"},
        "destination_config": {"name": "deanslist"},
    },
    {
        "asset_name": "deanslist_iready_lessons_json",
        "key_prefix": "deanslist",
        "query_config": {
            "query_type": "schema",
            "query_value": {
                "table": {
                    "name": "deanslist_iready_lessons",
                    "schema": "extracts",
                }
            },
        },
        "file_config": {"stem": "deanslist_iready_lessons", "suffix": "json"},
        "destination_config": {"name": "deanslist"},
    },
    {
        "asset_name": "deanslist_missing_assignments_json",
        "key_prefix": "deanslist",
        "query_config": {
            "query_type": "schema",
            "query_value": {
                "table": {
                    "name": "deanslist_missing_assignments",
                    "schema": "extracts",
                }
            },
        },
        "file_config": {"stem": "deanslist_missing_assignments", "suffix": "json"},
        "destination_config": {"name": "deanslist"},
    },
    {
        "asset_name": "deanslist_mod_standards_json",
        "key_prefix": "deanslist",
        "query_config": {
            "query_type": "schema",
            "query_value": {
                "table": {
                    "name": "deanslist_mod_standards",
                    "schema": "extracts",
                }
            },
        },
        "file_config": {"stem": "deanslist_mod_standards", "suffix": "json"},
        "destination_config": {"name": "deanslist"},
    },
    {
        "asset_name": "deanslist_promo_status_json",
        "key_prefix": "deanslist",
        "query_config": {
            "query_type": "schema",
            "query_value": {
                "table": {
                    "name": "deanslist_promo_status",
                    "schema": "extracts",
                }
            },
        },
        "file_config": {"stem": "deanslist_promo_status", "suffix": "json"},
        "destination_config": {"name": "deanslist"},
    },
    {
        "asset_name": "deanslist_reading_levels_json",
        "key_prefix": "deanslist",
        "query_config": {
            "query_type": "schema",
            "query_value": {
                "table": {
                    "name": "deanslist_reading_levels",
                    "schema": "extracts",
                }
            },
        },
        "file_config": {"stem": "deanslist_reading_levels", "suffix": "json"},
        "destination_config": {"name": "deanslist"},
    },
    {
        "asset_name": "deanslist_sight_words_json",
        "key_prefix": "deanslist",
        "query_config": {
            "query_type": "schema",
            "query_value": {
                "table": {
                    "name": "deanslist_sight_words",
                    "schema": "extracts",
                }
            },
        },
        "file_config": {"stem": "deanslist_sight_words", "suffix": "json"},
        "destination_config": {"name": "deanslist"},
    },
    {
        "asset_name": "deanslist_state_test_scores_json",
        "key_prefix": "deanslist",
        "query_config": {
            "query_type": "schema",
            "query_value": {
                "table": {
                    "name": "deanslist_state_test_scores",
                    "schema": "extracts",
                }
            },
        },
        "file_config": {"stem": "deanslist_state_test_scores", "suffix": "json"},
        "destination_config": {"name": "deanslist"},
    },
    {
        "asset_name": "deanslist_student_misc_json",
        "key_prefix": "deanslist",
        "query_config": {
            "query_type": "schema",
            "query_value": {
                "table": {
                    "name": "deanslist_student_misc",
                    "schema": "extracts",
                }
            },
        },
        "file_config": {"stem": "deanslist_student_misc", "suffix": "json"},
        "destination_config": {"name": "deanslist"},
    },
    {
        "asset_name": "deanslist_transcript_gpas_json",
        "key_prefix": "deanslist",
        "query_config": {
            "query_type": "schema",
            "query_value": {
                "table": {
                    "name": "deanslist_transcript_gpas",
                    "schema": "extracts",
                }
            },
        },
        "file_config": {"stem": "deanslist_transcript_gpas", "suffix": "json"},
        "destination_config": {"name": "deanslist"},
    },
]:
    sftp_extract_assets.append(sftp_extract_asset_factory(**sftp_extract_config))

test = gsheet_extract_asset_factory(
    asset_name="test",
    key_prefix="gsheets",
    query_config={
        "query_type": "text",
        "query_value": (
            "SELECT "
            "n AS n0, n + 1 AS n1, n + 2 AS n2, n + 3 AS n3, n + 4 AS n4 "
            "FROM utilities.row_generator_smallint "
            "WHERE n <= 5"
        ),
    },
    file_config={"stem": "test", "suffix": "gsheet"},
)
