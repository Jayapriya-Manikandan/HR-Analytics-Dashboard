import streamlit as st
import pandas as pd
import plotly.express as px

from utils import load_css

load_css()

st.set_page_config(
    page_title="HR Analytics",
    page_icon="📈",
    layout="wide"
)


# Load Dataset
@st.cache_data
def load_data():
    df = pd.read_csv("data/WA_Fn-UseC_-HR-Employee-Attrition.csv")
    return df


df = load_data()


st.title("📈 HR Workforce Analytics")
st.markdown(
    "Deep analysis of employee trends and organizational patterns."
)

st.divider()


# Filters

st.subheader("🔍 Analytics Filters")

col1, col2 = st.columns(2)

with col1:
    department = st.selectbox(
        "Select Department",
        ["All"] + list(df["Department"].unique())
    )

with col2:
    gender = st.selectbox(
        "Select Gender",
        ["All"] + list(df["Gender"].unique())
    )


filtered_df = df.copy()

if department != "All":
    filtered_df = filtered_df[
        filtered_df["Department"] == department
    ]

if gender != "All":
    filtered_df = filtered_df[
        filtered_df["Gender"] == gender
    ]


st.divider()


# Trend Analysis

st.subheader("📊 Employee Distribution")


col1, col2 = st.columns(2)


with col1:
    role_count = (
        filtered_df["JobRole"]
        .value_counts()
        .reset_index()
    )

    role_count.columns = [
        "Job Role",
        "Count"
    ]

    fig1 = px.bar(
        role_count,
        x="Job Role",
        y="Count",
        title="Employees by Job Role"
    )

    st.plotly_chart(
        fig1,
        use_container_width=True
    )


with col2:

    age_data = filtered_df.groupby(
        "Age"
    ).size().reset_index(
        name="Employees"
    )

    fig2 = px.line(
        age_data,
        x="Age",
        y="Employees",
        markers=True,
        title="Age Trend Analysis"
    )

    st.plotly_chart(
        fig2,
        use_container_width=True
    )


st.divider()


# Attrition Trend

st.subheader("🚪 Attrition Analysis")


attrition_df = (
    filtered_df["Attrition"]
    .value_counts()
    .reset_index()
)

attrition_df.columns = [
    "Attrition",
    "Employees"
]


fig3 = px.pie(
    attrition_df,
    values="Employees",
    names="Attrition",
    hole=0.4,
    title="Employee Attrition Status"
)

st.plotly_chart(
    fig3,
    use_container_width=True
)


st.divider()


# Salary Analysis

st.subheader("💰 Income Analysis")

fig4 = px.scatter(
    filtered_df,
    x="MonthlyIncome",
    y="JobRole",
    color="Attrition",
    title="Income vs Attrition"
)

st.plotly_chart(
    fig4,
    use_container_width=True
)
