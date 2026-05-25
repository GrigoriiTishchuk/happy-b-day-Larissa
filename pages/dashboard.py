import streamlit as st
from components.communication import render_communication_tab
from components.kpi_cards import render_kpis
from components.timeline import render_timeline
from components.map_view import render_map
from components.personal_notes import render_pdf
from styles.style import load_styles
from components.effects import init_particles
from utils.audio import play_ambient 

# INIT
st.set_page_config(page_title="Dashboard", layout="wide")
load_styles()
init_particles()
play_ambient()
# -----------------------------
# HEADER
# -----------------------------
st.title("Relationship Research Dashboard")
st.markdown("""<div><h3>Emotional analytics system • confidential archive</h3></div>""", unsafe_allow_html=True)
st.markdown("---")
# -----------------------------
# KPI SECTION
# -----------------------------
render_kpis()
st.markdown("---")
# -----------------------------
# MAIN SECTIONS
# -----------------------------
tab1, tab2, tab3, tab4 = st.tabs([
    "🧠 Timeline",
    "🗺️ Map",
    "💬 Communication",
    "📸 Personal notes"
])

with tab1:
    render_timeline()

with tab2:
    render_map()

with tab3:
    render_communication_tab()

with tab4:
    render_pdf()