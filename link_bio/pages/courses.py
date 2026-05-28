import reflex as rx
import link_bio.utils as utils
from link_bio.components.footer import footer
from link_bio.components.navbar import navbar
from link_bio.views.header import header
from link_bio.views.courses_links import courses_links
from link_bio.views.sponsors import sponsors
import link_bio.styles.styles as styles
from link_bio.styles.styles import Size as Size
from link_bio.routes import Route
from link_bio.state.pagesstate import PagesState

#class State(rx.State):
    #pass

@rx.page(
    route=Route.COURSES.value,
    title=utils.courses_title,
    description=utils.courses_description,
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
        utils.lang(),
        navbar(),
        rx.center(
            rx.vstack(
                header(details=False, live=PagesState.live),
                courses_links(),
                sponsors(),
                max_width=styles.MAX_WIDTH,
                width="100%",
                margin_y=Size.BIG.value,
                padding=Size.BIG.value,
            ),
        ),
        footer(),
    )
