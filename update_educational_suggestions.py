import sqlite3

# Ruta de la base de datos
DB_PATH = 'diabetes_management.db'

# Nuevos mensajes para cada rango
updates = [
    (0, 54, "Tu nivel de glucosa está MUY BAJO. Ingiere agua con azucar o un carbohidrato de injesta rapida y dirigete a urgencias Busca atención médica inmediata, en caso de ambulacia llama al 131", "MUY BAJO"),
    (54, 70, "Tu nivel de glucosa está bajo. Considera consumir una fuente rápida de carbohidratos como agua con azucar disuelta, jugo de frutas o caramelos, si tus valores no suben considera ir a urgencias", "Bajo"),
    (70, 131, "¡Excelente! Tu nivel de glucosa está en un rango saludable. Mantén tus hábitos actuales.", "Saludable"),
    (131, 181, "Tu nivel de glucosa está elevado. Si es postprandial o despues de comer, no hay problema. Si no, considera realizar actividad física moderada.", "Elevado"),
    (181, 251, "Tu nivel de glucosa está alto. Revisa tu alimentación y considera consultar con tu médico.", "Alto"),
    (251, 999, "Tu nivel de glucosa está MUY ALTO. Es importante que consultes con tu médico lo antes posible, si los valores se mantienen en las proximas horas se sugiere considerar ir a urgencias", "Muy Alto")
]

def update_suggestions():
    conn = sqlite3.connect(DB_PATH)
    cursor = conn.cursor()
    for min_v, max_v, suggestion, category in updates:
        cursor.execute(
            """
            UPDATE educational_suggestions
            SET suggestion = ?
            WHERE min_value = ? AND max_value = ? AND category = ?
            """,
            (suggestion, min_v, max_v, category)
        )
    conn.commit()
    conn.close()
    print("Mensajes educativos actualizados correctamente.")

if __name__ == "__main__":
    update_suggestions() 