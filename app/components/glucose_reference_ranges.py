import reflex as rx

def glucose_reference_ranges_box() -> rx.Component:
    """Componente para mostrar los rangos de referencia clínicos de glucosa en sangre, con mejor estética y claridad."""
    return rx.el.div(
        rx.el.h3(
            "Rangos de Referencia Clínicos de Glucosa en Sangre",
            class_name="text-xl font-semibold mb-4 text-gray-800 dark:text-white",
        ),
        rx.el.div(
            rx.el.table(
                rx.el.thead(
                    rx.el.tr(
                        rx.el.th("Estado metabólico", class_name="px-4 py-3 border-b bg-gray-100 dark:bg-gray-700 text-gray-700 dark:text-gray-200 text-sm font-semibold text-left rounded-tl-lg"),
                        rx.el.th("Rango de glucosa en sangre (mg/dL)", class_name="px-4 py-3 border-b bg-gray-100 dark:bg-gray-700 text-gray-700 dark:text-gray-200 text-sm font-semibold text-left"),
                        rx.el.th("Descripción", class_name="px-4 py-3 border-b bg-gray-100 dark:bg-gray-700 text-gray-700 dark:text-gray-200 text-sm font-semibold text-left rounded-tr-lg"),
                    )
                ),
                rx.el.tbody(
                    rx.el.tr(
                        rx.el.td("😨 Hipoglucemia grave", class_name="px-4 py-2 border-b bg-white dark:bg-gray-800 text-gray-700 dark:text-gray-300"),
                        rx.el.td("< 54", class_name="px-4 py-2 border-b bg-white dark:bg-gray-800 text-gray-700 dark:text-gray-300"),
                        rx.el.td("Riesgo severo inmediato", class_name="px-4 py-2 border-b bg-white dark:bg-gray-800 text-gray-700 dark:text-gray-300"),
                    ),
                    rx.el.tr(
                        rx.el.td("😰 Hipoglucemia moderada", class_name="px-4 py-2 border-b bg-gray-50 dark:bg-gray-700 text-gray-700 dark:text-gray-300"),
                        rx.el.td("54–69", class_name="px-4 py-2 border-b bg-gray-50 dark:bg-gray-700 text-gray-700 dark:text-gray-300"),
                        rx.el.td("Requiere acción para prevenir síntomas", class_name="px-4 py-2 border-b bg-gray-50 dark:bg-gray-700 text-gray-700 dark:text-gray-300"),
                    ),
                    rx.el.tr(
                        rx.el.td("😊 Rango óptimo (ayunas)", class_name="px-4 py-2 border-b bg-white dark:bg-gray-800 text-gray-700 dark:text-gray-300"),
                        rx.el.td("80–130", class_name="px-4 py-2 border-b bg-white dark:bg-gray-800 text-gray-700 dark:text-gray-300"),
                        rx.el.td("Rango preprandial recomendado por ADA", class_name="px-4 py-2 border-b bg-white dark:bg-gray-800 text-gray-700 dark:text-gray-300"),
                    ),
                    rx.el.tr(
                        rx.el.td("😊 Rango óptimo (postprandial)", class_name="px-4 py-2 border-b bg-gray-50 dark:bg-gray-700 text-gray-700 dark:text-gray-300"),
                        rx.el.td("< 180", class_name="px-4 py-2 border-b bg-gray-50 dark:bg-gray-700 text-gray-700 dark:text-gray-300"),
                        rx.el.td("Rango dentro de 1–2 horas después de comer (postprandial)", class_name="px-4 py-2 border-b bg-gray-50 dark:bg-gray-700 text-gray-700 dark:text-gray-300"),
                    ),
                    rx.el.tr(
                        rx.el.td("😐 Glucosa alta", class_name="px-4 py-2 border-b bg-white dark:bg-gray-800 text-gray-700 dark:text-gray-300"),
                        rx.el.td("181–250", class_name="px-4 py-2 border-b bg-white dark:bg-gray-800 text-gray-700 dark:text-gray-300"),
                        rx.el.td("Nivel alto, debe considerarse ajuste o monitoreo frecuente", class_name="px-4 py-2 border-b bg-white dark:bg-gray-800 text-gray-700 dark:text-gray-300"),
                    ),
                    rx.el.tr(
                        rx.el.td("😬 Glucosa muy alta", class_name="px-4 py-2 bg-gray-50 dark:bg-gray-700 text-gray-700 dark:text-gray-300 rounded-bl-lg"),
                        rx.el.td("> 250", class_name="px-4 py-2 bg-gray-50 dark:bg-gray-700 text-gray-700 dark:text-gray-300"),
                        rx.el.td("Críticamente alto", class_name="px-4 py-2 bg-gray-50 dark:bg-gray-700 text-gray-700 dark:text-gray-300 rounded-br-lg"),
                    ),
                ),
                class_name="w-full text-sm text-left overflow-x-auto",
            ),
            class_name="overflow-x-auto rounded-lg shadow border border-gray-200 dark:border-gray-700",
        ),
        rx.el.p(
            "Nota: Estas son pautas generales basadas segun la ADA (American Diabetes Association). Siempre consulte a su Medico para asesoramiento personalizado.",
            class_name="text-xs text-gray-500 dark:text-gray-400 mt-4 italic text-center",
        ),
        class_name="p-6 bg-white dark:bg-gray-800 rounded-lg shadow border border-gray-200 dark:border-gray-700 mt-6",
    ) 