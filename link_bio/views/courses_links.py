import reflex as rx
from link_bio.components.link_button import link_button
from link_bio.components.title import title
from link_bio.styles.styles import Size as Size
from link_bio.routes import Route


def courses_links() -> rx.Component:
    return rx.vstack(
        title("Tecnologías usadas en este proyecto"),
        link_button("Reflex", "Framework web Python", "https://reflex.dev", "icons/link.svg"),
        link_button("Python", "Lenguaje de programación", "https://python.org", "icons/link.svg"),
        link_button("Supabase", "Base de datos y backend", "https://supabase.com", "icons/link.svg"),
        link_button("Twitch API", "Detección de streams en vivo", "https://dev.twitch.tv", "icons/link.svg"),
        link_button("ConfigCat", "Feature flags y configuración", "https://configcat.com", "icons/link.svg"),
        link_button("Vercel", "Deploy del frontend", "https://vercel.com", "icons/link.svg"),
        link_button("Railway", "Deploy del backend", "https://railway.app", "icons/link.svg"),
        link_button("Docker", "Contenedores y despliegue", "https://docker.com", "icons/link.svg"),
        width="100%",
        gap=Size.MEDIUM.value,
    )
