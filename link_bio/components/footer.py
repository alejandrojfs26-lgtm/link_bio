import reflex as rx
import datetime
from link_bio.styles.styles import Size as Size
from link_bio.styles.colors import TextColor as TextColor
from link_bio.styles.colors import Color as Color
from link_bio.styles.fonts import FontWeight

def footer() -> rx.Component:
    return rx.vstack(
        rx.image(
            src="fluor.jpg",
            height=Size.VERYBIG.value,
            width="auto",
            alt="Logotipo",
            opacity="0.6",
        ),
        rx.link(
            f"© 2014-{datetime.date.today().year} MoureDev by Brais Moure",
            href="https://mouredev.com",
            is_external=True,
            font_size=Size.MEDIUM.value,
            color=TextColor.FOOTER.value,
            font_weight=FontWeight.MEDIUM.value,
            _hover={"color": Color.PRIMARY.value},
        ),
        rx.text(
            "Building software with ♥ from Galicia to the world",
            font_size=Size.SMALL.value,
            color=TextColor.FOOTER.value,
        ),
        padding_bottom=Size.BIG.value,
        padding_x=Size.BIG.value,
        align="center",
        width="100%",
    )