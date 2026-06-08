import reflex as rx
import link_bio.utils as utils
from link_bio.components.footer import footer
from link_bio.components.navbar import navbar
from link_bio.views.header import header
import link_bio.styles.styles as styles
from link_bio.styles.styles import Size as Size
from link_bio.styles.colors import Color as Color
from link_bio.styles.colors import TextColor as TextColor
from link_bio.routes import Route
from link_bio.state.pagesstate import PagesState
from link_bio.state.translator_state import TranslatorState


def translation_card(lang_name: str) -> rx.Component:
    return rx.cond(
        TranslatorState.translations[lang_name],
        rx.box(
            rx.hstack(
                rx.vstack(
                    rx.text(lang_name, color=TextColor.HEADER.value, font_weight="bold"),
                    rx.text(
                        TranslatorState.translations[lang_name]["text"],
                        color=TextColor.BODY.value,
                        font_size=Size.DEFAULT.value,
                    ),
                    width="100%",
                    gap=Size.SMALL.value,
                ),
                rx.cond(
                    TranslatorState.translations[lang_name]["audio_b64"],
                    rx.audio(
                        url=f"data:audio/mp3;base64,{TranslatorState.translations[lang_name]['audio_b64']}",
                        width="2.5em",
                        height="2.5em",
                    ),
                ),
                width="100%",
                gap=Size.DEFAULT.value,
                align="center",
            ),
            bg=Color.CONTENT.value,
            border=f"1px solid {Color.BORDER.value}",
            border_radius="12px",
            padding=Size.DEFAULT.value,
            width="100%",
        ),
    )


def translate_view() -> rx.Component:
    return rx.vstack(
        rx.heading("Traductor", color=TextColor.HEADER.value, font_size=Size.LARGE.value),
        rx.text(
            "Traduce texto a varios idiomas con audio incluido",
            color=TextColor.BODY.value,
            font_size=Size.MEDIUM.value,
        ),
        rx.text_area(
            placeholder="Escribe algo en español...",
            value=TranslatorState.source_text,
            on_change=TranslatorState.set_source_text,
            width="100%",
            min_height="120px",
            bg=Color.CONTENT.value,
            border=f"1px solid {Color.BORDER.value}",
            border_radius="12px",
            padding=Size.DEFAULT.value,
            color=TextColor.HEADER.value,
            _placeholder={"color": TextColor.FOOTER.value},
        ),
        rx.button(
            rx.cond(
                TranslatorState.loading,
                rx.spinner(color=TextColor.HEADER.value),
                rx.text("Traducir", color=TextColor.HEADER.value),
            ),
            on_click=TranslatorState.translate,
            bg=Color.PRIMARY.value,
            border_radius="12px",
            padding_x=Size.BIG.value,
            padding_y=Size.SMALL.value,
            cursor="pointer",
            _hover={"bg": Color.SECONDARY.value},
        ),
        rx.cond(
            TranslatorState.translations,
            rx.vstack(
                rx.foreach(
                    TranslatorState.translations,
                    lambda kv: translation_card(kv[0]),
                ),
                width="100%",
                gap=Size.MEDIUM.value,
            ),
        ),
        width="100%",
        gap=Size.MEDIUM.value,
    )


@rx.page(
    route=Route.TRANSLATE.value,
    title=utils.translate_title,
    description=utils.translate_description,
    on_load=[
        PagesState.check_live,
    ]
)
def translate() -> rx.Component:
    return rx.box(
        utils.lang(),
        navbar(),
        rx.center(
            rx.vstack(
                header(details=False, live=PagesState.live),
                translate_view(),
                max_width=styles.MAX_WIDTH,
                width="100%",
                margin_y=Size.BIG.value,
                padding=Size.BIG.value,
            ),
        ),
        footer(),
    )
