import streamlit as st

from utils.data_loader import load_dataset
from utils.visualization import plot_histogram

df = load_dataset()

fig = plot_histogram(df, "MonthlyCharges")

st.plotly_chart(fig, use_container_width=True)