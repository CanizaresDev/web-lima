
import reflex as rx

from web.styles import styles

from . import pages


app = rx.App(
    stylesheets=styles.STYLESHEETS,
    style=styles.BASE_STYLE   
)

