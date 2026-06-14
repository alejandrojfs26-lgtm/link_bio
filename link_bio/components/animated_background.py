import reflex as rx
from link_bio.styles.colors import Color


def animated_background() -> rx.Component:
    return rx.fragment(
        rx.html(
            "<style>"
            "@keyframes gradientMove {"
            "0%{transform:translate(0,0) scale(1)}"
            "25%{transform:translate(1.5%,-0.8%) scale(1.03)}"
            "50%{transform:translate(-1%,1.2%) scale(0.97)}"
            "75%{transform:translate(-0.8%,-1%) scale(1.02)}"
            "100%{transform:translate(0,0) scale(1)}"
            "}"
            "</style>"
        ),
        rx.box(
            position="fixed",
            top="0",
            left="0",
            width="100vw",
            height="100vh",
            z_index="0",
            pointer_events="none",
            bg="#000",
        ),
        rx.box(
            position="fixed",
            top="0",
            left="0",
            width="100vw",
            height="100vh",
            z_index="0",
            pointer_events="none",
            background=(
                f"radial-gradient(ellipse 85% 65% at 15% 20%, {Color.GRADIENT_VIOLET.value}66 0%, transparent 60%),"
                f"radial-gradient(ellipse 65% 75% at 85% 15%, {Color.GRADIENT_MAGENTA.value}59 0%, transparent 55%),"
                f"radial-gradient(ellipse 75% 55% at 50% 85%, {Color.GRADIENT_CORAL.value}4D 0%, transparent 50%)"
            ),
            animation="gradientMove 30s ease-in-out infinite alternate",
        ),
        rx.box(
            position="fixed",
            top="0",
            left="0",
            width="100vw",
            height="100vh",
            z_index="0",
            pointer_events="none",
            bg="rgba(5, 5, 8, 0.35)",
        ),
    )
