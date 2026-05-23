import streamlit as st

def render_gallery():
    st.subheader("Memory Archive")
    cols = st.columns(3)
    for i, col in enumerate(cols):
        with col:
            st.image("assets/images/gallery/sample.jpg")
            st.caption(f"Memory #{i+1}")