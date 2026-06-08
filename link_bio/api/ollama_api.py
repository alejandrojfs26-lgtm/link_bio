import os
import dotenv
from openai import OpenAI

dotenv.load_dotenv()


class OllamaAPI:

    def __init__(self):
        self.base_url = os.getenv("OLLAMA_URL", "http://localhost:11434/v1")
        self.api_key = os.getenv("OLLAMA_API_KEY", "ollama")
        self.model = os.getenv("OLLAMA_MODEL", "llama3.2:1b")
        self._client = None

    @property
    def client(self):
        if self._client is None:
            self._client = OpenAI(
                base_url=self.base_url,
                api_key=self.api_key,
            )
        return self._client

    def chat(self, messages: list[dict]) -> str:
        response = self.client.chat.completions.create(
            model=self.model,
            messages=messages,
            stream=False,
        )
        return response.choices[0].message.content or ""


OLLAMA_API = OllamaAPI()
