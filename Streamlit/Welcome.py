import streamlit as st
import os
from PIL import Image

st.markdown(
    """
    <style>
    .css-1jc7ptx, .e1ewe7hr3, .viewerBadge_container__1QSob,
    .styles_viewerBadge__1yB5_, .viewerBadge_link__1S137,
    .viewerBadge_text__1JaDK {
        display: none;
    }
    </style>
    """,
    unsafe_allow_html=True
)

st.title("G-Limited Human Resource Hub")
st.subheader("Enhancing Retention Strategies")

# Directories
parent_directory = os.path.dirname(os.path.dirname(__file__))
assets_dir = os.path.join(parent_directory, 'Machine Learning', 'assets')
# hr_png_path = os.path.join(assets_dir, 'hr.jpeg')
hr_png_path = "Streamlit/assets/hr.jpeg"

st.image(Image.open(hr_png_path), width=500)

st.markdown("""
Employee turnover is a significant challenge for organizations, impacting productivity, morale, and overall performance.
In response, this project introduces an innovative HR web application that leverages machine learning to predict
employee attrition and empowers HR professionals to proactively implement retention strategies. The system utilizes ML
algorithms to analyze employee data and identify patterns indicative of potential turnover. HR personnel can then 
experiment with various features to determine the most effective interventions for retaining staff or facilitating 
voluntary resignations.

## Functionalities of this web app
<b>The primary objective of the HR web application is to provide HR professionals with actionable insights into
employee retention and resignation factors. The following are detailed functions of the web app:</b>

- <b>Predictive Modeling:</b> Machine learning algorithms analyze historical data to forecast the likelihood of employee
turnover.
- <b>Feature Manipulation:</b> HR personnel can adjust various features such as compensation, job satisfaction, and
training opportunities to observe their influence on turnover predictions.
- <b>Scenario Planning:</b> Users can simulate different scenarios to understand the potential outcomes of specific 
interventions or policy changes.
- <b>Data Ingestion:</b> Employee data, including demographics, performance metrics, and job-related variables, is
collected from internal HR systems.

## Benefits:
<b>Implementing the HR resource web application offers several benefits for organizations:</b>
- <b>Proactive Retention:</b> By identifying at-risk employees early, organizations can implement targeted interventions
to mitigate turnover.
- <b>Data-Driven Decision Making:</b> HR professionals can make informed decisions based on predictive analytics,
reducing reliance on guesswork.
- <b>Cost Savings:</b> Lowering employee turnover rates can result in significant cost savings associated with
recruitment, training, and lost productivity.
- <b>Enhanced Employee Engagement:</b> Tailored retention strategies can improve job satisfaction and engagement,
leading to higher morale and productivity.
- <b>Continuous Improvement:</b> The ability to experiment with different scenarios enables organizations to
continuously refine their retention strategies based on real-time feedback.

## Conclusion:
The HR resource web application represents a valuable tool for organizations seeking to address the challenge of 
employee turnover. By harnessing the power of machine learning and data-driven decision-making, HR professionals can 
proactively identify and retain valuable talent, ultimately contributing to the long-term success and sustainability of
the organization.
""", unsafe_allow_html=True)

st.warning("Development is still ongoing to improve the efficiency of the ML model")
