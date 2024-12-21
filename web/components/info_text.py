
import reflex as rx

from web.styles.styles import Size
from web.styles.colors import Color, TextColor

def info_text(title: str, body: str) -> rx.Component:

    return rx.box(
        rx.text.span(
            title, 
            font_weight="bold", 
            color=Color.PRIMARY.value,
        ),
        f" {body}",
        font_size=Size.MEDIUM.value,
        color=TextColor.BODY.value,

    )