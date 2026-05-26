import streamlit as st

def load_styles():
    st.markdown("""
    <style>
    .stApp {
        background: linear-gradient(135deg, #0b1020, #0f172a, #111827);
        color: white;
    }
    h1, h2, h3 {
        color: #7dd3fc;
        font-family: Inter, sans-serif;
    }
    .stMetric {
        background: rgba(255,255,255,0.05);
        padding: 10px;
        border-radius: 10px;
    }
    .stButton > button {
        background-color: #1f2937;
        color: white;
        border-radius: 10px;
        border: none;
        padding: 0.5rem 1rem;
    }

    .stButton > button:hover {
        background-color: #374151;
        color: white;
    }

    .stButton > button:active {
        background-color: #111827;
    }
    audio {
        display: none;
    }
    </style>
    """, unsafe_allow_html=True)