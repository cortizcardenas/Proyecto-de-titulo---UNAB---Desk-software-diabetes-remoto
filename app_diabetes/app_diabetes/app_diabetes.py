import reflex as rx
from datetime import datetime
from .pages.educacion import educacion
from .pages.graficos import graficos
from .database.db_manager import DatabaseManager
from .state.navigation_state import NavigationState

# Crear una instancia global del DatabaseManager
db_manager = DatabaseManager()
db_manager.create_tables()

class FormState(rx.State):
    nombre: str = ""
    correo: str = ""
    glicemia: int = 0
    mensaje: str = ""
    color_alerta: str = "green"
    mostrar_formulario: bool = False
    error_nombre: str = ""
    error_correo: str = ""
    historial: list[dict] = []
    modulo_seleccionado: str = ""
    es_registro: bool = True  # True para registro, False para inicio de sesión
    usuario_id: int = 0  # ID del usuario actual

    def set_nombre(self, nombre):
        self.nombre = nombre.strip()

    def set_correo(self, correo):
        self.correo = correo.strip()

    def set_modulo(self, modulo):
        self.modulo_seleccionado = modulo
        return NavigationState.set_modulo(modulo)

    def toggle_modo(self):
        """Alterna entre modo registro e inicio de sesión."""
        self.es_registro = not self.es_registro
        self.error_nombre = ""
        self.error_correo = ""

    def cargar_historial(self):
        """Carga el historial de registros desde la base de datos."""
        if self.usuario_id > 0:
            registros = db_manager.obtener_registros_glicemia(self.usuario_id)
            self.historial = [
                {
                    "fecha": datetime.strptime(registro[3], "%Y-%m-%d %H:%M:%S").strftime("%Y-%m-%d"),
                    "hora": datetime.strptime(registro[3], "%Y-%m-%d %H:%M:%S").strftime("%H:%M:%S"),
                    "glicemia": registro[2]
                }
                for registro in registros
            ]

    def mostrar(self):
        if self.correo == "":
            self.error_correo = "⚠️ Por favor ingresa tu correo electrónico"
            return
        if not "@" in self.correo or not "." in self.correo:
            self.error_correo = "⚠️ Por favor ingresa un correo electrónico válido"
            return

        if self.es_registro:
            # Modo registro
            if self.nombre == "":
                self.error_nombre = "⚠️ No has ingresado nada, por favor ingresa tu nombre"
                return

            # Intentar registrar el usuario
            if db_manager.registrar_usuario(self.nombre, self.correo):
                usuario = db_manager.obtener_usuario(self.correo)
                if usuario:
                    self.usuario_id = usuario[0]
                    self.mostrar_formulario = True
                    self.error_nombre = ""
                    self.error_correo = ""
                    self.cargar_historial()
            else:
                self.error_correo = "⚠️ Este correo electrónico ya está registrado"
        else:
            # Modo inicio de sesión
            usuario = db_manager.obtener_usuario(self.correo)
            if usuario:
                self.usuario_id = usuario[0]
                self.nombre = usuario[1]  # Obtener el nombre del usuario
                self.mostrar_formulario = True
                self.error_nombre = ""
                self.error_correo = ""
                self.cargar_historial()
            else:
                self.error_correo = "⚠️ Correo electrónico no registrado"

    def reset_formulario(self):
        self.nombre = ""
        self.correo = ""
        self.glicemia = 0
        self.mensaje = ""
        self.color_alerta = "green"
        self.mostrar_formulario = False
        self.error_nombre = ""
        self.error_correo = ""
        self.modulo_seleccionado = ""
        self.es_registro = True
        self.usuario_id = 0
        self.historial = []

    def set_glicemia(self, glicemia):
        try:
            self.glicemia = int(glicemia)
        except ValueError:
            self.glicemia = 0

    def guardar_datos(self):
        if self.glicemia < 70:
            self.mensaje = "⚠️ Glicemia baja: ¡Cuidado!"
            self.color_alerta = "red"
        elif self.glicemia > 180:
            self.mensaje = "⚠️ Glicemia alta."
            self.color_alerta = "yellow"
        else:
            self.mensaje = "✅ Glicemia dentro del rango normal"
            self.color_alerta = "green"

        # Registrar la glicemia en la base de datos
        if self.usuario_id > 0:
            if db_manager.registrar_glicemia(self.usuario_id, self.glicemia):
                # Actualizar el historial
                self.cargar_historial()

        self.glicemia = 0

