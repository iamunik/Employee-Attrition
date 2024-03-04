import pandas as pd
import numpy as np


def cleaned(data_cleaned):
    data_cleaned['BusinessTravel'] = data_cleaned['BusinessTravel'].map({'Travel_Rarely': 0,
                                                                         'Travel_Frequently': 1,
                                                                         'Non-Travel': 2}).astype('int64')
    
    data_cleaned['Department'] = data_cleaned['Department'].map({'Sales': 0,
                                                                 'Research & Development': 1,
                                                                 'Human Resources': 2}).astype('int64')

    data_cleaned['EducationField'] = data_cleaned['EducationField'].map({'Life Sciences': 0,
                                                                         'Medical': 1,
                                                                         'Marketing': 2,
                                                                         'Technical Degree': 3,
                                                                         'Human Resources': 4,
                                                                         'Other': 5}).astype('int64')

    data_cleaned['Gender'] = data_cleaned['Gender'].map({'Male': 0,
                                                         'Female': 1}).astype('int64')

    data_cleaned['OverTime'] = data_cleaned['OverTime'].map({'No': 0,
                                                             'Yes': 1}).astype('int64')

    data_cleaned['MaritalStatus'] = data_cleaned['MaritalStatus'].map({'Single': 0,
                                                                       'Married': 1,
                                                                       'Divorced': 2}).astype('int64')

    data_cleaned['JobRole'] = data_cleaned['JobRole'].map({'Sales Executive': 0,
                                                           'Research Scientist': 1,
                                                           'Laboratory Technician': 2,
                                                           'Manufacturing Director': 3,
                                                           'Healthcare Representative': 4,
                                                           'Manager': 5,
                                                           'Sales Representative': 6,
                                                           'Research Director': 7,
                                                           'Human Resources': 8}).astype('int64')

    return data_cleaned


def clean_analysis(data):
    # AgeGroup
    bins_age = [18, 20, 30, 40, 50, 60]
    group_age = ['<20', '20-29', '30-39', '40-49', '50-59']

    # Filling NaN with 60+ because we used the right False keyword which will by default ignore the rightmost digit (60)
    data['AgeGroup'] = pd.cut(data['Age'],
                              bins=bins_age,
                              labels=group_age,
                              right=False).cat.add_categories('60+').fillna('60+')

    # Business Travel
    data.BusinessTravel = data.BusinessTravel.str.replace('_', ' ').str.replace("-", " ")

    # Distance From Home
    bins_education = [1, 11, 20, 30]
    labels_education = ['Very Close', 'Close', 'Far']
    data['DistanceFrom_Home'] = pd.cut(data['DistanceFromHome'],
                                       bins=bins_education,
                                       labels=labels_education,
                                       right=False)

    # Education
    data.Education = data.Education.map({1: "Below College",
                                         2: "College",
                                         3: "Bachelor",
                                         4: "Master",
                                         5: "Doctor"})

    # Performance Rating
    data.PerformanceRating = data.PerformanceRating.map({3: "Excellent",
                                                         4: "Outstanding"})

    # WorkLife Balance
    data.WorkLifeBalance = data.WorkLifeBalance.map({1: 'Bad',
                                                     2: 'Good',
                                                     3: 'Better',
                                                     4: 'Best'})
    return data


# Clean columns that have four options 1 - 4
# ['EnvironmentSatisfaction', 'RelationshipSatisfaction', 'JobInvolvement', 'JobSatisfaction']
def four_options(value, data):
    data[value] = data[value].map({1: 'Low',
                                   2: 'Medium',
                                   3: 'High',
                                   4: 'Very High'})


# Clean columns that deal with levels
# ['JobLevel', 'StockOptionLevel']
def level_columns(value, data):
    data[value] = "Lvl " + data[value].astype(str)


# Define a function to create the BINS for columns that deals with years
# ['TotalWorkingYears', 'YearsAtCompany']
def create_bins(column, data):
    bins = [0, 10, 20, 30]
    group = ['0-10 years', '11-20 years', '21-29 years']

    data[column] = pd.cut(data[column],
                          bins=bins,
                          labels=group,
                          right=False).cat.add_categories('31-40 years').fillna('31-40 years')


# Function to append years or year to columns that deals with years
# ['TrainingTimesLastYear', 'YearsInCurrentRole', 'YearsSinceLastPromotion', 'YearsWithCurrManager']
def years(col, data):
    data[col] = data[col].astype(str) + " " + np.where(data[col] == 0, 'year', 'years')


def values(var, a: str):
    attr = var[a].value_counts().reset_index()
    attr.columns = ['category', 'counts']
    return attr
