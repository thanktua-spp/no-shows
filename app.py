from joblib import load
import streamlit as st
import pickle
import pandas as pd

# Load the model
svc_model = pickle.load(open('models/SVC.sav', "rb"))
decision_tree_model = pickle.load(open('models/DecisionTreeClassifier.sav', "rb"))
randomforest_model = pickle.load(open('models/RandomForestClassifier.sav', "rb"))
logistic_regression_model = pickle.load(open('models/LogisticRegression.sav', "rb"))
xgb_model = pickle.load(open('models/xgb.XGBClassifier.sav', "rb"))
mlp_model = pickle.load(open('models/MLPClassifier.sav', "rb"))

def hot_encode_inputs(inputs):
    headers = [
        'Age', 'AwaitingTime', 'Number_Missed', 'SMS_received_0', 'SMS_received_1',
        'Scholarship_0', 'Scholarship_1', 'Handcap_0', 'Handcap_1', 'Gender_F', 'Gender_M',
        'Hipertension_0', 'Hipertension_1', 'Diabetes_0', 'Diabetes_1', 'Alcoholism_0', 'Alcoholism_1'
    ]
    
    encoded_inputs = []
    for item in inputs:
        if item == 'Yes':
            encoded_inputs.append(1)
        elif item == 'No':
            encoded_inputs.append(0)
        elif item == 'Male':
            encoded_inputs.extend([0, 1])  # Male: [0, 1]
        elif item == 'Female':
            encoded_inputs.extend([1, 0])  # Female: [1, 0]
        else:
            encoded_inputs.append(item)
    
    # Fill in any missing values with 0
    while len(encoded_inputs) < len(headers):
        encoded_inputs.append(0)
    
    return encoded_inputs#pd.DataFrame(encoded_inputs, columns=headers)

    

def make_prediction(age, scholarship, hipertension, diabetes, alcoholism, sms_received, awaiting_time, number_missed, handicap, gender, selected_model):
    st.write(f"Inputs: {age}, {awaiting_time}, {number_missed}, {sms_received}, {scholarship}, {handicap}, {gender}, {diabetes}, {alcoholism}, {selected_model}")
    # Perform model prediction here based on selected_model and input values
    if gender == 'Male': gender = 1
    else: gender = 0

    parameters = [age, awaiting_time, number_missed, sms_received, scholarship, handicap, gender, hipertension, diabetes, alcoholism]
    parameters_enc = hot_encode_inputs(parameters)
    
    if selected_model == "Logistic":
        prediction = logistic_regression_model.predict([parameters_enc])[0]
    elif selected_model == "DecisionTree":
        prediction = decision_tree_model.predict([parameters_enc])[0]
    elif selected_model == "XGBoost":
        prediction = xgb_model.predict([parameters_enc])[0]
    elif selected_model == "RandomForest":
        prediction = randomforest_model.predict([parameters_enc])[0]
    elif selected_model == "SVC":
        prediction = svc_model.predict([parameters_enc])[0]
    elif selected_model == "MLP":
        prediction = mlp_model.predict([parameters_enc])[0]     
          
    if prediction == 1: return "No shows"
    else: return "Shows"


def main():
    st.title('No Shows Application Demo Interface')
    st.write('Hello, welcome! This is an interactive demo interface were you can make real time predictions using several trained models')
    
    st.title("Patient Information")
    age = st.slider('Age', 1, 150, 27, 1)
    gender = st.radio('Gender', ["Male", "Female"], index=0)
    number_missed = st.slider('Number of appointment missed', 0, 10, 0, 1)

    hipertension, diabetes, alcoholism, handicap, sms_received, scholarship = st.columns(6)
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

    awaiting_time = st.slider('Awaiting time in days', 0, 15, 0, 1)
    selected_model = st.radio('Model', ["Logistic", "DecisionTree", "RandomForest", "XGBoost", "MLP", "SVC"])

    if st.button('Prediction'):
        prediction = make_prediction(age, scholarship, hipertension, diabetes, alcoholism, sms_received, awaiting_time, number_missed, handicap, gender, selected_model)
        st.write(f"Prediction: {prediction}")



if __name__ == '__main__':
    main()
