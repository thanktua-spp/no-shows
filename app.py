from joblib import load
import streamlit as st



def make_prediction(age, scholarship, hipertension, diabetes, alcoholism, sms_received, awaiting_time, number_missed, handicap, gender, selected_model):
    st.write(f"Inputs: {age}, {gender}, {number_missed}, {hipertension}, {diabetes}, {alcoholism}, {handicap}, {sms_received}, {awaiting_time}, {selected_model}")
    # Perform model prediction here based on selected_model and input values
    prediction = "Your prediction"  # Replace this with your prediction logic
    return prediction

st.sidebar.title("Patient Information")
age = st.sidebar.slider('Age', 1, 150, 27, 1)
gender = st.sidebar.selectbox('Gender', ["Male", "Female"], index=0)
number_missed = st.sidebar.slider('Number of appointment missed', 0, 10, 0, 1)

hipertension, diabetes, alcoholism, handicap, sms_received, scholarship = st.sidebar.columns(6)
with hipertension:
    hipertension = st.radio('Hypertension', ["Yes", "No"])
with diabetes:
    diabetes = st.radio('Diabetes', ["Yes", "No"])
with alcoholism:
    alcoholism = st.radio('Alcoholism', ["Yes", "No"])
with handicap:
    handicap = st.radio('Disability', ["Yes", "No"])
with sms_received:
    sms_received = st.radio('SMS', ["Yes", "No"])
with scholarship:
    scholarship = st.radio('Scholarship', ["Yes", "No"])

awaiting_time = st.sidebar.slider('Awaiting time in days', 0, 15, 0, 1)
selected_model = st.sidebar.selectbox('Model', ["Logistic", "DecisionTree", "RandomForest", "XGBoost", "MLP", "SVC"])

if st.sidebar.button('Prediction'):
    prediction = make_prediction(age, scholarship, hipertension, diabetes, alcoholism, sms_received, awaiting_time, number_missed, handicap, gender, selected_model)
    st.write(f"Prediction: {prediction}")
