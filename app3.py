{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": 5,
   "id": "ed960239-9583-41ab-bdf0-80206226873f",
   "metadata": {},
   "outputs": [],
   "source": [
    "import streamlit as st\n",
    "import numpy as np\n",
    "import joblib\n",
    "\n",
    "# Load the full pipeline (preprocessing + model inside)\n",
    "pipeline = joblib.load(\"laptop_price_pipeline_2.pkl\")\n",
    "\n",
    "st.title(\"💻 Laptop Price Predictor\")\n",
    "st.write(\"Predict the price of a laptop based on its specifications.\")\n",
    "\n",
    "# --- User Inputs ---\n",
    "company = st.selectbox(\"Company\", [\n",
    "    \"Apple\", \"Dell\", \"HP\", \"Lenovo\", \"Asus\", \"Acer\", \"MSI\", \"Toshiba\", \"Other\"\n",
    "])\n",
    "type_name = st.selectbox(\"Type\", [\"Ultrabook\", \"Gaming\", \"Notebook\", \"Netbook\", \"Workstation\"])\n",
    "ram = st.slider(\"RAM (GB)\", 2, 64, 8, step=2)\n",
    "weight = st.number_input(\"Weight (kg)\", 0.5, 5.0, 1.5)\n",
    "Cpu = st.selectbox(\"CPU Brand\", [\"Intel Core i7\", \"Intel Core i5\", \"Intel Core i3\", \"AMD\", \"Other\"])\n",
    "Gpu = st.selectbox(\"GPU Brand\", [\"Nvidia\", \"AMD\", \"Intel\", \"Other\"])\n",
    "OpSys = st.selectbox(\"Operating System\", [\"Windows\", \"Mac\", \"Linux\", \"No OS\", \"Other\"])\n",
    "\n",
    "# --- Create input dict (let pipeline handle encoding & scaling) ---\n",
    "input_data = {\n",
    "    \"Company\": company,\n",
    "    \"TypeName\": type_name,\n",
    "    \"Ram\": ram,\n",
    "    \"Weight\": weight,\n",
    "    \"Cpu brand\": Cpu,\n",
    "    \"Gpu brand\": Gpu,\n",
    "    \"os\": OpSys\n",
    "}\n",
    "\n",
    "# Convert to 2D array (or DataFrame if pipeline expects it)\n",
    "import pandas as pd\n",
    "input_df = pd.DataFrame([input_data])\n",
    "\n",
    "# --- Prediction ---\n",
    "if st.button(\"Predict Price\"):\n",
    "    prediction = pipeline.predict(input_df)[0]\n",
    "    st.success(f\"💰 Estimated Laptop Price: **₹{int(prediction):,}**\")\n"
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
