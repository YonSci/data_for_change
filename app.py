# Import necessary libraries
import streamlit as st
import pandas as pd
import pickle

def intro():
       st.sidebar.success("Select a page")
       
       
def Deficiency_Predictor():
       st.markdown(f'# {list(page_names_to_funcs.keys())[1]}')
       #st.title('Vitamin/Mineral Deficiency Predictor')

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
