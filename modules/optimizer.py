import streamlit as st
import numpy as np
import pandas as pd
from scipy.optimize import linprog

def optimize_budget():
    st.subheader("Advanced Multi-Constraint LP Resource Optimizer (SciPy HiGHS)")
    st.markdown("Solves complex resource allocation under strict budgetary, nutritional, and logistical bounds.")
    
    col_opt1, col_opt2 = st.columns(2)
    with col_opt1:
        total_budget = st.number_input("Total Grant Allocation ($)", 1000.0, 50000.0, 7500.0, step=500.0)
        min_human_meals = st.slider("Minimum Mandatory Human Meals", 100, 1000, 300)
    with col_opt2:
        human_vs_animal_bias = st.slider("Vulnerability Equity Index (Human vs Animal Weight)", 0.1, 0.9, 0.65)
        emergency_buffer = st.slider("Emergency Reserve Ratio (%)", 5, 25, 10) / 100.0

    effective_budget = total_budget * (1 - emergency_buffer)
    
    # Decision variables: [Hot Meals, Thermal Blankets, Animal Feed Sacks, Vet Trauma Kits, Mobile Shelter Fuel]
    # Cost vector
    c = [-12.0 * human_vs_animal_bias, -45.0 * human_vs_animal_bias, -55.0 * (1 - human_vs_animal_bias), -110.0 * (1 - human_vs_animal_bias), -80.0]
    
    A_ub = [
        [3.5, 16.0, 22.0, 42.0, 30.0],  # Budget constraint
        [1.0, 0.0, 0.0, 0.0, 0.0],       # Min human meals constraint
        [-1.0, 0.0, 0.0, 0.0, 0.0]       # Upper bound for min human meals
    ]
    b_ub = [
        effective_budget,
        -min_human_meals,
        -min_human_meals
    ]
    
    bounds = [
        (min_human_meals, effective_budget / 3.5),
        (20, effective_budget / 16.0),
        (15, effective_budget / 22.0),
        (5, effective_budget / 42.0),
        (10, effective_budget / 30.0)
    ]
    
    res = linprog(c, A_ub=A_ub, b_ub=b_ub, bounds=bounds, method='highs')
    
    if res.success:
        allocation = np.floor(res.x)
        unit_costs = np.array([3.5, 16.0, 22.0, 42.0, 30.0])
        total_spent = np.dot(allocation, unit_costs)
        slack_cash = total_budget - total_spent
        
        st.success(f"Optimal Allocation Vector Converged (HiGHS Solver Status: Optimal)")
        
        m1, m2, m3, m4, m5 = st.columns(5)
        m1.metric("Hot Meals", f"{int(allocation[0])}", f"${allocation[0]*3.5:.1f}")
        m2.metric("Blankets", f"{int(allocation[1])}", f"${allocation[1]*16.0:.1f}")
        m3.metric("Animal Feed", f"{int(allocation[2])}", f"${allocation[2]*22.0:.1f}")
        m4.metric("Vet Kits", f"{int(allocation[3])}", f"${allocation[3]*42.0:.1f}")
        m5.metric("Fuel Units", f"{int(allocation[4])}", f"${allocation[4]*30.0:.1f}")
        
        st.markdown("### Financial & Operational Auditing Matrix")
        audit_df = pd.DataFrame({
            "Resource Category": ["Hot Human Meals", "Thermal Blankets", "Animal Feed Sacks", "Vet Trauma Kits", "Mobile Shelter Fuel"],
            "Units Allocated": allocation,
            "Unit Cost ($)": unit_costs,
            "Total Subtotal ($)": allocation * unit_costs,
            "Marginal Impact Score": [-c[0], -c[1], -c[2], -c[3], -c[4]]
        })
        st.dataframe(audit_df, use_container_width=True)
        st.info(f"Emergency Reserve Retained: ${total_budget * emergency_buffer:.2f} | Unallocated Liquid Slack: ${slack_cash:.2f}")
    else:
        st.error("Linear Programming solver failed to converge under strict boundary conditions. Adjust constraints.")
