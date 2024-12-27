
import web.constants as const
from .twitch_api import TwitchAPI


TWITCH_API = TwitchAPI()


async def repo() -> str:
    return const.ALBERTO_LINKEDIN_URL


async def live(user: str) -> bool:
    return TWITCH_API.live(user)