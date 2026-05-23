import streamlit as st
from utils.loaders import load_json

def render_timeline():
    st.subheader("Memory Timeline")
    memories = load_json("data/memories.json")
    for m in memories:
        st.markdown(f"""
        **{m['title']}**  
        {m['description']}
        ---
        """)