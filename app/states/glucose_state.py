import reflex as rx
import datetime
import csv
import io
from typing import TypedDict, Optional, List, Dict
from app import database
from app.states.auth_state import AuthState


class GlucoseReading(TypedDict):
    id: int
    timestamp: str
    value: float
    notes: Optional[str]
    categoria: str


class FormattedReadingDict(TypedDict):
    id: int
    timestamp: str
    formatted_timestamp: str
    value: float
    notes: Optional[str]
    categoria: str
    status: str


class ChartReadingDict(TypedDict):
    timestamp: str
    value: float
    categoria: str


class GlucoseState(rx.State):
    """Gestiona las lecturas de glucosa y estadísticas relacionadas."""

    readings: List[GlucoseReading] = []
    new_reading_value: str = ""
    new_reading_notes: str = ""
    new_reading_category: str = "ayuno"
    healthy_min: float = 70.0
    healthy_max: float = 130.0
    postprandial_max: float = 180.0
    current_suggestion: str = ""

    @rx.var
    async def user_id(self) -> int | None:
        """Returns the current user's ID if logged in."""
        auth_state = await self.get_state(AuthState)
        if auth_state.current_user:
            return auth_state.current_user["id"]
        return None

    @rx.var
    def average_glucose(self) -> float:
        """Calculates the average glucose reading across all categories."""
        if not self.readings:
            return 0.0
        total = sum((r["value"] for r in self.readings))
        return round(total / len(self.readings), 1)

    @rx.var
    def average_glucose_status(self) -> str:
        """Determina el estado del promedio de glucosa usando la lógica de Ayuno."""
        avg = self.average_glucose
        if avg == 0.0 and (not self.readings):
            return "Sin lecturas"
        elif avg < 54:
            return "MUY BAJO"
        elif avg < 70:
            return "Bajo"
        elif avg <= 130:
            return "Saludable"
        elif avg <= 250:
            return "Alto"
        else:
            return "Muy Alto"

    @rx.var
    def count_low_readings(self) -> int:
        """Cuenta el número de lecturas bajas."""
        return len([r for r in self.readings if r["value"] < self.healthy_min])

    @rx.var
    def count_healthy_readings(self) -> int:
        """Cuenta el número de lecturas saludables."""
        return len([r for r in self.readings if self.healthy_min <= r["value"] <= self.healthy_max])

    @rx.var
    def count_high_readings(self) -> int:
        """Cuenta el número de lecturas altas."""
        return len([r for r in self.readings if r["value"] > self.healthy_max])

    def _get_reading_status(self, value: float, categoria: str) -> str:
        """Determina si una lectura es baja, saludable o alta basado en los rangos y categoría."""
        if value < 54:
            return "MUY BAJO"
        elif value < 70:
            return "Bajo"
        elif value <= 130:
            return "Saludable"
        elif value <= 250 and categoria == "2hrs Despues de Comer":
            return "Saludable"
        elif value <= 130 and (categoria == "3hrs Despues de Comer" or categoria == "Antes de Dormir"):
            return "Saludable"
        elif value <= 250:
            return "Alto"
        else:
            return "Muy Alto"

    @rx.var
    def formatted_readings(
        self,
    ) -> List[FormattedReadingDict]:
        """Formatea las lecturas para mostrar, incluyendo marca de tiempo, estado y categoría."""
        formatted: List[FormattedReadingDict] = []
        sorted_readings = sorted(
            self.readings,
            key=lambda r: datetime.datetime.fromisoformat(
                r["timestamp"]
            ),
            reverse=True,
        )
        for r in sorted_readings:
            try:
                dt = datetime.datetime.fromisoformat(
                    r["timestamp"]
                )
                formatted_ts = dt.strftime("%Y-%m-%d %H:%M")
            except ValueError:
                formatted_ts = "Invalid Date"
            status = self._get_reading_status(r["value"], r["categoria"])
            formatted.append(
                FormattedReadingDict(
                    id=r["id"],
                    timestamp=r["timestamp"],
                    formatted_timestamp=formatted_ts,
                    value=r["value"],
                    notes=r["notes"],
                    categoria=r["categoria"],
                    status=status,
                )
            )
        return formatted

    @rx.var
    def readings_for_chart(self) -> List[ChartReadingDict]:
        """Formats readings for the recharts component (sorted chronologically)."""
        sorted_readings = sorted(
            self.readings,
            key=lambda r: datetime.datetime.fromisoformat(
                r["timestamp"]
            ),
        )
        return [
            ChartReadingDict(
                timestamp=datetime.datetime.fromisoformat(
                    r["timestamp"]
                ).strftime("%m/%d %H:%M"),
                value=r["value"],
                categoria=r["categoria"],
            )
            for r in sorted_readings
        ]

    @rx.event(background=True)
    async def load_readings(self):
        """Loads readings for the current user from the database."""
        async with self:
            auth_state = await self.get_state(AuthState)
            _user_id = (
                auth_state.current_user["id"]
                if auth_state.current_user
                else None
            )
        if _user_id is None:
            print(
                "No user logged in, cannot load readings."
            )
            async with self:
                self.readings = []
            return
        db_readings = database.get_glucose_readings(
            _user_id
        )
        async with self:
            loaded_readings = []
            for r in db_readings:
                categoria_val = "No especificado"
                if (
                    "categoria" in r.keys()
                    and r["categoria"] is not None
                    and (r["categoria"] != "")
                ):
                    categoria_val = r["categoria"]
                loaded_readings.append(
                    GlucoseReading(
                        id=r["id"],
                        timestamp=r["timestamp"],
                        value=r["value"],
                        notes=r["notes"],
                        categoria=categoria_val,
                    )
                )
            self.readings = loaded_readings
            print(
                f"Loaded {len(self.readings)} readings for user {_user_id}"
            )

    @rx.event(background=True)
    async def add_reading(self, form_data: dict):
        """Agrega una nueva lectura de glucosa con categoría."""
        async with self:
            auth_state = await self.get_state(AuthState)
            _user_id = (
                auth_state.current_user["id"]
                if auth_state.current_user
                else None
            )
        if _user_id is None:
            yield rx.toast.error(
                "Debes iniciar sesión para agregar lecturas."
            )
            return
        value_str = form_data.get(
            "glucose_value", ""
        ).strip()
        notes = (form_data.get("notes") or "").strip()
        categoria = form_data.get(
            "categoria", "ayuno"
        ).strip()
        timestamp = datetime.datetime.now().isoformat()
        if not value_str:
            yield rx.toast.warning(
                "El valor de glucosa no puede estar vacío."
            )
            return
        try:
            value = float(value_str)
            if value <= 0:
                yield rx.toast.warning(
                    "El valor de glucosa debe ser positivo."
                )
                return
        except ValueError:
            yield rx.toast.error(
                "Valor de glucosa inválido. Por favor ingrese un número."
            )
            return
        valid_categories = [
            "Ayuno",
            "2hrs Despues de Comer",
            "3hrs Despues de Comer",
            "Antes de Dormir",
        ]
        if categoria not in valid_categories:
            yield rx.toast.warning(
                f"Categoría inválida seleccionada: {categoria}. Usando 'no especificado' por defecto."
            )
            categoria = "no especificado"
        success = database.add_glucose_reading(
            _user_id,
            timestamp,
            value,
            categoria,
            notes if notes else None,
        )
        if success:
            async with self:
                self.new_reading_value = ""
                self.new_reading_notes = ""
                self.new_reading_category = "ayuno"
            yield rx.toast.success("Lectura de glucosa agregada.")
            yield GlucoseState.load_readings
        else:
            yield rx.toast.error(
                "No se pudo guardar la lectura en la base de datos."
            )

    @rx.event(background=True)
    async def delete_reading(self, reading_id: int):
        """Elimina una lectura de glucosa."""
        async with self:
            auth_state = await self.get_state(AuthState)
            _user_id = (
                auth_state.current_user["id"]
                if auth_state.current_user
                else None
            )
        if _user_id is None:
            yield rx.toast.error(
                "Debes iniciar sesión para eliminar lecturas."
            )
            return
        success = database.delete_glucose_reading(
            reading_id, _user_id
        )
        if success:
            yield rx.toast.success("Lectura eliminada.")
            yield GlucoseState.load_readings
        else:
            yield rx.toast.error(
                "No se pudo eliminar la lectura."
            )

    @rx.event
    def set_new_reading_category(self, categoria: str):
        """Actualiza la categoría seleccionada para una nueva lectura."""
        self.new_reading_category = categoria

    @rx.event(background=True)
    async def export_data_csv(self):
        """Exporta las lecturas de glucosa actuales a un archivo CSV, incluyendo el nombre del usuario."""
        if not self.formatted_readings:
            yield rx.toast.warning("No hay datos para exportar.")
            return
        async with self:
            auth_state = await self.get_state(AuthState)
            user_name = (
                auth_state.user_full_name
                if auth_state.current_user
                else "Usuario Desconocido"
            )
            current_formatted_readings = self.formatted_readings
        if not current_formatted_readings:
            yield rx.toast.warning(
                "No hay datos para exportar después de la verificación final."
            )
            return
        output = io.StringIO()
        writer = csv.writer(output)
        headers = [
            "Usuario",
            "Fecha y Hora Original",
            "Fecha y Hora Formateada",
            "Valor (mg/dL)",
            "Estado",
            "Categoría",
            "Notas",
        ]
        writer.writerow(headers)
        for reading in current_formatted_readings:
            writer.writerow(
                [
                    user_name,
                    reading["timestamp"],
                    reading["formatted_timestamp"],
                    reading["value"],
                    reading["status"],
                    reading["categoria"],
                    reading["notes"] if reading["notes"] else "",
                ]
            )
        csv_data = output.getvalue()
        output.close()
        filename = f"lecturas_glucosa_{user_name.replace(' ', '_')}_{datetime.datetime.now().strftime('%Y%m%d_%H%M%S')}.csv"
        yield rx.download(data=csv_data, filename=filename)

    def get_educational_suggestion(self):
        """Obtiene una sugerencia educativa basada en el promedio de glucosa actual."""
        from app.components.educational_suggestion import get_suggestion_for_glucose
        self.current_suggestion = get_suggestion_for_glucose(self.average_glucose)