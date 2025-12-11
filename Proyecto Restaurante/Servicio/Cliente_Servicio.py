from typing import List, Optional
from base_datos.conexion_db import Conexion         # Importa la clase para manejar la conexión a la base de datos
from Modelo.Cliente import Cliente                  # Importa la clase Cliente para representar objetos cliente

from Principal import LISTA_CLIENTES                # Lista global que almacena temporalmente los clientes


"""Clase que gestiona todas las operaciones relacionadas con clientes en la base de datos."""
class ClienteServicio:
    # def __init__(self):

    #Agrega un cliente a la base de datos y devuelve su ID.
    def agregar_cliente_bd(self, c: Cliente):
        
        conn = Conexion()   # Crea una instancia de conexión a la BD
        cursor = conn.conectar()  # Obtiene el cursor para ejecutar consultas

        try:
            # Inserta un nuevo cliente en la tabla 'clientes'
            cursor.execute("""
            INSERT INTO clientes (nombre, apellido, email, telefono) 
            VALUES (?, ?, ?, ?)""", 
            (c.nombre, c.apellido, c.email, c.telefono))

            conn.commit()                  # Guarda los cambios en la BD
            return cursor.lastrowid        # Retorna el ID del cliente agregado
        except Exception as e:
            return []                      # Retorna lista vacía en caso de error
        finally:
            conn.cerrar()                  # Cierra la conexión   

    def obtener_clientes_bd(self):
        """Obtiene todos los clientes de la base de datos y actualiza LISTA_CLIENTES"""
        LISTA_CLIENTES.clear()             # Limpia la lista antes de cargar
        conn = Conexion()
        cursor = conn.conectar()

        try:
            cursor.execute("SELECT * FROM clientes")     # Consulta todos los clientes
            rows = cursor.fetchall()
            LISTA_CLIENTES.clear()
            # Crea objetos Cliente por cada fila obtenida y los agrega a LISTA_CLIENTES
            return LISTA_CLIENTES.extend([Cliente(id_cliente=row[0], nombre=row[1], 
                                     apellido=row[2], email=row[3], telefono=row[4]) for row in rows])
        except Exception as ex:
            return []
        finally:
            conn.cerrar()

    def obtener_cliente_por_id(self, id_cliente) -> Cliente:
        """Devuelve un cliente de LISTA_CLIENTES según su ID."""
        if LISTA_CLIENTES:
            cliente = next((m for m in LISTA_CLIENTES if m.id_cliente == id_cliente),None)
        return cliente

    def validar_cliente(self, nombre: str, apellido: str) -> Cliente:
        """Busca un producto por su nombre y apellido en la lista de cliente."""
        if LISTA_CLIENTES:
            cliente = next((c for c in LISTA_CLIENTES if nombre.strip().lower()==c.nombre.strip().lower() and apellido.strip().lower()==c.apellido.strip().lower()), None)
            if cliente:
                return cliente
        return None
    
    def Buscar_clientes(self, nombre: str, apellido: str):
        """Busca un producto por su nombre y apellido en la lista de cliente."""
        f_clientes = [c for c in LISTA_CLIENTES if (nombre.strip().lower() in c.nombre and apellido.strip().lower() in c.apellido)]
        if f_clientes:
            return f_clientes
        return None
    
    def actualizar_cliente_bd(self, c: Cliente):
        """Actualiza un cliente en la base de datos."""
        conn = Conexion()
        cursor = conn.conectar()

        try:
            cursor.execute("""
            UPDATE clientes 
            SET nombre=?, apellido=?, email=?, telefono=? 
            WHERE id=?""",
            (c.nombre, c.apellido, c.email, c.telefono, c.id_cliente))

            conn.commit()
            return cursor.rowcount      # Retorna número de filas afectadas

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
        return LISTA_CLIENTES                                 # Lista que contiene todos los clientes actualmente cargado