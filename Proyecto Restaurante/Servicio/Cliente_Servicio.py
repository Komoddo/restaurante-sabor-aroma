from typing import List, Dict, Tuple, Optional
from base_datos.conexion_db import Conexion
from Modelo.Cliente import Cliente

from Principal import LISTA_CLIENTES

class ClienteServicio:
    # def __init__(self):

    def agregar_cliente_bd(self, c: Cliente):
        
        conn = Conexion()
        cursor = conn.conectar()

        try:
            cursor.execute("""
            INSERT INTO clientes (nombre, apellido, email, telefono) 
            VALUES (?, ?, ?, ?)""", 
            (c.nombre, c.apellido, c.email, c.telefono))

            conn.commit()
            return cursor.lastrowid

        except Exception as e:
            return []
        finally:
            conn.cerrar()

    def obtener_clientes_bd(self):
        LISTA_CLIENTES.clear()
        conn = Conexion()
        cursor = conn.conectar()

        try:
            cursor.execute("SELECT * FROM clientes")
            rows = cursor.fetchall()
            LISTA_CLIENTES.clear()
            return LISTA_CLIENTES.extend([Cliente(id_cliente=row[0], nombre=row[1], 
                                     apellido=row[2], email=row[3], telefono=row[4]) for row in rows])
        except Exception as ex:
            return []
        finally:
            conn.cerrar()

    def obtener_cliente_por_id(self, id_cliente) -> Cliente:
        if LISTA_CLIENTES:
            cliente = next((m for m in LISTA_CLIENTES if m.id_cliente == id_cliente),None)
        return cliente

    def validar_cliente(self, nombre: str, apellido: str) -> Cliente:
        """Busca un producto por su nombre y apellido en la lista de cliente."""
        if LISTA_CLIENTES:
            cliente = next((c for c in LISTA_CLIENTES if nombre==c.nombre.strip().lower() and apellido==c.apellido.strip().lower()), None)
            if cliente:
                return cliente
        return None
    
    def Buscar_clientes(self, nombre: str, apellido: str):
        """Busca un producto por su nombre y apellido en la lista de cliente."""
        f_clientes = [c for c in LISTA_CLIENTES if (nombre.strip() in c.nombre and apellido.strip() in c.apellido)]
        if f_clientes:
            return f_clientes
        return None
    
    def actualizar_cliente(self, c: Cliente):
        conn = Conexion()
        cursor = conn.conectar()

        try:
            cursor.execute("""
            UPDATE clientes 
            SET nombre=?, apellido=?, email=?, telefono=? 
            WHERE id=?""",
            (c.nombre, c.apellido, c.email, c.telefono, c.id_cliente))

            conn.commit()
            return cursor.rowcount

        except Exception as e:
            return 0
        finally:
            conn.cerrar()

    def obtener_cliente_por_id_bd(self, id: int) -> Optional[Cliente]:
        """Obtiene un cliente por su ID."""
        conn = Conexion()
        cursor = conn.conectar()

        try:
            cursor.execute("SELECT * FROM clientes WHERE id=?", (id,))
            row = cursor.fetchone()
            if row:
                return Cliente(id=row[0], nombre=row[1], apellido=row[2], email=row[3], telefono=row[4])
            return None
        except Exception as e:
            return None
        finally:
            conn.cerrar()

    def obtener_lista_clientes(self) -> List[Cliente]:
        """Devuelve la lista completa de clientes."""
        return LISTA_CLIENTES