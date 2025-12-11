from typing import List, Optional       # Tipos para anotaciones
from base_datos.conexion_db import Conexion          # Manejo de conexión a BD
from Modelo.Empleado import Empleado                 # Modelo Empleado
from Principal import LISTA_EMPLEADOS                # Lista global de empleados en memoria

"""Servicio encargado de manejar todas las operaciones sobre empleados."""
class EmpleadoServicio:
    def __init__(self):
        self.empleados = []           # Lista interna de empleados
        self.f_Empleado = []          # Lista filtrada temporal

    def agregar_empleado_bd(self, e: Empleado):
        """Agrega un empleado a la base de datos y devuelve su ID."""
        conn = Conexion()             # Conexión a la BD
        cursor = conn.conectar()      # Cursor para ejecutar SQL

        try:
            cursor.execute("""
            INSERT INTO Empleados (nombre, apellido, dni, cargo, telefono, estado) 
            VALUES (?, ?, ?, ?, ?, ?)""", 
            (e.nombre, e.apellido, e.dni, e.cargo, e.telefono, e.estado))             # Inserta el empleado

            conn.commit()                      # Guarda los cambios en BD
            return cursor.lastrowid

        except Exception as e:
            return []                           # Retorna ID del empleado agregado
        finally:
            conn.cerrar()                       # Cierra conexión

    def obtener_Empleados_bd(self):
        """Obtiene todos los empleados de la base de datos y actualiza LISTA_EMPLEADOS."""
        conn = Conexion()                       # Conexión a la BD
        cursor = conn.conectar()                # Cursor para ejecutar consultas    

        try:
            LISTA_EMPLEADOS.clear()             # Limpia la lista antes de cargar los dato
            cursor.execute("SELECT * FROM Empleados")    # Consulta todos los empleados
            rows = cursor.fetchall()                     # Obtiene todas las filas
            return LISTA_EMPLEADOS.extend([Empleado(id=row[0], nombre=row[1], apellido=row[2], 
                                                    dni=row[3], cargo=row[4], telefono=row[5], 
                                                    estado=row[6]) for row in rows])             # Convierte cada fila en objeto Empleado y lo agrega
        except Exception as e:
            return []                 # Retorna lista vacía si hay error
        finally:
            conn.cerrar()             # Cierra conexión

    def validar_Empleado(self, nombre: str, apellido: str) -> Empleado:
        """Busca un producto por su nombre y apellido en la lista de Empleado."""
        Empleado = next((e for e in LISTA_EMPLEADOS if nombre==e.nombre.strip().lower() and apellido==e.apellido.strip().lower()), None)
        return Empleado             # Retorna el empleado encontrado o None

    def obtener_Empleado_por_dni(self, dni: str) -> Empleado:
        """Busca un producto por su nombre y apellido en la lista de Empleado."""
        empleado = next((e for e in LISTA_EMPLEADOS if dni.strip()==e.dni), None)
        return empleado             # Retorna el empleado encontrado o None
  
    def actualizar_Empleado_bd(self, e: Empleado):
        """Actualiza un empleado en la base de datos."""
        conn = Conexion()          # Conexión a BD                  
        cursor = conn.conectar()   # Cursor para ejecutar consulta

        try:
            cursor.execute("""
            UPDATE Empleados 
            SET nombre=?, apellido=?, cargo=?, telefono=?, estado=? 
            WHERE id=?""",
            (e.nombre, e.apellido, e.cargo, e.telefono, e.estado, e.id))      # Actualiza empleado

            conn.commit()                  # Guarda cambios en BD
            return cursor.rowcount         # Retorna filas afectadas

        except Exception as ex:
            return 0                       # Retorna 0 si ocurre error
        finally:
            conn.cerrar()

    def obtener_Empleado_por_id_bd(self, id: int) -> Optional[Empleado]:
        """Obtiene un Empleado por su ID."""
        conn = Conexion()
        cursor = conn.conectar()               # Cursor para ejecutar consulta

        try:
            cursor.execute("SELECT * FROM Empleados WHERE id=?", (id,))         # Consulta por ID
            row = cursor.fetchone()       # Obtiene la fila
            if row:
                return Empleado(id=row[0], nombre=row[1], apellido=row[2], dni=row[3], cargo=row[4], telefono=row[4], estado=row[5])    # Crea objeto Empleado
            return None            # Retorna None si no encuentra
        except Exception as ex:
            return None
        finally:
            conn.cerrar()            # Cierra conexión

    def obtener_empleados_por_cargo(self):
        """Muestra una lista completa de empleados."""
        cargos = {} # Diccionario vacío
        activos = [activo for activo in LISTA_EMPLEADOS if activo.estado.lower()=="activo"]
        if activos:
            for item in activos:
                cargo = item.cargo       # Obtiene cargo del empleado
                if cargo not in cargos:
                    cargos[cargo] = []   # Crea lista si no existe
                cargos[cargo].append(item)    # Agrega empleado
            if(cargos):                      # Retorna diccionario de cargos
                return cargos
        return None                      # Retorna None si no hay empleados

    def obtener_empleados_por_cargo_estado(self):
        """Muestra una lista completa de empleados."""
        estructura = {}
        [estructura.setdefault(e.cargo, {}).setdefault(e.estado, []).append(e) for e in LISTA_EMPLEADOS]
        return estructura                 # Retorna diccionario estructurado

    def obtener_empleado_por_id(self, id_empleado: int) -> Empleado:
        """Busca un empleado por su ID en la lista de empleados."""
        empleado = next((e for e in LISTA_EMPLEADOS if (e.id==id_empleado and e.estado.lower()=="activo")),None)
        if empleado:                
            return empleado                         # Retorna empleado activo o None
        return empleado 
    
    def obtener_lista_empleados(self) -> List[Empleado]:
        """Devuelve la lista completa de empleados."""
        return LISTA_EMPLEADOS
    
    def crear_cargos(self):
        """Crea un diccionario de cargos con números consecutivos."""
        lista_cargos = sorted({p.cargo for p in LISTA_EMPLEADOS})          # Obtiene cargos únicos
        cargos = {i: c for i, c in enumerate(lista_cargos, start=1)}       # Asigna números consecutivos
        return cargos                                                      # Retorna diccionario {1: 'Gerente', 2: 'Cajero', ...}
    
    def crear_estados(self):
        """Crea un diccionario de estados con números consecutivos."""
        lista_estados = sorted({p.estado for p in LISTA_EMPLEADOS})
        estados = {i: c for i, c in enumerate(lista_estados, start=1)}
        return estados
