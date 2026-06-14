from deep_translator import GoogleTranslator

LANGUAGES = [
    {"name": "Inglés", "code": "en", "tts_code": "en-US"},
    {"name": "Francés", "code": "fr", "tts_code": "fr-FR"},
    {"name": "Portugués", "code": "pt", "tts_code": "pt-BR"},
    {"name": "Alemán", "code": "de", "tts_code": "de-DE"},
]

_translators = {}


def _get_translator(target: str) -> GoogleTranslator:
    if target not in _translators:
        _translators[target] = GoogleTranslator(source="es", target=target)
    return _translators[target]


def translate_text(text: str, target_lang: str) -> str:
    translator = _get_translator(target_lang)
    return translator.translate(text)


def translate_all(text: str) -> list[dict]:
    results = []
    for lang in LANGUAGES:
        try:
            translated = translate_text(text, lang["code"])
            results.append({
                "name": lang["name"],
                "code": lang["code"],
                "tts_code": lang["tts_code"],
                "text": translated,
            })
        except Exception:
            results.append({
                "name": lang["name"],
                "code": lang["code"],
                "tts_code": lang["tts_code"],
                "text": "(error al traducir)",
            })
    return results
