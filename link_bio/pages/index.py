import reflex as rx
import link_bio.utils as utils
from link_bio.components.footer import footer
from link_bio.components.navbar import navbar
from link_bio.views.header import header
from link_bio.views.index_links import index_links
from link_bio.views.sponsors import sponsors
import link_bio.styles.styles as styles
from link_bio.styles.styles import Size as Size

#class State(rx.State):
    #pass

@rx.page(
    title=utils.index_title,
    description=utils.index_description,
)

def index() -> rx.Component:
    return rx.box(
        utils.lang(),
        navbar(),
        rx.center(
            rx.vstack(
                header(),
                index_links(),
                sponsors(),
                max_width=styles.MAX_WIDTH,
                width="100%",
                margin_y=Size.BIG.value,
                padding=Size.BIG.value,
            ),
        ),
        footer(),
    )
