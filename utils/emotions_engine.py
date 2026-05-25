from transformers import pipeline
# lazy-load model (important for Streamlit performance)
_model = None

def get_model():
    global _model
    if _model is None:
        _model = pipeline("sentiment-analysis",model="cardiffnlp/twitter-roberta-base-sentiment")
    return _model

def detect_emotion(text: str):
    """
    ML-only sentiment detection.
    """
    model = get_model()
    if not text or not text.strip():
        return {
            "score": 0.0,
            "label": "neutral"
        }
    result = model(text[:512])[0]
    label = result["label"]
    score = result["score"]
    # normalize to [-1, 1]
    if label == "POSITIVE":
        final_score = float(score)
        final_label = "positive"
    else:
        final_score = -float(score)
        final_label = "negative"
    return {
        "score": final_score,
        "label": final_label
    }