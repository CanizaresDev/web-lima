
import reflex as rx

from web.styles.styles import Size, SizeInt

from web import constants as const
from web.components.title import title
from web.components.link_sponsor import link_sponsor


def sponsors() -> rx.Component:
    return rx.vstack(
        title("Colaboran"),
        rx.grid(
            link_sponsor("/cara-alberto.webp", const.ALBERTO_LINKEDIN_URL),
            link_sponsor("/cara-paloma.png", const.PALOMA_LINKEDIN_URL),
            align="center",
            justify="center",
            width="100%",    
            spacing=SizeInt.BIG.value,
            columns=rx.breakpoints(
                initial="1",
                xs="2"
            )
        ),
        width="100%",
        margin_top=Size.BIG.value,
    )