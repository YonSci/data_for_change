# Import necessary libraries
import streamlit as st
import pandas as pd
import pickle


st.sidebar.success("Select a page")


        display = Image.open('emi_logo.jpg')

        authenticator.logout("Logout", "sidebar")
        st.sidebar.title(f"Welcome!, {name}")


        col1, col2= st.columns((3,7))
        col1.image(display, width = 200)
        col2.title("Ethiopian Meteorological Institute Climate Data Analysis Tool (EMI-CDAT)")
        st.markdown(
            """
            ---
            """
            )
        st.markdown(
                """
                The **Ethiopian Meteorological Institute Climate Data Analysis Tool (EMI-CDAT)** web application is designed to automate the data work flow at the Meteorological Data and Climatology Directorate and to generate charts, graphs, maps, and tabular outputs, as well as intermediate results required for the production of climate bulletins. 
                
                **EMI-CDAT** is build & deploy using the [Streamlit](https://docs.streamlit.io/) application development tool. The [Altair](https://altair-viz.github.io/index.html), [Bokeh](https://bokeh.org/), [Holoviews](https://holoviews.org/), [Plotly  Graphing Libraries](https://plotly.com/graphing-libraries/), [SciPy](https://scipy.org/), [NCAR PyNGL](https://www.pyngl.ucar.edu/index.shtml), & [PyNIO](https://www.pyngl.ucar.edu/index.shtml) visualizations packages are used to improve the statistical visualization and mapping capabilities of the App.
                """
                )
        st.markdown(
                    """
                    ---
                    EMI-CDAT App features includes:
                    - Reading input data in tabular formats such as Microsoft Excel spreadsheet (.xlsx) & comma separate value (.csv) & covert it to a Data-frame.
                    - The input data includes daily rainfall, maximum & minimum temperature.
                    - Summary report on the missing data
                    - Transform the data-frame to netCDF file format.
                    - Generate basic summary & indices in a tabular formats.
                    - Produce intermediate results & time series plots.
                    - Generates maps required for monthly, seasonal (i.e., Bega, Belg, Kiremt), & annual climate bulletins.
                    """
                    )
        
        st.markdown(
        """
        ---
        """
        )
                
        st.markdown('### Our Partners')
        display1 = Image.open('aiccra.png')
        #display2 = Image.open('CGIAT.png')
        #display3 = Image.open('CCAFS.png')
        
        col1, col2, col3 = st.columns(3)
        
        col1, col2, col3 = st.columns(3)
        col1.image(display1, width = 450)
        # col2.image(display2, width = 200)
        # col3.image(display3, width = 200)
        
        st.markdown('Copyright @2022 EMI-CDAT')
        st.markdown(
                        """
                        ---
                        """
                        )



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
