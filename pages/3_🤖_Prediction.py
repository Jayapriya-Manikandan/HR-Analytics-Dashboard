import streamlit as st
import pandas as pd
import joblib

from utils import load_css

load_css()

st.set_page_config(
    page_title="HR Prediction",
    page_icon="🤖",
    layout="wide"
)


# Load Model
@st.cache_resource
def load_model():
    model = joblib.load("model/attrition_model.pkl")
    encoders = joblib.load("model/label_encoders.pkl")
    return model, encoders


model, encoders = load_model()


# Load Dataset
@st.cache_data
def load_data():
    return pd.read_csv(
        "data/WA_Fn-UseC_-HR-Employee-Attrition.csv"
    )


df = load_data()

all_features = df.drop(
    "Attrition",
    axis=1
).columns


st.title("🤖 Employee Attrition Prediction")

st.write(
    "AI powered HR system to predict employee attrition risk."
)

st.divider()


input_data = {}


# Personal Details

st.subheader("👤 Personal Details")

col1, col2 = st.columns(2)

with col1:
    input_data["Age"] = st.number_input(
        "Age",
        value=int(df["Age"].mean())
    )

with col2:
    input_data["Gender"] = st.selectbox(
        "Gender",
        df["Gender"].unique()
    )


# Job Details

st.subheader("💼 Job Information")

col1, col2 = st.columns(2)

with col1:

    input_data["Department"] = st.selectbox(
        "Department",
        df["Department"].unique()
    )

    input_data["JobRole"] = st.selectbox(
        "Job Role",
        df["JobRole"].unique()
    )


with col2:

    input_data["JobLevel"] = st.selectbox(
        "Job Level",
        sorted(df["JobLevel"].unique())
    )

    input_data["YearsAtCompany"] = st.number_input(
        "Years At Company",
        value=int(df["YearsAtCompany"].mean())
    )


# Salary Details

st.subheader("💰 Salary Information")

col1, col2 = st.columns(2)

with col1:

    input_data["MonthlyIncome"] = st.number_input(
        "Monthly Income",
        value=int(df["MonthlyIncome"].mean())
    )


with col2:

    input_data["OverTime"] = st.selectbox(
        "OverTime",
        df["OverTime"].unique()
    )


# Satisfaction Details

st.subheader("😊 Satisfaction Details")

col1, col2 = st.columns(2)

with col1:

    input_data["JobSatisfaction"] = st.selectbox(
        "Job Satisfaction",
        sorted(df["JobSatisfaction"].unique())
    )


with col2:

    input_data["WorkLifeBalance"] = st.selectbox(
        "Work Life Balance",
        sorted(df["WorkLifeBalance"].unique())
    )


st.divider()


if st.button("🔮 Predict Attrition"):

    input_df = pd.DataFrame(
        [input_data]
    )


    # Add missing features

    for column in all_features:

        if column not in input_df.columns:

            if df[column].dtype.kind == "O":

                input_df[column] = df[column].mode()[0]

            else:

                input_df[column] = pd.to_numeric(
                    df[column],
                    errors="coerce"
                ).median()


    # Encoding

    for column, encoder in encoders.items():

        if column in input_df.columns:

            input_df[column] = encoder.transform(
                input_df[column]
            )


    input_df = input_df[all_features]


    # Prediction

    prediction = model.predict(
        input_df
    )

    probability = model.predict_proba(
        input_df
    )


    risk = round(
        probability[0][1] * 100,
        2
    )


    if prediction[0] == 1:

        st.error(
            "🚨 Employee may leave the company"
        )

    else:

        st.success(
            "✅ Employee likely to stay"
        )


    st.metric(
        "Attrition Probability",
        f"{risk}%"
    )


    # Risk Analysis

    st.subheader("📊 Risk Analysis")

    st.progress(
        risk / 100
    )


    if risk < 30:

        st.success(
            "🟢 Low Risk - Employee is likely to stay"
        )

    elif risk < 70:

        st.warning(
            "🟡 Medium Risk - Employee needs attention"
        )

    else:

        st.error(
            "🔴 High Risk - Employee may leave soon"
        )


    # Download Report

    report = pd.DataFrame(
        {
            "Prediction":
            [
                "Leave" if prediction[0] == 1 else "Stay"
            ],

            "Probability":
            [
                f"{risk}%"
            ],

            "Risk_Level":
            [
                "Low" if risk < 30 else "Medium" if risk < 70 else "High"
            ]
        }
    )


    st.download_button(
        label="📥 Download Prediction Report",
        data=report.to_csv(index=False),
        file_name="HR_Prediction_Report.csv",
        mime="text/csv"
    )
