import reflex as rx
import sqlite3
import os
from typing import Optional, Tuple, Any, Dict

DATABASE_PATH = "diabetes_management.db"


def get_db_connection() -> sqlite3.Connection:
    """Establishes a connection to the SQLite database."""
    conn = sqlite3.connect(DATABASE_PATH)
    conn.row_factory = sqlite3.Row
    conn.execute("PRAGMA foreign_keys = ON;")
    return conn


def _table_exists(
    cursor: sqlite3.Cursor, table_name: str
) -> bool:
    """Checks if a table exists in the database."""
    cursor.execute(
        "SELECT name FROM sqlite_master WHERE type='table' AND name=?",
        (table_name,),
    )
    return cursor.fetchone() is not None


def _get_table_columns(
    cursor: sqlite3.Cursor, table_name: str
) -> Dict[str, str]:
    """Gets the columns and their types for a given table."""
    cursor.execute(f"PRAGMA table_info({table_name})")
    return {
        col["name"]: col["type"].upper()
        for col in cursor.fetchall()
    }


def _add_column_if_not_exists(
    conn: sqlite3.Connection,
    cursor: sqlite3.Cursor,
    table_name: str,
    column_name: str,
    column_def: str,
):
    """Adds a column to a table if it doesn't already exist."""
    columns = _get_table_columns(cursor, table_name)
    if column_name not in columns:
        print(
            f"Column '{column_name}' not found in '{table_name}'. Adding it..."
        )
        try:
            cursor.execute(
                f"ALTER TABLE {table_name} ADD COLUMN {column_name} {column_def}"
            )
            conn.commit()
            print(
                f"Column '{column_name}' added to '{table_name}' successfully."
            )
        except Exception as e:
            print(
                f"Error adding column '{column_name}' to '{table_name}': {e}"
            )
            conn.rollback()
    else:
        print(
            f"Column '{column_name}' already exists in '{table_name}'."
        )


def _add_cascade_delete_to_readings(
    conn: sqlite3.Connection, cursor: sqlite3.Cursor
):
    """Adds ON DELETE CASCADE to the glucose_readings foreign key if missing
    AND ensures the 'categoria' column exists during potential recreation.
    """
    print(
        "Verificando clave foránea y columnas para lecturas_glucosa..."
    )
    cursor.execute(
        "PRAGMA foreign_key_list(glucose_readings)"
    )
    fk_info = cursor.fetchall()
    columns = _get_table_columns(cursor, "glucose_readings")
    needs_fk_update = True
    for fk in fk_info:
        if (
            fk["table"] == "users"
            and fk["on_delete"] == "CASCADE"
        ):
            needs_fk_update = False
            break
    if needs_fk_update or "categoria" not in columns:
        action = (
            "Agregando ON DELETE CASCADE y asegurando columna 'categoria'"
            if needs_fk_update and "categoria" not in columns
            else (
                "Agregando ON DELETE CASCADE"
                if needs_fk_update
                else "Agregando columna 'categoria'"
            )
        )
        print(
            f"{action} para clave foránea de lecturas_glucosa..."
        )
        try:
            cursor.execute("PRAGMA foreign_keys=off;")
            cursor.execute("BEGIN TRANSACTION;")
            cursor.execute(
                "\n                CREATE TABLE glucose_readings_new (\n                    id INTEGER PRIMARY KEY AUTOINCREMENT,\n                    user_id INTEGER NOT NULL,\n                    timestamp DATETIME NOT NULL,\n                    value REAL NOT NULL,\n                    notes TEXT,\n                    categoria TEXT DEFAULT 'No especificado', -- Agregar categoria con valor por defecto\n                    FOREIGN KEY (user_id) REFERENCES users (id) ON DELETE CASCADE\n                );\n                "
            )
            if "categoria" in columns:
                cursor.execute(
                    "\n                    INSERT INTO glucose_readings_new (id, user_id, timestamp, value, notes, categoria)\n                    SELECT id, user_id, timestamp, value, notes, categoria FROM glucose_readings;\n                    "
                )
            else:
                cursor.execute(
                    "\n                    INSERT INTO glucose_readings_new (id, user_id, timestamp, value, notes)\n                    SELECT id, user_id, timestamp, value, notes FROM glucose_readings;\n                    "
                )
            cursor.execute("DROP TABLE glucose_readings;")
            cursor.execute(
                "ALTER TABLE glucose_readings_new RENAME TO glucose_readings;"
            )
            conn.commit()
            cursor.execute("PRAGMA foreign_keys=on;")
            print(f"{action} completado exitosamente.")
        except Exception as e:
            print(
                f"Error durante recreación de tabla: {e}. Rollback."
            )
            conn.rollback()
            try:
                cursor.execute("PRAGMA foreign_keys=on;")
            except Exception as fk_e:
                print(
                    f"No se pudo re-habilitar claves foráneas después de rollback: {fk_e}"
                )
    else:
        print(
            "ON DELETE CASCADE y columna 'categoria' ya presentes para lecturas_glucosa."
        )


