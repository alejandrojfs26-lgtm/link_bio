import dotenv
import configcatclient
import os
import json

dotenv.load_dotenv()


class ConfigCatAPI:

    CONFIGCAT_API_KEY = os.environ.get("CONFIGCAT_API_KEY")

    def __init__(self) -> None:
        if self.CONFIGCAT_API_KEY:
            self.configcat = configcatclient.get(self.CONFIGCAT_API_KEY)

    def schedule(self) -> dict:
        if not self.CONFIGCAT_API_KEY:
            return {}
        response = self.configcat.get_value("live_schedule", "{}")
        return json.loads(response)
