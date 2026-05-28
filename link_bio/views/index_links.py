import reflex as rx
from link_bio.components.link_button import link_button
from link_bio.components.title import title
from link_bio.components.featured_links import featured_links
from link_bio.styles.styles import Size as Size
from link_bio.routes import Route
from link_bio.model.featured import Featured

def index_links(featured: list[Featured]) -> rx.Component:
    return rx.vstack(
        title("Comunidad"),
        link_button(
            "Cursos gratis", 
            "Directos de programación", 
            Route.COURSES.value, 
            "icons/twitch.svg",
            is_external=False
        ),
        link_button("YouTube", "Tutoriales y cursos gratis", "https://youtube.com/@mouredev", "circle_play"),
        link_button("YouTube (canal secundario)", "Contenido extra", "https://youtube.com/@mouredevtv", "circle_play"),
        link_button("Discord", "Comunidad de desarrollo", "https://discord.gg/mouredev", "message_circle"),
        link_button("LinkedIn", "Perfil profesional", "https://linkedin.com/in/mouredev", "briefcase"),
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
        title("Recursos"),
        link_button("GitHub", "Código abierto y proyectos", "https://github.com/mouredev", "code"),
        link_button("Blog", "Artículos técnicos", "https://mouredev.com/blog", "globe"),
        title("Contacto"),
        link_button(
            "MyPublicInbox",
            "Respuesta rápida",
            "https://mypublicinbox.com/mouredev",
            "mail",
        ),
        width="100%",
        gap=Size.MEDIUM.value,
    
    )
    