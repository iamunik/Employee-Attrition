from cleaner import cleaned
import streamlit as st
import pandas as pd
import joblib
import os

st.header("Employee Data")
st.subheader("G-Limited employees")

# Directories
parent_directory = os.path.dirname(os.path.dirname(__file__))
assets_dir = os.path.join(parent_directory, 'assets')
model_path = os.path.join(assets_dir, 'attr_model_class.joblib')
attr_path = os.path.join(assets_dir, 'attr.csv')

# ML model
model = joblib.load(model_path)

# Normal data
df = pd.read_csv(attr_path)

data = df[['EmployeeNumber', 'Age', 'BusinessTravel', 'DailyRate', 'Department', 'DistanceFromHome', 'Education',
           'EducationField', 'EnvironmentSatisfaction', 'Gender', 'HourlyRate', 'JobInvolvement', 'JobLevel',
           'JobRole', 'JobSatisfaction', 'MaritalStatus', 'MonthlyIncome', 'MonthlyRate', 'NumCompaniesWorked',
           'OverTime', 'PercentSalaryHike', 'PerformanceRating', 'RelationshipSatisfaction', 'StandardHours',
           'StockOptionLevel', 'TotalWorkingYears', 'TrainingTimesLastYear', 'WorkLifeBalance', 'YearsAtCompany',
           'YearsInCurrentRole', 'YearsSinceLastPromotion', 'YearsWithCurrManager']]

# Cleaned data
data2 = cleaned(data.copy)

a = model.predict(data2.loc[:, data2.columns[1:]])
data['Employee_Leaving'] = a
data['Employee_Leaving'] = data['Employee_Leaving'].map({0: "No", 1: "Yes"})

st.dataframe(data.set_index('EmployeeNumber'), use_container_width=True)
