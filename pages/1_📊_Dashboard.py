import streamlit as st
import pandas as pd
import plotly.express as px

from utils import load_css

load_css()

st.set_page_config(
    page_title="HR Dashboard",
    page_icon="📊",
    layout="wide"
)


# Load Dataset
@st.cache_data
def load_data():
    df = pd.read_csv("data/WA_Fn-UseC_-HR-Employee-Attrition.csv")
    return df


df = load_data()


# Title
st.title("📊 HR Workforce Dashboard")
st.markdown(
    "Interactive overview of employee demographics and workforce insights."
)

st.divider()


# KPI Cards
col1, col2, col3, col4 = st.columns(4)

with col1:
    st.metric(
        "Total Employees",
        len(df)
    )

with col2:
    attrition = (df["Attrition"] == "Yes").sum()
    st.metric(
        "Attrition Count",
        attrition
    )

with col3:
    rate = round((attrition / len(df)) * 100, 2)
    st.metric(
        "Attrition Rate",
        f"{rate}%"
    )

with col4:
    avg_age = round(df["Age"].mean(), 1)
    st.metric(
        "Average Age",
        avg_age
    )


st.divider()


# Charts

col1, col2 = st.columns(2)


with col1:
    st.subheader("🏢 Department Distribution")

    dept = df["Department"].value_counts()

    fig1 = px.bar(
        dept,
        x=dept.index,
        y=dept.values,
        labels={
            "x": "Department",
            "y": "Employees"
        }
    )

    st.plotly_chart(
        fig1,
        use_container_width=True
    )


with col2:
    st.subheader("🚪 Attrition Overview")

    attrition_data = df["Attrition"].value_counts()

    fig2 = px.pie(
        values=attrition_data.values,
        names=attrition_data.index,
        hole=0.4
    )

    st.plotly_chart(
        fig2,
        use_container_width=True
    )


st.divider()


# Age Analysis

st.subheader("📈 Employee Age Analysis")

fig3 = px.histogram(
    df,
    x="Age",
    nbins=20,
    title="Age Distribution"
)

st.plotly_chart(
    fig3,
    use_container_width=True
)
