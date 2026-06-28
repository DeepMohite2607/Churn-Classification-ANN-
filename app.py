import pandas as pd 
import numpy as np
import pickle
import tensorflow as tf
from tensorflow.keras.models import load_model
from sklearn.preprocessing import LabelEncoder, StandardScaler, OneHotEncoder
import streamlit as st
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent

# Load the saved model
model = load_model(BASE_DIR / 'model.h5')

with open(BASE_DIR / 'label_encoder_gender.pkl', 'rb') as f:
    label_encoder = pickle.load(f)

with open(BASE_DIR / 'standard_scaler.pkl', 'rb') as f:
    scaler = pickle.load(f)

with open(BASE_DIR / 'onehot_encoder_geo.pkl', 'rb') as f:
    onehot_encoder = pickle.load(f)


# Define the Streamlit app

st.title("Customer Churn Prediction")

#User Inputs

geography = st.selectbox("Select Geography", onehot_encoder.categories_[0])
gender = st.selectbox("Select Gender", label_encoder.classes_)
age = st.slider("Select Age", 18, 92)
balance = st.number_input("Enter Balance", min_value=0.0, step=0.01)
credit_score = st.number_input("Enter Credit Score", min_value=0, step=1)
estimated_salary = st.number_input("Enter Estimated Salary", min_value=0.0, step=0.01)
tenure = st.slider("Select Tenure", 0, 10)
number_of_products = st.slider("Select Number of Products", 1, 4)
has_credit_card = st.selectbox("Has Credit Card?", [1, 0])
is_active_member = st.selectbox("Is Active Member?", [1, 0])

# Create a DataFrame from user inputs
input_data = pd.DataFrame({
    'CreditScore': [credit_score],
    'Gender': [gender],
    'Age': [age],   
    'Tenure': [tenure],
    'Balance': [balance],
    'NumOfProducts': [number_of_products],
    'HasCrCard': [has_credit_card],
    'IsActiveMember': [is_active_member],
    'EstimatedSalary': [estimated_salary],
    'Geography': [geography]
})

# Preprocess the input data
geo_encoded = onehot_encoder.transform(pd.DataFrame({'Geography': [geography]})).toarray()
geo_encoded_df = pd.DataFrame(geo_encoded, columns=onehot_encoder.get_feature_names_out(['Geography']))

input_data = pd.concat([input_data.drop('Geography', axis=1), geo_encoded_df], axis=1)

gender_encoded = label_encoder.transform(input_data['Gender'])
input_data['Gender'] = gender_encoded

input_data = input_data[scaler.feature_names_in_]
input_scaled = scaler.transform(input_data)

# Make predictions
predictions = model.predict(input_scaled)
prediction_proba = predictions[0][0]

st.write(f"Prediction Probability of Churn: {prediction_proba}")
# Display the predictions
if prediction_proba > 0.5:
    st.write("The customer is likely to churn.")
else:   
    st.write("The customer is not likely to churn.")
