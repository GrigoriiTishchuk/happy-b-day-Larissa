import streamlit as st
from utils.kpi_engine import load_events, compute_kpis

def render_kpis():
    events = load_events()
    kpis = compute_kpis(events)
    col1, col2, col3, col4 = st.columns(4)
    
    # MEMORY UNITS
    col1.markdown("""
    <div style="display:flex; align-items:center; gap:6px;">
        <span style="font-weight:600;">Memory Units</span>
        <span title="Total number of shared recorded events"
              style="cursor:help; opacity:0.7;">❓</span>
    </div>
    """, unsafe_allow_html=True)
    col1.metric("", kpis["memory_count"])

    # INTENSITY
    col2.markdown("""
    <div style="display:flex; align-items:center; gap:6px;">
        <span style="font-weight:600;">Emotional Intensity</span>
        <span title="Average emotional strength across all recorded events"
              style="cursor:help; opacity:0.7;">❓</span>
    </div>
    """, unsafe_allow_html=True)
    col2.metric("", kpis["avg_intensity"])

    # EMOTION STATE
    col3.markdown("""
    <div style="display:flex; align-items:center; gap:6px;">
        <span style="font-weight:600;">Dominant State</span>
        <span title="Most frequently observed emotional state"
              style="cursor:help; opacity:0.7;">❓</span>
    </div>
    """, unsafe_allow_html=True)
    col3.metric("", kpis["dominant_emotion"])

    # STABILITY
    col4.markdown("""
    <div style="display:flex; align-items:center; gap:6px;">
        <span style="font-weight:600;">System Stability</span>
        <span title="Consistency of emotional patterns over time"
              style="cursor:help; opacity:0.7;">❓</span>
    </div>
    """, unsafe_allow_html=True)
    col4.metric("", kpis["stability"])

    st.markdown("---")
    st.markdown(f"""
    ### System Interpretation
    - Emotional density: **{kpis['density']} events/day**
    - System state: **adaptive but stable**
    - Relationship model: **continuously evolving dataset**
    """)