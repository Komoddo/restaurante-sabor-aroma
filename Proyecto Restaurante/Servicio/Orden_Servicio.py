from base_datos.conexion_db import Conexion
from Modelo.Orden import Orden
from Modelo.Mesa import Mesa
from Servicio.OrdenDetalle_Servicio import OrdenDetalleServicio
from Principal import LISTA_ORDENES

class OrdenServicio:
    def __init__(self):
        self.ordenes = []
        self.f_ordenes = []

    def agregar_orden_lista(self, orden:Orden):
        LISTA_ORDENES.append(orden)

    def crear_orden_bd(self, o: Orden):
        try:
            conn = Conexion()
            cursor = conn.conectar()
            cursor.execute("""
                INSERT INTO ordenes (id_mesa, id_empleado, id_cliente, fecha_hora, nro_personas, estado, nota, total_parcial)
                VALUES (?, ?, ?, ?, ?, ?, ?, ?)""",
                (o.id_mesa, o.id_empleado, o.id_cliente, o.fecha_hora, o.nro_personas, o.estado, o.nota, o.total))

            conn.commit()
            return cursor.lastrowid
        except Exception as e:
            print("Error al crear orden:", e)
        finally:
            conn.cerrar()

    def actualizar_total_orden_bd(self, o: Orden):
        try:
            conexion = Conexion()
            cursor = conexion.conectar()

            cursor.execute('''UPDATE ordenes SET total_parcial = ? WHERE id_orden = ? ''', (o.total ,o.id_orden))
            conexion.conn.commit()
            return cursor.rowcount

        except Exception as e:
            print("Error al obtener orden:", e)

    def actualizar_orden_bd(self, o: Orden):
        try:
            conexion = Conexion()
            cursor = conexion.conectar()

            cursor.execute('''UPDATE ordenes SET
                           id_mesa = ?,
                           nro_personas = ? 
                           WHERE id_orden = ? ''', (o.id_mesa, o.nro_personas ,o.id_orden))
            conexion.conn.commit()
            return cursor.rowcount

        except Exception as e:
            print("Error al obtener orden:", e)

    def obtener_por_id(self, id_orden):
        try:
            conexion = Conexion()
            cursor = conexion.conectar()

            sql = "SELECT * FROM ordenes WHERE id_orden = ?"
            cursor.execute(sql, (id_orden,))
            row = cursor.fetchone()

            if row:
                return Orden(*row)
            return None

        except Exception as e:
            print("Error al obtener orden:", e)

    def obtener_orden_pendiente_por_id(self, id_orden:int)->Orden:
        orden = None
        if LISTA_ORDENES:
            orden = next((o for o in LISTA_ORDENES if o.id_orden==id_orden and o.estado.lower()=="pendiente"),None)
        if orden:
            return orden
        return None

    def obtener_ordenes_bd(self):
        try:
            LISTA_ORDENES.clear()
            ods = OrdenDetalleServicio()
            conn = Conexion()
            cursor = conn.conectar()
            cursor.execute("SELECT * FROM ordenes")
            rows = cursor.fetchall()

            # return [Orden(*row) for row in rows]
            LISTA_ORDENES.extend([Orden(id_orden=row[0], id_mesa=row[1], id_empleado=row[2], 
                                     id_cliente=row[3], fecha_hora=row[4], nro_personas=row[5],
                                     estado=row[6], nota=row[7], total=row[8]) for row in rows])
            if LISTA_ORDENES:
                for orden in LISTA_ORDENES:
                    detalles = ods.obtener_detalles_por_orden(orden.id_orden)
                    if detalles:
                        for detalle in detalles:
                            orden.agregar_detalle(detalle)
        except Exception as e:
            print("Error al listar ordenes:", e)

    def obtener_ordenes_pendientes(self):
        if LISTA_ORDENES:
            pendientes = [o for o in LISTA_ORDENES if o.estado.lower() == "pendiente"]
            return pendientes
        return None

    def actualizar_estado_pedido_bd(self, id_orden, nuevo_estado):
        try:
            conn = conn()
            cursor = conn.conectar()

            sql = "UPDATE ordenes SET estado = ? WHERE id_orden = ?"
            cursor.execute(sql, (nuevo_estado, id_orden))

            conn.conn.commit()
            return cursor.rowcount
        except Exception as e:
            print("Error al actualizar estado:", e)

    def validar_orden_completa(self, orden: Orden):
        if not orden.id_mesa or not orden.id_empleado or not orden.id_cliente:
            return False
        return True