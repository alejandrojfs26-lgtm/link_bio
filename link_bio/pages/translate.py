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

def translation_card(item: dict) -> rx.Component:
    return rx.box(
        rx.hstack(
            rx.vstack(
                rx.text(item["name"], color=TextColor.HEADER.value, font_weight="bold"),
                rx.text(
                    item["text"],
                    color=TextColor.BODY.value,
                    font_size=Size.DEFAULT.value,
                ),
                width="100%",
                gap=Size.SMALL.value,
            ),
            rx.button(
                rx.icon(tag="play", color=Color.PRIMARY.value),
                on_click=TranslatorState.play_tts(item["text"], item["tts_code"]),
                bg="transparent",
                border=f"1px solid {Color.BORDER.value}",
                border_radius="50%",
                padding="0",
                width="2.5em",
                height="2.5em",
                display="flex",
                align_items="center",
                justify_content="center",
                cursor="pointer",
                _hover={"border_color": Color.PRIMARY.value},
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
    )


def translate_view() -> rx.Component:
    return rx.vstack(
        rx.heading("Traductor", color=TextColor.HEADER.value, font_size=Size.LARGE.value),
        rx.text(
            "Escribe o usa el micrófono para traducir a varios idiomas",
            color=TextColor.BODY.value,
            font_size=Size.MEDIUM.value,
        ),
        rx.hstack(
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
            rx.vstack(
                rx.button(
                    rx.cond(
                        TranslatorState.listening,
                        rx.spinner(color=Color.PRIMARY.value),
                        rx.icon(tag="mic", color=Color.PRIMARY.value),
                    ),
                    on_click=TranslatorState.listen_speech,
                    bg=Color.CONTENT.value,
                    border=f"1px solid {Color.BORDER.value}",
                    border_radius="12px",
                    padding="0",
                    width="3em",
                    height="3em",
                    display="flex",
                    align_items="center",
                    justify_content="center",
                    cursor="pointer",
                    _hover={"border_color": Color.PRIMARY.value},
                ),
                align_items="center",
            ),
            gap=Size.SMALL.value,
            width="100%",
            align="start",
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
            TranslatorState.translations.length() > 0,
            rx.vstack(
                rx.foreach(
                    TranslatorState.translations,
                    translation_card,
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
