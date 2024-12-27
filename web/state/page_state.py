
import reflex as rx

from web.api.api import live

USER = "knekro"

class PageState(rx.State):   
    is_live: bool = False

    async def check_live(self):
        self.is_live = await live(USER)

