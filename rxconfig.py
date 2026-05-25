import reflex as rx

config = rx.Config(
    app_name="link_bio",
    api_url="https://linkbio-backend.up.railway.app",
    deploy_url="https://linkbio-frontend.vercel.app",
    backend_host="0.0.0.0",
    cors_allowed_origins=[
        "http://localhost:3000",
        "https://linkbio-frontend.vercel.app",
        "https://linkbio-backend.up.railway.app",
    ],
    plugins=[
        rx.plugins.SitemapPlugin(),
        rx.plugins.TailwindV4Plugin(),
        rx.plugins.RadixThemesPlugin(),
    ]
)