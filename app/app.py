import reflex as rx
from app.pages.sign_in import sign_in
from app.pages.sign_up import sign_up
from app.pages.dashboard import dashboard
from app.states.auth_state import AuthState
from app.states.glucose_state import GlucoseState
from app.database import initialize_database

initialize_database()


def index() -> rx.Component:
    """Default page, redirects based on login status."""
    return rx.el.div(
        rx.cond(
            AuthState.is_logged_in,
            rx.el.div("Redirecting to dashboard..."),
            rx.el.div("Redirecting to sign in..."),
        ),
        on_mount=rx.cond(
            AuthState.is_logged_in,
            rx.redirect("/dashboard"),
            rx.redirect("/sign-in"),
        ),
    )


app = rx.App(theme=rx.theme(appearance="light"))
app.add_page(index, route="/")
app.add_page(sign_in, route="/sign-in")
app.add_page(sign_up, route="/sign-up")
app.add_page(
    dashboard,
    route="/dashboard",
    on_load=[
        AuthState.check_session,
        GlucoseState.load_readings,
    ],
)