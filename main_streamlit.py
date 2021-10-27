import pandas as pd
import streamlit as st
import pickle
import numpy as np

model = pickle.load(open(r"model.pkl",'rb'))     ## Load pickeled ml model

## Main Function
def main():
    """ main() contains all UI structure elements; getting and storing user data can be done within it"""
    st.title("Titanic Survival Prediction")                                                                              ## Title/main heading
    st.image(r"titanic_sinking.jpg", caption="Sinking of 'RMS Titanic' : 15 April 1912 in North Atlantic Ocean",use_column_width=True) ## image import
    st.write("""## Would you have survived From Titanic Disaster?""")                                                    ## Sub heading

    ## Framing UI Structure

    # slider for user input(ranges from 1 to 75 & default 30)
    age = st.slider("Enter Age :", 1, 75, 30)             

    # slider for user input(ranges from 15 to 500 & default 40)                                                      
    fare = st.slider("Fare (in 1912 $) :", 15, 500, 40)    

    # Select box
    SibSp = st.selectbox("How many Siblings or spouses are travelling with you?", [0, 1, 2, 3, 4, 5, 6, 7, 8]) 

    sex = st.selectbox("Select Gender:", ["Male","Female"])  # select box for gender[Male|Female]
    if (sex == "Male"):                                      # selected gender changes to [Male:0 Female:1]
        Sex=0
    else:
        Sex=1

    # Select box for passenger-class
    Pclass= st.selectbox("Select Passenger-Class:",[1,2,3])                        

    ## Getting & Framing Data: Collecting user-input into dictionary
    data={"Age":age,"Fare":fare,"SibSp":SibSp,"Sex":Sex,"Pclass":Pclass}

    df=pd.DataFrame(data,index=[0])      ## converting dictionary to Dataframe
    return df

data=main()                             ## calling Main()

## Prediction:

## prediction button created,which returns predicted value from ml model(pickle file)
if st.button("Predict"):    
    result = model.predict(data)              ## prediction of user-input

    if result[0] == 1:
        st.write("***congratulation !!!....*** **You probably would have made it!**")
        st.image(r"lifeboat.jfif")
    else:
        st.write("***Better Luck Next time !!!!...*** **you're probably Ended up like 'Jack'**")
        st.image(r"Rip.jfif")