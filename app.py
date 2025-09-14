{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": 3,
   "id": "ed960239-9583-41ab-bdf0-80206226873f",
   "metadata": {},
   "outputs": [],
   "source": [
    "import streamlit as st\n",
    "import numpy as np\n",
    "import pandas as pd\n",
    "import joblib\n",
    "\n",
    "# Load trained pipeline (includes preprocessing + model)\n",
    "pipeline = joblib.load(\"laptop_price_pipeline.pkl\")\n",
    "\n",
    "st.title(\"💻 Laptop Price Predictor\")\n",
    "\n",
    "st.write(\"Fill in the laptop specifications to predict the price:\")\n",
    "\n",
    "# ----------------- User Inputs -----------------\n",
    "company = st.selectbox(\"Brand\", [\"Dell\", \"HP\", \"Lenovo\", \"Asus\", \"Apple\", \"Acer\", \"MSI\", \"Other\"])\n",
    "laptop_type = st.selectbox(\"Type\", [\"Ultrabook\", \"Gaming\", \"Notebook\", \"Netbook\", \"Workstation\", \"2 in 1 Convertible\", \"Other\"])\n",
    "cpu = st.selectbox(\"CPU\", [\"Intel Core i3\", \"Intel Core i5\", \"Intel Core i7\", \"AMD Ryzen 5\", \"AMD Ryzen 7\", \"Other\"])\n",
    "gpu = st.selectbox(\"GPU\", [\"Intel Integrated\", \"NVIDIA GTX\", \"NVIDIA RTX\", \"AMD Radeon\", \"Other\"])\n",
    "os = st.selectbox(\"Operating System\", [\"Windows\", \"MacOS\", \"Linux\", \"No OS\"])\n",
    "\n",
    "ram = st.slider(\"RAM (GB)\", 2, 64, 8, step=2)\n",
    "weight = st.number_input(\"Weight (kg)\", min_value=0.5, max_value=5.0, value=1.5, step=0.1)\n",
    "touchscreen = st.selectbox(\"Touchscreen\", [\"No\", \"Yes\"])\n",
    "ips = st.selectbox(\"IPS Display\", [\"No\", \"Yes\"])\n",
    "screen_width = st.number_input(\"Screen Width (px)\", min_value=800, max_value=4000, value=1920)\n",
    "screen_height = st.number_input(\"Screen Height (px)\", min_value=600, max_value=2500, value=1080)\n",
    "\n",
    "hdd = st.slider(\"HDD (GB)\", 0, 2000, 0, step=128)\n",
    "ssd = st.slider(\"SSD (GB)\", 0, 2000, 256, step=128)\n",
    "\n",
    "# ----------------- Feature Engineering -----------------\n",
    "ppi = ((screen_width**2 + screen_height**2) ** 0.5) / (15.6)  # Assuming avg 15.6 inch screen\n",
    "\n",
    "# Convert Yes/No to binary\n",
    "touchscreen = 1 if touchscreen == \"Yes\" else 0\n",
    "ips = 1 if ips == \"Yes\" else 0\n",
    "\n",
    "# Create input dataframe\n",
    "input_data = pd.DataFrame([{\n",
    "    \"company\": company,\n",
    "    \"type\": laptop_type,\n",
    "    \"ram\": ram,\n",
    "    \"weight\": weight,\n",
    "    \"touchscreen\": touchscreen,\n",
    "    \"ips\": ips,\n",
    "    \"ppi\": ppi,\n",
    "    \"cpu\": cpu,\n",
    "    \"hdd\": hdd,\n",
    "    \"ssd\": ssd,\n",
    "    \"gpu\": gpu,\n",
    "    \"os\": os\n",
    "}])\n",
    "\n",
    "# ----------------- Prediction -----------------\n",
    "if st.button(\"Predict Price\"):\n",
    "    predicted_price = pipeline.predict(input_data)[0]\n",
    "    st.success(f\"💰 Predicted Laptop Price: ₹ {int(predicted_price):,}\")\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "96539431-f914-47c8-b8c2-a7e2696ec9db",
   "metadata": {},
   "outputs": [],
   "source": []
  }
 ],
 "metadata": {
  "kernelspec": {
   "display_name": "Python 3 (ipykernel)",
   "language": "python",
   "name": "python3"
  },
  "language_info": {
   "codemirror_mode": {
    "name": "ipython",
    "version": 3
   },
   "file_extension": ".py",
   "mimetype": "text/x-python",
   "name": "python",
   "nbconvert_exporter": "python",
   "pygments_lexer": "ipython3",
   "version": "3.12.7"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 5
}
