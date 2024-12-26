
import reflex as rx

from web.styles.styles import Size, SizeInt
from web.routes import Route

from web import constants as const
from web.components.title import title
from web.components.link_button import link_button


def index_links() -> rx.Component:

    return rx.vstack(
        title("Aficiones"),
        link_button("Dormir", "Cada momento que puedo", "."),
        link_button("Jugar", "Cuando mis papis quieren", "."),
        link_button("Pasear", "Cuando mis papis pueden", "."),
        link_button("Sofá", "Siempre que estoy en casa", "."),
        link_button("Cursos", "Todo lo quete puedo enseñar", Route.COURSES.value),


        rx.spacer(height=Size.MAXIMUM.value),

        title("Contacto"),
        link_button(
            "MyPublicInbox", 
            "Respuesta rápida y con preferencia", 
            const.MYPUBLICINBOX_URL,
        ),
        link_button(
            "Email", 
            const.EMAIL, 
            f"mailto:{const.EMAIL}"
        ),
        align="center",
        width="100%",
        spacing=SizeInt.MEDIUM.value,
    )