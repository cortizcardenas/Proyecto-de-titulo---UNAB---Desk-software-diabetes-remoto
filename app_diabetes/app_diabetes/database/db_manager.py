"""
Módulo para manejar la base de datos local SQLite.
"""

import sqlite3
from pathlib import Path

class DatabaseManager:
    _instance = None
    _initialized = False

    def __new__(cls):
        if cls._instance is None:
            cls._instance = super(DatabaseManager, cls).__new__(cls)
        return cls._instance

    def __init__(self):
        if not self._initialized:
            # Asegurarse de que el directorio existe
            db_dir = Path("app_diabetes/database")
            db_dir.mkdir(exist_ok=True)
            
            self.db_path = db_dir / "diabeduca.db"
            self._initialized = True

    def get_connection(self):
        """Obtiene una nueva conexión a la base de datos."""
        try:
            conn = sqlite3.connect(str(self.db_path))
            cursor = conn.cursor()
            return conn, cursor
        except sqlite3.Error as e:
            print(f"Error al conectar con la base de datos: {e}")
            return None, None

    def create_tables(self):
        """Crea las tablas necesarias si no existen."""
        conn, cursor = self.get_connection()
        if not conn or not cursor:
            return

        try:
            # Tabla de usuarios
            cursor.execute('''
                CREATE TABLE IF NOT EXISTS usuarios (
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    nombre TEXT NOT NULL,
                    correo TEXT UNIQUE NOT NULL,
                    fecha_registro TIMESTAMP DEFAULT CURRENT_TIMESTAMP
                )
            ''')

            # Tabla de registros de glicemia
            cursor.execute('''
                CREATE TABLE IF NOT EXISTS registros_glicemia (
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    usuario_id INTEGER,
                    valor INTEGER NOT NULL,
                    fecha TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
                    FOREIGN KEY (usuario_id) REFERENCES usuarios (id)
                )
            ''')

            conn.commit()
        except sqlite3.Error as e:
            print(f"Error al crear las tablas: {e}")
        finally:
            conn.close()

    def registrar_usuario(self, nombre: str, correo: str) -> bool:
        """
        Registra un nuevo usuario en la base de datos.
        
        Args:
            nombre (str): Nombre del usuario
            correo (str): Correo electrónico del usuario
            
        Returns:
            bool: True si el registro fue exitoso, False en caso contrario
        """
        conn, cursor = self.get_connection()
        if not conn or not cursor:
            return False

        try:
            cursor.execute(
                "INSERT INTO usuarios (nombre, correo) VALUES (?, ?)",
                (nombre, correo)
            )
            conn.commit()
            return True
        except sqlite3.IntegrityError:
            print("El correo electrónico ya está registrado")
            return False
        except sqlite3.Error as e:
            print(f"Error al registrar usuario: {e}")
            return False
        finally:
            conn.close()

    def obtener_usuario(self, correo: str) -> tuple:
        """
        Obtiene un usuario por su correo electrónico.
        
        Args:
            correo (str): Correo electrónico del usuario
            
        Returns:
            tuple: Datos del usuario o None si no existe
        """
        conn, cursor = self.get_connection()
        if not conn or not cursor:
            return None

        try:
            cursor.execute(
                "SELECT * FROM usuarios WHERE correo = ?",
                (correo,)
            )
            return cursor.fetchone()
        except sqlite3.Error as e:
            print(f"Error al obtener usuario: {e}")
            return None
        finally:
            conn.close()

    def registrar_glicemia(self, usuario_id: int, valor: int) -> bool:
        """
        Registra un nuevo valor de glicemia para un usuario.
        
        Args:
            usuario_id (int): ID del usuario
            valor (int): Valor de glicemia
            
        Returns:
            bool: True si el registro fue exitoso, False en caso contrario
        """
        conn, cursor = self.get_connection()
        if not conn or not cursor:
            return False

        try:
            cursor.execute(
                "INSERT INTO registros_glicemia (usuario_id, valor) VALUES (?, ?)",
                (usuario_id, valor)
            )
            conn.commit()
            return True
        except sqlite3.Error as e:
            print(f"Error al registrar glicemia: {e}")
            return False
        finally:
            conn.close()

    def obtener_registros_glicemia(self, usuario_id: int) -> list:
        """
        Obtiene todos los registros de glicemia de un usuario.
        
        Args:
            usuario_id (int): ID del usuario
            
        Returns:
            list: Lista de registros de glicemia
        """
        conn, cursor = self.get_connection()
        if not conn or not cursor:
            return []

        try:
            cursor.execute(
                "SELECT * FROM registros_glicemia WHERE usuario_id = ? ORDER BY fecha DESC",
                (usuario_id,)
            )
            return cursor.fetchall()
        except sqlite3.Error as e:
            print(f"Error al obtener registros de glicemia: {e}")
            return []
        finally:
            conn.close() 