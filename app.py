
import streamlit as st

import pandas as pd
import joblib

# Load saved models
classification_model = joblib.load("best_classification_model.joblib")
regression_model = joblib.load("best_regression_model.joblib")

# Page configuration
st.set_page_config(
    page_title="Real Estate Investment Advisor",
    page_icon="🏠",
    layout="wide"
)

# App title
st.title("🏠 Real Estate Investment Advisor")
st.write("Predict Property Investment Potential and Future Value")

st.divider()

# Property input form
st.header("Enter Property Details")

with st.form("property_form"):

    col1, col2 = st.columns(2)

    with col1:
        area = st.number_input("Area (sqft)", min_value=1.0, value=1500.0)
        bedrooms = st.number_input("Bedrooms", min_value=1, value=3)
        bathrooms = st.number_input("Bathrooms", min_value=1, value=2)
        floors = st.number_input("Floors", min_value=1, value=1)
        year_built = st.number_input(
            "Year Built", min_value=1900, max_value=2026, value=2015
        )

    with col2:
        location_score = st.number_input(
            "Location Score", min_value=0.0, value=7.0
        )
        school_score = st.number_input(
            "School Score", min_value=0.0, value=8.0
        )
        current_price = st.number_input(
            "Current Property Price (₹)",
            min_value=1.0,
            value=500000.0
        )

    submit = st.form_submit_button("Predict Property Value")

# Prediction
if submit:

    property_age = 2026 - year_built
    price_per_sqft = current_price / area

    # Classification input
    classification_input = pd.DataFrame([{
        "Area_sqft": area,
        "Bedrooms": bedrooms,
        "Bathrooms": bathrooms,
        "Floors": floors,
        "Property_Age": property_age,
        "Location_Score": location_score,
        "School_Score": school_score,
        "Current_Price": current_price,
        "Price_Per_Sqft": price_per_sqft
    }])

    # Regression input
    regression_input = pd.DataFrame([{
        "Area_sqft": area,
        "Bedrooms": bedrooms,
        "Bathrooms": bathrooms,
        "Floors": floors,
        "Property_Age": property_age,
        "Location_Score": location_score,
        "School_Score": school_score,
        "Current_Price": current_price
    }])

    # Make predictions
    investment_prediction = classification_model.predict(
        classification_input
    )[0]

    future_price = regression_model.predict(
        regression_input
    )[0]

    # Display results
    st.divider()
    st.header("Prediction Results")

    result_col1, result_col2 = st.columns(2)

    with result_col1:
        st.subheader("Investment Classification")

        if investment_prediction == 1:
            st.success("Good Investment")
        else:
            st.warning("Not Good Investment")

    with result_col2:
        st.subheader("Estimated Price After 5 Years")
        st.metric(
            "Predicted Future Price",
            f"₹ {future_price:,.2f}"
        )

    st.info(
        "These predictions are based on the trained machine learning "
        "models and the dataset used in this project."
    )
