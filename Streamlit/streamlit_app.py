import json
import streamlit as st
import requests
import os

user_options = {}

st.title('Term Loan Subscription Prediction')
current_dir = os.path.dirname(os.path.abspath(__file__))

file_path = os.path.join(current_dir, "streamlit_options.json")
print("Looking for:", file_path)
streamlit_options = json.load(open(file_path))

for field_name, range in streamlit_options["slider_fields"].items():
    a, b = range
    min_val=round(a)
    max_val=round(b)
    current_value = round((min_val + max_val)/2)
    user_options[field_name] = st.sidebar.slider(field_name, min_val, max_val, value=current_value)

for field_name, values in streamlit_options["single_select_fields"].items():
    user_options[field_name] = st.sidebar.selectbox(field_name, values)


user_options


if st.button('Predict'):
    data = json.dumps(user_options, indent=2)
    r = requests.post('http://142.93.202.5:8000/predict', data=data)
    st.write(r.json())
    