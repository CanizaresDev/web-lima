
import reflex as rx

from web.styles import styles
from web.styles.colors import Color, TextColor
from web.styles.fonts import Font

from web.components.link_icon import link_icon
from web.components.info_text import info_text

def header(details:bool = True) -> rx.Component:

    return rx.box(
        rx.vstack(
            rx.hstack(
                rx.avatar(
                    src="/lima-rosquilla.png",
                    fallback="LC",
                    size="7",
                    variant="solid", 
                    high_contrast=True,
                ),
                rx.vstack(
                    rx.heading(
                        "Lima la Mejor",
                        style=styles.title_style,
                    ),
                    rx.text(
                        "La mejor perrita del mundo",
                        color=TextColor.HEADER.value,
                    ),
                    rx.hstack(
                        link_icon("."),
                        link_icon("."),
                        link_icon("."),
                    ),
                    align="start",
                    gap=styles.Size.SMALL,
                    padding_top=styles.Size.ZERO.value,
                ),
                align="start",
                gap=styles.Size.BIG.value,
            ),
            rx.cond(
                details,
                rx.vstack(
                    rx.flex(
                        info_text("2", "años de vida perruna"),
                        rx.spacer(),
                        info_text("+10", "ganas de jugar"),
                        rx.spacer(),
                        info_text("+1000", "amor que dar"),
                        width="100%"
                    ),
                    rx.text(
                        """Es la perrhija de Paloma y Alberto. 
                        Es muy activa y le gusta salir de paseo todas las tardes. 
                        No le gustan los gatos y encontrarse con otros perros cuando va con correa.""",
                        font_size=styles.Size.MEDIUM.value,
                    ),
                    align="start",
                    gap=styles.Size.BIG.value,
                )
            ),
            align="center",
            gap=styles.Size.BIG,
            color=TextColor.BODY.value,
        ),
    )