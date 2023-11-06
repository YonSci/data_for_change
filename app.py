# Import necessary libraries
import streamlit as st
import pandas as pd
import pickle

# Load the saved model
with open('random_forest_model.pkl', 'rb') as f:
    model = pickle.load(f)

# Define the app layout
st.title('Vitamin/Mineral Deficiency Predictor')
st.sidebar.title('User Input Features')
st.sidebar.markdown('Please enter the following information:')