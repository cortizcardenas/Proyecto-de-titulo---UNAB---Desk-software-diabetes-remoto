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
            rx.el.p(
                "ℹ️ Recuerda: La educación continua es clave para el autocuidado en diabetes. Consulta siempre fuentes confiables nacionales como la ADICH (Asociación de Diabéticos de Chile) , MINSAL o tu medico tratante.",
                class_name="mt-2 text-xs text-blue-700 dark:text-blue-300 bg-blue-50 dark:bg-blue-900/30 rounded p-2",
            ),
            rx.el.p(
                "ADICH (Asociación de Diabéticos de Chile): +56 2 2678 0500 | Fundación Diabetes Juvenil: +56 2 2367 3900",
                class_name="mt-1 text-xs text-blue-700 dark:text-blue-300 bg-blue-50 dark:bg-blue-900/30 rounded p-2 text-center",
            ),
            rx.el.p(
                "💡 Tip: La insulina de acción rápida comienza a actuar a los 15 minutos de la inyección, alcanza su pico en 1 hora y dura entre 2 y 4 horas. La insulina de acción prolongada actúa varias horas después de la inyección y mantiene su efecto estable durante unas 24 horas.",
                class_name="mt-2 text-xs text-yellow-800 bg-yellow-100 dark:text-yellow-200 dark:bg-yellow-900/30 rounded p-2",
            ),
            rx.el.p(
                "Fuente: Información extraída de las páginas web de la Asociación Americana de Diabetes (ADA), la Asociación de Diabéticos de Chile (ADICH) y el Ministerio de Salud (MINSAL).",
                class_name="mt-2 text-xs text-gray-500 dark:text-gray-400 italic text-center",
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