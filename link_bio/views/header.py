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
                    "@mouredev",
                    margin_top=Size.ZERO.value,
                    color=TextColor.BODY.value,
                    font_weight=FontWeight.MEDIUM.value,
                ),
                rx.hstack(
                    link_icon("https://twitch.tv/mouredev", "icons/twitch.svg"),
                    link_icon("https://x.com/mouredev", "icons/twitter.svg"),
                    link_icon("https://github.com/mouredev", "icons/twitch.svg"),
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
            info_text("+13", "años de experiencia"),
            rx.spacer(),
            info_text("+50", "proyectos"),
            rx.spacer(),
            info_text("+10K", "estudiantes"),
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
        ),
        rx.text(
            "Soy ingeniero de software y divulgador. Te enseño programación e inteligencia artificial desde cero. Aquí podrás encontrar todos mis enlaces de interés ¡Bienvenid@!",
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
