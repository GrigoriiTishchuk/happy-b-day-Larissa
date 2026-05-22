import streamlit as st
import time
from utils.sfx import play_click

def typewriter(text: str, speed: float = 0.03, sound_every: int = 3):
    placeholder = st.empty()
    output = ""
    for i, char in enumerate(text):
        output += char
        placeholder.markdown(
            f"""
            <div style="
                font-size:20px;
                color:#7dd3fc;
                font-family:monospace;
                letter-spacing:1px;
                line-height: 1.1;
                margin:0;
                padding:0;
                white-space: pre-wrap;
                ">
                {output}<span style='opacity:0.6'>▌</span>
            </div>
            """,
            unsafe_allow_html=True
        )
        # SOUND LOGIC (FIXED)
        # NOT PER CHARACTER, BUT EVERY NTH CHARACTER TO AVOID OVERLOAD
        if char != " " and i % sound_every == 0:
            play_click("soft")
        # strong punctuation accent
        if char in [".", "!", "?"]:
            play_click("hard")
            time.sleep(speed * 6)
        else:
            time.sleep(speed)

    return placeholder