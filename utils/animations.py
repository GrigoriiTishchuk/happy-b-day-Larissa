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

def fade_transition(duration=1.2):
    st.markdown(f"""
    <style>
    @keyframes fadeToBlack {{
        from {{
            opacity: 0;
        }}
        to {{
            opacity: 1;
        }}
    }}
    .fade-overlay {{
        position: fixed;
        top: 0;
        left: 0;
        width: 100vw;
        height: 100vh;
        background: black;
        z-index: 999999;
        pointer-events: none;
        animation: fadeToBlack {duration}s ease-in-out forwards;
    }}
    </style>

    <div class="fade-overlay"></div>
    """, unsafe_allow_html=True)

    time.sleep(duration)