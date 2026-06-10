import reflex as rx
import link_bio.styles.styles as styles
from link_bio.styles.styles import Size as Size
from link_bio.styles.colors import Color as Color
from link_bio.styles.colors import TextColor as TextColor
from link_bio.styles.fonts import FontWeight


def featured_links(item) -> rx.Component:
    return rx.link(
        rx.button(
            rx.vstack(
                rx.box(
                    rx.image(
                        src=item.image,
                        width="100%",
                        height="auto",
                        border_radius="8px",
                    ),
                    border_radius="8px",
                    overflow="hidden",
                ),
                rx.text(
                    item.title,
                    font_size=Size.DEFAULT.value,
                    font_weight=FontWeight.MEDIUM.value,
                    color=TextColor.HEADER.value,
                    width="100%",
                    text_align="center",
                ),
                padding=Size.SMALL.value,
                gap=Size.SMALL.value,
                width="100%",
            ),
            background=f"linear-gradient(135deg, {Color.CONTENT.value}, rgba(0, 153, 255, 0.05))",
            border=f"1px solid rgba(0, 153, 255, 0.1)",
            _hover={
                "background": f"linear-gradient(135deg, rgba(0, 153, 255, 0.1), {Color.CONTENT.value})",
                "border_color": Color.PRIMARY.value,
                "transform": "translateY(-2px)",
            },
        ),
        href=item.url,
        is_external=True,
        width="100%",
    )
