import reflex as rx

config = rx.Config(
    app_name="web",
    cors_allowed_origins=[
        "http://localhost:3000",
        "https://lima-web-orcin.vercel.app"
    ]
)