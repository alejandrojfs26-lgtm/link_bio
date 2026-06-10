import reflex as rx
from enum import Enum
from .colors import Color as Color
from .colors import TextColor as TextColor
from .fonts import Font, FontWeight

MAX_WIDTH = "600px"

STYLESHEETS = [
    "https://fonts.googleapis.com/css2?family=Inter:wght@300;500;700&display=swap",
    "https://fonts.googleapis.com/css2?family=Geist:wght@400;500;700&display=swap",
    "https://cdnjs.cloudflare.com/ajax/libs/animate.css/4.1.1/animate.min.css",
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

GLASS_BG = "rgba(13, 13, 20, 0.6)"
GLASS_BORDER = "rgba(255, 255, 255, 0.06)"

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
        "background": GLASS_BG,
        "backdrop_filter": "blur(12px)",
        "-webkit-backdrop-filter": "blur(12px)",
        "white_space": "normal",
        "text_align": "start",
        "border": f"1px solid {GLASS_BORDER}",
        "transition": "all 0.3s ease",
        "_hover": {
            "background": "rgba(0, 153, 255, 0.1)",
            "border_color": Color.PRIMARY.value,
            "transform": "translateY(-2px)",
            "box_shadow": "0 8px 25px rgba(0, 153, 255, 0.12)",
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

glass_style = {
    "background": GLASS_BG,
    "backdrop_filter": "blur(12px)",
    "-webkit-backdrop-filter": "blur(12px)",
    "border": f"1px solid {GLASS_BORDER}",
    "border_radius": "12px",
}