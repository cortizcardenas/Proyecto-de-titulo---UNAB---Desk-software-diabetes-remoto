import reflex as rx
from app.components.sign_in_card import sign_in_card
from app.states.auth_state import AuthState
from app.components.footer import footer_disclaimer


def sign_in():
    return rx.el.div(
        rx.el.div(
            sign_in_card(),
            class_name="flex-grow flex flex-col items-center justify-center",
        ),
        footer_disclaimer(),
        class_name=rx.cond(
            AuthState.theme == "dark",
            "flex flex-col min-h-screen bg-gray-900 p-4 dark",
            "flex flex-col min-h-screen bg-gray-100 p-4",
        ),
    )