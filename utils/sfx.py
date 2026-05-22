import streamlit as st

def play_click(volume_note="soft"):
    """
    Invisible sound trigger for Streamlit UI.
    No audio widget shown on screen.
    """
    if volume_note == "soft":
        src = "assets/audio/click.mp3"
    else:
        src = "assets/audio/spacebar.mp3"

    audio_html = f"""
    <audio autoplay hidden style="display:none;padding:0;margin:0;height:0;width:0;overflow:hidden;position:absolute;top:-1000px;left:-1000px;">
        <source src="{src}" type="audio/mp3">
    </audio>
    """
    st.markdown(audio_html, unsafe_allow_html=True)