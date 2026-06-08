import reflex as rx
from link_bio.api.translator_api import translate_all


class TranslatorState(rx.State):
    source_text: str = ""
    translations: dict = {}
    loading: bool = False

    def set_source_text(self, value: str):
        self.source_text = value

    def translate(self):
        if not self.source_text.strip():
            return

        self.loading = True
        self.translations = {}

        yield

        try:
            self.translations = translate_all(self.source_text)
        except Exception:
            self.translations = {
                "Error": {"text": "Ocurrió un error al traducir. Intenta de nuevo.", "audio_b64": ""}
            }

        self.loading = False
