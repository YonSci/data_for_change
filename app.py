# Import necessary libraries
import streamlit as st
import pandas as pd
import pickle

def intro():
        import streamlit as st
        from PIL import Image
            
        st.sidebar.success("Select a page")
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




page_names_to_funcs = {
        "🏠 Landing Page": intro,
        "🗃️ Data Importing & Missing Data": data_reading_module,
        "🖩 Data Converter & Basic Summary ": basic_summary,
        "📊 Indices Calculator": intermediate_result,
        "📈 Time Series Plots ": time_series_plots,
        "💾 Interpolation & netCDF Convector":  netCDF_convector,
        "🌍 Map Room ":   mapping_tool,
    }




demo_name = st.sidebar.selectbox("Navigation Panel", page_names_to_funcs.keys())
page_names_to_funcs[demo_name]()
