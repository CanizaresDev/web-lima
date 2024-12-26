
import reflex as rx

from web.styles.styles import Size


def link_sponsor(image: str, url: str) -> rx.Component:
    return rx.center(
        rx.link(
            rx.image(
                src=image,
                height=Size.VERY_BIG.value,
                width="auto"
            ),
            href=url,
            is_external=True,    
        )
    )