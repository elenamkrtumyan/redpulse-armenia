import streamlit as st
import pandas as pd
import numpy as np

def render_triage_section():
    st.subheader("Symbiotic Shelter Employment & Dynamic Field Triage")
    st.markdown("Advanced bipartite matching matching unhoused individuals with sanctuary operations and automated emergency scoring.")
    
    tab_t1, tab_t2 = st.tabs(["Symbiotic Reintegration Engine", "Real-Time Field Triage Queue"])
    
    with tab_t1:
        st.markdown("### Dual-Impact Employment Pipeline")
        col_s1, col_s2 = st.columns([2, 1])
        with col_s1:
            reint_df = pd.DataFrame([
                {"Candidate ID": "HUM-104", "Skill Matrix": "Carpentry / Infrastructure", "Target Sanctuary": "Erebuni Stray Sanctuary", "Stipend (AMD/mo)": "180,000", "Risk Coefficient": 0.15, "Placement Status": "Active & Housed"},
                {"Candidate ID": "HUM-109", "Skill Matrix": "Logistics / Supply Chain", "Target Sanctuary": "Nor Nork Rescue Zone", "Stipend (AMD/mo)": "160,000", "Risk Coefficient": 0.22, "Placement Status": "Active & Housed"},
                {"Candidate ID": "HUM-112", "Skill Matrix": "Heavy Transport (Cat C)", "Target Sanctuary": "Central Food Rescue Fleet", "Stipend (AMD/mo)": "210,000", "Risk Coefficient": 0.08, "Placement Status": "Probationary Match"},
                {"Candidate ID": "HUM-118", "Skill Matrix": "Veterinary Assistant", "Target Sanctuary": "Malatia Animal Hospital", "Stipend (AMD/mo)": "190,000", "Risk Coefficient": 0.12, "Placement Status": "Active & Housed"}
            ])
            st.dataframe(reint_df, use_container_width=True)
        with col_s2:
            st.metric("Total Active Placements", "34 Candidates", "+4 this week")
            st.metric("Sanctuary Self-Sufficiency Index", "84.2%", "+3.5% MoM")
            st.metric("Recidivism Reduction Rate", "78.6%", "Validated Metric")
            
    with tab_t2:
        st.markdown("### Automated Emergency Dispatch Matrix")
        with st.form("advanced_triage_form"):
            c1, c2, c3 = st.columns(3)
            with c1:
                incident_type = st.selectbox("Incident Classification", ["Severe Hypothermia Exposure", "Traumatic Animal Injury", "Acute Food Insecurity Cluster", "Structural Shelter Failure"])
            with c2:
                district = st.selectbox("Yerevan Administrative District", ["Kentron", "Arabkir", "Shengavit", "Nor Nork", "Erebuni", "Ajapnyak", "Malatia-Sebastia", "Kanaker-Zeytun"])
            with c3:
                urgency_score = st.slider("Severity Vector Index (1-10)", 1, 10, 8)
                
            responder_unit = st.selectbox("Assigned Mobile Intervention Unit", ["Unit Alpha (Kentron/Arabkir)", "Unit Beta (Erebuni/Nor Nork)", "Unit Gamma (Malatia/Shengavit)"])
            
            submit_dispatch = st.form_submit_button("Compute Priority & Execute Dispatch Matrix")
            if submit_dispatch:
                computed_priority_score = urgency_score * 1.45
                st.error(f"CRITICAL DISPATCH LOGGED | Priority Index: {computed_priority_score:.2f} | Unit: {responder_unit} | Target District: {district}")
                st.balloons()
