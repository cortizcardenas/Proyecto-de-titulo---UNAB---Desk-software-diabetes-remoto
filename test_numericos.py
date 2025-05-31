import pytest
from app.states.glucose_state import GlucoseState
import datetime

# Helper para crear lecturas

def make_reading(value, categoria="Ayuno", id=1):
    return {
        "id": id,
        "timestamp": datetime.datetime.now().isoformat(),
        "value": value,
        "notes": None,
        "categoria": categoria,
    }

def test_average_glucose():
    state = GlucoseState()
    state.readings = [make_reading(100), make_reading(120), make_reading(80)]
    assert state.average_glucose == 100.0

def test_count_low_readings():
    state = GlucoseState()
    state.readings = [make_reading(60), make_reading(80), make_reading(69)]
    assert state.count_low_readings == 2

def test_count_healthy_readings():
    state = GlucoseState()
    state.readings = [make_reading(70), make_reading(100), make_reading(130), make_reading(69)]
    assert state.count_healthy_readings == 3

def test_count_high_readings():
    state = GlucoseState()
    state.readings = [make_reading(131), make_reading(150), make_reading(129)]
    assert state.count_high_readings == 2

def test_average_glucose_status():
    state = GlucoseState()
    state.readings = [make_reading(50), make_reading(60)]
    assert state.average_glucose_status == "Bajo" or state.average_glucose_status == "MUY BAJO"
    state.readings = [make_reading(80), make_reading(90)]
    assert state.average_glucose_status == "Saludable"
    state.readings = [make_reading(200), make_reading(220)]
    assert state.average_glucose_status == "Alto"
    state.readings = [make_reading(300), make_reading(320)]
    assert state.average_glucose_status == "Muy Alto"

def test_get_reading_status():
    state = GlucoseState()
    assert state._get_reading_status(50, "Ayuno") == "MUY BAJO"
    assert state._get_reading_status(60, "Ayuno") == "Bajo"
    assert state._get_reading_status(100, "Ayuno") == "Saludable"
    assert state._get_reading_status(140, "Ayuno") == "Alto"
    assert state._get_reading_status(300, "Ayuno") == "Muy Alto"
    # Postprandial
    assert state._get_reading_status(180, "2hrs Despues de Comer") == "Saludable"
    assert state._get_reading_status(240, "2hrs Despues de Comer") == "Saludable"
    assert state._get_reading_status(251, "2hrs Despues de Comer") == "Muy Alto" 