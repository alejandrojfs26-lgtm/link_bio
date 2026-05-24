import reflex as rx
from link_bio.styles.styles import Size as Size
from link_bio.styles.colors import Color as Color
from link_bio.styles.fonts import Font, FontWeight
from link_bio.routes import Route
from link_bio.components.ant_components import float_button

def navbar() -> rx.Component:
    return rx.hstack(
        rx.link(
        rx.heading(
            rx.text.span("moure", color=Color.PRIMARY.value),
            rx.text.span("dev", color=Color.SECONDARY.value),
            font_weight=FontWeight.BOLD.value,
            font_family=Font.LOGO.value,
            font_size=Size.LARGE.value,
        ),
        href=Route.INDEX.value
        ),
        float_button(
            icon_src="icons/twitch.svg",
            href="https://youtube.com",
        ),
        position="sticky",
        bg=Color.BACKGROUND.value,
        padding_x=Size.BIG.value,
        padding_y=Size.DEFAULT.value,
        z_index="999",
        top="0",
        border_bottom=f"1px solid {Color.BORDER.value}",
    )

