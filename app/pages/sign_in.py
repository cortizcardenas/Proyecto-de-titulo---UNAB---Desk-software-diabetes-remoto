import reflex as rx
from app.components.sign_in_card import sign_in_card
from app.states.auth_state import AuthState


def sign_in():
    return rx.el.div(
        sign_in_card(),
        class_name=rx.cond(
            AuthState.theme == "dark",
            "flex flex-col items-center justify-center min-h-screen bg-gray-900 p-4 dark",
            "flex flex-col items-center justify-center min-h-screen bg-gray-100 p-4",
        ),
    )