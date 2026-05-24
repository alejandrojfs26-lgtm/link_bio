import reflex as rx
import link_bio.styles.styles as styles
from link_bio.styles.styles import Size as Size
from link_bio.styles.colors import Color as Color

def link_button(title: str, body: str, url: str, icon: str, is_external=True) -> rx.Component:
    icon_component = rx.image(
        src=icon,
        width="2em",
        height="2em",
    ) if icon.endswith(".svg") or icon.endswith(".png") or icon.endswith(".jpg") else rx.icon(
        tag=icon,
        font_size=Size.LARGE.value,
        color=Color.PRIMARY.value,
    )
    return rx.link(
        rx.button(
            rx.hstack(
                rx.box(
                    icon_component,
                    display="flex",
                    align_items="center",
                    justify_content="center",
                    min_width="2em",
                    margin="1em"
                ),
                rx.vstack(
                    rx.text(title, style=styles.button_title_style),
                    rx.text(body, style=styles.button_body_style),
                    gap="0",
                    align_items="start",
                    padding_y=Size.SMALL.value,
                    padding_right=Size.SMALL.value,
                ),
                width="100%",
                spacing="4",
                align="center",
            )
        ),
        href=url,
        is_external=is_external,
        width="100%",
    )
