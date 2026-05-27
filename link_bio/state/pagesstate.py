import reflex as rx
from link_bio.api.api import TWITCH_API, hello_content, featured
from typing import Any

class PagesState(rx.State):

    is_live: bool
    featured_info: list[dict[str, Any]] = []

    async def check_live(self):
        is_live, _ = TWITCH_API.live("mouredev")
        self.is_live = is_live

    @rx.var
    def say_hello(self) -> str:
        return hello_content()

    async def featured_links(self): 
        featured_info = await featured()
        self.featured_info = featured_info

            