import reflex as rx
from link_bio.styles.colors import Color



def float_button(icon_src: str = "icons/twitch.svg", href: str = "https://youtube.com") -> rx.Component:
    return rx.link(
        rx.box(
            rx.image(
                src=icon_src,
                width="1.5em",
                height="1.5em",
            ),
            position="fixed",
            bottom="2em",
            right="2em",
            bg=Color.PRIMARY.value,
            width="3.5em",
            height="3.5em",
            border_radius="50%",
            display="flex",
            align_items="center",
            justify_content="center",
            box_shadow="0 4px 12px rgba(0,0,0,0.3)",
            _hover={
                "bg": Color.SECONDARY.value,
                "transform": "scale(1.1)",
                "transition": "all 0.2s ease",
            },
            z_index="999",
            cursor="pointer",
        ),
        href=href,
        is_external=True,
    )