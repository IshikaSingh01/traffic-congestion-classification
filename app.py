import streamlit as st
import pandas as pd
import joblib

# Load model
model = joblib.load("deploy_model.pkl")

# Page settings
st.set_page_config(
    page_title="Traffic Congestion Classifier",
    page_icon="🚦",
    layout="centered"
)

# Title
st.title("🚦 Traffic Congestion Classification")
st.write(
    "Enter the current traffic and environmental conditions "
    "to predict the traffic congestion level."
)

st.divider()

# Input fields
avg_speed = st.number_input(
    "Average Speed (km/h)",
    min_value=0.0,
    max_value=150.0,
    value=40.0
)

density = st.number_input(
    "Vehicle Density (vehicles/km)",
    min_value=0.0,
    max_value=300.0,
    value=50.0
)

wait_time = st.number_input(
    "Average Waiting Time (seconds)",
    min_value=0.0,
    max_value=1000.0,
    value=60.0
)

occupancy = st.number_input(
    "Road Occupancy (%)",
    min_value=0.0,
    max_value=100.0,
    value=50.0
)

flow = st.number_input(
    "Traffic Flow (vehicles/hour)",
    min_value=0.0,
    max_value=10000.0,
    value=1500.0
)

queue = st.number_input(
    "Queue Length (vehicles)",
    min_value=0.0,
    max_value=500.0,
    value=20.0
)

acceleration = st.number_input(
    "Average Acceleration (m/s²)",
    min_value=-10.0,
    max_value=10.0,
    value=0.0
)

signal = st.selectbox(
    "Signal State",
    [0, 1, 2]
)

incident = st.selectbox(
    "Incident Level",
    [0, 1, 2, 3]
)

temperature = st.number_input(
    "Temperature (°C)",
    min_value=-20.0,
    max_value=60.0,
    value=25.0
)

visibility = st.number_input(
    "Visibility (km)",
    min_value=0.0,
    max_value=50.0,
    value=10.0
)

rain = st.number_input(
    "Rain Intensity (mm/h)",
    min_value=0.0,
    max_value=100.0,
    value=0.0
)

st.divider()

# Prediction button
if st.button("🚦 Predict Traffic Congestion", use_container_width=True):

    input_data = pd.DataFrame([{
        "avg_speed_kmph": avg_speed,
        "density_veh_per_km": density,
        "avg_wait_time_s": wait_time,
        "occupancy_pct": occupancy,
        "flow_veh_per_hr": flow,
        "queue_length_veh": queue,
        "avg_accel_ms2": acceleration,
        "signal_state_num": signal,
        "incident_num": incident,
        "temp_c": temperature,
        "visibility_km": visibility,
        "rain_intensity_mmph": rain
    }])

    prediction = model.predict(input_data)[0]

    st.success(
        f"Predicted Traffic Condition: **{prediction}**"
    )

    # Probability
    if hasattr(model, "predict_proba"):
        probabilities = model.predict_proba(input_data)[0]

        st.subheader("Prediction Probabilities")

        probability_df = pd.DataFrame({
            "Traffic Condition": model.classes_,
            "Probability": probabilities
        })

        probability_df["Probability"] = (
            probability_df["Probability"] * 100
        ).round(2)

        st.dataframe(
            probability_df,
            use_container_width=True
        )