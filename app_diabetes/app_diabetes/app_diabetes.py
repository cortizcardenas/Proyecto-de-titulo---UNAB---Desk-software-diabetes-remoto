import reflex as rx

class FormState(rx.State):
    glicemia: int = 0
    alimentacion: str = ""
    ejercicio: str = ""
    mensaje: str = ""
    mostrar_formulario: bool = False

    def set_glicemia(self, glicemia):
        try:
            self.glicemia = int(glicemia)
        except ValueError:
            self.glicemia = 0

    def set_alimentacion(self, alimentacion):
        self.alimentacion = alimentacion

    def set_ejercicio(self, ejercicio):
        self.ejercicio = ejercicio

    def mostrar(self):
        self.mostrar_formulario = True

    def reset_formulario(self):
        self.mostrar_formulario = False

    def guardar_datos(self):
        print("Datos guardados:", self.glicemia, self.alimentacion, self.ejercicio)

        if self.glicemia < 70:
            self.mensaje = "⚠️ Glicemia baja: ¡Cuidado!"
        elif self.glicemia > 180:
            self.mensaje = "⚠️ Glicemia alta."
        else:
            self.mensaje = "✅ Datos registrados correctamente"

def index():
    return rx.container(
        rx.cond(
            FormState.mostrar_formulario,
            rx.vstack(
                rx.heading("🩸 Registro de Glicemia", size="4"),
                rx.input(
                    placeholder="Nivel de glicemia (mg/dL)",
                    type="number",
                    on_change=FormState.set_glicemia,
                ),
                rx.input(
                    placeholder="¿Qué comiste?",
                    on_change=FormState.set_alimentacion,
                ),
                rx.input(
                    placeholder="¿Hiciste ejercicio?",
                    on_change=FormState.set_ejercicio,
                ),
                rx.button("Guardar", on_click=FormState.guardar_datos),
                rx.text(FormState.mensaje, color="red"),
                spacing="2"
            ),
            rx.center(
                rx.vstack(
                    rx.heading("¡Bienvenido a tu App de Diabetes! ", size="4"),
                    rx.text("Presiona el botón para comenzar."),
                    rx.button("Entrar", size="3", on_click=FormState.mostrar),
                    spacing="3"
                ),
                height="100vh"
            )
        ),
        on_mount=FormState.reset_formulario,  # 👈 esta es la forma correcta
        padding="2em"
    )


app = rx.App()
app.add_page(index)
