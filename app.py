# Importing Libraries for Steamlit Dashboard 

import pandas as pd 
import numpy as np
import streamlit as st 

# load in data
diabetes = pd.read_csv('diabetes.csv')
diabetes = diabetes.head(100)

## Header ##
st.header('Diagnostic Measurements for Predicting Diabetes Among Females')
st.subheader('By: Alice Wu HHA507 Data Science at Stony Brook University')
## Caption ##
st.caption('This dashboard uses a dataset originally from the National Institute of Diabetes and Digestive and Kidney Diseases. The objective of the dataset is to diagnostically predict whether a patient has diabetes, based on certain diagnostic measurements included in the dataset. Constraints of the Dataset: (1)All patients here are females and at least 21 years old of Pima Indian heritage.')

## Toggle ##
if st.checkbox('Show first 100 records of Diabetes Prediction Dataset'):
    st.dataframe(diabetes)

## Code Block  ##

## Dataframe and Chart 1: BMI Levels ##
st.subheader('BMI Levels Among Patients')

diabetes = pd.read_csv('diabetes.csv')

BMI = diabetes['BMI'].value_counts()

st.bar_chart(BMI)

st.caption("This bar chart illustrates the count of unique BMI levels among female patients.")

## DataFrame and Chart 2: Vitals Among Patients ##
st.subheader('Vitals Levels Among Patients')

chart_data = pd.DataFrame(np.random.randn(20, 4), columns=['Glucose','Insulin','BloodPressure', 'Pregnancies'])

st.line_chart(chart_data)

st.caption("This line chart illustrates to vitals levels of female patients used as diagnostic measurements to predict diabetes.")
