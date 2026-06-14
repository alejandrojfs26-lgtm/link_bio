import reflex as rx
import link_bio.utils as utils
from link_bio.components.footer import footer
from link_bio.components.navbar import navbar
from link_bio.components.ant_components import float_button
from link_bio.components.animated_background import animated_background
from link_bio.views.header import header
from link_bio.views.courses_links import courses_links
from link_bio.views.sponsors import sponsors
import link_bio.styles.styles as styles
from link_bio.styles.styles import Size as Size
from link_bio.styles.colors import Color as Color
from link_bio.routes import Route
from link_bio.state.pagesstate import PagesState

#class State(rx.State):
    #pass

@rx.page(
    route=Route.TECHS.value,
    title=utils.techs_title,
    description=utils.techs_description,
    on_load=[
        PagesState.check_live,
        rx.call_script(
            "Intl.DateTimeFormat().resolvedOptions().timeZone",
            PagesState.set_timezone,
        ),
        rx.call_script(
            "(navigator.language || navigator.languages[0])",
            PagesState.set_locale,
        ),
    ]
)

def courses() -> rx.Component:
    return rx.box(
        animated_background(),
        float_button(
            icon_src="icons/twitch.svg",
            href="https://youtube.com",
        ),
        float_button(
            icon_src="icons/whatsapp.svg",
            href="https://wa.me/34644992100",
            side="left",
            bg_color=Color.WHATSAPP.value,
            bg_hover=Color.WHATSAPP_HOVER.value,
        ),
        rx.box(
            utils.lang(),
            navbar(),
            rx.vstack(
                header(details=False, live=PagesState.live),
                courses_links(),
                sponsors(),
                footer(),
                height="100dvh",
                width="100%",
                max_width=styles.MAX_WIDTH,
                margin_x="auto",
                padding_x=Size.BIG.value,
                padding_y=Size.DEFAULT.value,
                spacing="0",
                overflow_x="hidden",
            ),
            position="relative",
            z_index="1",
        ),
    )
