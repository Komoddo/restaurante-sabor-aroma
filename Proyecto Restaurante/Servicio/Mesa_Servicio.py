from typing import List, Tuple                 # Tipos para anotaciones
from base_datos.conexion_db import Conexion    # Manejo de conexión a BD
from Modelo.Mesa import Mesa                   # Modelo Mesa
from Principal import LISTA_MESAS              # Lista global de mesas en memoria

class MesaServicio:
    # def __init__(self):

# Servicio para manejar todas las operaciones sobre mesas
    def agregar_mesa(self, mesa: Mesa):
        conn = Conexion()                 # Conexión a la BD
        cursor = conn.conectar()          # Cursor para ejecutar SQL
        try:
            cursor.execute("""
            INSERT INTO mesas (numero, capacidad, estado) VALUES (?, ?, ?)
            """, (mesa.numero, mesa.capacidad, mesa.estado))                # Inserta nueva mesa
            conn.commit()                                                    # Guarda los cambios en BD
        except Exception as ex:
            return []                  # Retorna lista vacía si hay error
        finally:
            conn.cerrar()              # Cierra la conexión

    def obtener_mesas_bd(self):
        LISTA_MESAS.clear()            # Limpia la lista antes de cargar datos
        
        conn = Conexion()
        cursor = conn.conectar()        # Cursor para ejecutar consul
        
        try:
            cursor.execute("SELECT * FROM mesas")          # Consulta todas las mesas
            rows = cursor.fetchall()                       # Obtiene todas las filas
            if not rows: 
                return []                                   # Retorna lista vacía si no hay mesas
            
            # Convierte cada fila en objeto Mesa y lo agrega a la lista global
            return LISTA_MESAS.extend([Mesa(id=r[0], numero=r[1], 
                                            capacidad=r[2], estado=r[3]) for r in rows])
        except Exception as e:
            return []                       # Retorna lista vacía si hay error
        finally:
            conn.cerrar()                   # Cierra la conexión

    def obtener_mesas_lst(self):
        if LISTA_MESAS:
            return LISTA_MESAS               # Retorna lista de mesas si hay dato
        return None                          # Retorna None si lista vacía  

    def obtener_mesa_por_id(self, id_mesa) -> Mesa:
        if LISTA_MESAS:
             # Busca mesa en la lista por ID
            mesa = next((m for m in LISTA_MESAS if m.id_mesa == id_mesa),None)
        return mesa             # Retorna la mesa encontrada o None

    def actualizar_estado_mesa_bd(self, mesa_id, nuevo_estado):
        conn = Conexion()
        cursor = conn.conectar()       # Cursor para ejecutar actualización
        try:
            cursor.execute("""
            UPDATE mesas SET estado=? WHERE id=?
            """, (nuevo_estado, mesa_id))               # Actualiza estado de la mesa
            conn.commit()                               # Guarda cambios en BD
        except Exception as ex:
            return []                                    # Retorna lista vacía si h
        finally:
            conn.cerrar()

    def obtener_mesas_disponibles(self, num_personas: int) -> List[Mesa]:
        mesas_disponibles = []
        if LISTA_MESAS:
            # Filtra mesas disponibles con capacidad suficiente
            mesas_disponibles = [m for m in LISTA_MESAS if m.estado.lower()=="disponible" and m.capacidad>=num_personas]

        # Ordena por número de mesa antes de retornar
        if mesas_disponibles:
            return sorted(mesas_disponibles, key=lambda x: int(x.numero))
        return None                    # Retorna None si no hay mes
        
    def obtener_mesa_disponible_por_id(self, mesa_id: int) -> Mesa:
        # Busca mesa específica por ID y que esté disponible
        for m in LISTA_MESAS:
            if m.id == mesa_id and m.estado == "Disponible":
                return m
        return None                      # Retorna None si no está disponible o no existe