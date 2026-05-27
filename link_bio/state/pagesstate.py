import reflex as rx
from link_bio.api.api import TWITCH_API, hello_content
from link_bio.api.SupabaseAPI import SupabaseAPI
from link_bio.model.live import Live

SUPABASE_API = SupabaseAPI()

class PagesState(rx.State):

    live: Live
    featured_info: list[dict]

    async def check_live(self):
        self.live = TWITCH_API.live("mouredev")

    def say_hello(self) -> str:
        return hello_content()

    async def featured_links(self):
        self.featured_info = SUPABASE_API.featured()

            