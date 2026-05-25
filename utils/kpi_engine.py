import json
from collections import Counter
from datetime import datetime
import pandas as pd
def load_events(path="data/events.json"):
    with open(path, "r", encoding="utf-8") as f:
        return json.load(f)

# MAIN DASHBOARD KPIS
def compute_kpis(events):
    if not events:
        return {}
    # METRICS
    memory_count = len(events)
    intensities = [e.get("intensity", 0.5) for e in events]
    avg_intensity = sum(intensities) / len(intensities)
    emotions = [e.get("emotion", "unknown")for e in events]
    dominant_emotion = Counter(emotions).most_common(1)[0][0]
    # TIME SPREAD (density proxy)
    dates = sorted([
        datetime.strptime(e["date"], "%Y-%m-%d")
        for e in events
        if "date" in e
    ])
    if len(dates) > 1:
        span_days = (dates[-1] - dates[0]).days + 1
        density = memory_count / span_days
    else:
        density = 1

    # STABILITY INDEX (pseudo)
    variance = sum(
        (x - avg_intensity) ** 2 for x in intensities
    ) / len(intensities)
    stability = max(0, 1 - variance)
    return {
        "memory_count": memory_count,
        "avg_intensity": round(avg_intensity, 2),
        "dominant_emotion": dominant_emotion,
        "density": round(density, 2),
        "stability": round(stability, 2)
    }

def build_texts_df(messages):
    df = pd.DataFrame(messages)
    df["date"] = df["datetime"].dt.date
    df["hour"] = df["datetime"].dt.hour
    # Fill missing emotion/sentiment data with neutral defaults
    df["sentiment_label"] = df["sentiment_label"]
    df["sentiment_score"] = df["sentiment_score"]
    df["emotion"] = df["emotion"]
    return df

# KPIS FOR COMMUNICATION
def compute_basic_metrics(df):
    return {
        "total_messages": len(df),
        "unique_days": df["date"].nunique(),
        "messages_per_day": len(df) / max(df["date"].nunique(), 1)
    }