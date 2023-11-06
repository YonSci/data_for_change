# Import necessary libraries
import streamlit as st
import pandas as pd
import pickle


# Define the app layout
st.title('Vitamin/Mineral Deficiency Predictor')
st.sidebar.title('User Input Features')
st.sidebar.markdown('Please enter the following information:')


# Add user input fields
illness_type = st.sidebar.selectbox('Illness Type', ['Type 1 Diabetes', 'Type 2 Diabetes', 'Hypertension', 'Heart Disease'])
food_consumption_annual = st.sidebar.slider('Food Consumption (Annual)', 0, 100, 50)
tobacco_consumption_annual = st.sidebar.slider('Tobacco Consumption (Annual)', 0, 100, 50)
health_annual_consumption = st.sidebar.slider('Health Annual Consumption', 0, 100, 50)
total_annual_consumption_per_household = st.sidebar.slider('Total Annual Consumption per Household', 0, 100, 50)
poor_hh_below_poverty_line = st.sidebar.slider('Poor Households Below Poverty Line', 0, 100, 50)
received_SSN = st.sidebar.slider('Received Social Security Number', 0, 1, 0)
sugar_product = st.sidebar.slider('Sugar Product', 0, 1, 0)
age_categories = st.sidebar.selectbox('Age Categories', ['0-18', '19-30', '31-50', '51-70', '71+'])
household_latitude = st.sidebar.text_input('Household Latitude')
household_longitude = st.sidebar.text_input('Household Longitude')

# Make predictions
input_data = [[illness_type, food_consumption_annual, tobacco_consumption_annual, health_annual_consumption, total_annual_consumption_per_household, poor_hh_below_poverty_line, received_SSN, sugar_product, age_categories, household_latitude, household_longitude]]
input_df = pd.DataFrame(input_data, columns=['illness_type', 'food_consumption_annual', 'tobacco_consumption_annual', 'health_annual_consumption', 'total_annual_consumption_per_household', 'poor_hh_below_poverty_line', 'received_SSN', 'sugar_product', 'age_categories', 'household_latitude', 'household_longitude'])
prediction = model.predict(input_df)

# Display the results
st.subheader('Prediction')
st.write(prediction)
