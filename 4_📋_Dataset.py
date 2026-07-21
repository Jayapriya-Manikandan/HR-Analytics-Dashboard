import streamlit as st
import pandas as pd

# Page configuration
st.set_page_config(
    page_title="HR Dataset",
    page_icon="📋",
    layout="wide"
)

# Load dataset
@st.cache_data
def load_data():
    df = pd.read_csv("data/WA_Fn-UseC_-HR-Employee-Attrition.csv")
    return df

df = load_data()

# Title
st.title("📋 Employee Dataset Explorer")
st.markdown("Explore and filter employee records from the HR database.")

st.divider()

# Dataset information cards
col1, col2, col3 = st.columns(3)

with col1:
    st.metric("Total Employees", df.shape[0])

with col2:
    st.metric("Total Features", df.shape[1])

with col3:
    st.metric("Missing Values", df.isnull().sum().sum())


st.divider()

# Search
st.subheader("🔍 Search Employee Data")

search = st.text_input(
    "Search by Employee Number or Job Role"
)

filtered_df = df.copy()

if search:
    filtered_df = df[
        df.astype(str)
        .apply(
            lambda row: row.str.contains(search, case=False).any(),
            axis=1
        )
    ]

# Filters
st.subheader("🎯 Filters")

col1, col2 = st.columns(2)

with col1:
    department = st.multiselect(
        "Select Department",
        df["Department"].unique()
    )

with col2:
    jobrole = st.multiselect(
        "Select Job Role",
        df["JobRole"].unique()
    )


if department:
    filtered_df = filtered_df[
        filtered_df["Department"].isin(department)
    ]

if jobrole:
    filtered_df = filtered_df[
        filtered_df["JobRole"].isin(jobrole)
    ]


st.divider()

# Display dataset
st.subheader("📊 Employee Records")

st.dataframe(
    filtered_df,
    use_container_width=True
)


# Download option
csv = filtered_df.to_csv(index=False)

st.download_button(
    label="📥 Download Dataset CSV",
    data=csv,
    file_name="HR_Filtered_Dataset.csv",
    mime="text/csv"
)