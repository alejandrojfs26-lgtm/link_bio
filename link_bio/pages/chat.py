import reflex as rx
import link_bio.utils as utils
from link_bio.components.footer import footer
from link_bio.components.navbar import navbar
from link_bio.components.ant_components import float_button
from link_bio.components.chat_loader import chat_loader
from link_bio.components.animated_background import animated_background
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
                class_name=rx.cond(~is_user, "typewriter", ""),
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
    return rx.form(
        rx.hstack(
            rx.input(
                placeholder="Escribe tu mensaje...",
                value=ChatState.input_text,
                on_change=ChatState.set_input_text,
                name="mensaje",
                width="100%",
                height="3em",
                bg=Color.CONTENT.value,
                border=f"1px solid {Color.BORDER.value}",
                border_radius="12px",
                padding_x=Size.DEFAULT.value,
                padding_y="0",
                style={"color": "#FFFFFF", "caret_color": "#FFFFFF"},
                _placeholder={"color": "#6B6B80"},
            ),
            rx.button(
                rx.cond(
                    ChatState.loading,
                    rx.spinner(color=TextColor.HEADER.value, size="2"),
                    rx.icon(tag="send", color=TextColor.HEADER.value),
                ),
                type="submit",
                bg=Color.CONTENT.value,
                border=f"1px solid {Color.BORDER.value}",
                border_radius="12px",
                padding="0",
                width="3em",
                height="3em",
                min_width="3em",
                display="flex",
                align_items="center",
                justify_content="center",
                cursor="pointer",
            ),
            gap=Size.SMALL.value,
            width="100%",
        ),
        on_submit=ChatState.send_message,
        width="100%",
    )


def chat_area() -> rx.Component:
    return rx.box(
        rx.foreach(ChatState.messages, chat_message),
        id="chat-msgs",
        width="100%",
        flex="1",
        min_height="0",
        overflow_y="auto",
        padding=Size.DEFAULT.value,
        bg=Color.BACKGROUND.value,
        border_radius="12px",
        border=f"1px solid {Color.BORDER.value}",
    )


def chat_view() -> rx.Component:
    return rx.vstack(
        rx.hstack(
            rx.heading("Chat con IA", color=TextColor.HEADER.value, font_size=Size.LARGE.value),
            rx.hstack(
                rx.cond(
                    ChatState.loading,
                    rx.hstack(
                        chat_loader(),
                        rx.text(
                            "La IA está pensando...",
                            color=TextColor.FOOTER.value,
                            font_size=Size.SMALL.value,
                        ),
                        gap=Size.SMALL.value,
                        align="center",
                    ),
                ),
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
                gap=Size.DEFAULT.value,
                align="center",
            ),
            justify="between",
            width="100%",
        ),
        chat_area(),
        chat_input(),
        width="100%",
        flex="1",
        min_height="0",
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
        animated_background(),
        float_button(
            icon_src="icons/whatsapp.svg",
            href="https://wa.me/34644992100",
            bg_color=Color.WHATSAPP.value,
            bg_hover=Color.WHATSAPP_HOVER.value,
        ),
        rx.box(
            utils.lang(),
            navbar(),
            rx.vstack(
                header(details=False, live=PagesState.live),
                chat_view(),
                footer(),
                height="100dvh",
                width="100%",
                max_width=styles.MAX_WIDTH,
                margin_x="auto",
                padding_x=Size.BIG.value,
                padding_y=Size.DEFAULT.value,
                spacing="0",
            ),
            position="relative",
            z_index="1",
        ),
    )
