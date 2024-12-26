
import reflex as rx


# Common
preview = "rosquilla.png"
_meta = [
    {"name": "og.type", "content": "website"},
    {"name": "og.image", "content": preview}
]

def lang() -> rx.Component:
    return rx.script("document.documentElement.lang='es'")


# Index
index_title = "Lima | Una perrita buena"
index_description = "Hola, esta es la web de Lima. Una perrita de 2 años que sólo tiene ganas de jugar y recibir cariños"
index_meta = [
    {"name": "og.title", "content": index_title},
    {"name": "og.description", "content": index_description}
]
index_meta.extend(_meta)

# Courses
courses_title = "Lima | Cursos"
courses_description = "TOdo lo que Lima te puede enseñar"
courses_meta = [
    {"name": "og.title", "content": courses_title},
    {"name": "og.description", "content": courses_description}
]
courses_meta.extend(_meta)
