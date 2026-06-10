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

    def send_message(self, form_data: dict = None):
        text = self.input_text.strip()
        if not text:
            return

        self.messages.append({"role": "user", "content": text})
        self.input_text = ""
        self.loading = True

        yield
        yield rx.call_script(
            "setTimeout(function(){var e=document.getElementById('chat-msgs');if(e)e.scrollTop=e.scrollHeight;},30)"
        )

        try:
            api_messages = [m for m in self.messages if m["role"] in ("user", "assistant")]
            if not any(m["role"] == "system" for m in api_messages):
                api_messages.insert(0, {"role": "system", "content": "Eres un asistente muy util."})

            response = CHAT_API.chat(api_messages)
            self.typing_text = response
            self.typing_pos = 0
            self.messages.append({"role": "assistant", "content": ""})
            yield

            yield rx.call_script(
                "(function(){var t='_typing';if(window[t])return;window[t]=setInterval(function(){reflex.call('chat_state.typing_tick')},30)})()"
            )

        except Exception as e:
            self.messages.append({
                "role": "assistant",
                "content": f"No pude conectar con la IA: {e}. Configura GROQ_API_KEY (gratis en console.groq.com) en el .env"
            })
            self.loading = False
            yield

    def typing_tick(self):
        self.typing_pos += 1
        self.messages[-1] = {
            "role": "assistant",
            "content": self.typing_text[:self.typing_pos],
        }
        if self.typing_pos >= len(self.typing_text):
            self.typing_text = ""
            self.typing_pos = 0
            self.loading = False
            yield rx.call_script(
                "clearInterval(window._typing);window._typing=null;"
            )
            yield rx.call_script(
                "setTimeout(function(){var e=document.getElementById('chat-msgs');if(e)e.scrollTop=e.scrollHeight;},30)"
            )
        else:
            yield rx.call_script(
                "setTimeout(function(){var e=document.getElementById('chat-msgs');if(e)e.scrollTop=e.scrollHeight;},30)"
            )

    def clear_chat(self):
        self.messages = []
        self.typing_text = ""
        self.typing_pos = 0
