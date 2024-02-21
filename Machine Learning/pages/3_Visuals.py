import streamlit as st
import os
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

st.title("Chart Section")
st.subheader("This is experimental :)")

parent_directory = os.path.dirname(os.path.dirname(__file__))
assets_dir = os.path.join(parent_directory, 'assets')
cleaned_path = os.path.join(assets_dir, 'attr_cleaned.csv')

# attrition = data['Attrition'].value_counts()
# gender = data['Gender'].value_counts()
# marital = data['MaritalStatus'].value_counts()
# department = data['Department'].value_counts()
#
# fig_attr = px.bar(attrition, title="Attrition")
# fig_gender = px.pie(gender, values="count", names=['Male', "Female"], title="Gender distribution of staffs")
# fig_marital = px.pie(marital, values='count', names=['Married', 'Single', 'Divorced'], title="Marital status of staffs")
# fig_dept = px.pie(department, values='count', names=['Research & Development', 'Sales', 'Human Resources'])
#
# col1, col2 = st.columns(2)
#
# with col1:
#     st.plotly_chart(fig_attr, use_container_width=True)
#
#
# with col2:
#     st.plotly_chart(fig_gender, use_container_width=True)
#
# with col1:
#     # st.table(department)
#     st.plotly_chart(fig_marital, use_container_width=True)
#
# with col2:
#     st.plotly_chart(fig_dept, use_container_width=False)

data = pd.read_csv(cleaned_path)
attr = data['Attrition'].value_counts()

st.bar_chart(attr)
st.table(attr)

col1, col2, col3 = st.columns(3)

# with col1:
    # st.bar_chart(plt.plot(model))

