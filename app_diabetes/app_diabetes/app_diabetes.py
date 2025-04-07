import reflex as rx
from datetime import datetime



class FormState(rx.State):
    nombre: str = ""
    glicemia: int = 0
    mensaje: str = ""
    color_alerta: str = "green"
    mostrar_formulario: bool = False
    error_nombre: str = ""
    historial: list[dict] = []

    def set_nombre(self, nombre):
        self.nombre = nombre.strip()

    def mostrar(self):
        if self.nombre == "":
            self.error_nombre = "⚠️ No has ingresado nada, por favor ingresa tu nombre"
        else:
            self.mostrar_formulario = True
            self.error_nombre = ""

    def reset_formulario(self):
        self.nombre = ""
        self.glicemia = 0
        self.mensaje = ""
        self.color_alerta = "green"
        self.mostrar_formulario = False
        self.error_nombre = ""

    def set_glicemia(self, glicemia):
        try:
            self.glicemia = int(glicemia)
        except ValueError:
            self.glicemia = 0

    def guardar_datos(self):
        print(f"Usuario: {self.nombre}, Glicemia: {self.glicemia}")

        if self.glicemia < 70:
            self.mensaje = "⚠️ Glicemia baja: ¡Cuidado!"
            self.color_alerta = "red"
        elif self.glicemia > 180:
            self.mensaje = "⚠️ Glicemia alta."
            self.color_alerta = "yellow"
        else:
            self.mensaje = "✅ Glicemia dentro del rango normal"
            self.color_alerta = "green"

        ahora = datetime.now()
        self.historial.append({
            "fecha": ahora.strftime("%Y-%m-%d"),
            "hora": ahora.strftime("%H:%M:%S"),
            "glicemia": self.glicemia
        })

        self.glicemia = 0


def index():
    return rx.container(
        rx.cond(
            FormState.mostrar_formulario,
            rx.vstack(
                rx.hstack(
                    rx.image(
                        
                        src="/images/logo2.png",
                        height="60px",
                        margin_right="1em"
                    ),
                    rx.vstack(
                        rx.heading(
                            f"🩸 Registro de Glicemia para {FormState.nombre}",
                            size="6",
                            color="blue.800",
                        ),
                        rx.text(
                            "Educación y control, en tus manos",
                            color="gray.600",
                            font_style="italic"
                        ),
                        align="start",
                    ),
                    align="center",
                    width="100%",
                    margin_bottom="2em"
                ),
                rx.vstack(
                    rx.input(
                        placeholder="Nivel de glicemia (mg/dL)",
                        type="number",
                        value=FormState.glicemia,
                        on_change=FormState.set_glicemia,
                        width="300px",
                        margin_bottom="1em",
                        bg="white",
                        color="black",
                        _placeholder={"color": "blackAlpha.700"},
                        _hover={"bg": "white"},
                        _focus={"bg": "white"}
                    ),
                    rx.hstack(
                        rx.button(
                            "Guardar",
                            on_click=FormState.guardar_datos,
                            color_scheme="blue",
                            size="3"
                        ),
                        rx.button(
                            "Regresar",
                            color_scheme="gray",
                            on_click=FormState.reset_formulario,
                            size="3"
                        ),
                        spacing="2",
                        margin_bottom="1em"
                    ),
                    rx.cond(
                        FormState.mensaje != "",
                        rx.hstack(
                            rx.box(
                                width="15px",
                                height="15px",
                                border_radius="50%",
                                bg=FormState.color_alerta
                            ),
                            rx.text(
                                FormState.mensaje,
                                color=FormState.color_alerta,
                                font_weight="bold"
                            ),
                            spacing="2",
                            align="center",
                            margin_bottom="1em"
                        )
                    ),
                    width="100%",
                    align="center"
                ),
                rx.vstack(
                    rx.heading(
                        "📋 Historial de Registros",
                        size="5",
                        color="blue.600",
                        margin_bottom="1em"
                    ),
                    rx.foreach(
                        FormState.historial,
                        lambda item: rx.text(
                            f"{item['fecha']} {item['hora']} - Glicemia: {item['glicemia']} mg/dL",
                            margin_bottom="0.5em"
                        )
                    ),
                    width="100%",
                    align="center",
                    padding="1em",
                    border_radius="lg",
                    bg="gray.50"
                ),
                spacing="4",
                width="100%",
                max_width="800px",
                padding="2em",
                border_radius="lg",
                box_shadow="lg",
                bg="gray.50"
            ),
            rx.center(
                rx.vstack(
                    rx.image(
                        
                        src="/images/logo1.png",
                        height="500px",         
                        margin_bottom="1em"
                    ),
                    rx.heading(
                        "Bienvenido a Diabeduca!",
                        size="9",
                        color="blue.800",
                        margin_bottom="0.5em"
                    ),
                    rx.text(
                        "Educación y control, en tus manos",
                        color="gray.600",
                        font_style="italic",
                        margin_bottom="1.5em"
                    ),
                    rx.input(
                        placeholder="Nombre completo",
                        on_change=FormState.set_nombre,
                        width="300px",
                        margin_bottom="1em",
                        bg="gray",
                        color="black",
                        _placeholder={"color": "blackAlpha.900"},
                        _hover={"bg": "white"},
                        _focus={"bg": "white"}
                    ),
                    rx.button(
                        "Entrar",
                        on_click=FormState.mostrar,
                        color_scheme="blue",
                        size="4"
                    ),
                    rx.text(
                        FormState.error_nombre,
                        color="red.600",
                        font_weight="bold"
                    ),
                    spacing="3",
                    align="center",
                    padding="2em",
                    border_radius="lg",
                    box_shadow="lg",
                    bg="gray.100"
                ),
                height="100vh",
                bg="gray.200"
            )
        ),
        on_mount=FormState.reset_formulario,
        padding="2em",
        bg="gray.200"
    )


app = rx.App()
app.add_page(index)
