import numpy
import pandas
from dagster import (
    AssetExecutionContext,
    MultiPartitionKey,
    MultiPartitionsDefinition,
    Output,
    StaticPartitionsDefinition,
    asset,
)
from dagster_gcp import BigQueryResource
from google.cloud import bigquery
from sklearn.cluster import DBSCAN
from sklearn.decomposition import PCA
from sklearn.ensemble import IsolationForest

from teamster.core.utils.functions import (
    check_avro_schema_valid,
    get_avro_schema_valid_check_spec,
)

from .. import CODE_LOCATION
from .schema import ASSET_FIELDS

FIT_TRANSFORM_COLUMNS = [
    "etr1a",
    "etr1b",
    "etr2a",
    "etr2b",
    "etr2c",
    "etr2d",
    "etr3a",
    "etr3b",
    "etr3c",
    "etr3d",
    "etr4a",
    "etr4b",
    "etr4c",
    "etr4d",
    "etr4e",
    "etr4f",
    "etr5a",
    "etr5b",
    "etr5c",
    "so1",
    "so2",
    "so3",
    "so4",
    "so5",
    "so6",
    "so7",
    "so8",
]


def get_iqr_outliers(df: pandas.DataFrame):
    q1 = numpy.percentile(df["overall_score"], 25)
    q3 = numpy.percentile(df["overall_score"], 75)

    iqr = q3 - q1  # type: ignore

    outliers_array = numpy.where(
        (df["overall_score"] < q1 - 1.5 * iqr) | (df["overall_score"] > q3 + 1.5 * iqr)
    )[0]

    df["is_iqr_outlier"] = df["observer_employee_number"].isin(
        df.loc[outliers_array]["observer_employee_number"].tolist()
    )

    return df


def get_pca(df: pandas.DataFrame):
    pca = PCA(n_components=2)

    principal_components = pca.fit_transform(X=df[FIT_TRANSFORM_COLUMNS])

    pca_df = pandas.DataFrame(
        data=principal_components,
        columns=["pc1", "pc2"],
    )

    df = pandas.merge(left=df, right=pca_df, left_index=True, right_index=True)

    # percent of variance
    df["pc1_variance_explained"] = pca.explained_variance_ratio_[0]
    df["pc2_variance_explained"] = pca.explained_variance_ratio_[1]

    return df


def get_dbscan(df):
    # All time Outlier Detction Using PCA
    # 0.6 is the historic optimal epsilon, but we may need to adjust
    outlier_detection = DBSCAN(min_samples=3, eps=0.6)

    clusters = outlier_detection.fit_predict(X=df[["pc1", "pc2"]])

    cluster_df = pandas.DataFrame(data=clusters, columns=["cluster"])

    df = pandas.merge(left=df, right=cluster_df, left_index=True, right_index=True)

    return df


def get_isolation_forest(df: pandas.DataFrame):
    model = IsolationForest(contamination=0.1)  # assuming 10% of the data are outliers

    model.fit(X=df[FIT_TRANSFORM_COLUMNS])

    outliers = model.predict(X=df[FIT_TRANSFORM_COLUMNS])

    tree_df = pandas.DataFrame(data=outliers, columns=["tree_outlier"])

    df = pandas.merge(left=df, right=tree_df, left_index=True, right_index=True)

    return df


@asset(
    key=[CODE_LOCATION, "performance_management", "outlier_detection"],
    io_manager_key="io_manager_gcs_avro",
    group_name="performance_management",
    partitions_def=MultiPartitionsDefinition(
        {
            "academic_year": StaticPartitionsDefinition(["2023"]),
            "term": StaticPartitionsDefinition(["PM1", "PM2", "PM3"]),
        }
    ),
    output_required=False,
    check_specs=[
        get_avro_schema_valid_check_spec(
            [CODE_LOCATION, "performance_management", "outlier_detection"]
        )
    ],
)
def outlier_detection(context: AssetExecutionContext, db_bigquery: BigQueryResource):
    partition_key: MultiPartitionKey = context.partition_key  # type: ignore
    schema = ASSET_FIELDS["outlier_detection"]

    # load data from extract view
    with db_bigquery.get_client() as bq:
        bq_client = bq

    dataset_ref = bigquery.DatasetReference(
        project=bq_client.project, dataset_id="kipptaf_extracts"
    )

    rows = bq_client.list_rows(
        table=dataset_ref.table("rpt_python__manager_pm_averages")
    )

    df_global = rows.to_dataframe()

    df_global.dropna(inplace=True)
    df_global.reset_index(inplace=True, drop=True)

    # subset current year/term
    df_current: pandas.DataFrame = df_global[
        (
            df_global["academic_year"]
            == int(partition_key.keys_by_dimension["academic_year"])
        )
        & (df_global["form_term"] == partition_key.keys_by_dimension["term"])
    ]

    # exit if no data for partition
    if df_current.shape[0] == 0:
        return Output(value=([], schema), metadata={"records": 0})

    df_current.reset_index(inplace=True, drop=True)

    # calculate outliers columns: all-time
    df_global = get_iqr_outliers(df_global)
    df_global = get_pca(df_global)
    df_global = get_dbscan(df_global)
    df_global = get_isolation_forest(df_global)

    # calculate outliers columns: current term
    df_current = get_iqr_outliers(df_current)
    df_current = get_pca(df_current)
    df_current = get_dbscan(df_current)
    df_current = get_isolation_forest(df_current)

    # merge all-time rows to matching current term rows
    df_current = pandas.merge(
        left=df_current,
        right=df_global[
            [
                "observer_employee_number",
                "academic_year",
                "form_term",
                "cluster",
                "is_iqr_outlier",
                "pc1_variance_explained",
                "pc1",
                "pc2_variance_explained",
                "pc2",
                "tree_outlier",
            ]
        ],
        how="left",
        left_on=["observer_employee_number", "academic_year", "form_term"],
        right_on=["observer_employee_number", "academic_year", "form_term"],
        suffixes=["_current", "_global"],
    )

    data = df_current.to_dict(orient="records")

    yield Output(value=(data, schema), metadata={"records": df_current.shape[0]})

    yield check_avro_schema_valid(
        asset_key=context.asset_key, records=data, schema=schema
    )


_all = [
    outlier_detection,
]
