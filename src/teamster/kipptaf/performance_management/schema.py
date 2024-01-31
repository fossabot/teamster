OUTLIER_DETECTION_FIELDS = [
    {"name": "observer_employee_number", "type": ["null", "long"], "default": None},
    {"name": "academic_year", "type": ["null", "long"], "default": None},
    {"name": "form_term", "type": ["null", "string"], "default": None},
    {"name": "term_num", "type": ["null", "long"], "default": None},
    {"name": "etr1a", "type": ["null", "double"], "default": None},
    {"name": "etr1b", "type": ["null", "double"], "default": None},
    {"name": "etr2a", "type": ["null", "double"], "default": None},
    {"name": "etr2b", "type": ["null", "double"], "default": None},
    {"name": "etr2c", "type": ["null", "double"], "default": None},
    {"name": "etr2d", "type": ["null", "double"], "default": None},
    {"name": "etr3a", "type": ["null", "double"], "default": None},
    {"name": "etr3b", "type": ["null", "double"], "default": None},
    {"name": "etr3c", "type": ["null", "double"], "default": None},
    {"name": "etr3d", "type": ["null", "double"], "default": None},
    {"name": "etr4a", "type": ["null", "double"], "default": None},
    {"name": "etr4b", "type": ["null", "double"], "default": None},
    {"name": "etr4c", "type": ["null", "double"], "default": None},
    {"name": "etr4d", "type": ["null", "double"], "default": None},
    {"name": "etr4e", "type": ["null", "double"], "default": None},
    {"name": "etr4f", "type": ["null", "double"], "default": None},
    {"name": "etr5a", "type": ["null", "double"], "default": None},
    {"name": "etr5b", "type": ["null", "double"], "default": None},
    {"name": "etr5c", "type": ["null", "double"], "default": None},
    {"name": "so1", "type": ["null", "double"], "default": None},
    {"name": "so2", "type": ["null", "double"], "default": None},
    {"name": "so3", "type": ["null", "double"], "default": None},
    {"name": "so4", "type": ["null", "double"], "default": None},
    {"name": "so5", "type": ["null", "double"], "default": None},
    {"name": "so6", "type": ["null", "double"], "default": None},
    {"name": "so7", "type": ["null", "double"], "default": None},
    {"name": "so8", "type": ["null", "double"], "default": None},
    {"name": "overall_score", "type": ["null", "double"], "default": None},
    {"name": "is_iqr_outlier_current", "type": ["null", "boolean"], "default": None},
    {"name": "cluster_current", "type": ["null", "long"], "default": None},
    {"name": "tree_outlier_current", "type": ["null", "long"], "default": None},
    {"name": "cluster_global", "type": ["null", "long"], "default": None},
    {"name": "is_iqr_outlier_global", "type": ["null", "boolean"], "default": None},
    {"name": "tree_outlier_global", "type": ["null", "long"], "default": None},
    {"name": "pc1_global", "type": ["null", "double"], "default": None},
    {"name": "pc1_current", "type": ["null", "double"], "default": None},
    {"name": "pc2_global", "type": ["null", "double"], "default": None},
    {"name": "pc2_current", "type": ["null", "double"], "default": None},
    {
        "name": "pc1_variance_explained_current",
        "type": ["null", "double"],
        "default": None,
    },
    {
        "name": "pc1_variance_explained_global",
        "type": ["null", "double"],
        "default": None,
    },
    {
        "name": "pc2_variance_explained_current",
        "type": ["null", "double"],
        "default": None,
    },
    {
        "name": "pc2_variance_explained_global",
        "type": ["null", "double"],
        "default": None,
    },
]

ASSET_FIELDS = {
    "outlier_detection": OUTLIER_DETECTION_FIELDS,
}