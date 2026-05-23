import streamlit as st
import time

def typewriter(text: str, speed: float = 0.03):
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
        # strong punctuation accent
        if char in [".", "!", "?"]:
            time.sleep(speed * 6)
        else:
            time.sleep(speed)

    return placeholder