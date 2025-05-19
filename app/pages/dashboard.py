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


def _stat_box(
    label: str, value: rx.Var[int], color_class: str
) -> rx.Component:
    """Función auxiliar para crear un cuadro de estadísticas para contadores."""
    return rx.el.div(
        rx.el.span(
            value.to_string(),
            class_name=f"text-2xl font-bold {color_class}",
        ),
        rx.el.span(
            label,
            class_name="text-xs text-gray-500 dark:text-gray-400 mt-1",
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
                        glucose_history_list(),
                        class_name="flex flex-col gap-6 w-full lg:w-1/3",
                    ),
                    rx.el.div(
                        glucose_chart(),
                        rx.el.div(
                            rx.el.h3(
                                "Estadísticas",
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
                                        "Bajo",
                                        rx.el.span(
                                            rx.icon(
                                                tag="arrow_down",
                                                size=16,
                                                class_name="inline mr-1 align-text-bottom",
                                            ),
                                            "Bajo - ¡Precaución!",
                                            class_name="ml-2 text-sm font-semibold text-blue-600 dark:text-blue-400 px-2 py-0.5 rounded bg-blue-100 dark:bg-blue-900/50",
                                        ),
                                    ),
                                    (
                                        "Alto",
                                        rx.el.span(
                                            rx.icon(
                                                tag="flag_triangle_right",
                                                size=16,
                                                class_name="inline mr-1 align-text-bottom",
                                            ),
                                            "Alto - Monitorear",
                                            class_name="ml-2 text-sm font-semibold text-yellow-600 dark:text-yellow-400 px-2 py-0.5 rounded bg-yellow-100 dark:bg-yellow-900/50",
                                        ),
                                    ),
                                    (
                                        "Saludable",
                                        rx.el.span(
                                            rx.icon(
                                                tag="square_check",
                                                size=16,
                                                class_name="inline mr-1 align-text-bottom",
                                            ),
                                            "Rango Saludable",
                                            class_name="ml-2 text-sm font-semibold text-green-600 dark:text-green-400 px-2 py-0.5 rounded bg-green-100 dark:bg-green-900/50",
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
                                ),
                                _stat_box(
                                    "Saludables",
                                    GlucoseState.count_healthy_readings,
                                    "text-green-600 dark:text-green-400",
                                ),
                                _stat_box(
                                    "Altas",
                                    GlucoseState.count_high_readings,
                                    "text-red-600 dark:text-red-400",
                                ),
                                class_name="grid grid-cols-3 gap-3 mt-4",
                            ),
                            class_name="p-6 bg-white dark:bg-gray-800 rounded-lg shadow border border-gray-200 dark:border-gray-700 mt-6",
                        ),
                        glucose_reference_ranges_box(),
                        class_name="flex flex-col gap-6 w-full lg:w-2/3",
                    ),
                    class_name="flex flex-col lg:flex-row gap-6 lg:gap-8",
                ),
                class_name="container mx-auto px-4 py-8",
            )
        ),
        class_name=rx.cond(
            AuthState.theme == "dark",
            "min-h-screen bg-gray-900 dark",
            "min-h-screen bg-gray-100",
        ),
    )