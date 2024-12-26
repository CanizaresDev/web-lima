
import reflex as rx

from web.components.navbar import navbar
from web.components.footer import footer
from web.views.header import header
from web.views.courses_links import courses_links
from web.views.sponsors import sponsors

from web.styles import styles
from web.styles.styles import SizeInt
import web.utils as utils
from web.routes import Route


@rx.page(
        route=Route.COURSES.value,
        title=utils.courses_title,
        description=utils.courses_description,
        image=utils.preview,
        meta=utils.courses_meta
)
def courses() -> rx.Component:
    return rx.box(
        utils.lang(),
        navbar(),
        rx.center(
            rx.vstack(
                header(details=False),
                courses_links(),
                sponsors(),
                align="center",
                max_width=styles.MAX_WIDTH,
                width="100%",
                margin_y=styles.Size.BIG.value,
                padding=styles.Size.BIG.value,
                spacing=SizeInt.VERY_BIG.value
            )
        ),
        footer()
    )