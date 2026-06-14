import time
from translate import Translator

LANGUAGES = [
    {"name": "Inglés", "code": "en", "tts_code": "en-US"},
    {"name": "Francés", "code": "fr", "tts_code": "fr-FR"},
    {"name": "Portugués", "code": "pt", "tts_code": "pt-BR"},
    {"name": "Alemán", "code": "de", "tts_code": "de-DE"},
]

_last_request = 0.0


def translate_text(text: str, target_lang: str, source_lang: str = "es") -> str:
    global _last_request
    elapsed = time.time() - _last_request
    if elapsed < 0.5:
        time.sleep(0.5 - elapsed)
    _last_request = time.time()

    translator = Translator(from_lang=source_lang, to_lang=target_lang)
    result = translator.translate(text)

    if not result or "MYMEMORY" in result:
        raise ValueError(f"Error al traducir a {target_lang}: servicio no disponible")
    return result


def translate_all(text: str) -> list[dict]:
    errors = []
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
        except Exception as e:
            errors.append(lang["name"])
            results.append({
                "name": lang["name"],
                "code": lang["code"],
                "tts_code": lang["tts_code"],
                "text": "(error al traducir)",
            })

    if errors and not results:
        raise ValueError(f"Error de traducción en: {', '.join(errors)}")
    return results
