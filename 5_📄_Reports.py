import streamlit as st
import pandas as pd

st.set_page_config(
    page_title="HR Reports",
    page_icon="📄",
    layout="wide"
)

# Load dataset
@st.cache_data
def load_data():
    df = pd.read_csv("data/WA_Fn-UseC_-HR-Employee-Attrition.csv")
    return df

df = load_data()

st.title("📄 HR Analytics Reports")
st.markdown("Generate business-style employee reports from HR data.")

st.divider()

# Summary cards
col1, col2, col3, col4 = st.columns(4)

with col1:
    st.metric(
        "Total Employees",
        len(df)
    )

with col2:
    attrition_count = (df["Attrition"] == "Yes").sum()
    st.metric(
        "Employees Left",
        attrition_count
    )

with col3:
    attrition_rate = round(
        (attrition_count / len(df)) * 100,
        2
    )
    st.metric(
        "Attrition Rate",
        f"{attrition_rate}%"
    )

with col4:
    avg_age = round(df["Age"].mean(), 1)
    st.metric(
        "Average Age",
        avg_age
    )


st.divider()

# Department report
st.subheader("🏢 Department-wise Report")

dept_report = (
    df.groupby("Department")["Attrition"]
    .value_counts()
    .unstack()
    .fillna(0)
)

st.dataframe(
    dept_report,
    use_container_width=True
)


st.divider()

# Job role report
st.subheader("💼 Job Role Analysis")

role_report = (
    df.groupby("JobRole")
    .agg(
        Employees=("EmployeeNumber","count"),
        Average_Age=("Age","mean")
    )
    .reset_index()
)

role_report["Average_Age"] = role_report["Average_Age"].round(1)

st.dataframe(
    role_report,
    use_container_width=True
)


st.divider()

# Download report

report_csv = role_report.to_csv(index=False)

st.download_button(
    label="📥 Download HR Report",
    data=report_csv,
    file_name="HR_Report.csv",
    mime="text/csv"
)