import reflex as rx
from link_bio.styles.colors import Color, TextColor


TECH_STACK = [
    ("Reflex", "#6C5CE7"),
    ("Python", "#3776AB"),
    ("Supabase", "#3ECF8E"),
    ("Groq", "#F97316"),
    ("Twitch", "#9146FF"),
    ("ConfigCat", "#1C7ED6"),
    ("Vercel", "#FFFFFF"),
    ("Railway", "#E0E0E0"),
    ("Docker", "#2496ED"),
]


def _tech_badge(name: str, color: str) -> rx.Component:
    return rx.box(
        rx.text(
            name,
            font_size="0.85rem",
            font_weight="500",
            color=color,
            white_space="nowrap",
        ),
        display="inline-flex",
        align_items="center",
        padding_x="1rem",
        padding_y="0.4rem",
        border_radius="9999px",
        border=f"1px solid {color}33",
        bg=f"{color}0a",
    )


def _tech_row() -> rx.Component:
    return rx.hstack(
        *[_tech_badge(n, c) for n, c in TECH_STACK],
        gap="0.75rem",
        flex_shrink="0",
        justify_content="space-around",
    )


def tech_marquee(speed: str = "normal") -> rx.Component:
    duration = {"slow": "120s", "normal": "40s", "fast": "10s"}.get(speed, "40s")
    return rx.box(
        _tech_row(),
        _tech_row(),
        display="flex",
        flex_direction="row",
        gap="0.75rem",
        flex_shrink="0",
        animation=f"marquee {duration} linear infinite",
        _hover={"animation-play-state": "paused"},
        width="max-content",
    )
