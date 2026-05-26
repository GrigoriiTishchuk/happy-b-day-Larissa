import streamlit as st
import time
from utils.animations import typewriter, fade_transition
st.set_page_config(
    page_title="Relationship Research Dashboard",
    layout="wide",
    initial_sidebar_state="collapsed"
)
# STYLE
st.markdown("""
<style>
audio {
    display: none;
}
.stApp {
    background: linear-gradient(135deg, #0b1020, #0f172a, #111827);
    color: white;
}
h1, h2, h3 {
    color: #7dd3fc;
    font-family: Inter, sans-serif;
}
.center {
    text-align: center;
}

</style>
""", unsafe_allow_html=True)


# STATE INIT
if "phase" not in st.session_state:
    st.session_state.phase = "gate"

# 1. START GATE (IMPORTANT FOR AUDIO)
if st.session_state.phase == "gate":
    st.title("Emotional Research System")
    st.markdown("### System requires initialization to activate sensory modules.")
    if st.button("▶ Initialize System"):
        st.session_state.phase = "boot"
        st.rerun()

# 2. BOOT SEQUENCE (TYPEWRITER + SOUND)
elif st.session_state.phase == "boot":
    st.title("Initializing System...")
    st.audio("assets/audio/keyboard1.mp3",autoplay=True)
    boot_messages = [
        "INITIALIZING RELATIONSHIP RESEARCH SYSTEM...",
        "RESEARCH SUBJECT: LARISSA ZOЁ HERRMANN...",
        "LOADING EMOTIONAL DATASETS...",
        "SYNCING MEMORY ARCHIVES...",
        "CALIBRATING AFFECTIVE METRICS...",
        "SYSTEM READY."
    ]
    placeholder = st.empty()
    for msg in boot_messages:
        typewriter(msg, speed=0.02)
        time.sleep(0.5) 
    time.sleep(1.5)
    fade_transition()
    st.session_state.phase = "intro"
    st.rerun()

# 3. INTRO VIDEO
elif st.session_state.phase == "intro":
    st.markdown("<h1 class='center'>Message From Lead Researcher</h1>", unsafe_allow_html=True)
    st.markdown("---")
    st.video("assets/video/intro.mp4", muted=True)
    st.markdown("---")
    if st.button("Enter Research Dashboard"):
        fade_transition()
        st.session_state.phase = "dashboard"
        st.rerun()

# 4. DASHBOARD ROUTE
elif st.session_state.phase == "dashboard":
    st.switch_page("pages/dashboard.py")