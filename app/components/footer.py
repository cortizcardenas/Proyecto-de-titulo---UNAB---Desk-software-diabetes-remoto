import reflex as rx

def footer_disclaimer() -> rx.Component:
    return rx.el.footer(
        rx.el.div(
            rx.el.p(
                "⚠️ DiabEduca se encuentra en fase de prototipo. Esta versión es experimental y está en desarrollo activo. La aplicación no ha sido validada clínicamente y no reemplaza el consejo médico profesional.",
                class_name="text-sm text-gray-600 dark:text-gray-400 p-3 bg-yellow-50 dark:bg-yellow-900/20 border border-yellow-200 dark:border-yellow-800 rounded-lg text-center",
            ),
            class_name="container mx-auto mb-4 mt-8 flex justify-center",
        ),
        class_name="w-full"
    ) 