import reflex as rx


@rx.page(route="/")
def index() -> rx.Component:
    # Welcome Page (Index)
    return rx.box(
        rx.center(
            rx.vstack(
                rx.heading(
                    "Enlaces favoritos",
                    id="cabecera"
                ),
                rx.list.unordered(
                    rx.list.item(
                        rx.link("Buscadores", id="buscadores", href="/buscadores", is_external=False)
                    ),
                    # He tenido que llamar la página: "/redessociales" en vez de: "/redes_sociales" porque si no, no encuentra la página y me da error 404.
                    # Tampoco admite guiones porque Reflex interpreta los guiones como otra cosa.
                    rx.list.item(
                        rx.link("Redes sociales", id="redes", href="/redes_sociales", is_external=False)
                    ),
                    list_style_type="none",


                )
            )
            
        )
        
    )  