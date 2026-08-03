import numpy as np 
import pandas as pd 
import matplotlib.pyplot as plt
import plotly.express as px
import plotly.graph_objects as go

def get_numeric_columns(df):
    return df.select_dtypes(include = np.number).columns.tolist()   #np use for because avoide writing the integer bit like int 64,int8
def get_categorical_columns(df): 
    return df.select_dtypes(include=["object","category","bool"]).columns.tolist()

#histogram
def histogram(df,column):
    fig = px.histogram(
        df,
        x=column,
        title = f"Histogram - {column}",
        template = "plotly_white"
    )
    fig.update_layout(height =500)
    return fig

#BOXPLOT
def box_plot(df,column):
    fig = px.box(
        df,
        y=column,
        title = f"Box Plot - {column}",
        template = "plotly_white"
    )
    fig.update_layout(height =500)
    return fig

#scater ploter
def scatter_plot(df,x,y,color = None):
    fig = px.scatter(
        df,
        x=x,
        y=y,
        color=color,
        title = f"Scatter plot-{x}vs{y}",
        template = "plotly_white"
    )
    fig.update_layout(height =500)    
    return fig

#DENSITY PLOT
def density_plot(df, column):
    fig = px.histogram(
        df,
        x=column,
        histnorm="probability density",
        marginal="violin",
        template="plotly_white",
        title=f"Density Plot - {column}"
    )
    fig.update_layout(height=500)
    return fig

#VIOLIN PLOT
def violin_plot(df, column):
    fig = px.violin(
        df,
        y=column,
        box=True,
        points="all",
        template="plotly_white",
        title=f"Violin Plot - {column}"
    )
    fig.update_layout(height=500)
    return fig

#LINE CHART
def line_chart(df, x, y):
    fig = px.line(
        df,
        x=x,
        y=y,
        markers=True,
        template="plotly_white",
        title=f"{y} vs {x}"
    )
    fig.update_layout(height=500)
    return fig

#BAR GRAPH
def bar_chart(df, x, y):
    fig = px.bar(
        df,
        x=x,
        y=y,
        template="plotly_white",
        title=f"{y} by {x}"
    )
    fig.update_layout(height=500)
    return fig

#PIE CHART
def pie_chart(df, column):    
    counts = df[column].value_counts().reset_index()
    counts.columns = [column, "Count"]
    fig = px.pie(
        counts,
        names=column,
        values="Count",
        title=f"Pie Chart - {column}"
    )
    fig.update_layout(height=550)
    return fig

# COUNT PLOT
def count_plot(df, column):
    counts = df[column].value_counts().reset_index()
    counts.columns = [column, "Count"]
    fig = px.bar(
        counts,
        x=column,
        y="Count",
        template="plotly_white",
        title=f"Count Plot - {column}"
    )
    fig.update_layout(height=500)
    return fig


# PAIR PLOT (Scatter Matrix)
def pair_plot(df):
    numeric_cols = get_numeric_columns(df)
    if len(numeric_cols) < 2:
        return None

    fig = px.scatter_matrix(
        df,
        dimensions=numeric_cols,
        title="Pair Plot",
        template="plotly_white"
    )

    fig.update_layout(
        height=800,
        width=900
    )
    return fig

# CORRELATION HEATMAP
def correlation_heatmap(df, method="pearson"):
    numeric_df = df.select_dtypes(include=np.number)
    if numeric_df.empty:
        return None
    corr = numeric_df.corr(method=method)
    fig = px.imshow(
        corr,
        text_auto=".2f",
        color_continuous_scale="RdBu_r",
        aspect="auto",
        title=f"{method.capitalize()} Correlation Heatmap"
    )
    fig.update_layout(height=700)
    return fig

# MISSING VALUE BAR CHART
def missing_bar(df):
    missing = df.isnull().sum()
    missing = missing[missing > 0]
    if len(missing) == 0:
        return None
    missing_df = pd.DataFrame({
        "Column": missing.index,
        "Missing Values": missing.values
    })

    fig = px.bar(
        missing_df,
        x="Column",
        y="Missing Values",
        title="Missing Values",
        template="plotly_white"
    )

    fig.update_layout(height=500)

    return fig

# OUTLIER BOX PLOT
def outlier_plot(df, column):

    fig = px.box(
        df,
        y=column,
        points="outliers",
        template="plotly_white",
        title=f"Outlier Detection - {column}"
    )
    fig.update_layout(height=500)
    return fig

# NUMERIC COLUMN DROPDOWN
def numeric_dropdown(df):
    return df.select_dtypes(
        include=np.number
    ).columns.tolist()

# CATEGORICAL COLUMN DROPDOWN
def categorical_dropdown(df):
    return df.select_dtypes(
        include=["object", "category"]
    ).columns.tolist()

# PLOT PREVIEW
def preview(df):
    return df.head()

# CHECK CATEGORICAL
def is_categorical(df, column):
    return (
        df[column].dtype == "object"
        or str(df[column].dtype) == "category"
    )

# COLUMN EXISTS
def column_exists(df, column):
    return column in df.columns

# VALUE COUNTS
def value_counts(df, column):
    return (
        df[column]
        .value_counts()
        .reset_index()
        .rename(columns={
            "index": column,
            column: "Count"
        })
    )

# CORRELATION MATRIX
def correlation_matrix(df, method="pearson"):
    return (
        df.select_dtypes(include=np.number)
        .corr(method=method)
    )