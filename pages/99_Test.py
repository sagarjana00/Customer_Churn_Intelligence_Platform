import streamlit as st

from utils.data_loader import load_preprocessor

preprocessor = load_preprocessor()

st.write(preprocessor.feature_names_in_)