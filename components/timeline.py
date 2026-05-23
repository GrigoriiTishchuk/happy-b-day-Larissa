import streamlit as st
from utils.loaders import load_json

def render_timeline():
    events = load_json("data/events.json", default=[])
    st.subheader("Memory Timeline")
    # chronological order
    events = sorted(events, key=lambda x: x["date"])
    for event in events:
        # -----------------------------------
        # EVENT CARD
        # -----------------------------------
        st.markdown(f"""
        <div style="
            background: rgba(255,255,255,0.03);
            padding: 22px;
            border-radius: 18px;
            margin-bottom: 25px;
            border: 1px solid rgba(125,211,252,0.12);
            backdrop-filter: blur(6px);
        ">
            <div style="
                font-size: 13px;
                letter-spacing: 2px;
                color: #7dd3fc;
                opacity: 0.8;
                margin-bottom: 6px;
                font-family: monospace;
            ">
                {event['date']}
            </div>

            <div style="
                font-size: 30px;
                font-weight: 700;
                color: white;
                margin-bottom: 10px;
            ">
                {event['title']}
            </div>

            <div style="
                font-size: 16px;
                line-height: 1.8;
                color: rgba(255,255,255,0.88);
                margin-bottom: 18px;
            ">
                {event['story']}
            </div>
        </div>
        """, unsafe_allow_html=True)
        # -----------------------------------
        # TAGS
        # -----------------------------------
        if event.get("tags"):
            tags_html = ""
            for tag in event["tags"]:
                tags_html += f"""
                <span style="
                    background: rgba(125,211,252,0.12);
                    color: #7dd3fc;
                    padding: 6px 12px;
                    border-radius: 999px;
                    font-size: 12px;
                    margin-right: 8px;
                    font-family: monospace;
                ">
                    #{tag}
                </span>
                """
            st.markdown(tags_html, unsafe_allow_html=True)
        st.write("")
        # -----------------------------------
        # IMAGES
        # -----------------------------------
        media = event.get("media", [])
        if media:
            cols = st.columns(min(len(media), 3))
            for i, img in enumerate(media):
                with cols[i % 3]:
                    try:
                        st.image(
                            img,
                            width="stretch"
                        )
                    except:
                        st.warning(f"Missing image: {img}")
        else:
            st.markdown("""
            <div style="
                opacity: 0.55;
                font-style: italic;
                padding-top: 5px;
                padding-bottom: 15px;
                font-size: 14px;
                border-left: 2px solid rgba(125,211,252,0.3);
                padding-left: 12px;
                margin-top: 8px;
                color: rgba(255,255,255,0.75);
            ">
                ARCHIVE STATUS:<br>
                No visual material recovered.<br>
                Memory reconstructed from emotional logs.
            </div>
            """, unsafe_allow_html=True)
        st.markdown("<br>", unsafe_allow_html=True)