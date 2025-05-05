import reflex as rx
from app.states.auth_state import AuthState


def navbar() -> rx.Component:
    return rx.el.div(
        rx.el.div(
            rx.el.a(
                "Diabeduca",
                href="/dashboard",
                class_name="text-xl font-bold text-gray-800 dark:text-white hover:text-blue-600 dark:hover:text-blue-400",
            ),
            rx.el.div(
                rx.el.span(
                    f"Usuario: {AuthState.user_full_name}",
                    class_name="text-sm text-gray-600 dark:text-gray-300 hidden md:inline-block",
                ),
                rx.el.button(
                    rx.cond(
                        AuthState.theme == "light",
                        rx.icon(tag="moon"),
                        rx.icon(tag="sun"),
                    ),
                    on_click=AuthState.toggle_theme,
                    class_name="p-2 rounded-md text-gray-600 dark:text-gray-300 hover:bg-gray-100 dark:hover:bg-gray-700 transition-colors",
                    title=rx.cond(
                        AuthState.theme == "light",
                        "Switch to Dark Mode",
                        "Switch to Light Mode",
                    ),
                ),
                rx.el.button(
                    "Cerrar sesión",
                    on_click=AuthState.sign_out,
                    class_name="px-4 py-2 text-sm font-medium text-white bg-red-600 rounded-md hover:bg-red-700 focus:outline-none focus:ring-2 focus:ring-red-500 focus:ring-offset-2 dark:bg-red-500 dark:hover:bg-red-600 dark:focus:ring-offset-gray-800",
                ),
                class_name="flex items-center space-x-4",
            ),
            class_name="container mx-auto flex justify-between items-center py-4 px-6",
        ),
        class_name="bg-white dark:bg-gray-800 shadow-md sticky top-0 z-50 border-b border-gray-200 dark:border-gray-700",
    )