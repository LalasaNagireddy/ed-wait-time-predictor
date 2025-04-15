
import streamlit as st
import pandas as pd
import joblib

st.set_page_config(page_title="ED Wait Time Predictor", layout="centered")

st.title("Smart Triage ED Wait Time Predictor")

st.markdown("Enter triage vitals to estimate wait time (in minutes):")

temperature = st.number_input("Temperature (°F)", 90, 110, step=1)
heartrate = st.number_input("Heart Rate (bpm)", 30, 200, step=1)
resprate = st.number_input("Respiratory Rate", 5, 40, step=1)
o2sat = st.number_input("Oxygen Saturation (%)", 70, 100, step=1)
sbp = st.number_input("Systolic Blood Pressure", 80, 200, step=1)
dbp = st.number_input("Diastolic Blood Pressure", 40, 120, step=1)
pain = st.number_input("Pain (0–10)", 0, 10, step=1)
china_ai_model = st.selectbox("Were vitals taken within 10 minutes?", ["No", "Yes"])
china_ai_model = 1 if china_ai_model == "Yes" else 0

user_data = pd.DataFrame([{
    "temperature_x": temperature,
    "heartrate_x": heartrate,
    "resprate_x": resprate,
    "o2sat_x": o2sat,
    "sbp_x": sbp,
    "dbp_x": dbp,
    "pain_x": pain,
    "china_ai_model": china_ai_model
}])

if st.button("Predict Wait Time"):
    st.warning("This is a demo. Prediction model not connected.")
    # Example: wait_time = model.predict(user_data)
    # st.success(f"Estimated Wait Time: {wait_time[0]:.2f} minutes")

st.markdown("**Note:** This is a simulation based on the MIMIC-IV-ED dataset.")
