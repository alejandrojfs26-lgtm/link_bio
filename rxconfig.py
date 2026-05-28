import reflex as rx

config = rx.Config(
    app_name="link_bio",
    api_url="https://linkbio-backend.up.railway.app",  # Produccion. Para local: http://localhost:8000
    deploy_url="https://link-bio-blush-seven.vercel.app",
    backend_host="0.0.0.0",
    cors_allowed_origins=[
        "http://localhost:3000",
        "https://link-bio-blush-seven.vercel.app",
    ],
    plugins=[
        rx.plugins.SitemapPlugin(),
        rx.plugins.TailwindV4Plugin(),
        rx.plugins.RadixThemesPlugin(),
    ]
)