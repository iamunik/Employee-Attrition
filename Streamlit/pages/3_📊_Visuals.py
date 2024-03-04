from cleaner import clean_analysis, level_columns, create_bins, four_options, years, values
import plotly.express as px
import streamlit as st
import pandas as pd
import os


st.set_page_config(
    page_title="HR Visuals",
    page_icon="📊",
    layout="wide",
    initial_sidebar_state="expanded")


st.title("Chart Section")
st.subheader("G-Limited")

parent_directory = os.path.dirname(os.path.dirname(__file__))
assets_dir = os.path.join(parent_directory, 'assets')
cleaned_path = os.path.join(assets_dir, 'attr.csv')

# Read the data
data_ = pd.read_csv(cleaned_path)

# Initial data cleaning
cleaned_data = clean_analysis(data_)

# List of columns to be cleaned (All columns grouped based on similarity)
lvl_columns = ['JobLevel', 'StockOptionLevel']
column = ['TotalWorkingYears', 'YearsAtCompany']
columns = ['EnvironmentSatisfaction', 'RelationshipSatisfaction', 'JobInvolvement', 'JobSatisfaction']
yrs = ['TrainingTimesLastYear', 'YearsInCurrentRole', 'YearsSinceLastPromotion', 'YearsWithCurrManager']

# All function used are defined in cleaner.py
for i in columns:
    four_options(i, cleaned_data)

for i in lvl_columns:
    level_columns(i, cleaned_data)

for i in column:
    create_bins(i, cleaned_data)

for i in yrs:
    years(i, cleaned_data)

# Final Data
final_data = cleaned_data[['AgeGroup', 'Gender', 'MaritalStatus', 'Attrition', 'BusinessTravel', 'DistanceFrom_Home',
                           'Department', 'Education', 'EducationField', 'EnvironmentSatisfaction', 'JobInvolvement',
                           'JobLevel', 'JobRole', 'JobSatisfaction', 'HourlyRate', 'DailyRate', 'MonthlyIncome',
                           'MonthlyRate', 'NumCompaniesWorked', 'OverTime', 'PercentSalaryHike', 'PerformanceRating',
                           'RelationshipSatisfaction', 'StandardHours', 'StockOptionLevel', 'TotalWorkingYears',
                           'TrainingTimesLastYear', 'WorkLifeBalance', 'YearsAtCompany', 'YearsInCurrentRole',
                           'YearsSinceLastPromotion', 'YearsWithCurrManager']]
final_data['Attrition'] = final_data["Attrition"].map({"Yes": "Inactive", "No": "Active"})

# Selection box for filter
selection = st.selectbox("Filter by active or inactive staffs", ('Active', 'Inactive'), index=None)

# Condition to activate filter options
if not selection:
    data = final_data
else:
    data = final_data.query("Attrition == @selection")


# Function defined in cleaner.py, to apply value_counts() and reset index
marital = values(data, 'MaritalStatus')
department = values(data, 'Department')
attrition = values(data, "Attrition")
degree = values(data, "Education")
gender = values(data, 'Gender')
age = values(data, "AgeGroup")

# VISUALS :)
fig_attr = px.bar(attrition,
                  x='category',
                  y='counts',
                  text='counts',
                  title="Number of staffs (Active and Inactive)",
                  labels={"counts": " ", "category": "Attrition"},
                  color_discrete_sequence=px.colors.qualitative.Dark2)

fig_education = px.bar(degree,
                       x='category',
                       y='counts',
                       text='counts',
                       title="Educational Qualification of Staffs",
                       labels={"counts": " ", "category": "Educational Qualification"},
                       color_discrete_sequence=px.colors.qualitative.Dark2)

fig_age = px.bar(age,
                 x='category',
                 y='counts',
                 text='counts',
                 title="Age Group of Staffs",
                 labels={"counts": " ", "category": "Age Group"},
                 color_discrete_sequence=px.colors.qualitative.Dark2)

fig_gender = px.pie(gender,
                    values='counts',
                    names='category',
                    title="Gender distribution of staffs (%)",
                    hole=0.5,
                    color_discrete_sequence=px.colors.qualitative.Dark2)

fig_marital = px.pie(marital,
                     values='counts',
                     names='category',
                     title="Marital status of staffs (%)",
                     hole=0.5,
                     color_discrete_sequence=px.colors.qualitative.Dark2)

fig_dept = px.pie(department,
                  values='counts',
                  names='category',
                  hole=0.5,
                  title="Percentage of Staffs in each department",
                  color_discrete_sequence=px.colors.qualitative.Dark2)


col = st.columns((2, 2), gap='medium')

with col[0]:
    st.plotly_chart(fig_attr, use_container_width=True)

with col[1]:
    st.plotly_chart(fig_gender, use_container_width=True)

with col[0]:
    st.plotly_chart(fig_marital, use_container_width=True)

with col[1]:
    st.plotly_chart(fig_education, use_container_width=True)

with col[0]:
    st.plotly_chart(fig_age, use_container_width=True)

with col[1]:
    st.plotly_chart(fig_dept, use_container_width=True)
