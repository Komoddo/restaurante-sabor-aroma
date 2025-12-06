
from typing import List, Tuple
from base_datos.conexion_db import Conexion
from Modelo.Mesa import Mesa
from Principal import LISTA_MESAS

class MesaServicio:
    # def __init__(self):

    def agregar_mesa(self, mesa: Mesa):
        conn = Conexion()
        cursor = conn.conectar()
        try:
            cursor.execute("""
            INSERT INTO mesas (numero, capacidad, estado) VALUES (?, ?, ?)
            """, (mesa.numero, mesa.capacidad, mesa.estado))
            conn.commit()
        except Exception as ex:
            return []
        finally:
            conn.cerrar()

    def obtener_mesas_bd(self):
        LISTA_MESAS.clear()
        
        conn = Conexion()
        cursor = conn.conectar()
        
        try:
            cursor.execute("SELECT * FROM mesas")
            rows = cursor.fetchall()
            if not rows:
                return []
            
            return LISTA_MESAS.extend([Mesa(id=r[0], numero=r[1], 
                                            capacidad=r[2], estado=r[3]) for r in rows])
        except Exception as e:
            return []
        finally:
            conn.cerrar()

    def obtener_mesas_lst(self):
        if LISTA_MESAS:
            return LISTA_MESAS
        return None  

    def obtener_mesa_por_id(self, id_mesa) -> Mesa:
        if LISTA_MESAS:
            mesa = next((m for m in LISTA_MESAS if m.id_mesa == id_mesa),None)
        return mesa

    def actualizar_estado(self, mesa_id, nuevo_estado):
        conn = Conexion()
        cursor = conn.conectar()
        try:
            cursor.execute("""
            UPDATE mesas SET estado=? WHERE id=?
            """, (nuevo_estado, mesa_id))
            conn.commit()
            return cursor.rowcount
        except Exception as ex:
            return []
        finally:
            conn.cerrar()

    def obtener_mesas_disponibles(self, num_personas: int) -> List[Mesa]:
        mesas_disponibles = []
        if LISTA_MESAS:
            mesas_disponibles = [m for m in LISTA_MESAS if m.estado.lower()=="disponible" and m.capacidad>=num_personas]

        if mesas_disponibles:
            return sorted(mesas_disponibles, key=lambda x: int(x.numero))
        return None
        
    def obtener_mesa_disponible_por_id(self, mesa_id: int) -> Mesa:
        for m in LISTA_MESAS:
            if m.id == mesa_id and m.estado == "Disponible":
                return m
        return None