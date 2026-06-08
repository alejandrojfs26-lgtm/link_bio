import reflex as rx
from link_bio.api.translator_api import translate_all


class TranslatorState(rx.State):
    source_text: str = ""
    translations: list[dict] = []
    loading: bool = False
    listening: bool = False

    def set_source_text(self, value: str):
        self.source_text = value

    def play_tts(self, text: str, lang: str):
        safe = text.replace("\\", "\\\\").replace("'", "\\'").replace("\n", "\\n")
        js = (
            "var u=new SpeechSynthesisUtterance();"
            f"u.text='{safe}';u.lang='{lang}';u.rate=1.0;"
            "var vl=speechSynthesis.getVoices().filter(function(v){return v.lang.startsWith(u.lang)});"
            "var g=vl.filter(function(v){return v.name.indexOf('Google')>-1});"
            "if(g.length>0){u.voice=g[0]}else{"
            "var m=vl.filter(function(v){return v.name.indexOf('Microsoft')>-1});"
            "if(m.length>0){u.voice=m[0]}else if(vl.length>0){u.voice=vl[0]}"
            "}"
            "speechSynthesis.speak(u);"
        )
        yield rx.call_script(js)

    async def listen_speech(self):
        self.listening = True
        yield
        yield rx.call_script(
            "(()=>new Promise(r=>{var sr=new (window.SpeechRecognition||window.webkitSpeechRecognition)();sr.lang='es-ES';sr.interimResults=false;sr.onresult=e=>r(e.results[0][0].transcript);sr.start()}))()",
            TranslatorState.set_recognized_text,
        )

    def translate(self):
        if not self.source_text.strip():
            return

        self.loading = True
        self.translations = []

        yield

        try:
            self.translations = translate_all(self.source_text)
        except Exception:
            self.translations = [
                {"name": "Error", "text": "Ocurrió un error al traducir. Intenta de nuevo."}
            ]

        self.loading = False
