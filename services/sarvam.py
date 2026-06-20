
import requests
from config import SARVAM_API_KEY, SARVAM_MODEL, SARVAM_MODE


def translate_caption(caption, target_language_code):
    """
    Translate English caption to Indian language using Sarvam AI.

    Args:
        caption (str): English caption to translate
        target_language_code (str): Sarvam language code e.g. "gu-IN"

    Returns:
        str: Translated caption in target language
    """

    url = "https://api.sarvam.ai/translate"

    headers = {
        "api-subscription-key": SARVAM_API_KEY,
        "Content-Type": "application/json"
    }

    payload = {
        "input": caption,
        "source_language_code": "en-IN",
        "target_language_code": target_language_code,
        "mode": SARVAM_MODE,
        "model": SARVAM_MODEL
    }

    response = requests.post(url, json=payload, headers=headers)

    result = response.json()
    return result["translated_text"]