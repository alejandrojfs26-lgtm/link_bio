import reflex as rx
import link_bio.utils as utils
from link_bio.components.footer import footer
from link_bio.components.navbar import navbar
from link_bio.components.ant_components import float_button
from link_bio.components.animated_background import animated_background
from link_bio.views.header import header
from link_bio.views.index_links import index_links
from link_bio.views.sponsors import sponsors
import link_bio.styles.styles as styles
from link_bio.styles.styles import Size as Size
from link_bio.state.pagesstate import PagesState


@rx.page(
    title=utils.index_title,
    description=utils.index_description,
    on_load=[
        PagesState.check_live,
        PagesState.featured_links,
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

def index() -> rx.Component:
    return rx.box(
        animated_background(),
        float_button(
            icon_src="icons/twitch.svg",
            href="https://youtube.com",
        ),
        rx.box(
            utils.lang(),
            navbar(),
            rx.vstack(
                header(live=PagesState.live, next_live=PagesState.next_live),
                index_links(PagesState.featured_info),
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
