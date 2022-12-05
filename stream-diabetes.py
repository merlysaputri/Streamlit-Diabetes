import pickle
import numpy as np
import streamlit as st

# load save classifier
classifier = pickle.load(open('diabetes.sav', 'rb'))

# judul web
st.title('Prediksi Penyakit Diabetes')

col1, col2 = st.columns(2)
with col1:
    Pregnancies = st.text_input('Input nilai Pregnancies')
with col2:
    Glucose = st.text_input('Input Nilai Glucose')
with col1:
    BloodPressure = st.text_input('Input Nilai Blood Pressure')
with col2:
    SkinThickness = st.text_input('Input Nilai Skin Thickness')
with col1:
    Insulin = st.text_input('Input nilai insulin')
with col2:
    BMI = st.text_input('Input Nilai BMI')
with col1:
    DiabetesPedigreeFunction = st.text_input('Input Nilai Diabetes Pedigree Function')
with col2:
    Age = st.text_input('Input Nilai Age')

# code for prediction
diabetes_diagnosis = ''

# membuat tombol prediksi
if st.button('Hasil Prediksi'):
    diabetes_prediction = classifier.predict([[Pregnancies, Glucose, BloodPressure, SkinThickness, Insulin, BMI, DiabetesPedigreeFunction, Age]])

    if (diabetes_prediction[0]==1):
        diabetes_diagnosis = 'Pasien Terkena Penyakit Diabetes'
    else:
        diabetes_diagnosis = 'Pasien Tidak Terkena Diabetes'
    st.success(diabetes_diagnosis)









