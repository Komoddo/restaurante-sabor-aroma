import sqlite3

class Conexion:
    def __init__(self):
        self.conn = sqlite3.connect("base_datos/restaurante.db")
        self.conn.row_factory = sqlite3.Row  # Permite acceder por nombre a columnas

    def conectar(self):
        return self.conn.cursor()
    
    def commit(self):
        self.conn.commit()

    def cerrar(self):
        self.conn.close()
 
