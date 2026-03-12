from deep_translator import GoogleTranslator
from langdetect import detect

def detect_lang(text):
    
    # If message too short → assume English
    if len(text) < 5:
        return "en"

    try:
        lang = detect(text)

        # Fix wrong detections
        if lang in ["so", "fi", "et"]:
            return "en"

        return lang

    except:
        return "en"


def to_english(text):
    lang = detect_lang(text)

    if lang == "en":
        return text, "en"

    translated = GoogleTranslator(source=lang, target="en").translate(text)
    return translated, lang


def to_user_lang(text, lang):
    if lang == "en":
        return text

    translated = GoogleTranslator(source="en", target=lang).translate(text)
    return translated
