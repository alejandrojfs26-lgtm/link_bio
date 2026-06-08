from translate import Translator

LANGUAGES = [
    {"name": "Inglés", "code": "en", "tts_code": "en-US"},
    {"name": "Francés", "code": "fr", "tts_code": "fr-FR"},
    {"name": "Portugués", "code": "pt", "tts_code": "pt-BR"},
    {"name": "Alemán", "code": "de", "tts_code": "de-DE"},
]


def translate_text(text: str, target_lang: str, source_lang: str = "es") -> str:
    translator = Translator(from_lang=source_lang, to_lang=target_lang)
    return translator.translate(text)


def translate_all(text: str) -> list[dict]:
    results = []
    for lang in LANGUAGES:
        translated = translate_text(text, lang["code"])
        results.append({
            "name": lang["name"],
            "code": lang["code"],
            "tts_code": lang["tts_code"],
            "text": translated,
        })
    return results
