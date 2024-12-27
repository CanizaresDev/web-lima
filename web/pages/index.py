
import reflex as rx

from web.state.page_state import PageState
from web.components.navbar import navbar
from web.components.footer import footer
from web.views.header import header
from web.views.index_links import index_links
from web.views.sponsors import sponsors

from web.styles import styles
from web.styles.styles import SizeInt
import web.utils as utils
from web.routes import Route


@rx.page(
        route=Route.INDEX.value,
        title=utils.index_title,
        description=utils.index_description,
        image=utils.preview,
        meta=utils.index_meta,
        on_load=PageState.check_live
)
def index() -> rx.Component:
    return rx.box(
        utils.lang(),
        navbar(),
        rx.center(
            rx.vstack(
                header(
                    live=PageState.is_live
                ),
                index_links(),
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