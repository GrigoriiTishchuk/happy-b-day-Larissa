import streamlit as st

def play_ambient():
    st.audio(
        "assets/audio/NAD.mp3",
        autoplay=True,
        loop=True
    )