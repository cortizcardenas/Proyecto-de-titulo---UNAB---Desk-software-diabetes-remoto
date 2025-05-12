import reflex as rx
from app.states.auth_state import AuthState


def sign_in_card():
    return rx.el.div(
        rx.el.div(
            rx.el.h1(
                "Iniciar sesión en Diabeduca",
                class_name="text-2xl font-bold tracking-tight text-gray-900 dark:text-white",
            ),
            rx.el.p(
                "Ingresa tu correo y contraseña abajo.",
                class_name="text-sm text-gray-600 dark:text-gray-400 font-medium",
            ),
            class_name="flex flex-col space-y-1.5 text-center",
        ),
        rx.el.form(
            rx.el.div(
                rx.el.div(
                    rx.el.label(
                        "Correo electrónico",
                        class_name="text-sm font-medium leading-none peer-disabled:cursor-not-allowed peer-disabled:opacity-70 dark:text-gray-300",
                    ),
                    rx.el.input(
                        type="email",
                        placeholder="usuario@ejemplo.com",
                        name="email",
                        required=True,
                        class_name="flex h-10 w-full rounded-md border border-input bg-background px-3 py-2 text-sm ring-offset-background file:border-0 file:bg-transparent file:text-sm file:font-medium placeholder:text-muted-foreground focus-visible:outline-none focus-visible:ring-2 focus-visible:ring-ring focus-visible:ring-offset-2 disabled:cursor-not-allowed disabled:opacity-50 dark:bg-gray-700 dark:border-gray-600 dark:text-white dark:placeholder-gray-400",
                    ),
                    class_name="grid gap-2",
                ),
                rx.el.div(
                    rx.el.label(
                        "Contraseña",
                        class_name="text-sm font-medium leading-none peer-disabled:cursor-not-allowed peer-disabled:opacity-70 dark:text-gray-300",
                    ),
                    rx.el.input(
                        type="password",
                        name="password",
                        required=True,
                        placeholder="••••••••",
                        class_name="flex h-10 w-full rounded-md border border-input bg-background px-3 py-2 text-sm ring-offset-background file:border-0 file:bg-transparent file:text-sm file:font-medium placeholder:text-muted-foreground focus-visible:outline-none focus-visible:ring-2 focus-visible:ring-ring focus-visible:ring-offset-2 disabled:cursor-not-allowed disabled:opacity-50 dark:bg-gray-700 dark:border-gray-600 dark:text-white dark:placeholder-gray-400",
                    ),
                    class_name="grid gap-2",
                ),
                class_name="grid gap-4",
            ),
            rx.el.button(
                "Iniciar sesión",
                type_="submit",
                class_name="inline-flex items-center justify-center whitespace-nowrap rounded-md text-sm font-medium ring-offset-background transition-colors focus-visible:outline-none focus-visible:ring-2 focus-visible:ring-ring focus-visible:ring-offset-2 disabled:pointer-events-none disabled:opacity-50 bg-blue-600 text-primary-foreground hover:bg-blue-700 h-10 px-4 py-2 w-full dark:bg-blue-500 dark:hover:bg-blue-600 text-white",
            ),
            rx.el.div(
                rx.el.span(
                    "¿No tienes una cuenta?",
                    class_name="text-sm text-gray-500 dark:text-gray-400 font-medium",
                ),
                rx.el.a(
                    "Regístrate",
                    href="/sign-up",
                    class_name="text-sm text-blue-600 dark:text-blue-400 font-medium underline hover:text-blue-700 dark:hover:text-blue-500 transition-colors",
                ),
                class_name="mt-4 text-center text-sm flex flex-row gap-1 justify-center",
            ),
            class_name="grid gap-4",
            on_submit=AuthState.sign_in,
            reset_on_submit=True,
        ),
        class_name="p-6 rounded-xl bg-white dark:bg-gray-800 flex flex-col gap-4 shadow-lg border border-gray-200 dark:border-gray-700 text-black dark:text-white w-full max-w-md",
    )