import reflex as rx

import ReflexTdd.ReflexTdd



@rx.page(route="/buscadores")
def buscadores() -> rx.Component:
    return rx.box(
        rx.center(
            rx.vstack(
                rx.heading(
                    "Buscadores",
                    id="cabecera"
                ),
                rx.list.unordered(
                    rx.list.item(
                        rx.link("Google", id="google", href="https://www.google.com/", is_external=ReflexTdd.ReflexTdd.external)
                    ),
                    rx.list.item(
                        rx.link("Bing", id="bing", href="https://www.bing.com/", is_external=ReflexTdd.ReflexTdd.external)
                    ),
                    rx.list.item(
                        rx.link("Baidu", id="baidu", href="https://www.baidu.com/", is_external=ReflexTdd.ReflexTdd.external)
                    ),
                    list_style_type="none",


                ),

                rx.button(
                    rx.link("Volver", id="volver", href="/", is_external=False)
                )
            )
            
        )
    )