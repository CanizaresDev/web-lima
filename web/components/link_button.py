
import reflex as rx

from web.styles import styles
from web.styles.styles import Size, SizeInt


def link_button(title: str, body: str, url: str, is_external=False) -> rx.Component:

    return rx.link(
        rx.button(
            rx.hstack(
                rx.icon(
                    tag="heart",
                    width=Size.BIG.value,
                    height=Size.BIG.value,
                    margin=Size.MEDIUM.value,
                ),
                rx.vstack(
                    rx.text(title, style=styles.button_title_style),
                    rx.text(body, style=styles.button_body_style),
                    justify="center",
                    align_items="start",
                    width="100%",
                    spacing=SizeInt.SMALL.value,
                    margin=Size.ZERO.value,
                ),
                align="center",
                padding_x=Size.MEDIUM.value
            ),
        ),
        href=url,
        is_external=is_external,
        width="100%"
    )