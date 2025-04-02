import reflex as rx
from datetime import datetime

class FormState(rx.State):
    nombre: str = ""
    glicemia: int = 0
    mensaje: str = ""
    mostrar_formulario: bool = False
    error_nombre: str = ""
    historial: list[dict] = []  # Lista de registros

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
        elif self.glicemia > 180:
            self.mensaje = "⚠️ Glicemia alta."
        else:
            self.mensaje = "✅ Glicemia dentro del rango normal"

        ahora = datetime.now()
        self.historial.append({
            "fecha": ahora.strftime("%Y-%m-%d"),
            "hora": ahora.strftime("%H:%M:%S"),
            "glicemia": self.glicemia
        })

        self.glicemia = 0  # Limpiar input

def index():
    return rx.container(
        rx.cond(
            FormState.mostrar_formulario,
            rx.vstack(
                rx.heading(f"🩸 Registro de Glicemia para {FormState.nombre}", size="4"),
                rx.input(
                    placeholder="Nivel de glicemia (mg/dL)",
                    type="number",
                    value=FormState.glicemia,
                    on_change=FormState.set_glicemia
                ),
                rx.hstack(
                    rx.button("Guardar", on_click=FormState.guardar_datos),
                    rx.button("Regresar", color_scheme="gray", on_click=FormState.reset_formulario),
                    spacing="2"
                ),
                rx.text(FormState.mensaje, color="red"),
                rx.heading("📋 Historial de Registros", size="3"),
                rx.foreach(
                    FormState.historial,
                    lambda item: rx.text(
                        f"{item['fecha']} {item['hora']} - Glicemia: {item['glicemia']} mg/dL"
                    )
                ),
                spacing="2"
            ),
            rx.center(
                rx.vstack(
                    rx.heading("Bienvenido a tu App de Diabetes", size="4"),
                    rx.input(
                        placeholder="Nombre completo",
                        on_change=FormState.set_nombre,
                    ),
                    rx.button("Entrar", on_click=FormState.mostrar),
                    rx.text(FormState.error_nombre, color="red"),
                    spacing="3"
                ),
                height="100vh"
            )
        ),
        on_mount=FormState.reset_formulario,
        padding="2em"
    )

app = rx.App()
app.add_page(index)
