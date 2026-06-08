from dataclasses import dataclass
import reflex as rx
from link_bio.api.translator_api import translate_all


@dataclass
class TranslationItem:
    lang: str = ""
    text: str = ""
    audio_b64: str = ""


class TranslatorState(rx.State):
    source_text: str = ""
    translations: list[TranslationItem] = []
    loading: bool = False

    def set_source_text(self, value: str):
        self.source_text = value

    def translate(self):
        if not self.source_text.strip():
            return

        self.loading = True
        self.translations = []

        yield

        try:
            raw = translate_all(self.source_text)
            self.translations = [
                TranslationItem(lang=name, text=data["text"], audio_b64=data["audio_b64"])
                for name, data in raw.items()
            ]
        except Exception:
            self.translations = [
                TranslationItem(lang="Error", text="Ocurrió un error al traducir. Intenta de nuevo.")
            ]

        self.loading = False
