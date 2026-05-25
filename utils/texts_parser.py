import re
from datetime import datetime
from collections import defaultdict

def parse_texts(file_path):
    messages = []
    pattern = r"(\d{1,2}\.\d{1,2}\.\d{2,4}), (\d{1,2}:\d{2}) - (.*?): (.*)"
    with open(file_path, "r", encoding="utf-8") as f:
        for line in f:
            match = re.match(pattern, line)
            if match:
                date_str, time_str, sender, text = match.groups()
                try:
                    dt = datetime.strptime(
                        f"{date_str} {time_str}",
                        "%d.%m.%Y %H:%M"
                    )
                except:
                    continue
                messages.append({
                    "datetime": dt,
                    "sender": sender,
                    "text": text
                })
    return messages
