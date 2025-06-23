import os
import pickle
import streamlit as st
from streamlit_option_menu import option_menu

st.set_page_config(page_title='Prediction of Disease Outbreaks',layout='wide',page_icon='doctor')
diabetes_model=pickle.load(open(r"E:\AI-ML Projects\Health-Check-Disease PREDICTION\models\diabetes_model.sav",'rb'))
heart_model=pickle.load(open(r"E:\AI-ML Projects\Health-Check-Disease PREDICTION\models\heart_model.sav"),'rb')
# parkinson's_model=pickle.load(open(r"E:\AI-ML Projects\Health-Check-Disease PREDICTION\models\diabetes_model.sav"),)

with st.sidebar:
    selected=option_menu('Prediction of Disease Outbreak system',['Diabetes Prediction','Heart Disease Prediction','Parkinsons Diease Prediction'],
                         menu_icon='hospital-fill',icons=['activity','heart','person'],default_index=0)
if(selected=='Diabetes Prediction'):
    st.title('Diabetes Prediction using ML')
    col1,col2,col3=st.columns(3)
    with col1:
        Pregnancies=st.text_input('Number of Pregnancies')
    with col2:
        Glucose=st.text_input('Glucose level')
    with col3:
        BloodPressure=st.text_input('Blood Pressure value')
    with col1:
        skinthickness=st.text_input('Skin Thickness value')
    with col2:
        Insulin=st.text_input('Insulin level')
    with col3:
        BMI=st.text_input('BMI value')
    with col1:
        Pedigree=st.text_input('Diabetes Pedegree Function value')
    with col2:
        Age=st.text_input('Age of the person')
# if(selected=='Heart Disease Prediction'):

diagnosis=''
if(st.button('Diagnosis Test Results')):
    user_input=[Pregnancies,Glucose,BloodPressure,skinthickness,Insulin,BMI,Pedigree,Age]
    user_input=[float(x) for x in user_input]
    prediction=diabetes_model.predict([user_input])
    if(prediction[0]==1):
        diagnosis='The person is diabetic'
    else:
        diagnosis='The person is not diabetic'
st.success(diagnosis)