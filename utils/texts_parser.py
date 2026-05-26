import re
from datetime import datetime
from collections import defaultdict
from utils.emotions_engine import detect_emotion

def parse_texts(file_path):
    messages = []
    # WhatsApp export format: "dd.mm.yyyy, hh:mm - Sender: Message"
    pattern = r"(\d{1,2}\.\d{1,2}\.\d{2,4}), (\d{1,2}:\d{2}) - (.*?): (.*)"
    with open(file_path, "r", encoding="utf-8") as f:
        for line in f:
            match = re.match(pattern, line)
            if match:
                date_str, time_str, sender, text = match.groups()
                try:
                    dt = datetime.strptime(
                        f"{date_str} {time_str}",
                        "%d.%m.%Y %H:%M")
                except:
                    continue
                messages.append({
                    "datetime": dt,
                    "sender": sender,
                    "text": text
                })
    return messages

def enrich_messages(messages):
    enriched = []
    for m in messages:
        emo = detect_emotion(m["text"])
        # Unapcking dict with **m notation and adding new keys to message
        enriched.append({**m,
            # VADER core
            "sentiment_score": emo["score"],
            "sentiment_label": emo["label"],
            # your ML-style emotion label
            "emotion": emo["emotion"]
        })
    return enriched