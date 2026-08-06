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




def plot_model_comparison(df, metric):
    import plotly.express as px

    fig = px.bar(
        df.sort_values(metric, ascending=False),
        x="Model",
        y=metric,
        color="Model",
        text=metric,
        template="plotly_white",
        title=f"{metric} Comparison"
    )

    fig.update_traces(texttemplate="%{text:.3f}")

    fig.update_layout(
        title_x=0.5,
        showlegend=False,
        xaxis_title="",
        yaxis_title=metric
    )

    return fig