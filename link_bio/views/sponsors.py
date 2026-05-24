import reflex as rx
from link_bio.components.title import title
from link_bio.styles.styles import Size as Size
from link_bio.styles.colors import Color as Color

def sponsors() -> rx.Component:
    return rx.vstack(
        title("Colaboran"),
        rx.hstack(
            rx.image(
                src="aprobado.png",
                width="auto",
                height="50px",
                opacity="0.7",
                transition="opacity 0.2s ease",
                _hover={"opacity": "1"},
            ),
            rx.image(
                src="nasa.jpg",
                width="auto",
                height="50px",
                opacity="0.7",
                transition="opacity 0.2s ease",
                _hover={"opacity": "1"},
            ),
            gap=Size.BIG.value,
            justify="center",
            align="center",
            width="100%",
        ),
        align="center",
        width="100%",
        padding_top=Size.DEFAULT.value,
    )