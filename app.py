# Import necessary libraries
import streamlit as st
import pandas as pd
import numpy as np
from matplotlib import pyplot as plt
import seaborn as sns

import pickle



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
       The modeling process includes:
       - Importing required libraries and setting up file paths and names
       - Loading and inspecting the datasets, checking for missing data and handling any issues
       - Merging multiple data files into a single dataset
       - Cleaning the merged data by handling missing values, outliers etc.
       - Separating the data into predictor and target variables for modeling
       - Exploratory data analysis to understand relationships including summary statistics, correlations, and visualizations like boxplots
       - Preprocessing steps such as feature scaling to normalize the data
       - Encoding any categorical variables 
       - Fitting and evaluating various machine learning models such as Random Forests, Decision Trees, and Support Vector Machines on the data
       - Tuning model hyperparameters and selecting the best model based on accuracy metrics
       - Analyzing feature importance to understand the most predictive variables
       - Saving the best-performing model for future use

  The tool is designed to help address the issue of micronutrient deficiencies in Malawi, which is a significant public health concern. The tool combines insights from multiple sources to provide a comprehensive assessment of the risk of Vitamin/Mineral Deficiency in a given household. The tool has the potential to be a valuable resource for policymakers, researchers, and public health professionals working to address micronutrient deficiencies in Malawi and can be scaled up/adopted in other countries.

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

       # Load the trained machine-learning models    
       with open('DecisionTree1.pkl', 'rb') as f:   
              dt_model = pickle.load(f)

       with open('SupportVectorMachines1.pkl', 'rb') as f:
              svm_model = pickle.load(f)


      

    





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
