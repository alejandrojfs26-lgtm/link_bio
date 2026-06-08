import reflex as rx
from link_bio.api.ollama_api import OLLAMA_API


class ChatState(rx.State):
    messages: list[dict] = []
    input_text: str = ""
    loading: bool = False

    def send_message(self):
        if not self.input_text.strip():
            return

        self.messages.append({"role": "user", "content": self.input_text})
        self.input_text = ""
        self.loading = True

        yield

        try:
            api_messages = [m for m in self.messages if m["role"] in ("user", "assistant")]
            if not any(m["role"] == "system" for m in api_messages):
                api_messages.insert(0, {"role": "system", "content": "Eres un asistente muy util."})

            response = OLLAMA_API.chat(api_messages)
            self.messages.append({"role": "assistant", "content": response})
        except Exception:
            self.messages.append({
                "role": "assistant",
                "content": "No pude conectar con el modelo de IA. Asegúrate de que Ollama esté corriendo o configura OLLAMA_URL en el .env"
            })

        self.loading = False

    def clear_chat(self):
        self.messages = []
