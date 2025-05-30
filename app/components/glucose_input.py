import reflex as rx
from app.states.glucose_state import GlucoseState


def glucose_input_form() -> rx.Component:
    """Formulario para agregar una nueva lectura de glucosa, incluyendo selección de categoría."""
    categories = [
        "Ayuno",
        "2hrs Despues de Comer",
        "3hrs Despues de Comer",
        "Antes de Dormir",
    ]
    return rx.el.div(
        rx.el.h2(
            "Registrar Nueva Lectura",
            class_name="text-xl font-semibold mb-4 text-gray-800 dark:text-white",
        ),
        rx.el.form(
            rx.el.div(
                rx.el.label(
                    "Valor de Glucosa (mg/dL)",
                    html_for="glucose_value",
                    class_name="block text-sm font-medium text-gray-700 dark:text-gray-300 mb-1",
                ),
                rx.el.input(
                    type="number",
                    name="glucose_value",
                    id="glucose_value",
                    placeholder="e.g., 95",
                    step="0.1",
                    key=f"glucose-value-{GlucoseState.new_reading_value}",
                    default_value=GlucoseState.new_reading_value,
                    required=True,
                    class_name="w-full p-2 border border-gray-300 dark:border-gray-600 rounded-md shadow-sm focus:ring-blue-500 focus:border-blue-500 dark:bg-gray-700 dark:text-white dark:placeholder-gray-400",
                ),
                class_name="mb-4",
            ),
            rx.el.div(
                rx.el.label(
                    "Categoria",
                    html_for="categoria",
                    class_name="block text-sm font-medium text-gray-700 dark:text-gray-300 mb-1",
                ),
                rx.el.select(
                    rx.foreach(
                        categories,
                        lambda categoria: rx.el.option(
                            categoria.replace(
                                "-", " "
                            ).title(),
                            value=categoria,
                        ),
                    ),
                    name="categoria",
                    id="categoria",
                    value=GlucoseState.new_reading_category,
                    on_change=GlucoseState.set_new_reading_category,
                    class_name="w-full p-2 border border-gray-300 dark:border-gray-600 rounded-md shadow-sm focus:ring-blue-500 focus:border-blue-500 dark:bg-gray-700 dark:text-white",
                ),
                class_name="mb-4",
            ),
            rx.el.div(
                rx.el.label(
                    "Notas (Opcional)",
                    html_for="notes",
                    class_name="block text-sm font-medium text-gray-700 dark:text-gray-300 mb-1",
                ),
                rx.el.textarea(
                    name="notes",
                    id="notes",
                    placeholder="p.ej., Antes del desayuno, Me siento cansado",
                    rows=3,
                    key=f"notes-{GlucoseState.new_reading_notes}",
                    default_value=GlucoseState.new_reading_notes,
                    class_name="w-full p-2 border border-gray-300 dark:border-gray-600 rounded-md shadow-sm focus:ring-blue-500 focus:border-blue-500 dark:bg-gray-700 dark:text-white dark:placeholder-gray-400",
                ),
                class_name="mb-4",
            ),
            rx.el.button(
                "Agregar Lectura",
                type_="submit",
                class_name="w-full inline-flex justify-center py-2 px-4 border border-transparent shadow-sm text-sm font-medium rounded-md text-white bg-blue-600 hover:bg-blue-700 focus:outline-none focus:ring-2 focus:ring-offset-2 focus:ring-blue-500 dark:bg-blue-500 dark:hover:bg-blue-600 dark:focus:ring-offset-gray-800",
            ),
            on_submit=GlucoseState.add_reading,
        ),
        class_name="p-6 bg-white dark:bg-gray-800 rounded-lg shadow border border-gray-200 dark:border-gray-700",
    )