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
from link_bio.state.chat_state import ChatState
from link_bio.styles.fonts import FontWeight


def chat_message(msg: dict) -> rx.Component:
    is_user = msg["role"] == "user"
    return rx.hstack(
        rx.box(
            rx.text(
                msg["content"],
                color=rx.cond(is_user, TextColor.HEADER.value, TextColor.BODY.value),
                font_size=Size.DEFAULT.value,
            ),
            bg=rx.cond(is_user, Color.PRIMARY.value, Color.CONTENT.value),
            padding=Size.DEFAULT.value,
            border_radius="12px",
            border=f"1px solid {Color.BORDER.value}",
            max_width="85%",
            width="fit-content",
        ),
        width="100%",
        justify=rx.cond(is_user, "end", "start"),
    )


def chat_input() -> rx.Component:
    return rx.hstack(
        rx.input(
            placeholder="Escribe tu mensaje...",
            value=ChatState.input_text,
            on_change=ChatState.set_input_text,
            on_key_down=ChatState.send_message,
            width="100%",
            bg=Color.CONTENT.value,
            border=f"1px solid {Color.BORDER.value}",
            border_radius="12px",
            padding=Size.DEFAULT.value,
            color=TextColor.HEADER.value,
            _placeholder={"color": TextColor.FOOTER.value},
        ),
        rx.button(
            rx.cond(
                ChatState.loading,
                rx.spinner(color=TextColor.HEADER.value),
                rx.icon(tag="send", color=Color.PRIMARY.value),
            ),
            on_click=ChatState.send_message,
            bg=Color.CONTENT.value,
            border=f"1px solid {Color.BORDER.value}",
            border_radius="12px",
            padding=Size.SMALL.value,
            width="3em",
            height="3em",
            display="flex",
            align_items="center",
            justify_content="center",
            cursor="pointer",
        ),
        gap=Size.SMALL.value,
        width="100%",
    )


def chat_view() -> rx.Component:
    return rx.vstack(
        rx.hstack(
            rx.heading("Chat con IA", color=TextColor.HEADER.value, font_size=Size.LARGE.value),
            rx.button(
                rx.hstack(
                    rx.icon(tag="trash_2"),
                    rx.text("Limpiar"),
                    gap=Size.SMALL.value,
                ),
                on_click=ChatState.clear_chat,
                bg=Color.CONTENT.value,
                border=f"1px solid {Color.BORDER.value}",
                border_radius="12px",
                padding_x=Size.DEFAULT.value,
                padding_y=Size.SMALL.value,
                color=TextColor.BODY.value,
                font_size=Size.SMALL.value,
                cursor="pointer",
                width="auto",
                _hover={"border_color": Color.PRIMARY.value},
            ),
            justify="between",
            width="100%",
        ),
        rx.box(
            rx.foreach(
                ChatState.messages,
                chat_message,
            ),
            width="100%",
            height="400px",
            overflow_y="auto",
            padding=Size.SMALL.value,
            bg=Color.BACKGROUND.value,
            border_radius="12px",
            border=f"1px solid {Color.BORDER.value}",
        ),
        chat_input(),
        width="100%",
        gap=Size.MEDIUM.value,
    )


@rx.page(
    route=Route.CHAT.value,
    title=utils.chat_title,
    description=utils.chat_description,
    on_load=[
        PagesState.check_live,
    ]
)
def chat() -> rx.Component:
    return rx.box(
        utils.lang(),
        navbar(),
        rx.center(
            rx.vstack(
                header(details=False, live=PagesState.live),
                chat_view(),
                max_width=styles.MAX_WIDTH,
                width="100%",
                margin_y=Size.BIG.value,
                padding=Size.BIG.value,
            ),
        ),
        footer(),
    )
