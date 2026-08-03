import pandas as pd
import numpy as np


# =====================================================
# BASIC INFORMATION
# =====================================================

def dataset_shape(df):
    """Return dataset shape"""
    return df.shape


def get_columns(df):
    """Return all column names"""
    return list(df.columns)


def data_types(df):
    """Return datatype of every column"""
    return pd.DataFrame({
        "Column": df.columns,
        "Datatype": df.dtypes.astype(str)
    })


def memory_usage(df):
    """Memory usage in MB"""
    memory = df.memory_usage(deep=True).sum() / (1024 * 1024)
    return round(memory, 2)


def missing_values(df):
    """Missing value summary"""

    missing = df.isnull().sum()

    percent = (missing / len(df)) * 100

    result = pd.DataFrame({

        "Missing Values": missing,
        "Percentage (%)": percent.round(2)

    })

    return result.sort_values(
        by="Missing Values",
        ascending=False
    )


def duplicate_rows(df):
    """Duplicate rows count"""
    return int(df.duplicated().sum())


# =====================================================
# DATASET SUMMARY
# =====================================================

def describe_dataset(df):
    """Pandas describe"""
    return df.describe(include="all").T


# =====================================================
# NUMERIC SUMMARY
# =====================================================

def numeric_summary(df):

    numeric = df.select_dtypes(include=np.number)

    if numeric.empty:
        return pd.DataFrame()

    summary = pd.DataFrame(index=numeric.columns)

    summary["Count"] = numeric.count()
    summary["Mean"] = numeric.mean()
    summary["Median"] = numeric.median()
    summary["Mode"] = numeric.mode().iloc[0]
    summary["Min"] = numeric.min()
    summary["Max"] = numeric.max()

    summary["Variance"] = numeric.var()

    summary["Std Dev"] = numeric.std()

    summary["Skewness"] = numeric.skew()

    summary["Kurtosis"] = numeric.kurt()

    summary["Unique"] = numeric.nunique()

    return summary.round(3)


# =====================================================
# CATEGORICAL SUMMARY
# =====================================================

def categorical_summary(df):

    categorical = df.select_dtypes(
        include=["object", "category", "bool"]
    )

    if categorical.empty:
        return pd.DataFrame()

    summary = pd.DataFrame(index=categorical.columns)

    summary["Unique"] = categorical.nunique()

    summary["Most Frequent"] = categorical.mode().iloc[0]

    summary["Frequency"] = categorical.apply(
        lambda x: x.value_counts().iloc[0]
    )

    summary["Missing"] = categorical.isnull().sum()

    return summary


# =====================================================
# UNIQUE VALUES
# =====================================================

def unique_values(df):

    result = pd.DataFrame({

        "Column": df.columns,
        "Unique Values": df.nunique()

    })

    return result


# =====================================================
# NULL PERCENTAGE
# =====================================================

def null_percentage(df):

    return (df.isnull().mean() * 100).round(2)


# =====================================================
# CORRELATION
# =====================================================

def pearson_correlation(df):

    numeric = df.select_dtypes(include=np.number)

    return numeric.corr(method="pearson")


def spearman_correlation(df):

    numeric = df.select_dtypes(include=np.number)

    return numeric.corr(method="spearman")


# =====================================================
# COLUMN INFORMATION
# =====================================================

def column_information(df):

    info = pd.DataFrame(index=df.columns)

    info["Datatype"] = df.dtypes.astype(str)

    info["Missing"] = df.isnull().sum()

    info["Unique"] = df.nunique()

    info["Non Null"] = df.count()

    return info


# =====================================================
# OVERVIEW METRICS
# =====================================================

def overview(df):

    overview = {

        "Rows": df.shape[0],

        "Columns": df.shape[1],

        "Total Cells": df.shape[0] * df.shape[1],

        "Missing Cells": int(df.isnull().sum().sum()),

        "Duplicate Rows": int(df.duplicated().sum()),

        "Memory Usage (MB)": round(
            df.memory_usage(deep=True).sum() / (1024 * 1024),
            2
        )

    }

    return overview


# =====================================================
# DATA QUALITY REPORT
# =====================================================

def data_quality(df):

    quality = pd.DataFrame(index=df.columns)

    quality["Datatype"] = df.dtypes.astype(str)

    quality["Missing"] = df.isnull().sum()

    quality["Missing %"] = (
        df.isnull().mean() * 100
    ).round(2)

    quality["Unique"] = df.nunique()

    quality["Duplicates"] = df.duplicated().sum()

    return quality


# =====================================================
# NUMERIC COLUMN LIST
# =====================================================

def numeric_columns(df):

    return df.select_dtypes(include=np.number).columns.tolist()


# =====================================================
# CATEGORICAL COLUMN LIST
# =====================================================

def categorical_columns(df):

    return df.select_dtypes(
        include=["object", "category", "bool"]
    ).columns.tolist()


# =====================================================
# DATETIME COLUMN LIST
# =====================================================

def datetime_columns(df):

    return df.select_dtypes(
        include=["datetime64"]
    ).columns.tolist()


# =====================================================
# VALUE COUNTS
# =====================================================

def value_counts(df, column):

    return df[column].value_counts().reset_index().rename(

        columns={
            "index": column,
            column: "Count"
        }

    )


# =====================================================
# SAMPLE DATA
# =====================================================

def head(df, n=5):

    return df.head(n)


def tail(df, n=5):

    return df.tail(n)


def random_sample(df, n=5):

    return df.sample(min(n, len(df)))


# =====================================================
# DESCRIBE SINGLE COLUMN
# =====================================================

def column_statistics(df, column):

    series = df[column]

    result = {

        "Count": series.count(),

        "Missing": series.isnull().sum(),

        "Unique": series.nunique()

    }

    if pd.api.types.is_numeric_dtype(series):

        result.update({

            "Mean": series.mean(),

            "Median": series.median(),

            "Mode": series.mode().iloc[0],

            "Variance": series.var(),

            "Std": series.std(),

            "Min": series.min(),

            "Max": series.max(),

            "Skewness": series.skew(),

            "Kurtosis": series.kurt()

        })

    return result