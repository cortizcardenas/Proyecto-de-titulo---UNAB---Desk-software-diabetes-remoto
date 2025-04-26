"""
Módulo de educación de Diabeduca.
Contiene el contenido educativo sobre diabetes y su manejo.
"""

import reflex as rx
from app_diabetes.state.educational_state import EducationalState

def educacion():
    """Renderiza la página de contenido educativo."""
    return rx.container(
        rx.vstack(
            rx.heading("MÓDULO DE EDUCACIÓN EN PROGRESO", size="6", color="blue.800"),
            rx.text("Este módulo está actualmente en desarrollo", color="gray.600"),
            rx.button(
                "Volver",
                on_click=lambda: rx.redirect("/"),
                color_scheme="blue",
                size="3"
            ),
            spacing="4",
            align="center",
            padding="2em",
            border_radius="lg",
            box_shadow="lg",
            bg="gray.50"
        ),
        padding="2em",
        bg="gray.200"
    ) 