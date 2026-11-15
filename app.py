import streamlit as st
from modules.predictor import train_risk_model, predict_risk
from modules.optimizer import optimize_budget
from modules.triage import render_triage_section
import pandas as pd

st.set_page_config(page_title="ShelterPulse Armenia", layout="wide")
st.title("ShelterPulse Armenia: Enterprise Dual-Impact Platform")
st.markdown("Connecting surplus resources, environmental risk modeling, and symbiotic reintegration in Yerevan.")

tab1, tab2, tab3, tab4 = st.tabs(["Logistics & Routing", "Risk Predictor (ML)", "Budget Optimizer", "Field Triage & Symbiosis"])

with tab1:
    st.header("Surplus Food & Resource Routing")
    st.markdown("Optimized transport network connecting Yerevan supermarkets to shelters.")
    donors = st.slider("Active Donors", 1, 10, 4)
    st.success(f"Active route calculated across {donors} distribution nodes in Kentron and Arabkir districts.")

with tab2:
    st.header("Environmental Risk & Exposure Predictor")
    model = train_risk_model()
    col1, col2 = st.columns(2)
    with col1:
        temp = st.slider("Temperature (°C)", -20.0, 40.0, 2.0)
        hum = st.slider("Humidity (%)", 10.0, 100.0, 75.0)
        wind = st.slider("Wind Speed (km/h)", 0.0, 50.0, 12.0)
    with col2:
        ent = st.selectbox("Entity Type", [0, 1], format_func=lambda x: "Human" if x==0 else "Animal")
        shelter = st.selectbox("Shelter Access", [0, 1], format_func=lambda x: "No Access" if x==0 else "Secured Shelter")
    
    if st.button("Run Risk Prediction Model"):
        input_df = pd.DataFrame({'temp': [temp], 'humidity': [hum], 'wind_speed': [wind], 'entity_type': [ent], 'shelter_access': [shelter]})
        cls, probs = predict_risk(model, input_df)
        risk_labels = ["Low Risk (Stable)", "Moderate Risk (Monitor)", "Critical Exposure Risk (Immediate Action)"]
        st.metric("Predicted Vulnerability Status", risk_labels[cls], f"Confidence: {probs[cls]*100:.1f}%")

with tab3:
    st.header("Constrained Resource Allocation (SciPy)")
    bgt = st.number_input("Grant Budget ($)", 500.0, 10000.0, 2500.0)
    hw = st.slider("Human vs Animal Priority Weight", 0.0, 1.0, 0.6)
    optimize_budget(bgt, hw)

with tab4:
    render_triage_section()
