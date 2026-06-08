import reflex as rx
from link_bio.components.link_button import link_button
from link_bio.components.title import title
from link_bio.components.featured_links import featured_links
from link_bio.styles.styles import Size as Size
from link_bio.routes import Route
from link_bio.model.featured import Featured

def index_links(featured: list[Featured]) -> rx.Component:
    return rx.vstack(
        title("Herramientas"),
        link_button(
            "Chat con IA",
            "Chatea con un modelo de IA directamente desde tu navegador",
            Route.CHAT.value,
            "message_square",
            is_external=False
        ),
        link_button(
            "Traductor",
            "Traduce texto a varios idiomas con audio incluido",
            Route.TRANSLATE.value,
            "languages",
            is_external=False
        ),
        title("Comunidad"),
        link_button(
            "Diseño tecnología usada (Reflex)", 
            "Tecnologías y herramientas del proyecto", 
            Route.TECHS.value, 
            "icons/link.svg",
            is_external=False
        ),
        link_button("LinkedIn", "Perfil profesional", "https://linkedin.com/in/alejandro-fuentes-457595123", "briefcase"),
        link_button("GitHub", "Código abierto y proyectos", "https://github.com/alejandrojfs26-lgtm", "code"),
        rx.cond(
            featured,
            rx.vstack(
                title("Destacados"),
                rx.foreach(
                    featured,
                    lambda item: featured_links(item),
                ),
            ),
        ),
        title("Contacto"),
        link_button(
            "Email",
            "alejandrojfs26@gmail.com",
            "mailto:alejandrojfs26@gmail.com",
            "mail",
        ),
        width="100%",
        gap=Size.MEDIUM.value,
    
    )
    