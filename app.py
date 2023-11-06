# Import necessary libraries
import streamlit as st
import pandas as pd
import pickle
import sklearn


def intro():
       st.sidebar.success("Select a page")
       st.title('Vitamin/Mineral Deficiency Predictor')
       st.markdown(
                """
                The **Vitamin/Mineral Deficiency Predictor Tool** is a web application/dashboard that utilizes **Random Forest**, **Decision Tree**, and **Support Vector Machine** algorithms to predict Vitamin/Mineral Deficiency in a given household in Malawi. 
                
                The tool uses data collected from the Living Standards Measurement Study 2019-2020 of the World Bank, which includes predictors such as annual food consumption, annual drug consumption, annual tobacco consumption, annual health consumption, 
                total annual consumption, poverty line, received social safety net, and consumed foods such as Cereals, Grains, Roots, Tubers, Nuts, Pulses, vegetables, Meat, Fish, Fruits, Milk products, Fats, Oil, and Sugar products at the household level. 

                The tool is designed to help address the issue of micronutrient deficiencies in Malawi, which is a significant public health concern. The tool combines insights from multiple sources to provide a comprehensive assessment of the risk of Vitamin/Mineral Deficiency in a given household. The tool has the potential to be a valuable resource for policymakers, researchers, and public health professionals working to address micronutrient deficiencies in Malawi and can be scaled up/adopted in other countries.
                
               
                **Vitamin/Mineral Deficiency Predictor Tool** is build & deploy using the open source [Streamlit](https://docs.streamlit.io/) application development tool. For visualization, the  [Plotly  Graphing Libraries](https://plotly.com/graphing-libraries/) package is used to improve the mapping capabilities of the App.
                """
                )

       # Create a dictionary with the data 
       data = {'Algorithm': ['RF', 'DT', 'SVM'],
               'Accuracy': [0.9069, 0.9047, 0.8919],
               'Precision': [0.9615, 0.9816, 0.9394],
               'F1-score': [0.9263, 0.9318, 0.9082]
              }

        # Convert the dictionary to a pandas DataFrame
       df = pd.DataFrame(data)

        # Display the DataFrame as a table in Streamlit
       st.table(df)

       st.markdown(
                    """
                    ---
                    Vitamin/Mineral Deficiency Predictor Tool:
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
       
       
def Deficiency_Predictor():
       st.markdown(f'# {list(page_names_to_funcs.keys())[1]}')
       #st.title('Vitamin/Mineral Deficiency Predictor')

       # Load model
 
       with open('DecisionTree1.pkl', 'rb') as f:
             dt_model = pickle.load(f)

       with open('SupportVectorMachines1.pkl', 'rb') as f:
              svm_model = pickle.load(f)

       # Create a sidebar to allow the user to select the machine learning model
       model = st.sidebar.selectbox('Select Model', ['Random Forest', 'Decision Tree', 'SVM'])

       # Add the input fields to the first column
       illness_type = col1.selectbox('Illness Type', ['Type 1 Diabetes', 'Type 2 Diabetes', 'Hypertension', 'Heart Disease'])
       food_consumption_annual = col1.slider('Food Consumption (Annual)', 0, 100, 50)
       tobacco_consumption_annual = col1.slider('Tobacco Consumption (Annual)', 0, 100, 50)
       health_annual_consumption = col1.slider('Health Annual Consumption', 0, 100, 50)

       # Add the input fields to the second column
       total_annual_consumption_per_household = col2.slider('Total Annual Consumption per Household', 0, 100, 50)
       poor_hh_below_poverty_line = col2.slider('Poor Households Below Poverty Line', 0, 100, 50)
       received_SSN = col2.slider('Received Social Security Number', 0, 1, 0) 
       sugar_product = col2.slider('Sugar Product', 0, 1, 0)
       age_categories = col2.selectbox('Age Categories', ['0-18', '19-30', '31-50', '51-70', '71+'])





def Visualization():
       st.markdown(f'# {list(page_names_to_funcs.keys())[2]}')
       #st.title('Visualization')
       

page_names_to_funcs = {
        "🏠 Landing Page": intro,
        "📊 Vitamin/Mineral Deficiency Predictor": Deficiency_Predictor, 
        "📈 Visualization  ": Visualization,
    }




demo_name = st.sidebar.selectbox("Navigation Panel", page_names_to_funcs.keys())
page_names_to_funcs[demo_name]()
