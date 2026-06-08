import os
import dotenv
from openai import OpenAI

dotenv.load_dotenv()

GROQ_URL = "https://api.groq.com/openai/v1"
GROQ_MODEL = "llama3-8b-8192"


class ChatAPI:

    def __init__(self):
        self._client = None
        self._mode = None
        self._model = None

    @property
    def client(self):
        if self._client is None:
            groq_key = os.getenv("GROQ_API_KEY")
            ollama_url = os.getenv("OLLAMA_URL")

            if groq_key:
                self._mode = "groq"
                self._model = os.getenv("GROQ_MODEL", GROQ_MODEL)
                self._client = OpenAI(base_url=GROQ_URL, api_key=groq_key)
            elif ollama_url:
                self._mode = "ollama"
                self._model = os.getenv("OLLAMA_MODEL", "llama3.2:1b")
                self._client = OpenAI(base_url=ollama_url, api_key=os.getenv("OLLAMA_API_KEY", "ollama"))
            else:
                self._mode = None
        return self._client

    def chat(self, messages: list[dict]) -> str:
        if not self.client:
            raise ConnectionError(
                "No hay API configurada. Agrega GROQ_API_KEY (recomendado, gratis) "
                "u OLLAMA_URL en el archivo .env"
            )
        response = self.client.chat.completions.create(
            model=self._model,
            messages=messages,
            stream=False,
        )
        return response.choices[0].message.content or ""


CHAT_API = ChatAPI()
