import reflex as rx
from app.states.glucose_state import (
    GlucoseState,
    FormattedReadingDict,
)
from typing import List


def glucose_history_list() -> rx.Component:
    """Componente para mostrar la lista de lecturas de glucosa, incluyendo categoría."""
    return rx.el.div(
        rx.el.h2(
            "Historial de Glucosa",
            class_name="text-xl font-semibold mb-4 text-gray-800 dark:text-white",
        ),
        rx.el.div(
            rx.cond(
                GlucoseState.formatted_readings.length()
                > 0,
                rx.el.ul(
                    rx.foreach(
                        GlucoseState.formatted_readings.to(
                            List[FormattedReadingDict]
                        ),
                        lambda reading: rx.el.li(
                            rx.el.div(
                                rx.el.div(
                                    rx.el.span(
                                        reading[
                                            "formatted_timestamp"
                                        ],
                                        class_name="text-xs text-gray-500 dark:text-gray-400 mr-2 w-28 shrink-0",
                                    ),
                                    rx.el.span(
                                        f"{reading['value'].to(float):.1f} mg/dL",
                                        class_name="font-medium text-gray-800 dark:text-white mr-2 w-24 shrink-0",
                                    ),
                                    rx.el.span(
                                        reading["status"],
                                        class_name=rx.match(
                                            reading["status"],
                                            (
                                                "MUY BAJO",
                                                "text-purple-600 dark:text-purple-400 font-semibold text-xs px-1.5 py-0.5 rounded bg-purple-100 dark:bg-purple-900/50 mr-2",
                                            ),
                                            (
                                                "Bajo",
                                                "text-blue-600 dark:text-blue-400 font-semibold text-xs px-1.5 py-0.5 rounded bg-blue-100 dark:bg-blue-900/50 mr-2",
                                            ),
                                            (
                                                "Saludable",
                                                "text-green-600 dark:text-green-400 font-semibold text-xs px-1.5 py-0.5 rounded bg-green-100 dark:bg-green-900/50 mr-2",
                                            ),
                                            (
                                                "Alto",
                                                "text-yellow-700 dark:text-yellow-400 font-semibold text-xs px-1.5 py-0.5 rounded bg-yellow-100 dark:bg-yellow-900/50 mr-2",
                                            ),
                                            (
                                                "Muy Alto",
                                                "text-red-600 dark:text-red-400 font-semibold text-xs px-1.5 py-0.5 rounded bg-red-100 dark:bg-red-900/50 mr-2",
                                            ),
                                            "text-gray-600 dark:text-gray-400 font-semibold text-xs mr-2",
                                        ),
                                    ),
                                    rx.el.span(
                                        reading["categoria"]
                                        .to(str)
                                        .replace("-", " ")
                                        .title(),
                                        class_name="text-gray-500 dark:text-gray-400 text-xs italic px-1.5 py-0.5 rounded bg-gray-100 dark:bg-gray-700/50 mr-2",
                                    ),
                                    class_name="flex-grow flex items-center gap-1 flex-wrap",
                                ),
                                rx.el.button(
                                    rx.icon(
                                        tag="trash_2",
                                        size=14,
                                    ),
                                    on_click=lambda: GlucoseState.delete_reading(
                                        reading["id"].to(
                                            int
                                        )
                                    ),
                                    class_name="p-1 text-red-500 hover:text-red-700 dark:hover:text-red-400 rounded focus:outline-none focus:ring-1 focus:ring-red-400 shrink-0",
                                    title="Delete Reading",
                                    size="1",
                                ),
                                class_name="flex justify-between items-center gap-2",
                            ),
                            rx.cond(
                                reading.contains("notes")
                                & (reading["notes"] != None)
                                & (
                                    reading["notes"]
                                    .to(str)
                                    .length()
                                    > 0
                                ),
                                rx.el.p(
                                    rx.el.em(
                                        reading["notes"]
                                    ),
                                    class_name="text-xs text-gray-600 dark:text-gray-400 mt-1 pl-[calc(theme(spacing.28)+theme(spacing.2))] ",
                                ),
                                rx.fragment(),
                            ),
                            key=reading["id"].to(str),
                            class_name="py-2.5 px-3 border-b border-gray-200 dark:border-gray-700 hover:bg-gray-50 dark:hover:bg-gray-700/50 transition-colors",
                        ),
                    ),
                    class_name="divide-y divide-gray-200 dark:divide-gray-700",
                ),
                rx.el.p(
                    "Aún no hay lecturas registradas.",
                    class_name="text-gray-500 dark:text-gray-400 text-center py-4",
                ),
            ),
            class_name="max-h-96 overflow-y-auto border border-gray-200 dark:border-gray-600 rounded-md bg-white dark:bg-gray-800",
        ),
        class_name="p-6 bg-white dark:bg-gray-800 rounded-lg shadow border border-gray-200 dark:border-gray-700 mt-6",
    )