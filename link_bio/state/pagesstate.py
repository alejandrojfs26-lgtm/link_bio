import reflex as rx
from link_bio.api.api import TWITCH_API, SUPABASE_API, CONFIGCAT_API, schedule, hello_content
from link_bio.model.live import Live
from link_bio.model.featured import Featured
import link_bio.utils as utils


class PagesState(rx.State):

    live: Live = Live(live=False, title=None, user="")
    next_live: str = ""
    featured_info: list[Featured] = []
    client_tz: str = "Europe/Madrid"
    client_locale: str = "es-ES"

    async def check_live(self):
        try:
            self.live = TWITCH_API.live("ohnePixel")
        except Exception:
            self.live = Live(live=False, title=None, user="ohnePixel")

        try:
            schedule_dict = await schedule()
            self.next_live = utils.next_date(schedule_dict, self.client_tz, self.client_locale)
        except Exception:
            self.next_live = ""

    def set_timezone(self, tz: str):
        self.client_tz = tz
        self._recalc_schedule()

    def set_locale(self, locale: str):
        self.client_locale = locale
        self._recalc_schedule()

    def _recalc_schedule(self):
        try:
            schedule_dict = CONFIGCAT_API.schedule()
            self.next_live = utils.next_date(schedule_dict, self.client_tz, self.client_locale)
        except Exception:
            pass

    def say_hello(self) -> str:
        return hello_content()

    async def featured_links(self):
        try:
            self.featured_info = SUPABASE_API.featured()
        except Exception:
            self.featured_info = []
