import numpy as np
from sklearn.ensemble import RandomForestClassifier
import streamlit as st

@st.cache_resource
def train_risk_model():
    np.random.seed(42)
    X = np.random.rand(500, 5) # temp, humidity, wind, entity_type, shelter_access
    y = np.random.choice([0, 1, 2], size=500, p=[0.5, 0.3, 0.2])
    model = RandomForestClassifier(n_estimators=120, random_state=42)
    model.fit(X, y)
    return model

def predict_risk(model, input_data):
    probs = model.predict_proba(input_data)[0]
    pred_class = model.predict(input_data)[0]
    return pred_class, probs
