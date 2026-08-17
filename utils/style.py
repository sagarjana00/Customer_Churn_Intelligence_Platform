from pathlib import Path
import streamlit as st


def load_css():
    css_path = Path(__file__).resolve().parent.parent / "assets" / "styles" / "style.css"

    with open(css_path, "r", encoding="utf-8") as file:
        st.markdown(
            f"<style>{file.read()}</style>",
            unsafe_allow_html=True
        )