
import reflex as rx

import ReflexTdd.ReflexTdd


@rx.page(route="/redes_sociales")
def redes_sociales() -> rx.Component:
    return rx.box(
        rx.center(
            rx.vstack(
                rx.heading(
                    "Redes sociales",
                    id="cabecera"
                ),
                rx.list.unordered(
                    rx.list.item(
                        rx.link("Instagram", id="instagram", href="https://www.instagram.com/", is_external=ReflexTdd.ReflexTdd.external)
                    ),
                    rx.list.item(
                        rx.link("TikTok", id="tiktok", href="https://www.tiktok.com/", is_external=ReflexTdd.ReflexTdd.external)
                    ),
                    rx.list.item(
                        rx.link("Facebook", id="facebook", href="https://www.facebook.com/", is_external=ReflexTdd.ReflexTdd.external)
                    ),
                    list_style_type="none",


                ),

                rx.button(
                    rx.link("Volver", id="volver", href="/", is_external=False)
                )
            )
            
        )
    )