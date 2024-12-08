import pandas as pd
import numpy as np
import streamlit as st
import pickle



st.title("OLD Car Price Predictor")

col1,col2,col3=st.columns(3)
with col1:
    Fuel_Type=col1.selectbox("# Fuel Type",["Diesel","Petrol","CNG","LPG","Electric"])
with col2:
    Transmission=col2.selectbox("# Transmission",["Automatic","Manual"])
with col3:
    Year=col1.selectbox("# Year",[2019,2018,2017,2016,2015,2014,2013,2012,2011,2010,2009,2008,2007])
col1,col2,col3=st.columns(3)
with col1:
    Engine=col1.slider("# Engine",500,6000,step=50)
with col2:
    Kilometers_Driven=col2.slider("# kilometer Driven",1000,300000,step=500)
with col3:
    Seats=col2.selectbox("# Seats",[1,2,3,4,5,6,7])
col1,col2,col3=st.columns(3)
with col1:
    Power =col1.slider("# Power",50,600,step=2)
with col2:
    Mileage=col2.slider("# Mileage",0,40,step=1)
with col3:
    Owner_Type=col3.selectbox("# Owner Type",["Fourth & Above","Third","Second","First"])


Company=st.selectbox("Company",["bmw","audi","mercedes-benz","jeep","isuzu","volvo",'land','mini',"force",'chevrolet', 'skoda', "maruti","mahindra","tata","honda","toyota","volkswagen","skoda",'mitsubishi', "renault",'smart', 'ambassador',"fiat","datsun","ford",'hyundai', 'nissan',"bentley","lamborghini","porsche","jaguar"])

encode={"Fuel_Type":{"Diesel":1,"Petrol":2,"CNG":3,"LPG":4,"Electric":5},
        "Transmission":{"Automatic":1,"Manual":2},
        "Owner_Type":{"Fourth & Above":1,"Third":2,"Second":3,"First":4},
        "Company":{"bentley":1,"lamborghini":1,"porsche":1,"jaguar":1,
                    "force":3,'chevrolet':3, 'skoda':3, "maruti":3,"mahindra":3,"tata":3,"honda":3,"toyota":3,
                    "volkswagen":3,"skoda":3,'mitsubishi':3, "renault":3,'smart':3, 'ambassador':3,"fiat":3,"datsun":3,"ford":3,'hyundai':3, 'nissan':3,
                    "bmw":2,"audi":2,"mercedes-benz":2,"jeep":2,"isuzu":2,"volvo":2,'land':2,'mini':2}
                
        }



    #loading model
with open("new_m","rb") as file:
        gbt_line=pickle.load(file)
    
if(st.button("# Predict price")):
    Fuel_Type=encode["Fuel_Type"][Fuel_Type]
    Transmission=encode["Transmission"][Transmission]
    Owner_Type=encode["Owner_Type"][Owner_Type]
    Company=encode["Company"][Company]

    input=[[Year, Kilometers_Driven, Fuel_Type, Transmission, Owner_Type, Mileage,Engine,Power, Seats,Company]]

    an=gbt_line.predict(input)
    st.text("price =>"+str(an))

