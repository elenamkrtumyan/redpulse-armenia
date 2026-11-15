import streamlit as st
import pandas as pd

def render_triage_section():
    st.subheader("Symbiotic Shelter Employment & Field Triage")
    st.markdown("Matches unhoused individuals seeking stability with paid operational roles at animal sanctuaries.")
    
    col_sym, col_tri = st.columns(2)
    
    with col_sym:
        st.markdown("**Active Reintegration Placements**")
        reint_df = pd.DataFrame([
            {"Case ID": "HUM-104", "Skills": "Carpentry / Maintenance", "Assigned Sanctuary": "Erebuni Stray Sanctuary", "Role": "Kennel Construction & Repair", "Status": "Housed & Employed"},
            {"Case ID": "HUM-109", "Skills": "Animal Care / Logistics", "Assigned Sanctuary": "Nor Nork Animal Rescue Zone", "Role": "Feeding & Intake Coordinator", "Status": "Housed & Employed"},
            {"Case ID": "HUM-112", "Skills": "Driving (Cat B)", "Assigned Sanctuary": "Central Food Rescue Fleet", "Role": "Surplus Collection Driver", "Status": "Onboarding"}
        ])
        st.dataframe(reint_df, use_container_width=True)
        
    with col_tri:
        st.markdown("**Submit Field Triage Alert**")
        with st.form("triage_form"):
            alert_cat = st.selectbox("Emergency Category", ["Unhoused Person - Medical/Exposure", "Injured/Stray Animal - Urgent"])
            district = st.selectbox("Yerevan District", ["Kentron", "Shengavit", "Ajapnyak", "Erebuni", "Nor Nork", "Arabkir", "Malatia-Sebastia"])
            severity = st.select_slider("Observed Severity", options=["Low", "Moderate", "High", "Life-Threatening"])
            submitted = st.form_submit_button("Dispatch Rapid Response")
            if submitted:
                st.success(f"Triage Ticket Logged: {alert_cat} in {district} [{severity}]. Nearest mobile unit notified.")
