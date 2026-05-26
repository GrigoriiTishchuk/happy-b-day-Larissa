import streamlit as st
from utils.loaders import load_json


def render_timeline():
    events = load_json("data/events.json", default=[])
    events = sorted(events, key=lambda x: x["date"])
    st.subheader("Memory Timeline")
    for event in events:
        # CARD CONTAINER 
        with st.container():
            st.markdown(f"### {event['title']}")
            st.caption(event["date"])
            # STORY (no raw HTML)
            st.write(event["story"])
            # TAGS 
            tags = event.get("tags", [])
            if tags:
                cols = st.columns(len(tags))
                for i, tag in enumerate(tags):
                    with cols[i]:
                        st.markdown(
                            f"""
                            <div style="
                                background: rgba(125,211,252,0.12);
                                color: #7dd3fc;
                                padding: 6px 10px;
                                border-radius: 999px;
                                font-size: 12px;
                                text-align: center;
                                font-family: monospace;
                            ">
                                #{tag}
                            </div>
                            """,
                            unsafe_allow_html=True
                        )
            # MEDIA (safe handling)
            media = event.get("media", [])
            if media:
                cols = st.columns(min(len(media), 3))
                for i, img in enumerate(media):
                    with cols[i % 3]:
                        st.image(img, width="stretch")
            else:
                st.markdown("""
                <div style="
                    opacity: 0.5;
                    font-style: italic;
                    border-left: 2px solid rgba(125,211,252,0.3);
                    padding-left: 10px;
                    margin-top: 10px;
                ">
                    No visual archive available for this event.
                </div>
                """, unsafe_allow_html=True)
            st.divider()