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



def metric_cards(metrics):
    cols = st.columns(len(metrics))

    for col, (label, value) in zip(cols, metrics):
        with col:
            st.metric(label, value)


def business_insight(text: str):
    st.info(f"**Business Insight:** {text}")








