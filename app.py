# Import necessary libraries
import streamlit as st
import pandas as pd
import pickle

def intro():
       st.markdown(f'# {list(page_names_to_funcs.keys())[1]}')
       st.sidebar.success("Select a page")
       
       
def Deficiency_Predictor():
       st.markdown(f'# {list(page_names_to_funcs.keys())[2]}')
       st.title('Vitamin/Mineral Deficiency Predictor')

def Visualization():
       st.markdown(f'# {list(page_names_to_funcs.keys())[3]}')
       st.title('Vitamin/Mineral Deficiency Predictor')
       

page_names_to_funcs = {
        "🏠 Landing Page": intro,
        "📊 Vitamin/Mineral_Deficiency_Predictor": Deficiency_Predictor, 
        "📈 Visualization  ": Visualization,
    }




demo_name = st.sidebar.selectbox("Navigation Panel", page_names_to_funcs.keys())
page_names_to_funcs[demo_name]()
