import pandas as pd
import streamlit as st
from io import BytesIO


# -----------------------------
# LOAD DATASET
# -----------------------------
def load_data(uploaded_file):
    """
    Load CSV or Excel file
    """

    if uploaded_file is None:
        return None

    file_name = uploaded_file.name.lower()

    try:

        if file_name.endswith(".csv"):
            df = pd.read_csv(uploaded_file)

        elif file_name.endswith(".xlsx") or file_name.endswith(".xls"):
            df = pd.read_excel(uploaded_file)

        else:
            st.error("Unsupported File Format")
            return None

        return df

    except Exception as e:
        st.error(f"Error Loading File : {e}")
        return None


# -----------------------------
# FILE DETAILS
# -----------------------------
def get_file_details(uploaded_file):

    details = {
        "Filename": uploaded_file.name,
        "File Size (KB)": round(uploaded_file.size / 1024, 2),
        "File Type": uploaded_file.type,
    }

    return details


# -----------------------------
# MEMORY USAGE
# -----------------------------
def memory_usage(df):

    memory = df.memory_usage(deep=True).sum()

    return round(memory / (1024 * 1024), 2)


# -----------------------------
# DOWNLOAD CSV
# -----------------------------
def convert_csv(df):

    return df.to_csv(index=False).encode("utf-8")


# -----------------------------
# DOWNLOAD EXCEL
# -----------------------------
def convert_excel(df):

    output = BytesIO()

    with pd.ExcelWriter(output, engine="xlsxwriter") as writer:

        df.to_excel(writer, index=False, sheet_name="Cleaned_Data")

    return output.getvalue()


# -----------------------------
# DATA TYPES
# -----------------------------
def get_column_types(df):

    numerical = df.select_dtypes(include=["number"]).columns.tolist()

    categorical = df.select_dtypes(
        include=["object", "category", "bool"]
    ).columns.tolist()

    datetime_cols = df.select_dtypes(
        include=["datetime64"]
    ).columns.tolist()

    return numerical, categorical, datetime_cols


# -----------------------------
# MISSING VALUES
# -----------------------------
def missing_summary(df):

    missing = df.isnull().sum()

    percent = (missing / len(df)) * 100

    result = pd.DataFrame({

        "Missing Values": missing,
        "Percentage": percent.round(2)

    })

    return result.sort_values(
        by="Missing Values",
        ascending=False
    )


# -----------------------------
# DUPLICATE ROWS
# -----------------------------
def duplicate_count(df):

    return int(df.duplicated().sum())


# -----------------------------
# DATASET INFO
# -----------------------------
def dataset_info(df):

    info = {

        "Rows": df.shape[0],
        "Columns": df.shape[1],
        "Total Cells": df.shape[0] * df.shape[1],
        "Missing Cells": int(df.isnull().sum().sum()),
        "Duplicate Rows": duplicate_count(df),
        "Memory Usage (MB)": memory_usage(df)

    }

    return info


# -----------------------------
# COLUMN SUMMARY
# -----------------------------
def column_summary(df):

    summary = pd.DataFrame({

        "Data Type": df.dtypes.astype(str),
        "Unique Values": df.nunique(),
        "Missing": df.isnull().sum()

    })

    return summary


# -----------------------------
# DISPLAY DATASET INFO
# -----------------------------
def show_dataset_metrics(df):

    info = dataset_info(df)

    c1, c2, c3 = st.columns(3)

    c1.metric("Rows", info["Rows"])
    c2.metric("Columns", info["Columns"])
    c3.metric("Memory (MB)", info["Memory Usage (MB)"])

    c4, c5, c6 = st.columns(3)

    c4.metric("Duplicate Rows", info["Duplicate Rows"])
    c5.metric("Missing Cells", info["Missing Cells"])
    c6.metric("Total Cells", info["Total Cells"])


# -----------------------------
# RESET INDEX
# -----------------------------
def reset_dataframe(df):

    return df.reset_index(drop=True)


# -----------------------------
# CHECK EMPTY DATASET
# -----------------------------
def is_empty(df):

    if df is None:
        return True

    if df.empty:
        return True

    return False


# -----------------------------
# NUMERIC COLUMNS
# -----------------------------
def numeric_columns(df):

    return df.select_dtypes(include="number").columns.tolist()


# -----------------------------
# CATEGORICAL COLUMNS
# -----------------------------
def categorical_columns(df):

    return df.select_dtypes(
        include=["object", "category"]
    ).columns.tolist()