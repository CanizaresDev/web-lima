
import reflex as rx
from datetime import date

from web.styles.styles import Size
from web.styles.colors import TextColor


def footer() -> rx.Component:
    return rx.vstack(
        rx.link(
            f"@ Lima la mejor S.A. 2022-{date.today().year}",
            href=".",
            is_external=True,
            font_size=Size.MEDIUM.value,
            margin_top=Size.MEDIUM.value,
            color=TextColor.FOOTER.value,
        ),
        rx.text(
            "Ladrando y jugando desde casa para el mundo",
            font_size=Size.MEDIUM.value,
        ),
        align="center",
        gap=Size.ZERO.value,
        margin_bottom=Size.BIG.value,
        padding_bottom=Size.BIG.value,
        color=TextColor.FOOTER.value,
    )