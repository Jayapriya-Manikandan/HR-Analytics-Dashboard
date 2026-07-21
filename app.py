import streamlit as st

from utils import load_css

st.set_page_config(
    page_title="HR Intelligence Portal",
    page_icon="🏢",
    layout="wide"
)

load_css()


# Sidebar Branding

st.sidebar.title("🏢 HR Portal")

# Uncomment after adding logo.png inside assets folder
# st.sidebar.image(
#     "assets/logo.png",
#     width=120
# )

st.sidebar.markdown(
    """
    ---
    **AI Employee Analytics System**

    Navigate through:

    📊 Dashboard  
    📈 Analytics  
    🤖 Prediction  
    📋 Dataset  
    📄 Reports  
    ℹ️ About

    ---

    **Built With**

    🐍 Python  
    📊 Streamlit  
    🤖 Machine Learning
    """
)


# Main Header

st.markdown(
    """
    <div style="text-align:center;">

    <h1>🏢 HR Intelligence Portal</h1>

    <h3>
    AI Powered Employee Analytics System
    </h3>

    <p>
    Analyze workforce trends, predict employee attrition,
    and generate business insights.
    </p>

    </div>
    """,
    unsafe_allow_html=True
)


st.divider()


# Feature Cards

col1, col2, col3 = st.columns(3)


with col1:
    st.info(
        """
        ### 📊 Analytics Dashboard

        ✔ Employee insights  
        ✔ Department analysis  
        ✔ Workforce statistics
        """
    )


with col2:
    st.info(
        """
        ### 🤖 AI Prediction

        ✔ ML based prediction  
        ✔ Attrition probability  
        ✔ Risk analysis
        """
    )


with col3:
    st.info(
        """
        ### 📄 HR Reports

        ✔ Business reports  
        ✔ CSV download  
        ✔ Data summaries
        """
    )


st.divider()


st.subheader("🚀 Portal Capabilities")


features = [
    "Interactive employee analytics",
    "Workforce trend analysis",
    "Machine Learning attrition prediction",
    "Advanced filtering system",
    "Downloadable HR reports"
]


for feature in features:
    st.success("✓ " + feature)


st.divider()


st.markdown(
    """
    <div style="text-align:center;">
    HR Intelligence Portal | Data Science & Machine Learning Project
    </div>
    """,
    unsafe_allow_html=True
)