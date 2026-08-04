import streamlit as st

def section_title(title: str):
    st.divider()
    st.header(title)



def footer():
    st.divider()

    st.caption(
        "Developed by Sagar Jana | DATA lover"
    )

    st.caption(
        "Python • Scikit-learn • XGBoost • SHAP • Streamlit"
    )




def hero_section(title: str, subtitle: str):
    st.title(title)
    st.markdown(f"### {subtitle}")


