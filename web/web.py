
import reflex as rx

from web.components.navbar import navbar
from web.components.footer import footer
from web.views.header.header import header
from web.views.links.links import links
from web.views.sponsors.sponsors import sponsors

from web.styles import styles

class State(rx.State):
    pass


def index() -> rx.Component:
    
    return rx.box(
        navbar(),
        rx.center(
            rx.vstack(
                header(),
                links(),
                sponsors(),
                align="center",
                max_width=styles.MAX_WIDTH,
                width="100%",
                margin_y=styles.Size.BIG.value,
                padding=styles.Size.BIG.value
            )
        ),
        footer(),
    )
    


app = rx.App(
    style=styles.BASE_STYLE
)
app.add_page(index)
