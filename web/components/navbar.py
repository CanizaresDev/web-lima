
import reflex as rx

from web.styles.styles import Size, nav_bar_title_style
from web.styles.colors import Color, TextColor
from web.routes import Route


def navbar() -> rx.Component:

    return rx.hstack(
        rx.link(
            rx.box(
                rx.text.span(
                    "Lima",
                    color=Color.PRIMARY.value,
                ),
                rx.text.span(
                    " La Mejor",
                    color=Color.SECONDARY.value,
                ),
                style=nav_bar_title_style,
            ),
            href=Route.INDEX.value,
            is_external=False
        ),
        position="sticky",
        align="center",
        width="100%",
        bg=Color.CONTENT.value,
        padding_x=Size.DEFAULT, 
        padding_y=Size.SMALL,
        z_index="999",
        top="0",
    )
    