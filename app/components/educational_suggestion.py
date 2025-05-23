import reflex as rx
from app.states.glucose_state import GlucoseState
from app.database import get_db_connection

def get_suggestion_for_glucose(glucose_value: float) -> str:
    """Obtiene una sugerencia educativa basada en el valor de glucosa."""
    conn = get_db_connection()
    cursor = conn.cursor()
    try:
        cursor.execute(
            """
            SELECT suggestion 
            FROM educational_suggestions 
            WHERE ? >= min_value AND ? < max_value 
            LIMIT 1
            """,
            (glucose_value, glucose_value)
        )
        result = cursor.fetchone()
        return result[0] if result else "No hay sugerencias disponibles para este nivel de glucosa."
    finally:
        conn.close()

def educational_suggestion_box() -> rx.Component:
    """Componente que muestra una sugerencia educativa basada en el promedio de glucosa."""
    return rx.el.div(
        rx.el.div(
            rx.el.h3(
                "Sugerencia Educativa",
                class_name="text-lg font-semibold mb-3 text-gray-700 dark:text-gray-200",
            ),
            rx.el.button(
                "Obtener Sugerencia",
                on_click=GlucoseState.get_educational_suggestion,
                class_name="w-full px-4 py-2 bg-green-600 hover:bg-green-700 text-white font-medium rounded-lg transition-colors duration-200",
            ),
            rx.cond(
                GlucoseState.current_suggestion != "",
                rx.el.div(
                    rx.el.p(
                        GlucoseState.current_suggestion,
                        class_name="mt-4 p-4 bg-gray-50 dark:bg-gray-700 rounded-lg text-gray-700 dark:text-gray-300",
                    ),
                    class_name="mt-4",
                ),
            ),
            class_name="p-6 bg-white dark:bg-gray-800 rounded-lg shadow border border-gray-200 dark:border-gray-700",
        ),
    ) 