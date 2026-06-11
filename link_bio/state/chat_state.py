import asyncio
import reflex as rx
from link_bio.api.ollama_api import CHAT_API


class ChatState(rx.State):
    messages: list[dict] = []
    input_text: str = ""
    loading: bool = False
    typing_text: str = ""
    typing_pos: int = 0

    def set_input_text(self, value: str):
        self.input_text = value

    def clear_chat(self):
        self.messages = []
        self.typing_text = ""
        self.typing_pos = 0

    async def send_message(self, form_data: dict = None):
        text = self.input_text.strip()
        if not text:
            return

        self.messages.append({"role": "user", "content": text})
        self.input_text = ""
        self.loading = True
        yield

        try:
            api_messages = [m for m in self.messages if m["role"] in ("user", "assistant")]
            if not any(m["role"] == "system" for m in api_messages):
                api_messages.insert(0, {"role": "system", "content": "Eres un asistente muy util."})

            response = await asyncio.to_thread(CHAT_API.chat, api_messages)
            self.typing_text = response
            self.typing_pos = 0
            self.messages.append({"role": "assistant", "content": ""})
            yield

            for i in range(len(response)):
                self.typing_pos = i + 1
                self.messages[-1] = {
                    "role": "assistant",
                    "content": response[:i + 1],
                }
                await asyncio.sleep(0.015)
                yield

            self.typing_text = ""
            self.typing_pos = 0
            self.loading = False
            yield

        except Exception as e:
            self.messages.append({
                "role": "assistant",
                "content": f"No pude conectar con la IA: {e}. Configura GROQ_API_KEY (gratis en console.groq.com) en el .env"
            })
            self.loading = False
            yield
