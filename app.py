import streamlit as st
import pandas as pd
from src.pipeline.predict_pipeline import CustomData, PredictPipeline

st.set_page_config(page_title="Student Performance Predictor")

st.title("🎓 Student Math Score Predictor")

# Input fields
gender = st.selectbox("Gender", ["male", "female"])
race_ethnicity = st.selectbox("Race/Ethnicity", ["group A", "group B", "group C", "group D", "group E"])
parental_education = st.selectbox("Parental Level of Education", [
    "some high school", "high school", "some college",
    "associate's degree", "bachelor's degree", "master's degree"
])
lunch = st.selectbox("Lunch", ["standard", "free/reduced"])
test_prep = st.selectbox("Test Preparation Course", ["none", "completed"])
reading_score = st.number_input("Reading Score", 0, 100)
writing_score = st.number_input("Writing Score", 0, 100)

# Predict
if st.button("Predict Math Score"):
    try:
        data = CustomData(
            gender=gender,
            race_ethnicity=race_ethnicity,
            parental_level_of_education=parental_education,
            lunch=lunch,
            test_preparation_course=test_prep,
            reading_score=reading_score,
            writing_score=writing_score
        )
        final_df = data.get_data_as_data_frame()

        predict_pipeline = PredictPipeline()
        prediction = predict_pipeline.predict(final_df)

        st.success(f"Predicted Math Score: {prediction[0]:.2f}")
    except Exception as e:
        st.error(f"An error occurred: {e}")
