import plotly.express as px
import pandas as pd


def plot_histogram(df: pd.DataFrame, feature: str):
    fig = px.histogram(
        df,
        x=feature,
        title=f"Distribution of {feature}",
        marginal="box",
        template="plotly_white"
    )

    fig.update_layout(
        title_x=0.5,
        xaxis_title=feature,
        yaxis_title="Count"
    )

    return fig



def plot_boxplot(df: pd.DataFrame, feature: str):
    fig = px.box(
        df,
        y=feature,
        title=f"Box Plot of {feature}",
        template="plotly_white"
    )

    fig.update_layout(
        title_x=0.5,
        yaxis_title=feature
    )

    return fig



def plot_histogram_by_churn(df: pd.DataFrame, feature: str):
    fig = px.histogram(
        df,
        x=feature,
        color="Churn",
        barmode="overlay",
        marginal="box",
        template="plotly_white",
        title=f"{feature} Distribution by Churn"
    )

    fig.update_layout(
        title_x=0.5,
        xaxis_title=feature,
        yaxis_title="Count"
    )

    return fig





def plot_countplot(df: pd.DataFrame, feature: str):
    fig = px.histogram(
        df,
        x=feature,
        color="Churn",
        barmode="group",
        template="plotly_white",
        title=f"{feature} Distribution by Churn"
    )

    fig.update_layout(
        title_x=0.5,
        xaxis_title=feature,
        yaxis_title="Count"
    )

    return fig