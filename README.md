# Project on Vitamin/Mineral Deficiency Predictor Tool

The Vitamin/Mineral Deficiency Predictor Tool is a web application/dashboard that utilizes Random Forest, Decision Tree, and Support Vector Machine algorithms to predict Vitamin/Mineral Deficiency in a given household in Malawi.

The tool uses data collected from the Living Standards Measurement Study 2019-2020 of the World Bank, which includes predictors such as annual food consumption, annual drug consumption, annual tobacco consumption, annual health consumption, total annual consumption, poverty line, received social safety net, and consumed foods such as Cereals, Grains, Roots, Tubers, Nuts, Pulses, vegetables, Meat, Fish, Fruits, Milk products, Fats, Oil, and Sugar products at the household level.

**Jupyter Notebooks**
In the notebooks folder, there are two Jupyter notebooks that implement the machine learning workflow including:

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
  
In summary, the notebooks cover an end-to-end machine learning workflow including data preparation, exploratory analysis, model training and evaluation, hyperparameter tuning and model interpretation. Standard techniques like random forests and SVMs are implemented along with best practices like feature encoding and scaling.

The tool is designed to help address the issue of micronutrient deficiencies in Malawi, which is a significant public health concern. The tool combines insights from multiple sources to provide a comprehensive assessment of the risk of Vitamin/Mineral Deficiency in a given household. The tool has the potential to be a valuable resource for policymakers, researchers, and public health professionals working to address micronutrient deficiencies in Malawi and can be scaled up/adopted in other countries.

The vitamin/Mineral Deficiency Predictor Tool is built & deployed using the open-source Streamlit application development tool. For visualization, the Plotly Graphing Libraries package is used to improve the mapping capabilities of the App.


**Data Source**: 

Living Standards Measurement Study: Fifth Integrated Household Survey 2019-2020 Malawi

Link: https://microdata.worldbank.org/index.php/catalog/3818/get-microdata


Dashboard: https://dataforchange-uttp3nyzhzonjbxbbq8h2p.streamlit.app/


