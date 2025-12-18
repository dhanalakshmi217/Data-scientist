import streamlit as st
import pickle
import numpy as np

# Load model
with open("Insurance.pkl", "rb") as file:
    model = pickle.load(file)

st.title("🔮 Insurance Prediction App")

st.write("Enter input values to predict")

# Example inputs (change according to your model)
age = st.number_input("Age", min_value=1, max_value=100, value=25)


# Predict button
if st.button("Predict"):
    input_data = np.array([[age]])
    prediction = model.predict(input_data)

    st.success(f"✅ Prediction Result: {prediction[0]}")