
import reflex as rx

from web.styles import styles
from web.styles.styles import SizeInt


def title(text: str) -> rx.Component:

    return rx.heading(
        text,
        size=SizeInt.BIG.value,
        style=styles.title_style
    )