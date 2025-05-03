"""
Módulo de gráficos para visualización de niveles de glucosa.
"""

import reflex as rx
import plotly.graph_objects as go
from datetime import datetime, timedelta

def create_glucose_chart(data):
    """
    Crea un gráfico de línea para mostrar los niveles de glucosa a lo largo del tiempo.
    
    Args:
        data (list): Lista de diccionarios con fechas y niveles de glucosa.
    
    Returns:
        rx.Component: Componente de gráfico de Plotly.
    """
    # Datos de ejemplo para el gráfico
    fechas = [datetime.now() - timedelta(days=i) for i in range(7)]
    valores = [120, 140, 110, 130, 150, 125, 135]

    # Crear el gráfico
    fig = go.Figure()
    fig.add_trace(go.Scatter(
        x=fechas,
        y=valores,
        mode='lines+markers',
        name='Nivel de Glucosa'
    ))

    # Personalizar el diseño
    fig.update_layout(
        title='Niveles de Glucosa en la última semana',
        xaxis_title='Fecha',
        yaxis_title='Nivel de Glucosa (mg/dL)',
        template='plotly_white'
    )

    return rx.plotly(data=fig, height="400px")

def graficos():
    """Renderiza la página de gráficos."""
    return rx.container(
        rx.vstack(
            rx.hstack(
                rx.image(
                    src="/images/logo2.png",
                    height="60px",
                    margin_right="1em"
                ),
                rx.vstack(
                    rx.heading(
                        "🩸 Diabeduca - Módulo de Gráficos",
                        size="6",
                        color="blue.800",
                    ),
                    rx.text(
                        "Educación y control, en tus manos",
                        color="gray.600",
                        font_style="italic"
                    ),
                    align="start",
                ),
                rx.spacer(),
                rx.select(
                    ["Educación", "Gráficos"],
                    placeholder="Seleccionar modulo",
                    on_change=lambda x: rx.redirect(f"/{x.lower()}"),
                    width="300px",
                    size="3",
                    bg="gray.50",
                    color="black",
                    _placeholder={"color": "blackAlpha.700"},
                    _hover={"bg": "gray.100"},
                    _focus={"bg": "gray.100"}
                ),
                width="100%",
                padding="1em",
                bg="gray.50",
                border_bottom="1px solid",
                border_color="gray.200",
                position="sticky",
                top="0",
                z_index="1000",
                box_shadow="sm"
            ),
            rx.vstack(
                rx.heading("Visualización de Niveles de Glucosa", size="6", color="blue.800"),
                create_glucose_chart([]),  # Pasamos una lista vacía por ahora
                spacing="4",
                align="center",
                padding="2em",
                border_radius="lg",
                box_shadow="lg",
                bg="gray.50"
            ),
            spacing="4",
            width="100%",
            max_width="800px",
            padding="2em",
            border_radius="lg",
            box_shadow="lg",
            bg="gray.50"
        ),
        padding="2em",
        bg="gray.200"
    ) 