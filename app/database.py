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
                "\n                CREATE TABLE users (\n                    id INTEGER PRIMARY KEY AUTOINCREMENT,\n                    email TEXT UNIQUE NOT NULL,\n                    password TEXT NOT NULL,\n                    full_name TEXT NOT NULL,\n                    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP\n                )\n                "
            )
            print("Created 'users' table.")
            cursor.execute(
                "\n                CREATE TABLE glucose_readings (\n                    id INTEGER PRIMARY KEY AUTOINCREMENT,\n                    user_id INTEGER NOT NULL,\n                    timestamp DATETIME NOT NULL,\n                    value REAL NOT NULL,\n                    notes TEXT,\n                    categoria TEXT DEFAULT 'No especificado', -- Columna categoria agregada\n                    FOREIGN KEY (user_id) REFERENCES users (id) ON DELETE CASCADE\n                )\n                "
            )
            print(
                "Created 'glucose_readings' table with categoria and ON DELETE CASCADE."
            )
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
                    "\n                    CREATE TABLE users (\n                        id INTEGER PRIMARY KEY AUTOINCREMENT,\n                        email TEXT UNIQUE NOT NULL,\n                        password TEXT NOT NULL,\n                        full_name TEXT NOT NULL,\n                        created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP\n                    )\n                    "
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
                    "\n                    CREATE TABLE glucose_readings (\n                        id INTEGER PRIMARY KEY AUTOINCREMENT,\n                        user_id INTEGER NOT NULL,\n                        timestamp DATETIME NOT NULL,\n                        value REAL NOT NULL,\n                        notes TEXT,\n                        categoria TEXT DEFAULT 'No especificado', -- Categoria agregada\n                        FOREIGN KEY (user_id) REFERENCES users (id) ON DELETE CASCADE\n                    )\n                    "
                )
                conn.commit()
                print("Created 'glucose_readings' table.")
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