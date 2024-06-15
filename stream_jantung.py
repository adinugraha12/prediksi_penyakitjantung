import numpy as np
import pickle
import streamlit as st
import joblib


model = joblib.load('penyakit_jantung.sav')


st.title('Prediksi Penyakit Jantung')
col1, col2, col3 = st.columns(3)
col1, col2, col3 = st.columns(3)


with col1:
    Age = st.number_input('Umur/Age')
with col2:
    Gender = st.selectbox('Jenis Kelamin/Gender', options=[('Pria', 1), ('Wanita', 0)], format_func=lambda x: x[0])
with col3:
    Heart_rate = st.number_input('Detak Jantung/Heart rate')
with col1:
    Systolic_blood_pressure = st.number_input('Tekanan Darah Sistolik/Systolic blood pressure')
with col2: 
    Diastolic_blood_pressure = st.number_input('Tekanan Darah Diastolik/Diastolic blood pressure')
with col3:
    Blood_sugar = st.number_input('Kadar Gula Darah/Blood sugar')
with col1:
    CK_MB = st.number_input('CK-MB')
with col2:
    Troponin = st.number_input('Troponin')


Gender_value = Gender[1]

heart_diagnosis = ''

def make_prediction():
    try:
        if not Age:
            st.error("Please enter the age.")
            return ''
        if not Heart_rate:
            st.error("Please enter the heart rate.")
            return ''
        if not Systolic_blood_pressure:
            st.error("Please enter the systolic blood pressure.")
            return ''
        if not Diastolic_blood_pressure:
            st.error("Please enter the diastolic blood pressure.")
            return ''
        if not Blood_sugar:
            st.error("Please enter the blood sugar level.")
            return ''
        if not CK_MB:
            st.error("Please enter the CK-MB level.")
            return ''
        if not Troponin:
            st.error("Please enter the troponin level.")
            return ''

        if not Age or not Heart_rate or not Systolic_blood_pressure or not Diastolic_blood_pressure or not Blood_sugar or not CK_MB or not Troponin:
            st.error("Please fill in all fields.")
            return ''
        
        Age_val = float(Age)
        Heart_rate_val = float(Heart_rate)
        Systolic_bp_val = float(Systolic_blood_pressure)
        Diastolic_bp_val = float(Diastolic_blood_pressure)
        Blood_sugar_val = float(Blood_sugar)
        CK_MB_val = float(CK_MB)
        Troponin_val = float(Troponin)
        

        features = np.array([[Age_val, Gender_value, Heart_rate_val, Systolic_bp_val, Diastolic_bp_val, Blood_sugar_val, CK_MB_val, Troponin_val]])
        heart_prediction = model.predict(features)
        
        if heart_prediction[0] == 1:
            return 'Pasien Terkena Penyakit Jantung'
        else:
            return 'Pasien Tidak Terkena Penyakit Jantung'
    except ValueError as e:
        st.error(f"Invalid input: {e}")
        return ''
    except Exception as e:
        st.error(f"An error occurred: {e}")
        return ''


if st.button('Submit'):
    heart_diagnosis = make_prediction()

st.write(heart_diagnosis)