import reflex as rx
from app.states.auth_state import AuthState
from app.states.glucose_state import GlucoseState
from app.components.navbar import navbar
from app.components.glucose_input import glucose_input_form
from app.components.glucose_history import (
    glucose_history_list,
)
from app.components.glucose_chart import glucose_chart
from app.components.glucose_reference_ranges import glucose_reference_ranges_box
from app.components.educational_suggestion import educational_suggestion_box
from app.components.footer import footer_disclaimer


def _stat_box(
    label: str, value: rx.Var[int], color_class: str, icon: str
) -> rx.Component:
    """Función auxiliar para crear un cuadro de estadísticas para contadores."""
    return rx.el.div(
        rx.el.div(
            rx.el.span(
                icon,
                class_name="text-2xl mb-2",
            ),
            rx.el.span(
                value.to_string(),
                class_name=f"text-2xl font-bold {color_class}",
            ),
            rx.el.span(
                label,
                class_name="text-xs text-gray-500 dark:text-gray-400 mt-1",
            ),
            class_name="flex flex-col items-center justify-center",
        ),
        class_name="flex flex-col items-center justify-center p-3 rounded-md bg-gray-50 dark:bg-gray-700/50 border border-gray-200 dark:border-gray-600 text-center min-w-[70px]",
    )


def dashboard():
    """La página principal del dashboard que muestra la información de glucosa después del inicio de sesión."""
    return rx.el.div(
        navbar(),
        rx.el.main(
            rx.el.div(
                rx.el.h1(
                    "Bienvenido, ",
                    rx.el.span(
                        AuthState.user_full_name,
                        class_name="font-semibold",
                    ),
                    class_name="text-2xl md:text-3xl font-bold text-gray-800 dark:text-white mb-6",
                ),
                rx.el.div(
                    rx.el.div(
                        glucose_input_form(),
                        educational_suggestion_box(),
                        glucose_history_list(),
                        class_name="flex flex-col gap-6 w-full lg:w-1/3 h-full justify-between",
                        style={"minHeight": "100%"},
                    ),
                    rx.el.div(
                        glucose_chart(),
                        rx.el.div(
                            rx.el.h3(
                                "Resumen de Control Glucémico",
                                class_name="text-lg font-semibold mb-3 text-gray-700 dark:text-gray-200",
                            ),
                            rx.el.div(
                                rx.el.p(
                                    "Glucosa Promedio:",
                                    rx.el.span(
                                        f"{GlucoseState.average_glucose:.1f} mg/dL",
                                        class_name="font-semibold text-gray-800 dark:text-white ml-1",
                                    ),
                                    class_name="text-gray-600 dark:text-gray-400 text-lg",
                                ),
                                rx.match(
                                    GlucoseState.average_glucose_status,
                                    (
                                        "MUY BAJO",
                                        rx.el.span(
                                            "😨 MUY BAJO - Riesgo severo inmediato",
                                            class_name="ml-2 text-xl font-bold text-purple-600 dark:text-purple-400 px-6 py-3 rounded-lg bg-purple-100 dark:bg-purple-900/50",
                                            style={"minWidth": "360px", "display": "inline-block", "textAlign": "center"},
                                        ),
                                    ),
                                    (
                                        "Bajo",
                                        rx.el.span(
                                            "😰 Bajo - ¡Precaución!",
                                            class_name="ml-2 text-xl font-bold text-blue-600 dark:text-blue-400 px-6 py-3 rounded-lg bg-blue-100 dark:bg-blue-900/50",
                                            style={"minWidth": "360px", "display": "inline-block", "textAlign": "center"},
                                        ),
                                    ),
                                    (
                                        "Saludable",
                                        rx.el.span(
                                            "😊 Rango Saludable",
                                            class_name="ml-2 text-xl font-bold text-green-600 dark:text-green-400 px-6 py-3 rounded-lg bg-green-100 dark:bg-green-900/50",
                                            style={"minWidth": "360px", "display": "inline-block", "textAlign": "center"},
                                        ),
                                    ),
                                    (
                                        "Alto",
                                        rx.el.span(
                                            "😐 Alto - Monitorear",
                                            class_name="ml-2 text-xl font-bold text-yellow-700 dark:text-yellow-400 px-6 py-3 rounded-lg bg-yellow-100 dark:bg-yellow-900/50",
                                            style={"minWidth": "360px", "display": "inline-block", "textAlign": "center"},
                                        ),
                                    ),
                                    (
                                        "Muy Alto",
                                        rx.el.span(
                                            "😬 Muy Alto - Peligro",
                                            class_name="ml-2 text-xl font-bold text-red-600 dark:text-red-400 px-6 py-3 rounded-lg bg-red-100 dark:bg-red-900/50",
                                            style={"minWidth": "360px", "display": "inline-block", "textAlign": "center"},
                                        ),
                                    ),
                                    rx.el.span(
                                        GlucoseState.average_glucose_status,
                                        class_name="ml-2 text-xs text-gray-500 dark:text-gray-400",
                                    ),
                                ),
                                class_name="flex items-center",
                            ),
                            rx.el.div(
                                _stat_box(
                                    "Bajas",
                                    GlucoseState.count_low_readings,
                                    "text-blue-600 dark:text-blue-400",
                                    "😰",
                                ),
                                _stat_box(
                                    "Saludables",
                                    GlucoseState.count_healthy_readings,
                                    "text-green-600 dark:text-green-400",
                                    "😊",
                                ),
                                _stat_box(
                                    "Altas",
                                    GlucoseState.count_high_readings,
                                    "text-red-600 dark:text-red-400",
                                    "😐",
                                ),
                                class_name="grid grid-cols-3 gap-3 mt-4",
                            ),
                            rx.el.div(
                                rx.el.button(
                                    "Exportar Datos (CSV)",
                                    on_click=GlucoseState.export_data_csv,
                                    class_name="mt-4 w-full px-4 py-2 bg-blue-600 hover:bg-blue-700 text-white font-medium rounded-lg transition-colors duration-200 flex items-center justify-center gap-2",
                                ),
                                class_name="mt-4",
                            ),
                            class_name="p-6 bg-white dark:bg-gray-800 rounded-lg shadow border border-gray-200 dark:border-gray-700 mt-6",
                        ),
                        glucose_reference_ranges_box(),
                        class_name="flex flex-col gap-6 w-full lg:w-2/3 h-full justify-between",
                        style={"minHeight": "100%"},
                    ),
                    class_name="flex flex-col lg:flex-row gap-6 lg:gap-8 h-full",
                    style={"minHeight": "70vh"},
                ),
                class_name="container mx-auto px-4 py-8 flex-grow",
            ),
            class_name="flex-grow"
        ),
        footer_disclaimer(),
        class_name=rx.cond(
            AuthState.theme == "dark",
            "flex flex-col min-h-screen bg-gray-900 dark",
            "flex flex-col min-h-screen bg-[#e5e7eb]",
        ),
    )