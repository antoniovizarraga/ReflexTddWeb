import reflex as rx


@rx.page(route="/formulario", title="Formulario de registro - Mi web")
def formulario() -> rx.Component:
    return rx.box(
        rx.vstack(
            rx.hstack(
                rx.text("Nombre: "),
                rx.input(id="nombre", max_length=50)
            ),
            rx.hstack(
                rx.text("Apellidos: "),
                rx.input(id="apellidos", max_length=50)
            ),
            rx.hstack(
                rx.text("Sexo: "),
                rx.radio(
                    ["Hombre", "Mujer"],
                    direction="row"
                )
            ),
            rx.hstack(
                rx.text("Correo: "),
                rx.input(id="email")
            ),
            rx.hstack(
                rx.checkbox(default_checked=True, id="check-ofertas"),
                rx.text("Deseo recibir información sobre novedades y ofertas"),
                rx.checkbox(id="check-condiciones"),
                rx.text("Declaro haber leído y aceptar las condiciones generales del programa y la normativa sobre protección de datos")
            ),

            rx.button(
                rx.text("Enviar"),
                id="submit",
            )
        )
    )