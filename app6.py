{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": 6,
   "id": "ed960239-9583-41ab-bdf0-80206226873f",
   "metadata": {},
   "outputs": [],
   "source": [
    "import streamlit as st\n",
    "import pandas as pd\n",
    "import joblib\n",
    "\n",
    "# Load the pre-trained pipeline (preprocessing + model)\n",
    "pipeline = joblib.load(\"laptop_price_pipeline_2.pkl\")\n",
    "\n",
    "# --- Streamlit App ---\n",
    "st.title(\"💻 Laptop Price Predictor\")\n",
    "st.write(\"Predict the price of a laptop based on its specifications.\")\n",
    "\n",
    "# --- User Inputs ---\n",
    "company = st.selectbox(\"Company\", [\n",
    "    \"Apple\", \"Dell\", \"HP\", \"Lenovo\", \"Asus\", \"Acer\", \"MSI\", \"Toshiba\", \"Other\"\n",
    "])\n",
    "type_name = st.selectbox(\"Type\", [\"Ultrabook\", \"Gaming\", \"Notebook\", \"Netbook\", \"Workstation\"])\n",
    "ram = st.slider(\"RAM (GB)\", 2, 64, 8, step=2)\n",
    "weight = st.number_input(\"Weight (kg)\", min_value=0.5, max_value=5.0, value=1.5, step=0.1)\n",
    "cpu = st.selectbox(\"CPU Brand\", [\"Intel Core i7\", \"Intel Core i5\", \"Intel Core i3\", \"AMD\", \"Other\"])\n",
    "gpu = st.selectbox(\"GPU Brand\", [\"Nvidia\", \"AMD\", \"Intel\", \"Other\"])\n",
    "os = st.selectbox(\"Operating System\", [\"Windows\", \"Mac\", \"Linux\", \"No OS\", \"Other\"])\n",
    "\n",
    "# --- Prepare Input Data ---\n",
    "input_df = pd.DataFrame([{\n",
    "    \"Company\": company,\n",
    "    \"TypeName\": type_name,\n",
    "    \"Ram\": ram,\n",
    "    \"Weight\": weight,\n",
    "    \"Cpu brand\": cpu,\n",
    "    \"Gpu brand\": gpu,\n",
    "    \"os\": os\n",
    "}])\n",
    "\n",
    "# --- Make Prediction ---\n",
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
