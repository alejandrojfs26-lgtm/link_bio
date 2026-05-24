import reflex as rx
from link_bio.styles.styles import Size as Size
from link_bio.styles.colors import TextColor as TextColor
from link_bio.styles.colors import Color as Color
from link_bio.styles.fonts import FontWeight

def info_text(title: str, body: str) -> rx.Component:
    return rx.box(
        rx.text.span(
            f"{title} ",
            font_weight=FontWeight.BOLD.value,
            color=Color.PRIMARY.value,
        ),
        f"{body}",
        font_size=Size.MEDIUM.value,
        color=TextColor.BODY.value,
    )
