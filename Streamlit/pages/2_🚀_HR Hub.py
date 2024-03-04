from cleaner import cleaned
import streamlit as st
import pandas as pd
import numpy as np
import joblib
import os


st.set_page_config(
    page_title="HR Hub",
    page_icon="🚀",
    layout="wide",
    initial_sidebar_state="expanded")


# Directories
parent_directory = os.path.dirname(os.path.dirname(__file__))
assets_dir = os.path.join(parent_directory, 'assets')
model_path = os.path.join(assets_dir, 'attr_model_class.joblib')
attr_path = os.path.join(assets_dir, 'attr.csv')

# ML model
model = joblib.load(model_path)

# Raw HR data
df = pd.read_csv(attr_path)

# HR data
data = df[['EmployeeNumber', 'Age', 'BusinessTravel', 'DailyRate', 'Department', 'DistanceFromHome', 'Education',
           'EducationField', 'EnvironmentSatisfaction', 'Gender', 'HourlyRate', 'JobInvolvement', 'JobLevel',
           'JobRole', 'JobSatisfaction', 'MaritalStatus', 'MonthlyIncome', 'MonthlyRate', 'NumCompaniesWorked',
           'OverTime', 'PercentSalaryHike', 'PerformanceRating', 'RelationshipSatisfaction', 'StandardHours',
           'StockOptionLevel', 'TotalWorkingYears', 'TrainingTimesLastYear', 'WorkLifeBalance', 'YearsAtCompany',
           'YearsInCurrentRole', 'YearsSinceLastPromotion', 'YearsWithCurrManager']]

# ML cleaned data
data2 = cleaned(data)

prediction = model.predict(data2.loc[:, data.columns[1:]])

data['Employee_Leaving'] = prediction
data['Employee_Leaving'] = data['Employee_Leaving'].map({0: "No", 1: "Yes"})

# Streamlit app starts here
st.title("HR Hub")
st.subheader("Search for an Employee Number and edit features")

st.sidebar.markdown("""The reason for the legend or keys is to:
- Reduced clutter and improved usability,
- Flexibility and adaptability and also 
- to create a Dynamic and interactive experience

As opposed to using radio buttons for the lengthy number of features we have.""")

text_input_container = st.empty()

selected = text_input_container.number_input("Enter an employee number to search for:",
                                             placeholder='Enter employee number here.....')

button_clicked = st.button("Search")

data_select = data2.query("EmployeeNumber == @selected")

st.table(data_select.set_index("EmployeeNumber"))

col_1, col_2, col_3 = st.columns(3)

with col_1:
    # property_area = st.radio("Business Travel", [0, 1, 2], index=None)
    st.subheader("Business Travel")
    st.text("""
    0 - Travel_Rarely
    1 - Travel_Frequently
    2 - Non-Travel""")

with col_2:
    # department = st.radio("Department", [0, 1, 2], index=None)
    st.subheader("Department")
    st.text("""
    0 - Sales
    1 - Research & Development
    2 - Human Resources""")

with col_3:
    # marital_status = st.radio("Marital Status", [0, 1, 2], index=None)
    st.subheader("Marital Status")
    st.text("""
    0 - Single
    1 - Married
    2 - Divorced""")

with col_3:
    # gender = st.radio("Gender", [0, 1], index=None)
    st.subheader("Gender")
    st.text("""
    0 - Male
    1 - Female""")

with col_1:
    # job_role = st.radio("Job Role", [0, 1, 2, 3, 4, 5, 6, 7, 8], index=None)
    st.subheader("Job Role")
    st.text("""
    0 - Sales Executive
    1 - Research Scientist
    2 - Laboratory Technician
    3 - Manufacturing Director
    4 - Healthcare Representative
    5 - Manager
    6 - Sales Representative
    7 - Research Director
    8 - Human Resources""")

with col_2:
    # eduction_field = st.radio("Department", [0, 1, 2, 3, 4, 5], index=None)
    st.subheader("Education Field")
    st.text("""
    0 - Life Sciences
    1 - Medical
    2 - Marketing
    3 - Technical Degree
    4 - Human Resources
    5 - Others""")

with col_3:
    # overtime = st.radio("OverTime", [0, 1], index=None)
    st.subheader("OverTime")
    st.text("""
    0 - No
    1 - Yes""")

st.subheader("Editable DataFrame")
st.text("Here you can edit each columns to see how it affects the employee")

try:
    editor = st.data_editor(data_select.loc[:, data.columns[1:-1]])
    arra_y = np.array(editor)
    predictions = model.predict_proba(arra_y)
    if predictions[0, 0] * 100 > predictions[0, 1] * 100:
        st.success(f"There is a {round(predictions[0, 0]*100)}% chance that Employee Number '{round(selected)}' "
                   f"stays with the company.")
    elif predictions[0, 1] * 100 > predictions[0, 0] * 100:
        st.error(f"There is a {round(predictions[0, 1]*100)}% chance that Employee Number '{round(selected)}' "
                 f"leaves the company.")
    else:
        st.warning(f"There is a {round(predictions[0, 1]*100)}% chance that Employee Number '{round(selected)}'"
                   f"or goes")
except ValueError:
    st.warning("Search for employee number")

