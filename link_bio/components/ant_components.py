import reflex as rx
from link_bio.styles.colors import Color


def float_button(
    icon_src: str = "icons/twitch.svg",
    href: str = "https://youtube.com",
    side: str = "right",
    bg_color: str = Color.PRIMARY.value,
    bg_hover: str = Color.SECONDARY.value,
) -> rx.Component:
    pos_key = "right" if side == "right" else "left"
    return rx.link(
        rx.box(
            rx.image(
                src=icon_src,
                width="1.5em",
                height="1.5em",
            ),
            position="fixed",
            bottom="2em",
            **{pos_key: "2em"},
            bg=bg_color,
            width="3.5em",
            height="3.5em",
            border_radius="50%",
            display="flex",
            align_items="center",
            justify_content="center",
            box_shadow=f"0 0 20px {bg_color}4D",
            _hover={
                "bg": bg_hover,
                "transform": "scale(1.1)",
                "box_shadow": f"0 0 30px {bg_color}80",
                "transition": "all 0.2s ease",
            },
            z_index="999",
            cursor="pointer",
        ),
        href=href,
        is_external=True,
    )