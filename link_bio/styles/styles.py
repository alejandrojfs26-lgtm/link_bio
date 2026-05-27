import reflex as rx
from enum import Enum
from .colors import Color as Color
from .colors import TextColor as TextColor
from .fonts import Font, FontWeight

MAX_WIDTH = "600px"

STYLESHEETS = [
    "https://fonts.googleapis.com/css2?family=Inter:wght@300;500;700&display=swap",
    "../assets/css/styles.css"
]

class Size(Enum):
    ZERO = "0em"
    SMALL = "0.5em"
    MEDIUM = "0.8em"
    DEFAULT = "1em"
    LARGE = "1.5em"
    BIG = "2em"
    VERYBIG = "3em"

BASE_STYLE = {
    "font_family": Font.DEFAULT.value,
    "font_weight": FontWeight.LIGHT.value,
    "background_color": Color.BACKGROUND.value,
    rx.heading: {
        "color": TextColor.HEADER.value,
        "font_family": Font.TITLE.value,
        "font_weight": FontWeight.BOLD.value,
    },
    rx.button: {
        "width": "100%",
        "height": "100%",
        "display": "block",
        "padding": Size.SMALL.value,
        "border_radius": "12px",
        "color": TextColor.HEADER.value,
        "background_color": Color.CONTENT.value,
        "white_space": "normal",
        "text_align": "start",
        "border": f"1px solid {Color.BORDER.value}",
        "transition": "all 0.3s ease",
        "_hover": {
            "background_color": Color.SECONDARY.value,
            "border_color": Color.PRIMARY.value,
            "transform": "translateY(-2px)",
            "box_shadow": "0 8px 25px rgba(124, 91, 254, 0.15)",
        },
    },
    rx.link: {
        "text_decoration": "none",
        "_hover": {},
    },
}

title_style = dict(
    font_family=Font.TITLE.value,
    font_weight=FontWeight.BOLD.value,
    width="100%",
    padding_top=Size.DEFAULT.value,
    padding_bottom=Size.SMALL.value,
    color=TextColor.HEADER.value,
    font_size=Size.LARGE.value,
)

navbar_title_style = dict(
    font_family=Font.LOGO.value,
    font_weight=FontWeight.BOLD.value,
    font_size=Size.LARGE.value,
    color=TextColor.HEADER.value,
)

button_title_style = dict(
    font_family=Font.TITLE.value,
    font_weight=FontWeight.MEDIUM.value,
    font_size=Size.DEFAULT.value,
    color=TextColor.HEADER.value,
)

button_body_style = dict(
    font_size=Size.MEDIUM.value,
    font_weight=FontWeight.LIGHT.value,
    color=TextColor.BODY.value,
)