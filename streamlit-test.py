import streamlit as st
 
st.title("Housing Prices Prediction")
 
st.write("""
### Project description
We have trained several models to predict the price of a house based on features such as the area of the house and the condition and quality of their different rooms.
 
""")

import pickle
model = pickle.load(open('Desktop/WBS_bootcamp/wbs_platform_projects/project_6_deployment/trained_pipe_knn.sav', 'rb'))
 
import pandas as pd
new_house = pd.DataFrame({
    'LotArea':[9000],
    'TotalBsmtSF':[1000], 
    'BedroomAbvGr':[5], 
    'GarageCars':[4]
})
 
prediction = model.predict(new_house)
 
st.write("The price of the house is:", prediction)

import pickle
model = pickle.load(open('Desktop/WBS_bootcamp/wbs_platform_projects/project_6_deployment/trained_pipe_knn.sav', 'rb'))
 
LotArea = st.number_input("Lot Area")
TotalBsmtSF = st.number_input("Basement Square Feet")
BedroomAbvGr = st.number_input("Number of Bedrooms")
GarageCars = st.number_input("Car spaces in Garage")
 
import pandas as pd
new_house = pd.DataFrame({
    'LotArea':[LotArea],
    'TotalBsmtSF':[TotalBsmtSF], 
    'BedroomAbvGr':[BedroomAbvGr], 
    'GarageCars':[GarageCars]
})
 
st.write("The price of the house is:", prediction)
