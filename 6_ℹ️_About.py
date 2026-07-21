import streamlit as st

st.set_page_config(
    page_title="About HR Portal",
    page_icon="ℹ️",
    layout="wide"
)

st.title("ℹ️ About HR Analytics Portal")

st.markdown("""
## 🏢 Company HR Intelligence System

This project is a professional HR Analytics Portal designed to analyze
employee data, understand workforce trends, and predict employee attrition
using Machine Learning.

The portal provides business insights through interactive dashboards,
analytics reports, and AI-based predictions.
""")

st.divider()

# Project objectives
st.subheader("🎯 Project Objectives")

objectives = [
    "Analyze employee demographics and workforce patterns",
    "Identify factors affecting employee attrition",
    "Provide interactive HR dashboards",
    "Predict employee attrition probability using Machine Learning",
    "Generate downloadable HR reports"
]

for item in objectives:
    st.write("✅", item)


st.divider()

# Technology stack
st.subheader("🛠️ Technologies Used")

col1, col2, col3 = st.columns(3)

with col1:
    st.info("""
    🐍 Python
    
    Data Processing
    Machine Learning
    """)

with col2:
    st.info("""
    📊 Streamlit
    
    Interactive Web Dashboard
    """)

with col3:
    st.info("""
    🤖 ML Model
    
    Employee Attrition Prediction
    """)


st.divider()

# ML information
st.subheader("🤖 Machine Learning Model")

st.write("""
The system uses a classification model to predict whether an employee
is likely to leave the organization.

The prediction output includes:
- Attrition Prediction
- Probability Score
- Business Insights
""")


st.divider()

# Developer
st.subheader("👨‍💻 Developer")

st.write("""
Developed as a Data Science & Machine Learning Portfolio Project.

Skills demonstrated:
- Data Analysis
- Data Visualization
- Machine Learning
- Streamlit Deployment
""")

st.success("🚀 HR Analytics Portal - Ready for Deployment")