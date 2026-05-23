import streamlit as st
import pydeck as pdk
from utils.loaders import load_json


def render_map():
    st.subheader("Emotional Geography System")
    locations = load_json("data/events.json")
    if not locations:
        st.warning("No location data available.")
        return
    # -----------------------------
    # LAYER DATA
    # -----------------------------
    df = [
        {
            "name": loc["title"],
            "lat": loc["lat"],
            "lon": loc["lon"],
            "emotion": loc.get("emotion", "neutral"),
            "intensity": loc.get("intensity", 0.5),
            "summary": loc.get("summary", "")
        }
        for loc in locations
    ]
    # -----------------------------
    # COLOR MAPPING (emotional heat)
    # -----------------------------
    def get_color(intensity):
        # blue → purple → pink emotional gradient
        r = int(80 + intensity * 120)
        g = int(120 - intensity * 50)
        b = 255
        return [r, g, b]
    # attach colors
    for d in df:
        d["color"] = get_color(d["intensity"])
    # -----------------------------
    # PYDECK LAYER
    # -----------------------------
    layer = pdk.Layer(
        "ScatterplotLayer",
        data=df,
        get_position="[lon, lat]",
        get_color="color",
        get_radius=80,
        pickable=True,
        auto_highlight=True
    )
    # -----------------------------
    # VIEW STATE (HELSINKI CENTERED)
    # -----------------------------
    view_state = pdk.ViewState(
        latitude=60.1699,
        longitude=24.9384,
        zoom=12,
        pitch=40
    )
    # -----------------------------
    # TOOLTIP (MEMORY CARD)
    # -----------------------------
    tooltip = {
        "html": """
        <div style="
            background: rgba(0,0,0,0.8);
            padding: 10px;
            border-radius: 8px;
            color: white;
            font-family: monospace;
            width: 350px
        ">
            <b>{name}</b><br/>
            Emotion: {emotion}<br/>
            Summary: {summary}
        </div>
        """,
        "style": {
            "backgroundColor": "transparent"
        }
    }
    # -----------------------------
    # MAP RENDER
    # -----------------------------
    st.pydeck_chart(pdk.Deck(
        layers=[layer],
        initial_view_state=view_state,
        tooltip=tooltip
    ))