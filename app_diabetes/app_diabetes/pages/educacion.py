"""
Módulo de educación de Diabeduca.
Contiene el contenido educativo sobre diabetes y su manejo.
"""

import reflex as rx
from app_diabetes.state.educational_state import EducationalState

def education_page():
    """Renderiza la página de contenido educativo."""
    return rx.vstack(
        rx.heading("Educación Diabética", size="lg"),
        rx.text("Contenido educativo próximamente..."),
        align="center",
        spacing="4",
    ) 