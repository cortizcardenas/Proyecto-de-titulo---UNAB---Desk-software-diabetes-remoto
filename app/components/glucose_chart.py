import reflex as rx
from app.states.glucose_state import GlucoseState


def glucose_chart() -> rx.Component:
    """Componente para mostrar el gráfico de tendencia de glucosa."""
    return rx.el.div(
        rx.el.h2(
            "Tendencia de Glucosa",
            class_name="text-xl font-semibold mb-4 text-gray-800 dark:text-white",
        ),
        rx.cond(
            GlucoseState.readings_for_chart.length() > 1,
            rx.recharts.responsive_container(
                rx.recharts.line_chart(
                    rx.recharts.cartesian_grid(
                        stroke_dasharray="3 3",
                        stroke="#555555",
                    ),
                    rx.recharts.x_axis(
                        data_key="timestamp",
                        angle=-30,
                        text_anchor="end",
                        height=70,
                        stroke="#999999",
                    ),
                    rx.recharts.y_axis(
                        domain=[
                            "dataMin - 10",
                            "dataMax + 10",
                        ],
                        stroke="#999999",
                        label={
                            "value": "mg/dL",
                            "angle": -90,
                            "position": "insideLeft",
                            "style": {
                                "textAnchor": "middle",
                                "fill": "#999999",
                            },
                        },
                    ),
                    rx.recharts.tooltip(
                        content_style={
                            "backgroundColor": "#333333",
                            "borderColor": "#555555",
                        },
                        item_style={"color": "#eeeeee"},
                        label_style={"color": "#ffffff"},
                    ),
                    rx.recharts.legend(),
                    rx.recharts.line(
                        data_key="value",
                        name="Glucosa",
                        stroke="#3b82f6",
                        stroke_width=2,
                        dot={"r": 4, "fill": "#3b82f6"},
                        active_dot={
                            "r": 6,
                            "stroke": "#ffffff",
                            "fill": "#1d4ed8",
                        },
                        type="monotone",
                        connect_nulls=False,
                    ),
                    rx.recharts.reference_line(
                        y=GlucoseState.healthy_min.to(int),
                        label="Minimo Saludable",
                        stroke="#10b981",
                        stroke_dasharray="3 3",
                    ),
                    rx.recharts.reference_line(
                        y=GlucoseState.healthy_max.to(int),
                        label="Maximo Saludable",
                        stroke="#facc15",
                        stroke_dasharray="3 3",
                    ),
                    rx.recharts.reference_line(
                        y=GlucoseState.postprandial_max.to(int),
                        label="Maximo Postprandial",
                        stroke="#f97316",
                        stroke_dasharray="3 3",
                    ),
                    data=GlucoseState.readings_for_chart,
                    margin={
                        "top": 5,
                        "right": 30,
                        "left": 20,
                        "bottom": 40,
                    },
                ),
                width="100%",
                height=350,
            ),
            rx.el.p(
                "Se necesitan al menos dos lecturas para mostrar la gráfica de tendencia.",
                class_name="text-gray-500 dark:text-gray-400 text-center py-4",
            ),
        ),
        class_name="p-6 bg-white dark:bg-gray-800 rounded-lg shadow border border-gray-200 dark:border-gray-700 mt-6",
    )