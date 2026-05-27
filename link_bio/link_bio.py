import reflex as rx
import link_bio.styles.styles as styles
from link_bio.pages.index import index
from link_bio.pages.courses import courses
from link_bio.api.api import hello, live


class State(rx.State):
    pass


app = rx.App(
    stylesheets=styles.STYLESHEETS,
    style=styles.BASE_STYLE,
)

app._api.add_route("/hello", hello)
app._api.add_route("/live/{user}", live)
app._api.add_route("/user/{user}", live)