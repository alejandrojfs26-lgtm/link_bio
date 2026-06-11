import reflex as rx
from link_bio.styles.styles import Size
from link_bio.styles.colors import Color, TextColor
from link_bio.styles.fonts import Font, FontWeight
from link_bio.routes import Route
from link_bio.state.pagesstate import PagesState


LINKS = [
    ("Inicio", Route.INDEX.value),
    ("Chat", Route.CHAT.value),
    ("Traductor", Route.TRANSLATE.value),
    ("Tecnologías", Route.TECHS.value),
]


def _nav_links() -> list[rx.Component]:
    return [
        rx.link(
            label,
            id=f"nav-item-{label.lower()}",
            href=href,
            padding_x="1em",
            padding_y="0.35em",
            z_index="1",
            position="relative",
            color=TextColor.HEADER.value,
            font_size=Size.MEDIUM.value,
            font_family=Font.DEFAULT.value,
            font_weight=FontWeight.MEDIUM.value,
            _hover={"color": TextColor.HEADER.value, "text_decoration": "none"},
            on_mouse_enter=rx.call_script(f"moveNavCursor('nav-item-{label.lower()}')"),
            on_click=[
                PagesState.close_mobile,
                rx.call_script("document.body.style.overflow = ''"),
            ],
        )
        for label, href in LINKS
    ]


def navbar() -> rx.Component:
    return rx.fragment(
        rx.script("""
window.moveNavCursor = function(id) {
    var e = document.getElementById(id);
    var c = document.getElementById('nav-cursor');
    if (!e || !c) return;
    c.style.left = e.offsetLeft + 'px';
    c.style.width = e.offsetWidth + 'px';
    c.style.opacity = '1';
};
window.hideNavCursor = function() {
    var c = document.getElementById('nav-cursor');
    if (c) c.style.opacity = '0';
};
window.addEventListener('load', function() {
    var ticking = false;
    var handler = function() {
        var scrolled = window.scrollY > 10;
        reflex.call('pages_state.set_scrolled', scrolled);
    };
    window.addEventListener('scroll', function() {
        if (!ticking) {
            window.requestAnimationFrame(function() {
                handler();
                ticking = false;
            });
            ticking = true;
        }
    });
    handler();
});
"""),
        rx.box(
            rx.desktop_only(
                rx.hstack(
                    rx.link(
                        rx.heading(
                            "AF",
                            color=TextColor.HEADER.value,
                            font_family=Font.LOGO.value,
                            font_weight=FontWeight.BOLD.value,
                            font_size=Size.LARGE.value,
                        ),
                        href=Route.INDEX.value,
                        _hover={"opacity": "0.8", "text_decoration": "none"},
                    ),
                    rx.spacer(),
                    rx.box(
                        rx.hstack(
                            rx.box(
                                id="nav-cursor",
                                position="absolute",
                                height="100%",
                                border_radius="9999px",
                                bg=Color.PRIMARY.value,
                                opacity="0",
                                transition="all 0.2s cubic-bezier(0.34, 1.56, 0.64, 1)",
                                z_index="0",
                            ),
                            *_nav_links(),
                            position="relative",
                            align="center",
                            spacing="0",
                        ),
                        position="relative",
                        border_radius="9999px",
                        border="1px solid rgba(255,255,255,0.08)",
                        padding="3px",
                        on_mouse_leave=rx.call_script("hideNavCursor()"),
                        display="inline-flex",
                        background="rgba(255,255,255,0.03)",
                    ),
                    width="100%",
                    max_width=rx.cond(PagesState.scrolled, "900px", "1120px"),
                    margin="0 auto",
                    padding_x="1rem",
                    align="center",
                ),
                height="56px",
            ),
            rx.mobile_and_tablet(
                rx.box(
                    rx.hstack(
                        rx.link(
                            rx.heading(
                                "AF",
                                color=TextColor.HEADER.value,
                                font_family=Font.LOGO.value,
                                font_weight=FontWeight.BOLD.value,
                                font_size="1.15rem",
                            ),
                            href=Route.INDEX.value,
                            _hover={"opacity": "0.8", "text_decoration": "none"},
                        ),
                        rx.spacer(),
                        rx.button(
                            rx.cond(
                                PagesState.mobile_open,
                                rx.html(
                                    '<svg width="20" height="20" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round">'
                                    '<line x1="18" y1="6" x2="6" y2="18"/>'
                                    '<line x1="6" y1="6" x2="18" y2="18"/>'
                                    '</svg>'
                                ),
                                rx.html(
                                    '<svg width="20" height="20" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round">'
                                    '<line x1="3" y1="6" x2="21" y2="6"/>'
                                    '<line x1="3" y1="12" x2="21" y2="12"/>'
                                    '<line x1="3" y1="18" x2="21" y2="18"/>'
                                    '</svg>'
                                ),
                            ),
                            on_click=[
                                PagesState.toggle_mobile,
                                rx.call_script(
                                    "document.body.style.overflow = document.body.style.overflow === 'hidden' ? '' : 'hidden'"
                                ),
                            ],
                            variant="outline",
                            border="1px solid rgba(255,255,255,0.15)",
                            bg="transparent",
                            color=TextColor.HEADER.value,
                            width="2.5rem",
                            height="2.5rem",
                            padding="0",
                            display="flex",
                            align_items="center",
                            justify_content="center",
                            border_radius="8px",
                            cursor="pointer",
                            _hover={"bg": "rgba(255,255,255,0.06)"},
                        ),
                        width="100%",
                        padding_x="1rem",
                        align="center",
                    ),
                    height="56px",
                ),
                rx.cond(
                    PagesState.mobile_open,
                    rx.box(
                        rx.vstack(
                            *_nav_links(),
                            padding="1rem",
                            height="100%",
                            gap="0",
                        ),
                        position="fixed",
                        top="56px",
                        left="0",
                        right="0",
                        bottom="0",
                        bg="rgba(5,5,8,0.98)",
                        z_index="999",
                        backdrop_filter="blur(20px)",
                        style={
                            "-webkit-backdrop-filter": "blur(20px)",
                            "animation": "fadeInUp 0.15s ease-out",
                        },
                    ),
                ),
            ),
            position="sticky",
            top=rx.cond(PagesState.scrolled, "0.75rem", "0"),
            z_index="50",
            mx="auto",
            width="100%",
            max_width=rx.cond(PagesState.scrolled, "960px", "100%"),
            border_radius=rx.cond(PagesState.scrolled, "12px", "0"),
            border=rx.cond(PagesState.scrolled, "1px solid rgba(255,255,255,0.06)", "1px solid transparent"),
            box_shadow=rx.cond(PagesState.scrolled, "0 4px 24px rgba(0,0,0,0.3)", "none"),
            bg=rx.cond(
                PagesState.mobile_open,
                "rgba(5,5,8,0.95)",
                rx.cond(PagesState.scrolled, "rgba(5,5,8,0.9)", "rgba(5,5,8,0.85)"),
            ),
            backdrop_filter=rx.cond(
                PagesState.mobile_open,
                "blur(20px)",
                rx.cond(PagesState.scrolled, "blur(16px)", "blur(12px)"),
            ),
            transition="all 0.2s ease-out",
            padding_y="0",
        ),
    )
