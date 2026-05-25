import streamlit as st

def init_particles():
    st.markdown("""
    <style>
    /* soft animated background glow */
    .stApp {
        background: radial-gradient(circle at 20% 20%, rgba(125,211,252,0.08), transparent 40%),
                    radial-gradient(circle at 80% 80%, rgba(168,85,247,0.06), transparent 40%),
                    linear-gradient(135deg, #0b1020, #0f172a, #111827);
    }

    /* subtle floating noise layer */
    .stApp::before {
        content: "";
        position: fixed;
        top: 0;
        left: 0;
        width: 100%;
        height: 100%;
        pointer-events: none;
        opacity: 0.04;
        background-image: url("https://www.transparenttextures.com/patterns/noise.png");
    }

    </style>
    """, unsafe_allow_html=True)