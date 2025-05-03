"""
Estado compartido para la navegación entre módulos.
"""

import reflex as rx

class NavigationState(rx.State):
    """Estado para manejar la navegación entre módulos."""
    
    def set_modulo(self, modulo):
        """Navega al módulo seleccionado."""
        if modulo == "Educación":
            return rx.redirect("/educacion")
        elif modulo == "Gráficos":
            return rx.redirect("/graficos")
        return None

    def ir_a_inicio(self):
        """Redirige a la página principal."""
        return rx.redirect("/") 