def initialize_database():
    """Initializes the database and its tables if they don't exist,
    or updates schema if necessary."""
    needs_creation = not os.path.exists(DATABASE_PATH)
    conn = get_db_connection()
    cursor = conn.cursor()
    try:
        if needs_creation:
            print(
                "Database not found, creating and initializing tables..."
            )
            cursor.execute(
                """
                CREATE TABLE users (
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    email TEXT UNIQUE NOT NULL,
                    password TEXT NOT NULL,
                    full_name TEXT NOT NULL,
                    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
                )
                """
            )
            print("Created 'users' table.")
            cursor.execute(
                """
                CREATE TABLE glucose_readings (
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    user_id INTEGER NOT NULL,
                    timestamp DATETIME NOT NULL,
                    value REAL NOT NULL,
                    notes TEXT,
                    categoria TEXT DEFAULT 'No especificado',
                    FOREIGN KEY (user_id) REFERENCES users (id) ON DELETE CASCADE
                )
                """
            )
            print("Created 'glucose_readings' table with categoria and ON DELETE CASCADE.")
            
            # Crear tabla de sugerencias educativas
            cursor.execute(
                """
                CREATE TABLE educational_suggestions (
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    min_value REAL NOT NULL,
                    max_value REAL NOT NULL,
                    suggestion TEXT NOT NULL,
                    category TEXT NOT NULL,
                    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
                )
                """
            )
            print("Created 'educational_suggestions' table.")
            
            # Insertar sugerencias iniciales
            initial_suggestions = [
                (0, 54, "Tu nivel de glucosa está MUY BAJO. Ingiere agua con azucar o un carbohidrato de injesta rapida y dirigete a urgencias Busca atención médica inmediata, en caso de ambulacia llama al 131", "MUY BAJO"),
                (54, 70, "Tu nivel de glucosa está bajo. Considera consumir una fuente rápida de carbohidratos como agua con azucar disuelta, jugo de frutas o caramelos, si tus valores no suben considera ir a urgencias", "Bajo"),
                (70, 131, "¡Excelente! Tu nivel de glucosa está en un rango saludable. Mantén tus hábitos actuales.", "Saludable"),
                (131, 181, "Tu nivel de glucosa está elevado. Si es postprandial o despues de comer, no hay problema. Si no, considera realizar actividad física moderada.", "Elevado"),
                (181, 251, "Tu nivel de glucosa está alto. Revisa tu alimentación y considera consultar con tu médico.", "Alto"),
                (251, 999, "Tu nivel de glucosa está MUY ALTO. Es importante que consultes con tu médico lo antes posible, si los valores se mantienen en las proximas horas se sugiere considerar ir a urgencias", "Muy Alto")
            ]
            
            cursor.executemany(
                "INSERT INTO educational_suggestions (min_value, max_value, suggestion, category) VALUES (?, ?, ?, ?)",
                initial_suggestions
            )
            print("Inserted initial educational suggestions.")
            
            conn.commit()
            print("Database initialized successfully.")
        else:
            print(
                "Database already exists. Checking schema..."
            )
            if _table_exists(cursor, "users"):
                _add_column_if_not_exists(
                    conn,
                    cursor,
                    "users",
                    "full_name",
                    "TEXT NOT NULL DEFAULT 'Unknown User'",
                )
            else:
                print(
                    "Error: 'users' table is missing! Recreating..."
                )
                cursor.execute(
                    """
                    CREATE TABLE users (
                        id INTEGER PRIMARY KEY AUTOINCREMENT,
                        email TEXT UNIQUE NOT NULL,
                        password TEXT NOT NULL,
                        full_name TEXT NOT NULL,
                        created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
                    )
                    """
                )
                conn.commit()
                print("Created missing 'users' table.")
            
            if _table_exists(cursor, "glucose_readings"):
                _add_column_if_not_exists(
                    conn,
                    cursor,
                    "glucose_readings",
                    "categoria",
                    "TEXT DEFAULT 'No especificado'",
                )
                _add_cascade_delete_to_readings(
                    conn, cursor
                )
            else:
                print(
                    "Warning: 'glucose_readings' table is missing. Creating it now..."
                )
                cursor.execute(
                    """
                    CREATE TABLE glucose_readings (
                        id INTEGER PRIMARY KEY AUTOINCREMENT,
                        user_id INTEGER NOT NULL,
                        timestamp DATETIME NOT NULL,
                        value REAL NOT NULL,
                        notes TEXT,
                        categoria TEXT DEFAULT 'No especificado',
                        FOREIGN KEY (user_id) REFERENCES users (id) ON DELETE CASCADE
                    )
                    """
                )
                conn.commit()
                print("Created 'glucose_readings' table.")
            
            # Verificar y crear la tabla educational_suggestions si no existe
            if not _table_exists(cursor, "educational_suggestions"):
                print("Creating 'educational_suggestions' table...")
                cursor.execute(
                    """
                    CREATE TABLE educational_suggestions (
                        id INTEGER PRIMARY KEY AUTOINCREMENT,
                        min_value REAL NOT NULL,
                        max_value REAL NOT NULL,
                        suggestion TEXT NOT NULL,
                        category TEXT NOT NULL,
                        created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
                    )
                    """
                )
                
                # Insertar sugerencias iniciales
                initial_suggestions = [
                    (0, 54, "Tu nivel de glucosa está MUY BAJO. Busca atención médica inmediata y consume una fuente rápida de carbohidratos.", "MUY BAJO"),
                    (54, 70, "Tu nivel de glucosa está bajo. Considera consumir una fuente rápida de carbohidratos como jugo de frutas o caramelos.", "Bajo"),
                    (70, 131, "¡Excelente! Tu nivel de glucosa está en un rango saludable. Mantén tus hábitos actuales.", "Saludable"),
                    (131, 181, "Tu nivel de glucosa está elevado. Si es postprandial, monitorea. Si no, considera realizar actividad física moderada.", "Elevado"),
                    (181, 251, "Tu nivel de glucosa está alto. Revisa tu alimentación y considera consultar con tu médico.", "Alto"),
                    (251, 999, "Tu nivel de glucosa está MUY ALTO. Es importante que consultes con tu médico lo antes posible.", "Muy Alto")
                ]
                
                cursor.executemany(
                    "INSERT INTO educational_suggestions (min_value, max_value, suggestion, category) VALUES (?, ?, ?, ?)",
                    initial_suggestions
                )
                conn.commit()
                print("Created and populated 'educational_suggestions' table.")
            
            print("Database schema check complete.")
    except Exception as e:
        print(
            f"An error occurred during database initialization or schema check: {e}"
        )
        conn.rollback()
    finally:
        conn.close()


