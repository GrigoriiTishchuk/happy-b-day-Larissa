from vaderSentiment.vaderSentiment import SentimentIntensityAnalyzer

_analyzer = None
def get_model():
    global _analyzer
    if _analyzer is None:
        _analyzer = SentimentIntensityAnalyzer()
    return _analyzer


def detect_sentiment(text: str):
    """
    Returns:
    - compound score (-1 to 1)
    - label (positive/neutral/negative)
    """
    analyzer = get_model()
    score = analyzer.polarity_scores(text)["compound"]
    if score >= 0.05:
        label = "positive"
    elif score <= -0.05:
        label = "negative"
    else:
        label = "neutral"

    return {
        "score": score,
        "label": label
    }

def detect_emotion(text: str):
    res = detect_sentiment(text)
    score = res["score"]
    # lightweight emotion mapping (simple ML heuristic layer)
    if score > 0.6:
        emotion = "joy"
    elif score > 0.2:
        emotion = "affection"
    elif score > 0.05:
        emotion = "calm"
    elif score < -0.6:
        emotion = "anger"
    elif score < -0.2:
        emotion = "sadness"
    else:
        emotion = "neutral"
    res["emotion"] = emotion
    return res