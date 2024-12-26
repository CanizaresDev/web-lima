
import reflex as rx

from web.styles.styles import Size, SizeInt
from web.routes import Route

from web import constants as const
from web.components.title import title
from web.components.link_button import link_button


def courses_links() -> rx.Component:

    return rx.vstack(
        title("Cursos"),
        *[
            link_button(f"Curso {str(i)}", f"Descripción {str(i)}", ".") 
            for i in range(1, 5)
        ],

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