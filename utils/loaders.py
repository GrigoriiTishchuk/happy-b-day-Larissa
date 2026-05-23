import json
import os
import streamlit as st
import logging
@st.cache_data
def load_json(path: str, default=None):
    logger = logging.getLogger(__name__)
    """
    Safely loads JSON files for Streamlit apps.
    Args:
        path (str): relative or absolute file path
        default: fallback value if file is missing or broken
    Returns:
        dict or list (parsed JSON), or default
    """
    if default is None:
        default = {}
    try:
        # normalize path (important when running Streamlit)
        if not os.path.isabs(path):
            path = os.path.join(os.getcwd(), path)
        if not os.path.exists(path):
            return default
        with open(path, "r", encoding="utf-8") as f:
            return json.load(f)

    except json.JSONDecodeError:
        logger.warning(f"Failed to load JSON: {path}")
        return default
    except Exception:
        logger.error(f"Unexpected error occurred while loading JSON: {path}")
        return default