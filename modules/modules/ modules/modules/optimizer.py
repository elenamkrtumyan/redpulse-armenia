import streamlit as st
import numpy as np
from scipy.optimize import linprog

def optimize_budget():
    st.header("Constrained Resource Allocation (SciPy LP)")
    budget = st.number_input("Grant Budget ($)", 500.0, 10000.0, 2500.0)
    human_weight = st.slider("Human vs Animal Priority Weight", 0.0, 1.0, 0.6)
    
    costs = [2.5, 14.0, 18.0, 35.0]
    impacts = [
        -(10 * human_weight),
        -(45 * human_weight),
        -(50 * (1 - human_weight)),
        -(90 * (1 - human_weight))
    ]
    
    A_ub = [costs]
    b_ub = [budget]
    bounds = [
        (int(budget * 0.05 / 2.5), None),
        (int(budget * 0.05 / 14.0), None),
        (int(budget * 0.05 / 18.0), None),
        (int(budget * 0.05 / 35.0), None)
    ]
    
    res = linprog(impacts, A_ub=A_ub, b_ub=b_ub, bounds=bounds, method='highs')
    
    if res.success:
        q_meals, q_blankets, q_feed, q_vet = np.floor(res.x)
        spent = (q_meals*2.5) + (q_blankets*14.0) + (q_feed*18.0) + (q_vet*35.0)
        
        m1, m2, m3, m4 = st.columns(4)
        m1.metric("Hot Human Meals", f"{int(q_meals)} units", f"${q_meals*2.5:.1f}")
        m2.metric("Thermal Blankets", f"{int(q_blankets)} units", f"${q_blankets*14.0:.1f}")
        m3.metric("Animal Feed Sacks (10kg)", f"{int(q_feed)} sacks", f"${q_feed*18.0:.1f}")
        m4.metric("Veterinary Trauma Kits", f"{int(q_vet)} kits", f"${q_vet*35.0:.1f}")
        
        st.caption(f"Total Utilized Budget: ${spent:.2f} / ${budget:.2f} | Optimization Status: Optimal Solution Converged")
    else:
        st.error("Optimization failed to converge with current constraints.")
