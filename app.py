import streamlit as st
#import streamlit as st
import pandas as pd
#import joblib
import numpy as np 
import pickle

import base64

def add_bg_from_local(image_file):
    with open(image_file, "rb") as image_file:
        encoded_string = base64.b64encode(image_file.read())
    st.markdown(
    f"""
    <style>
    .stApp {{
        background-image: url(data:image/{"jpg"};base64,{encoded_string.decode()});
        background-size: contain, cover
    }}
    </style>
    """,
    unsafe_allow_html=True
    )
add_bg_from_local('img_file.jpg')    

# Title
st.header("EV Driving Range Prediction App")

col1, col2, col3 = st.columns(3) 


#Inputs
#city_roads = st.selectbox("City Roads :", ("Yes", "No"))

#highway = st.selectbox("Highway Roads :", ("Yes", "No"))
#country_roads = st.selectbox("Country Roads :", ("No", "Yes"))
#ac = st.selectbox("A/C   :", ("No", "Yes"))
#park_heating = st.selectbox("Park_Heating :", ("No", "Yes"))
#winter_tires = st.selectbox("Winter Tires  :", ("No","Yes"))
#fast_ds = st.selectbox("Is your driving style Fast ? :", ("No","Yes"))
#moderate_ds = st.selectbox("Is your driving style moderate ? :", ("Yes", "No"))
#avg_speed = st.number_input("What is the Avg_Speed in km/h",value=50.0)

with col1:
    city_roads = st.selectbox("City Roads :", ("Yes", "No"))

with col2:
    highway = st.selectbox("Highway Roads :", ("Yes", "No"))
    
with col3:
    country_roads = st.selectbox("Country Roads :", ("No", "Yes"))



col4, col5, col6 = st.columns(3)
with col4:
    ac = st.selectbox("A/C   :", ("Yes", "No"))
    
with col5:
    park_heating = st.selectbox("Park_Heating :", ("No", "Yes"))
    
with col6:
    winter_tires = st.selectbox("Winter Tires  :", ("No","Yes"))


col7, col8, col9 = st.columns(3)   
with col7:
    fast_ds = st.selectbox("Is your driving style Fast ? :", ("No","Yes"))
    
with col8:
    moderate_ds = st.selectbox("Is your driving style moderate ? :", ("Yes", "No"))
    
with col9:
    avg_speed = st.number_input("What is the Avg_Speed in km/h",value=50.0)


battery_capacity = st.number_input("Enter Remaining battery capacity(kWh)",value=15.0) 

# If button is pressed
if st.button("Submit"):
    
    # Unpickle classifier
    pickled_model = pickle.load(open('model.pkl', 'rb'))
    #X = np.array([battery_capacity,city_roads,highway,country_roads,ac,park_heating,winter_tires,fast_ds,moderate_ds,avg_speed])
    # Store inputs into dataframe
    X = pd.DataFrame([[battery_capacity,city_roads,highway,country_roads,ac,park_heating,winter_tires,fast_ds,moderate_ds,avg_speed]],columns = ["Battery_capacity","City_roads","Highway","Country_roads","AC","Park_heating","Winter_tires","Fast_ds","Moderate_ds","Avg_speed"])
    X = X.replace(["Yes", "No"], [1, 0])
    #X=X.reshape(-1, 10)
    # Get prediction
    if battery_capacity==0 or avg_speed==0:
        prediction = 0
    else :           
        prediction = pickled_model.predict(X)[0]
    
    # Output prediction
    st.text(f"Predicted Driving Range of your EV is {prediction}km")