def add_user(
    email: str, password_hash: str, full_name: str
) -> bool:
    """Adds a new user to the database. Stores password hash as TEXT."""
    conn = get_db_connection()
    cursor = conn.cursor()
    try:
        cursor.execute(
            "INSERT INTO users (email, password, full_name) VALUES (?, ?, ?)",
            (email, password_hash, full_name),
        )
        conn.commit()
        print(
            f"User {email} ({full_name}) added successfully."
        )
        return True
    except sqlite3.IntegrityError:
        print(
            f"Database Integrity Error: Email '{email}' already exists."
        )
        return False
    except Exception as e:
        print(f"Database error adding user '{email}': {e}")
        conn.rollback()
        return False
    finally:
        conn.close()


def get_user(email: str) -> Optional[sqlite3.Row]:
    """Retrieves a user by email. Returns a sqlite3.Row object or None."""
    conn = get_db_connection()
    cursor = conn.cursor()
    try:
        cursor.execute(
            "SELECT id, email, password, full_name FROM users WHERE email = ?",
            (email,),
        )
        user = cursor.fetchone()
        return user
    except Exception as e:
        print(f"Database error getting user '{email}': {e}")
        return None
    finally:
        conn.close()


def add_glucose_reading(
    user_id: int,
    timestamp: str,
    value: float,
    categoria: str,
    notes: Optional[str] = None,
) -> bool:
    """Agrega una lectura de glucosa para un usuario específico, incluyendo su categoría."""
    conn = get_db_connection()
    cursor = conn.cursor()
    try:
        cursor.execute(
            "INSERT INTO glucose_readings (user_id, timestamp, value, categoria, notes) VALUES (?, ?, ?, ?, ?)",
            (user_id, timestamp, value, categoria, notes),
        )
        conn.commit()
        return True
    except Exception as e:
        print(f"Error adding glucose reading: {e}")
        return False
    finally:
        conn.close()


