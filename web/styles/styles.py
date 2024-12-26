
from enum import Enum
import reflex as rx

from web.styles.colors import Color, TextColor
from web.styles.fonts import Font, FontWeight


# Constants
MAX_WIDTH = "600px"

# Sizes
class Size(Enum):
    ZERO = "0px !important"
    SMALL = "0.5em"
    MEDIUM = "0.8em"
    DEFAULT = "1em"
    LARGE = "1.5em"
    BIG = "2em"
    VERY_BIG = "8em"
    MAXIMUM = "15em"

class SizeInt(Enum):
    ZERO = "0"
    SMALL = "1"
    MEDIUM = "3"
    DEFAULT = "4"
    LARGE = "5"
    BIG = "6"
    VERY_BIG = "8"

# Styles

STYLESHEETS = [
    "https://fonts.googleapis.com/css2?family=Poppins:wght@300;500&display=swap",
    "https://fonts.googleapis.com/css2?family=Comfortaa:wght@500&display=swap"
]

BASE_STYLE = {
    "font-family": Font.DEFAULT.value,
    "background_color": Color.BACKGROUND.value,
    rx.heading: {
        "color": TextColor.HEADER.value,
        "font-family": Font.TITLE.value,
    },
    rx.button: {
        "width": "100%",
        "height": "100%",
        "display": "block",
        "padding": Size.SMALL.value,
        "border_radius": Size.DEFAULT.value,
        "color": TextColor.HEADER.value,
        "background_color": Color.CONTENT.value,
        "_hover": {
            "background_color": Color.SECONDARY.value,
            "cursor": "pointer",
        }
    },
    rx.link: {
        "text_decoration": "none",
    },
}

nav_bar_title_style = dict(
    font_family=Font.LOGO.value,
    font_weight=FontWeight.LIGHT.value,
    font_size=Size.LARGE.value,

)

title_style = dict(
    font_family=Font.TITLE.value,
    font_weight=FontWeight.MEDIUM.value,
    width="100%",
    align="center",
    color=TextColor.HEADER.value,
)


button_title_style = dict(
    font_family=Font.DEFAULT.value,
    font_weight=FontWeight.MEDIUM.value,
    font_size=Size.DEFAULT.value,
    color=TextColor.HEADER.value,
)

button_body_style = dict(
    font_weight=FontWeight.LIGHT.value,
    font_size=Size.MEDIUM.value,
    color=TextColor.BODY.value,
)