def index():
    return rx.container(
        rx.cond(
            FormState.mostrar_formulario,
            rx.vstack(
                rx.hstack(
                    rx.button(
                        "🏠",
                        on_click=NavigationState.ir_a_inicio,
                        size="3",
                        variant="ghost",
                        color_scheme="blue",
                        margin_right="1em"
                    ),
                    rx.image(
                        src="/images/logo2.png",
                        height="60px",
                        margin_right="1em"
                    ),
                    rx.vstack(
                        rx.heading(
                            f"🩸 Diabeduca - {FormState.nombre}",
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
                    rx.spacer(),
                    rx.select(
                        ["Educación", "Gráficos"],
                        placeholder="Seleccionar modulo",
                        on_change=FormState.set_modulo,
                        width="300px",
                        size="3",
                        bg="gray.50",
                        color="black",
                        _placeholder={"color": "blackAlpha.700"},
                        _hover={"bg": "gray.100"},
                        _focus={"bg": "gray.100"}
                    ),
                    width="100%",
                    padding="1em",
                    bg="gray.50",
                    border_bottom="1px solid",
                    border_color="gray.200",
                    position="sticky",
                    top="0",
                    z_index="1000",
                    box_shadow="sm"
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
                    rx.cond(
                        FormState.historial.length() > 0,
                        rx.foreach(
                            FormState.historial,
                            lambda item: rx.text(
                                f"{item['fecha']} {item['hora']} - Glicemia: {item['glicemia']} mg/dL",
                                margin_bottom="0.5em"
                            )
                        ),
                        rx.text(
                            "No hay registros disponibles",
                            color="gray.500",
                            font_style="italic"
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
                    rx.cond(
                        FormState.es_registro,
                        rx.input(
                            placeholder="Por favor, ingresa tu nombre",
                            on_change=FormState.set_nombre,
                            width="300px",
                            margin_bottom="1em",
                            bg="gray",
                            color="black",
                            _placeholder={"color": "blackAlpha.900"},
                            _hover={"bg": "white"},
                            _focus={"bg": "white"}
                        )
                    ),
                    rx.input(
                        placeholder="Ingresa tu correo electrónico",
                        on_change=FormState.set_correo,
                        width="300px",
                        margin_bottom="1em",
                        bg="gray",
                        color="black",
                        _placeholder={"color": "blackAlpha.900"},
                        _hover={"bg": "white"},
                        _focus={"bg": "white"}
                    ),
                    rx.hstack(
                        rx.button(
                            "Entrar",
                            on_click=FormState.mostrar,
                            color_scheme="blue",
                            size="4"
                        ),
                        rx.button(
                            rx.cond(
                                FormState.es_registro,
                                "Cambiar a Inicio de Sesión",
                                "Cambiar a Registro"
                            ),
                            on_click=FormState.toggle_modo,
                            color_scheme="gray",
                            size="4"
                        ),
                        spacing="2"
                    ),
                    rx.text(
                        FormState.error_nombre,
                        color="red.600",
                        font_weight="bold"
                    ),
                    rx.text(
                        FormState.error_correo,
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

# Crear la aplicación y agregar las páginas
app = rx.App()
app.add_page(index, route="/")
app.add_page(educacion, route="/educacion")
app.add_page(graficos, route="/graficos")
