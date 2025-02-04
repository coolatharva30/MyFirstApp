import streamlit as st
import numpy as np
import pickle

model = pickle.load(open("placement_model.pkl","rb"))

st.set_page_config(page_title="Student Placement Predictor")

st.header("Student Placement Predictor")

cgpa = st.number_input("Enter CGPA",max_value=10.0,step=0.1)
iq = st.number_input("Enter IQ Score",max_value=150,step=1)
profile = st.number_input("Enter Profile Score",max_value=100,step=1)

button = st.button("Predict")

if button:
    input_data = np.array([[cgpa,iq,profile]])
    result = model.predict(input_data)
    if result[0] != 0:
        st.success("Placed")
    else:
        st.error("Not Placed")