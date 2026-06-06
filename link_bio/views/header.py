from link_bio.components.link_button import link_button
import reflex as rx
from link_bio.components.link_icon import link_icon
from link_bio.components.info_text import info_text
from link_bio.components.title import title
from link_bio.styles.styles import Size as Size
from link_bio.styles.colors import TextColor as TextColor
from link_bio.styles.colors import Color as Color
from link_bio.styles.fonts import FontWeight
from link_bio.model.live import Live
from link_bio.state.pagesstate import PagesState


def header(details=True, live=Live(live=False, title=None, user=""), next_live: str = "") -> rx.Component:
    return rx.vstack(
        rx.hstack(
            rx.box(
    rx.avatar(
        name="Alejandro Fuentes",
        size="9",
        src="macbook.jpg",
    ),
    rx.cond(
        live.live,
        rx.box(
        width="14px",
        height="14px",
        bg=Color.PURPLE.value,
        border_radius="50%",
        border=Color.PURPLE.value,
        position="absolute",
        bottom="4px",
        right="4px",
        class_name="blink"
    )),
    position="relative",
    display="inline-block",
),
            rx.vstack(
                title("Alejandro Fuentes"),
                rx.text(
                    "@alejandrojfs26-lgtm",
                    margin_top=Size.ZERO.value,
                    color=TextColor.BODY.value,
                    font_weight=FontWeight.MEDIUM.value,
                ),
                rx.hstack(
                    link_icon("https://github.com/alejandrojfs26-lgtm", "icons/github.svg"),
                    link_icon("https://linkedin.com/in/alejandro-fuentes-457595123", "icons/linkedin.svg"),
                    spacing="4",
                    align="center",
                ),
                align_items="start",
            ),
            gap=Size.BIG.value,
        ),
        rx.cond(
            details,
        rx.vstack(
        rx.flex(
            info_text("+3", "proyectos publicados"),
            rx.spacer(),
            info_text("Python", "lenguaje principal"),
            rx.spacer(),
            info_text("Full-stack", "en desarrollo"),
            width="100%",
        ),
        rx.cond(
            live.live,
            link_button(
                "En directo en Twitch", 
                live.title,
                f"https://twitch.tv/{live.user}", 
                "icons/twitch.svg", 
                False,
            ),
            link_button(
                "Próximo directo", 
                next_live,
                "#", 
                "icons/twitch.svg", 
                False,
            ), 
            on_mount=[PagesState.check_live,
                      PagesState.featured_links]    
        ),
        rx.text(
            "Desarrollador full-stack apasionado por Python, IA y crear herramientas útiles. Aquí encontrarás mis proyectos y enlaces de interés.",
            font_weight=FontWeight.LIGHT.value,
            font_size=Size.MEDIUM.value,
            color=TextColor.BODY.value,
            line_height="1.6",
        ),
            width="100%",
            gap=Size.BIG.value,
        )
        
        ),
        gap=Size.BIG.value,
        align_items="start",
        width="100%",
    )
