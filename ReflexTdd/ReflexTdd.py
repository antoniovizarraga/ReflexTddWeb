"""Welcome to Reflex! This file outlines the steps to create a basic app."""

import reflex as rx

from rxconfig import config

external = True


class State(rx.State):
    """The app state."""

    ...


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
                        rx.link("Redes sociales", id="redes", href="/redessociales", is_external=False)
                    ),
                    list_style_type="none",


                )
            )
            
        )
        
    )  

def buscadores():
    return rx.box(
        rx.center(
            rx.vstack(
                rx.heading(
                    "Buscadores",
                    id="cabecera"
                ),
                rx.list.unordered(
                    rx.list.item(
                        rx.link("Google", id="google", href="https://www.google.com/", is_external=external)
                    ),
                    rx.list.item(
                        rx.link("Bing", id="bing", href="https://www.bing.com/", is_external=external)
                    ),
                    rx.list.item(
                        rx.link("Baidu", id="baidu", href="https://www.baidu.com/", is_external=external)
                    ),
                    list_style_type="none",


                ),

                rx.button(
                    rx.link("Volver", id="volver", href="/", is_external=False)
                )
            )
            
        )
    )

def redessociales():
    return rx.box(
        rx.center(
            rx.vstack(
                rx.heading(
                    "Redes sociales",
                    id="cabecera"
                ),
                rx.list.unordered(
                    rx.list.item(
                        rx.link("Instagram", id="instagram", href="https://www.instagram.com/", is_external=external)
                    ),
                    rx.list.item(
                        rx.link("TikTok", id="tiktok", href="https://www.tiktok.com/", is_external=external)
                    ),
                    rx.list.item(
                        rx.link("Facebook", id="facebook", href="https://www.facebook.com/", is_external=external)
                    ),
                    list_style_type="none",


                ),

                rx.button(
                    rx.link("Volver", id="volver", href="/", is_external=False)
                )
            )
            
        )
    )


app = rx.App()
app.add_page(index)
app.add_page(buscadores)
app.add_page(redessociales)
