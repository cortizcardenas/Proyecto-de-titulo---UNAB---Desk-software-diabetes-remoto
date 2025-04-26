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
            rx.heading("Visualización de Niveles de Glucosa", size="6", color="blue.800"),
            create_glucose_chart([]),  # Pasamos una lista vacía por ahora
            rx.button(
                "Volver",
                on_click=lambda: rx.redirect("/"),
                color_scheme="blue",
                size="3"
            ),
            spacing="4",
            align="center",
            padding="2em",
            border_radius="lg",
            box_shadow="lg",
            bg="gray.50"
        ),
        padding="2em",
        bg="gray.200"
    ) 