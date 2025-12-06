from typing import List, Dict, Tuple, Optional
from base_datos.conexion_db import Conexion
from Modelo.Empleado import Empleado
from Principal import LISTA_EMPLEADOS

class EmpleadoServicio:
    def __init__(self):
        self.empleados = []
        self.f_Empleado = []

    def agregar_Empleado_bd(self, e: Empleado):
        
        conn = Conexion()
        cursor = conn.conectar()

        try:
            cursor.execute("""
            INSERT INTO Empleados (nombre, apellido, dni, cargo, telefono, estado) 
            VALUES (?, ?, ?, ?, ?, ?)""", 
            (e.nombre, e.apellido, e.dni, e.cargo, e.telefono, e.estado))

            conn.commit()
            return cursor.lastrowid

        except Exception as e:
            return []
        finally:
            conn.cerrar()

    def obtener_Empleados_bd(self):
        conn = Conexion()
        cursor = conn.conectar()

        try:
            LISTA_EMPLEADOS.clear()
            cursor.execute("SELECT * FROM Empleados")
            rows = cursor.fetchall()
            return LISTA_EMPLEADOS.extend([Empleado(id=row[0], nombre=row[1], apellido=row[2], 
                                                    dni=row[3], cargo=row[4], telefono=row[5], 
                                                    estado=row[6]) for row in rows])
        except Exception as e:
            return []
        finally:
            conn.cerrar()

    def validar_Empleado(self, nombre: str, apellido: str) -> Empleado:
        """Busca un producto por su nombre y apellido en la lista de Empleado."""
        Empleado = next((e for e in LISTA_EMPLEADOS if nombre==e.nombre.strip().lower() and apellido==e.apellido.strip().lower()), None)
        return Empleado

    def obtener_Empleado_por_dni(self, dni: str) -> Empleado:
        """Busca un producto por su nombre y apellido en la lista de Empleado."""
        empleado = next((e for e in LISTA_EMPLEADOS if dni.strip()==e.dni), None)
        return empleado
    
    # def Buscar_Empleado(self, nombre: str):
    #     """Busca un producto por su nombre y apellido en la lista de Empleado."""
    #     self.f_Empleado.clear()
    #     if " " in nombre:
    #         n_a = nombre.split()
    #     self.f_Empleado = [e for e in self.Empleados if (n_a[0].strip() in e.nombre and n_a.strip() in e.apellido)]

    def actualizar_Empleado_bd(self, e: Empleado):
        conn = Conexion()
        cursor = conn.conectar()

        try:
            cursor.execute("""
            UPDATE Empleados 
            SET nombre=?, apellido=?, cargo=?, telefono=?, estado=? 
            WHERE id=?""",
            (e.nombre, e.apellido, e.cargo, e.telefono, e.estado, e.id))

            conn.commit()
            return cursor.rowcount

        except Exception as ex:
            return 0
        finally:
            conn.cerrar()

    def obtener_Empleado_por_id_bd(self, id: int) -> Optional[Empleado]:
        """Obtiene un Empleado por su ID."""
        conn = Conexion()
        cursor = conn.conectar()

        try:
            cursor.execute("SELECT * FROM Empleados WHERE id=?", (id,))
            row = cursor.fetchone()
            if row:
                return Empleado(id=row[0], nombre=row[1], apellido=row[2], dni=row[3], cargo=row[4], telefono=row[4], estado=row[5])
            return None
        except Exception as ex:
            return None
        finally:
            conn.cerrar()

    def obtener_empleados_por_cargo(self):
        """Muestra una lista completa de empleados."""
        cargos = {}
        for item in LISTA_EMPLEADOS:
            cargo = item.cargo
            if cargo not in cargos:
                cargos[cargo] = []
            cargos[cargo].append(item)
        if(cargos):
            return cargos
        return None

    def obtener_empleados_por_cargo_estado(self):
        estructura = {}
        [estructura.setdefault(e.cargo, {}).setdefault(e.estado, []).append(e) for e in LISTA_EMPLEADOS]
        return estructura

    def obtener_empleado_por_id(self, id_empleado: int) -> Empleado:
        empleado = next((e for e in LISTA_EMPLEADOS if (e.id==id_empleado and e.estado.lower()=="activo")),None)
        if empleado:
            return empleado
        return empleado
    
    def obtener_lista_empleados(self) -> List[Empleado]:
        """Devuelve la lista completa de empleados."""
        return LISTA_EMPLEADOS
    
    def crear_cargos(self):
        lista_cargos = sorted({p.cargo for p in LISTA_EMPLEADOS})
        cargos = {i: c for i, c in enumerate(lista_cargos, start=1)}
        return cargos
    
    def crear_estados(self):
        lista_estados = sorted({p.estado for p in LISTA_EMPLEADOS})
        estados = {i: c for i, c in enumerate(lista_estados, start=1)}
        return estados