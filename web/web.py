
import reflex as rx

from web.styles import styles

from . import pages
from .api.api import repo, live


app = rx.App(
    stylesheets=styles.STYLESHEETS,
    style=styles.BASE_STYLE   
)

app.api.add_api_route("/repo", repo)
app.api.add_api_route("/live/{user}", live)
