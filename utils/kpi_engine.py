import json
from collections import Counter
from datetime import datetime

def load_events(path="data/events.json"):
    with open(path, "r", encoding="utf-8") as f:
        return json.load(f)

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