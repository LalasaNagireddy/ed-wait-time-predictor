import streamlit as st
import pandas as pd
import numpy as np
import joblib

# Load model
model = joblib.load("model_rf.pkl")

st.set_page_config(page_title="Smart Triage ED Wait Time Predictor")
st.title("🧠 Smart Triage ED Wait Time Predictor")

st.markdown("Enter vitals collected during triage to simulate wait time prediction. This model is based on real data from MIMIC-IV-ED.")

# Input form
temp = st.number_input("Temperature (°F)", value=98.6)
hr = st.number_input("Heart Rate (bpm)", value=80)
rr = st.number_input("Respiratory Rate", value=18)
o2 = st.number_input("Oxygen Saturation (%)", value=97)
sbp = st.number_input("Systolic BP", value=120)
dbp = st.number_input("Diastolic BP", value=80)
pain = st.slider("Pain Level (0–10)", 0, 10, 5)
fast = st.radio("Were vitals taken within 10 minutes?", ["No", "Yes"])
china_ai_model = 1 if fast == "Yes" else 0

if st.button("Predict Wait Time"):
    input_df = pd.DataFrame([[temp, hr, rr, o2, sbp, dbp, pain, china_ai_model]],
                            columns=['temperature_x', 'heartrate_x', 'resprate_x', 'o2sat_x',
                                     'sbp_x', 'dbp_x', 'pain_x', 'china_ai_model'])
    prediction = model.predict(input_df)[0]
    st.success(f"🕒 Predicted ED Wait Time: {int(prediction)} minutes")

    if china_ai_model == 1:
        st.info("✅ Fast-track triage applied (AI-style). Wait time reduced.")
