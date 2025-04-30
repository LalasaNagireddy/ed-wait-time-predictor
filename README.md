# ED Wait Time Predictor

This project builds a machine learning model to predict Emergency Department (ED) wait times using patient vital signs and triage timing. It is inspired by AI-driven smart triage systems implemented in hospitals in China and explores how similar approaches could improve patient flow and efficiency in U.S. emergency departments.

This work was completed as part of the COMP401 Seminar at Kenyon College.

## Project Overview

- Predicts ED wait times using real hospital data from the MIMIC-IV-ED v2.2 dataset
- Simulates smart triage logic by flagging patients whose vitals were charted within 10 minutes
- Compares the performance of Random Forest and Linear Regression models
- Deploys the final trained model in an interactive web application using Streamlit

## Model Summary

Best performing model: Random Forest

Performance metrics:
- Mean Absolute Error (MAE): 99 minutes
- Root Mean Squared Error (RMSE): 217 minutes

Top predictive features:
- Systolic Blood Pressure
- Diastolic Blood Pressure
- Heart Rate
- Temperature
- Oxygen Saturation

## Repository Contents

| File | Description |
|------|-------------|
| `ed_wait_predictor.py` | Python script for the Streamlit application |
| `model_rf.pkl` | Trained Random Forest model file |
| `sample_input.csv` | Synthetic input sample for testing the app |
| `requirements.txt` | List of Python dependencies |
| `ed_wait_analysis.ipynb` | Full Google Colab notebook with data processing and model training |

## Deployed Application

The Streamlit web application is deployed at the following URL:

https://edwaitpredictor.streamlit.app

The app allows users to input patient vitals and triage timing to receive a predicted ED wait time, along with a recommendation on fast-tracking eligibility.

## Data Disclaimer

The full MIMIC-IV-ED dataset is not included in this repository due to size limitations and data-sharing restrictions. The dataset was accessed securely in Google Colab under a research data use agreement. Only a synthetic sample file is included in this repository to demonstrate the input format used by the model.

## Development Environment

- Developed in Google Colab
- Deployed using Streamlit Cloud
- Languages and libraries:
  - Python
  - pandas, numpy
  - scikit-learn
  - matplotlib
  - streamlit

## Acknowledgments

This project was supported by the Computer Science Department at Kenyon College.  
I would like to thank Professor James Skon for his guidance throughout the project.  
Additional insight on AI hospital systems in China was provided by the Inside China Business YouTube channel.

## Author

Lalasa Nagireddy  
Kenyon College  
COMP401: Senior Seminar in Computer Science  
