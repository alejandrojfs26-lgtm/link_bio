from link_bio.model.live import Live
import os
import dotenv
import requests
import time

dotenv.load_dotenv()


class TwitchAPI:

    CLIENT_ID = os.environ.get("TWITCH_CLIENT_ID")
    CLIENT_SECRET = os.environ.get("TWITCH_CLIENT_SECRET")

    def __init__(self):
        self.token = None
        self.token_exp = 0

    def generate_token(self):
        if not self.CLIENT_ID or not self.CLIENT_SECRET:
            return
        try:
            response = requests.post(
                "https://id.twitch.tv/oauth2/token",
                data={
                    "client_id": self.CLIENT_ID,
                    "client_secret": self.CLIENT_SECRET,
                    "grant_type": "client_credentials"
                },
                timeout=10,
            )

            if response.status_code == 200:
                data = response.json()
                self.token = data["access_token"]
                self.token_exp = time.time() + data["expires_in"]
            else:
                self.token = None
                self.token_exp = 0
        except requests.RequestException:
            self.token = None
            self.token_exp = 0

    def token_valid(self) -> bool:
        return bool(self.token) and time.time() < self.token_exp

    def live(self, user: str) -> Live:
        if not self.token_valid():
            self.generate_token()

        if not self.token_valid():
            return Live(live=False, title=None, user=user)

        try:
            response = requests.get(
                f"https://api.twitch.tv/helix/streams?user_login={user}",
                headers={
                    "Client-Id": self.CLIENT_ID,
                    "Authorization": f"Bearer {self.token}",
                },
                timeout=10,
            )

            if response.status_code == 200 and response.json().get("data"):
                data = response.json()["data"]
                return Live(
                    live=True,
                    title=data[0]["title"],
                    user=user
                )
        except requests.RequestException:
            pass

        return Live(live=False, title=None, user=user)