def get_glucose_readings(user_id: int) -> list[sqlite3.Row]:
    """Obtiene todas las lecturas de glucosa para un usuario específico, incluyendo categoría, ordenadas por marca de tiempo descendente."""
    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute(
        "SELECT id, timestamp, value, notes, categoria FROM glucose_readings WHERE user_id = ? ORDER BY timestamp DESC",
        (user_id,),
    )
    readings = cursor.fetchall()
    conn.close()
    return readings


def get_latest_glucose_reading(
    user_id: int,
) -> Optional[sqlite3.Row]:
    """Obtiene la lectura de glucosa más reciente para un usuario específico, incluyendo categoría."""
    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute(
        "SELECT id, timestamp, value, notes, categoria FROM glucose_readings WHERE user_id = ? ORDER BY timestamp DESC LIMIT 1",
        (user_id,),
    )
    reading = cursor.fetchone()
    conn.close()
    return reading


def delete_glucose_reading(
    reading_id: int, user_id: int
) -> bool:
    """Deletes a specific glucose reading belonging to a specific user."""
    conn = get_db_connection()
    cursor = conn.cursor()
    try:
        cursor.execute("PRAGMA foreign_keys = ON;")
        cursor.execute(
            "DELETE FROM glucose_readings WHERE id = ? AND user_id = ?",
            (reading_id, user_id),
        )
        conn.commit()
        deleted = cursor.rowcount > 0
        if not deleted:
            print(
                f"Reading ID {reading_id} not found for user {user_id} or already deleted."
            )
        else:
            print(
                f"Glucose reading {reading_id} for user {user_id} deleted."
            )
        return deleted
    except Exception as e:
        print(
            f"Database error deleting glucose reading {reading_id} for user {user_id}: {e}"
        )
        conn.rollback()
        return False
    finally:
        conn.close()


def delete_user(user_id: int) -> bool:
    """Deletes a user and their associated glucose readings (due to ON DELETE CASCADE)."""
    conn = get_db_connection()
    cursor = conn.cursor()
    try:
        cursor.execute("PRAGMA foreign_keys = ON;")
        cursor.execute(
            "DELETE FROM users WHERE id = ?", (user_id,)
        )
        conn.commit()
        deleted = cursor.rowcount > 0
        if not deleted:
            print(
                f"User ID {user_id} not found for deletion."
            )
        else:
            print(
                f"User ID {user_id} and associated data deleted successfully."
            )
        return deleted
    except Exception as e:
        print(
            f"Database error deleting user {user_id}: {e}"
        )
        conn.rollback()
        return False
    finally:
        conn.close()