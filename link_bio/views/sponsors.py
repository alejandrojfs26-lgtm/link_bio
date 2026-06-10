import reflex as rx
from link_bio.components.title import title
from link_bio.components.tech_marquee import tech_marquee
from link_bio.styles.styles import Size as Size
from link_bio.styles.colors import Color as Color, TextColor


def sponsors() -> rx.Component:
    return rx.vstack(
        title("Colaboran"),
        rx.box(
            rx.box(
                tech_marquee(speed="slow"),
                overflow="hidden",
                width="100%",
            ),
            width="100%",
        ),
        rx.text(
            "Tecnologías que uso en este proyecto",
            color=TextColor.FOOTER.value,
            font_size=Size.SMALL.value,
            padding_top=Size.SMALL.value,
        ),
        align="center",
        width="100%",
        padding_top=Size.DEFAULT.value,
        gap=Size.MEDIUM.value,
    )
