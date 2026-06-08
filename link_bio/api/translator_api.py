import base64
import tempfile
from translate import Translator
from gtts import gTTS

LANGUAGES = {
    "Inglés": "en",
    "Francés": "fr",
    "Portugués": "pt",
    "Alemán": "de",
}


def translate_text(text: str, target_lang: str, source_lang: str = "es") -> str:
    translator = Translator(from_lang=source_lang, to_lang=target_lang)
    return translator.translate(text)


def text_to_speech_b64(text: str, lang: str) -> str:
    tts = gTTS(text=text, lang=lang)
    with tempfile.NamedTemporaryFile(suffix=".mp3", delete=True) as f:
        tts.save(f.name)
        with open(f.name, "rb") as af:
            return base64.b64encode(af.read()).decode()


def translate_all(text: str) -> dict[str, dict]:
    results = {}
    for name, code in LANGUAGES.items():
        translated = translate_text(text, code)
        audio_b64 = text_to_speech_b64(translated, code)
        results[name] = {"text": translated, "audio_b64": audio_b64}
    return results
