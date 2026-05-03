import streamlit as st
import requests

st.title("🚢 Titanic Survival Predictor")

# Inputs
name = st.text_input("Name", "Braund, Mr. Owen Harris")
pclass = st.selectbox("Pclass", [1, 2, 3])
sex = st.selectbox("Sex", ["male", "female"])
age = st.number_input("Age", min_value=0.0, value=22.0)
sibsp = st.number_input("SibSp", min_value=0, value=1)
parch = st.number_input("Parch", min_value=0, value=0)
fare = st.number_input("Fare", min_value=0.0, value=7.25)
embarked = st.selectbox("Embarked", ["C", "Q", "S"])

# Button
if st.button("Predict"):
    data = {
        "Name": name,
        "Pclass": pclass,
        "Sex": sex,
        "Age": age,
        "SibSp": sibsp,
        "Parch": parch,
        "Fare": fare,
        "Embarked": embarked
    }

    res = requests.post("http://127.0.0.1:8000/predict", json=data)
    result = res.json()

    if "error" in result:
        st.error(result["error"])
    else:
        st.success(f"{result['result']} (Confidence: {result['confidence']})")