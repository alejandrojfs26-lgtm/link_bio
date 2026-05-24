import reflex as rx
from link_bio.styles.styles import Size as Size

def link_icon(url: str, image: str) -> rx.Component:
    return rx.link(
        rx.image(
            src=image,
            width=Size.LARGE.value,
            height=Size.LARGE.value,
            transition="transform 0.2s ease",
            _hover={"transform": "scale(1.15)"},
        ),
        href=url,
        is_external=True,
        display="flex",
        align_items="center",
        justify_content="center",

    )