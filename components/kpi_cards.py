import streamlit as st
def render_kpis():
    col1, col2, col3, col4 = st.columns(4)
    col1.metric("Shared Days", "∞", "+1 stability")
    col2.metric("Memory Density", "High", "↑ growing")
    col3.metric("Emotional Variance", "Stable", "low noise")
    col4.metric("Connection Index", "98%", "+2%")