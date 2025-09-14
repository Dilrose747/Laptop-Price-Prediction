import streamlit as st
import pandas as pd
import joblib

# Load the pre-trained pipeline (preprocessing + model)
pipeline = joblib.load("laptop_price_pipeline_2.pkl")

# --- Streamlit App ---
st.title("💻 Laptop Price Predictor")
st.write("Predict the price of a laptop based on its specifications.")

# --- User Inputs ---
company = st.selectbox("Company", [
    "Apple", "Dell", "HP", "Lenovo", "Asus", "Acer", "MSI", "Toshiba", "Other"
])
type_name = st.selectbox("Type", ["Ultrabook", "Gaming", "Notebook", "Netbook", "Workstation"])
ram = st.slider("RAM (GB)", 2, 64, 8, step=2)
weight = st.number_input("Weight (kg)", min_value=0.5, max_value=5.0, value=1.5, step=0.1)
cpu = st.selectbox("CPU Brand", ["Intel Core i7", "Intel Core i5", "Intel Core i3", "AMD", "Other"])
gpu = st.selectbox("GPU Brand", ["Nvidia", "AMD", "Intel", "Other"])
os = st.selectbox("Operating System", ["Windows", "Mac", "Linux", "No OS", "Other"])

# --- Prepare Input Data ---
input_df = pd.DataFrame([{
    "Company": company,
    "TypeName": type_name,
    "Ram": ram,
    "Weight": weight,
    "Cpu brand": cpu,
    "Gpu brand": gpu,
    "os": os
}])

# --- Make Prediction ---
if st.button("Predict Price"):
    prediction = pipeline.predict(input_df)[0]
    st.success(f"💰 Estimated Laptop Price: **₹{int(prediction):,}**")
