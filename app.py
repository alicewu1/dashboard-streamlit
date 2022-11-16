# Importing Libraries for Steamlit Dashboard 

import pandas as pd 
import numpy as np
import streamlit as st 

# load in data
diabetes = pd.read_csv('diabetes.csv')
diabetes = diabetes.head(100)

## Header ##
st.header('Diabetes Prediction Among Females')

## Caption ##
st.caption('This dataset is originally from the National Institute of Diabetes and Digestive and Kidney Diseases. The objective of the dataset is to diagnostically predict whether a patient has diabetes, based on certain diagnostic measurements included in the dataset. Several constraints were placed on the selection of these instances from a larger database. In particular, all patients here are females at least 21 years old of Pima Indian heritage.2')

## Toggle ##
if st.checkbox('Show first 100 records of Diabetes Prediction Dataset'):
    st.dataframe(diabetes)


## Charts ##

