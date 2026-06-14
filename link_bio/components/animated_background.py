import reflex as rx


def animated_background() -> rx.Component:
    return rx.fragment(
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
                "radial-gradient(ellipse 80% 60% at 15% 20%, hsla(14,100%,57%,0.5) 0%, transparent 60%),"
                "radial-gradient(ellipse 60% 70% at 85% 15%, hsla(340,82%,52%,0.4) 0%, transparent 55%),"
                "radial-gradient(ellipse 70% 50% at 50% 85%, hsla(45,100%,51%,0.35) 0%, transparent 50%)"
            ),
        ),
        rx.box(
            position="fixed",
            top="0",
            left="0",
            width="100vw",
            height="100vh",
            z_index="0",
            pointer_events="none",
            bg="rgba(5, 5, 8, 0.40)",
        ),
    )
