import reflex as rx

config = rx.Config(
    app_name="web",
    cors_allowed_origins=[
        "http://localhost:3000",
        "https://web-lima.up.railway.app"

    ]
)