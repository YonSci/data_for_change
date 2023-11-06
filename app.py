# Import necessary libraries
import streamlit as st
import pandas as pd
import pickle

def intro():
       st.sidebar.success("Select a page")
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
