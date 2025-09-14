import streamlit as st
import numpy as np
import joblib

# Load the full pipeline (preprocessing + model inside)
pipeline = joblib.load("laptop_price_pipeline.pkl")

st.title("💻 Laptop Price Predictor")
st.write("Predict the price of a laptop based on its specifications.")

# --- User Inputs ---
company = st.selectbox("Company", [
    "Apple", "Dell", "HP", "Lenovo", "Asus", "Acer", "MSI", "Toshiba", "Other"
])
type_name = st.selectbox("Type", ["Ultrabook", "Gaming", "Notebook", "Netbook", "Workstation"])
ram = st.slider("RAM (GB)", 2, 64, 8, step=2)
weight = st.number_input("Weight (kg)", 0.5, 5.0, 1.5)
touchscreen = st.selectbox("Touchscreen", ["No", "Yes"])
ips = st.selectbox("IPS Display", ["No", "Yes"])
ppi = st.slider("PPI (Pixels Per Inch)", 80, 300, 120)
cpu = st.selectbox("CPU Brand", ["Intel Core i7", "Intel Core i5", "Intel Core i3", "AMD", "Other"])
hdd = st.slider("HDD (GB)", 0, 2000, 0, step=128)
ssd = st.slider("SSD (GB)", 0, 2000, 256, step=128)
gpu = st.selectbox("GPU Brand", ["Nvidia", "AMD", "Intel", "Other"])
os = st.selectbox("Operating System", ["Windows", "Mac", "Linux", "No OS", "Other"])

# --- Create input dict (let pipeline handle encoding & scaling) ---
input_data = {
    "Company": company,
    "TypeName": type_name,
    "Ram": ram,
    "Weight": weight,
    "Touchscreen": 1 if touchscreen == "Yes" else 0,
    "Ips": 1 if ips == "Yes" else 0,
    "Ppi": ppi,
    "Cpu brand": cpu,
    "HDD": hdd,
    "SSD": ssd,
    "Gpu brand": gpu,
    "os": os
}

# Convert to 2D array (or DataFrame if pipeline expects it)
import pandas as pd
input_df = pd.DataFrame([input_data])

# --- Prediction ---
if st.button("Predict Price"):
    prediction = pipeline.predict(input_df)[0]
    st.success(f"💰 Estimated Laptop Price: **₹{int(prediction):,}**")
