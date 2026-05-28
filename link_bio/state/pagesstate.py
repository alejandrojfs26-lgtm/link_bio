import reflex as rx
from link_bio.api.api import TWITCH_API, SUPABASE_API, schedule, hello_content
from link_bio.model.live import Live
from link_bio.model.featured import Featured
import link_bio.utils as utils


class PagesState(rx.State):

    live: Live = Live(live=False, title=None, user="")
    next_live: str = ""
    featured_info: list[Featured] = []

    async def check_live(self):
        self.live = TWITCH_API.live("ohnePixel")
        schedule_dict = await schedule()
        self.next_live = utils.next_date(schedule_dict)

    def say_hello(self) -> str:
        return hello_content()

    async def featured_links(self):
        self.featured_info = SUPABASE_API.featured()