import reflex as rx
from typing import List, Tuple, Dict, TypedDict, NotRequired


class InfoSection(TypedDict):
    title: str
    ranges: List[Tuple[str, str, str]]
    details: NotRequired[str]


def glucose_reference_ranges_box() -> rx.Component:
    """Componente para mostrar los rangos de referencia clínicos de glucosa en sangre."""
    reference_sections: List[InfoSection] = [
        {
            "title": "1. Glucosa en Sangre en Ayunas (Sin ingesta de alimentos durante al menos 8 horas):",
            "ranges": [
                (
                    "Normal:",
                    "Entre 70 mg/dL y 99 mg/dL",
                    "text-green-700 dark:text-green-400",
                ),
                (
                    "Prediabetes (Glucosa en Ayunas Alterada):",
                    "Entre 100 mg/dL y 125 mg/dL",
                    "text-yellow-700 dark:text-yellow-400",
                ),
                (
                    "Diabetes:",
                    "126 mg/dL o superior (confirmado por dos mediciones separadas)",
                    "text-red-700 dark:text-red-400",
                ),
            ],
        },
        {
            "title": "2. Glucosa en Sangre 2 Horas Después de Comer (Postprandial):",
            "ranges": [
                (
                    "Normal:",
                    "Menos de 140 mg/dL",
                    "text-green-700 dark:text-green-400",
                ),
                (
                    "Prediabetes (Tolerancia a la Glucosa Alterada):",
                    "Entre 140 mg/dL y 199 mg/dL",
                    "text-yellow-700 dark:text-yellow-400",
                ),
                (
                    "Diabetes:",
                    "200 mg/dL o superior",
                    "text-red-700 dark:text-red-400",
                ),
            ],
        },
        {
            "title": "3. Glucosa en Sangre 3 Horas Después de Comer:",
            "details": "Típicamente, los niveles de glucosa en sangre deberían haber vuelto cerca de los niveles en ayunas después de tres horas:",
            "ranges": [
                (
                    "Normal:",
                    "Entre 70 mg/dL y 100 mg/dL (idealmente por debajo de 100 mg/dL)",
                    "text-green-700 dark:text-green-400",
                ),
                (
                    "Control de Glucosa Alterado (Considerar Seguimiento Clínico):",
                    "Entre 101 mg/dL y 139 mg/dL",
                    "text-yellow-700 dark:text-yellow-400",
                ),
                (
                    "Alto/Anormal:",
                    "140 mg/dL o superior (puede indicar mal control de glucosa o resistencia a la insulina)",
                    "text-red-700 dark:text-red-400",
                ),
            ],
        },
    ]

    def render_range_item(
        item_tuple: rx.Var[Tuple[str, str, str]],
    ) -> rx.Component:
        label = item_tuple[0]
        value = item_tuple[1]
        color_class_var = item_tuple[2]
        return rx.el.li(
            rx.el.strong(
                label,
                class_name="font-semibold "
                + color_class_var,
            ),
            " " + value,
            class_name="text-sm text-gray-700 dark:text-gray-300",
        )

    def render_info_section(
        section_data: rx.Var[InfoSection],
    ) -> rx.Component:
        return rx.el.div(
            rx.el.h4(
                section_data["title"],
                class_name="text-md font-semibold text-gray-800 dark:text-white mb-1",
            ),
            rx.cond(
                section_data.contains("details"),
                rx.el.p(
                    section_data["details"],
                    class_name="text-sm text-gray-600 dark:text-gray-400 mb-1 italic",
                ),
                rx.fragment(),
            ),
            rx.el.ul(
                rx.foreach(
                    section_data["ranges"].to(
                        List[Tuple[str, str, str]]
                    ),
                    render_range_item,
                ),
                class_name="list-disc list-inside space-y-1 pl-4",
            ),
            class_name="mb-4",
        )

    return rx.el.div(
        rx.el.h3(
            "Rangos de Referencia Clínicos de Glucosa en Sangre",
            class_name="text-xl font-semibold mb-4 text-gray-800 dark:text-white",
        ),
        rx.foreach(reference_sections, render_info_section),
        rx.el.p(
            "Nota: Estas son pautas generales. Consulte a su proveedor de atención médica para obtener asesoramiento personalizado.",
            class_name="text-xs text-gray-500 dark:text-gray-400 mt-4 italic text-center",
        ),
        class_name="p-6 bg-white dark:bg-gray-800 rounded-lg shadow border border-gray-200 dark:border-gray-700 mt-6",
    ) 