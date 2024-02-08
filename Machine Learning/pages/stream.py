import streamlit as st
import pandas as pd
import joblib

model = joblib.load("attr_model_class.joblib")
df = pd.read_csv("attr.csv")
df2 = pd.read_csv("ml_attr.csv")
data = df[['EmployeeNumber', 'Age', 'BusinessTravel', 'DailyRate', 'Department', 'DistanceFromHome', 'Education',
           'EducationField', 'EnvironmentSatisfaction', 'Gender', 'HourlyRate', 'JobInvolvement', 'JobLevel',
           'JobRole', 'JobSatisfaction', 'MaritalStatus', 'MonthlyIncome', 'MonthlyRate', 'NumCompaniesWorked',
           'OverTime', 'PercentSalaryHike', 'PerformanceRating', 'RelationshipSatisfaction', 'StandardHours',
           'StockOptionLevel', 'TotalWorkingYears', 'TrainingTimesLastYear', 'WorkLifeBalance', 'YearsAtCompany',
           'YearsInCurrentRole', 'YearsSinceLastPromotion', 'YearsWithCurrManager']]

data2 = df2[['Age', 'BusinessTravel', 'DailyRate', 'Department', 'DistanceFromHome', 'Education',
             'EducationField', 'EnvironmentSatisfaction', 'Gender', 'HourlyRate', 'JobInvolvement', 'JobLevel',
             'JobRole', 'JobSatisfaction', 'MaritalStatus', 'MonthlyIncome', 'MonthlyRate', 'NumCompaniesWorked',
             'OverTime', 'PercentSalaryHike', 'PerformanceRating', 'RelationshipSatisfaction', 'StandardHours',
             'StockOptionLevel', 'TotalWorkingYears', 'TrainingTimesLastYear', 'WorkLifeBalance', 'YearsAtCompany',
             'YearsInCurrentRole', 'YearsSinceLastPromotion', 'YearsWithCurrManager']]


a = model.predict(data2)
data['Employee Leaving'] = a
data['Employee Leaving'] = data['Employee Leaving'].map({0: "No", 1: "Yes"})

col_1, col_2, col_3, col_4 = st.columns(4)

with col_1:
    st.text("Keyyy")

with col_2:
    st.text("Unkey")

with col_3:
    st.text("Tukay")

with col_4:
    st.text("$kay")

with col_1:
    st.text("Keyyy")

with col_2:
    st.text("Unkey")

with col_3:
    st.text("Tukay")

with col_4:
    st.text("$kay")


text_input_container = st.empty()

selected = text_input_container.number_input("Enter an employee number to search for:",
                                             placeholder='Enter employee number here.....')
st.table(data.head(2))

button_clicked = st.button("OK")

data_select = data.query("EmployeeNumber == @selected")

st.table(data_select)
# st.table(data_select[0, 1:])
