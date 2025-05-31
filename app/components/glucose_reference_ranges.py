import reflex as rx

def glucose_reference_ranges_box() -> rx.Component:
    """Componente para mostrar los rangos de referencia clínicos de glucosa en sangre para personas con diabetes y personas sanas, en formato comparativo."""
    return rx.el.div(
        rx.el.h3(
            "Rangos de Referencia Clínicos de Glucosa en Sangre: Diabetes vs Persona Sana",
            class_name="text-xl font-semibold mb-4 text-gray-800 dark:text-white",
        ),
        rx.el.div(
            rx.el.table(
                rx.el.thead(
                    rx.el.tr(
                        rx.el.th("Estado metabólico (diabetes)", class_name="px-4 py-3 border-b bg-gray-100 dark:bg-gray-700 text-gray-700 dark:text-gray-200 text-sm font-semibold text-left rounded-tl-lg"),
                        rx.el.th("Rango (mg/dL) diabetes", class_name="px-4 py-3 border-b bg-gray-100 dark:bg-gray-700 text-gray-700 dark:text-gray-200 text-sm font-semibold text-left"),
                        rx.el.th("Descripción diabetes", class_name="px-4 py-3 border-b bg-gray-100 dark:bg-gray-700 text-gray-700 dark:text-gray-200 text-sm font-semibold text-left"),
                        rx.el.th("Estado metabólico (sano)", class_name="px-4 py-3 border-b bg-gray-100 dark:bg-gray-700 text-gray-700 dark:text-gray-200 text-sm font-semibold text-left"),
                        rx.el.th("Rango (mg/dL) sano", class_name="px-4 py-3 border-b bg-gray-100 dark:bg-gray-700 text-gray-700 dark:text-gray-200 text-sm font-semibold text-left"),
                        rx.el.th("Descripción sano", class_name="px-4 py-3 border-b bg-gray-100 dark:bg-gray-700 text-gray-700 dark:text-gray-200 text-sm font-semibold text-left rounded-tr-lg"),
                    )
                ),
                rx.el.tbody(
                    # Fila 1
                    rx.el.tr(
                        rx.el.td("😨 Hipoglucemia grave", class_name="px-4 py-2 border-b bg-white dark:bg-gray-800 text-gray-700 dark:text-gray-300"),
                        rx.el.td("< 54", class_name="px-4 py-2 border-b bg-white dark:bg-gray-800 text-gray-700 dark:text-gray-300"),
                        rx.el.td("Riesgo severo inmediato - Buscar atención médica", class_name="px-4 py-2 border-b bg-white dark:bg-gray-800 text-gray-700 dark:text-gray-300"),
                        rx.el.td("Normal", class_name="px-4 py-2 border-b bg-white dark:bg-gray-800 text-gray-700 dark:text-gray-300"),
                        rx.el.td("< 100", class_name="px-4 py-2 border-b bg-white dark:bg-gray-800 text-gray-700 dark:text-gray-300"),
                        rx.el.td("Ayuno normal", class_name="px-4 py-2 border-b bg-white dark:bg-gray-800 text-gray-700 dark:text-gray-300"),
                    ),
                    # Fila 2
                    rx.el.tr(
                        rx.el.td("😰 Hipoglucemia moderada", class_name="px-4 py-2 border-b bg-gray-50 dark:bg-gray-700 text-gray-700 dark:text-gray-300"),
                        rx.el.td("54–69", class_name="px-4 py-2 border-b bg-gray-50 dark:bg-gray-700 text-gray-700 dark:text-gray-300"),
                        rx.el.td("Requiere acción inmediata para prevenir síntomas", class_name="px-4 py-2 border-b bg-gray-50 dark:bg-gray-700 text-gray-700 dark:text-gray-300"),
                        rx.el.td("Prediabetes", class_name="px-4 py-2 border-b bg-gray-50 dark:bg-gray-700 text-gray-700 dark:text-gray-300"),
                        rx.el.td("100–125", class_name="px-4 py-2 border-b bg-gray-50 dark:bg-gray-700 text-gray-700 dark:text-gray-300"),
                        rx.el.td("Ayuno alterado (prediabetes)", class_name="px-4 py-2 border-b bg-gray-50 dark:bg-gray-700 text-gray-700 dark:text-gray-300"),
                    ),
                    # Fila 3
                    rx.el.tr(
                        rx.el.td("😊 Rango óptimo (ayunas)", class_name="px-4 py-2 border-b bg-white dark:bg-gray-800 text-gray-700 dark:text-gray-300"),
                        rx.el.td("70–130", class_name="px-4 py-2 border-b bg-white dark:bg-gray-800 text-gray-700 dark:text-gray-300"),
                        rx.el.td("Rango preprandial recomendado (diabetes)", class_name="px-4 py-2 border-b bg-white dark:bg-gray-800 text-gray-700 dark:text-gray-300"),
                        rx.el.td("Diabetes", class_name="px-4 py-2 border-b bg-white dark:bg-gray-800 text-gray-700 dark:text-gray-300"),
                        rx.el.td("≥ 126", class_name="px-4 py-2 border-b bg-white dark:bg-gray-800 text-gray-700 dark:text-gray-300"),
                        rx.el.td("Ayuno elevado (diabetes)", class_name="px-4 py-2 border-b bg-white dark:bg-gray-800 text-gray-700 dark:text-gray-300"),
                    ),
                    # Fila 4
                    rx.el.tr(
                        rx.el.td("😊 Rango óptimo (postprandial)", class_name="px-4 py-2 border-b bg-gray-50 dark:bg-gray-700 text-gray-700 dark:text-gray-300"),
                        rx.el.td("< 180", class_name="px-4 py-2 border-b bg-gray-50 dark:bg-gray-700 text-gray-700 dark:text-gray-300"),
                        rx.el.td("Rango dentro de 2-3 horas después de comer (diabetes)", class_name="px-4 py-2 border-b bg-gray-50 dark:bg-gray-700 text-gray-700 dark:text-gray-300"),
                        rx.el.td("-", class_name="px-4 py-2 border-b bg-gray-50 dark:bg-gray-700 text-gray-700 dark:text-gray-300"),
                        rx.el.td("-", class_name="px-4 py-2 border-b bg-gray-50 dark:bg-gray-700 text-gray-700 dark:text-gray-300"),
                        rx.el.td("-", class_name="px-4 py-2 border-b bg-gray-50 dark:bg-gray-700 text-gray-700 dark:text-gray-300"),
                    ),
                    # Fila 5
                    rx.el.tr(
                        rx.el.td("😐 Glucosa alta", class_name="px-4 py-2 border-b bg-white dark:bg-gray-800 text-gray-700 dark:text-gray-300"),
                        rx.el.td("181–250", class_name="px-4 py-2 border-b bg-white dark:bg-gray-800 text-gray-700 dark:text-gray-300"),
                        rx.el.td("Nivel alto, requiere monitoreo y posible ajuste (diabetes)", class_name="px-4 py-2 border-b bg-white dark:bg-gray-800 text-gray-700 dark:text-gray-300"),
                        rx.el.td("-", class_name="px-4 py-2 border-b bg-white dark:bg-gray-800 text-gray-700 dark:text-gray-300"),
                        rx.el.td("-", class_name="px-4 py-2 border-b bg-white dark:bg-gray-800 text-gray-700 dark:text-gray-300"),
                        rx.el.td("-", class_name="px-4 py-2 border-b bg-white dark:bg-gray-800 text-gray-700 dark:text-gray-300"),
                    ),
                    # Fila 6
                    rx.el.tr(
                        rx.el.td("😬 Glucosa muy alta", class_name="px-4 py-2 bg-gray-50 dark:bg-gray-700 text-gray-700 dark:text-gray-300 rounded-bl-lg"),
                        rx.el.td("> 250", class_name="px-4 py-2 bg-gray-50 dark:bg-gray-700 text-gray-700 dark:text-gray-300"),
                        rx.el.td("Nivel críticamente alto - Buscar atención médica (diabetes)", class_name="px-4 py-2 bg-gray-50 dark:bg-gray-700 text-gray-700 dark:text-gray-300"),
                        rx.el.td("-", class_name="px-4 py-2 bg-gray-50 dark:bg-gray-700 text-gray-700 dark:text-gray-300"),
                        rx.el.td("-", class_name="px-4 py-2 bg-gray-50 dark:bg-gray-700 text-gray-700 dark:text-gray-300"),
                        rx.el.td("-", class_name="px-4 py-2 bg-gray-50 dark:bg-gray-700 text-gray-700 dark:text-gray-300 rounded-br-lg"),
                    ),
                ),
                class_name="w-full text-sm text-left overflow-x-auto",
            ),
            class_name="overflow-x-auto rounded-lg shadow border border-gray-200 dark:border-gray-700",
        ),
        rx.el.p(
            "Nota: Estas son pautas generales basadas en la ADA (American Diabetes Association) y la literatura clínica. Siempre consulte a su Médico para asesoramiento personalizado.",
            class_name="text-xs text-gray-500 dark:text-gray-400 mt-4 italic text-center",
        ),
        class_name="p-6 bg-white dark:bg-gray-800 rounded-lg shadow border border-gray-200 dark:border-gray-700 mt-6",
    ) 