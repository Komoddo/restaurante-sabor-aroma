from Modelo.OrdenDetalle import OrdenDetalle
from base_datos.conexion_db import Conexion

class OrdenDetalleServicio:
    def __init__(self):
        self.detalles = []

    def quitar_detalle_por_id(self, id: int):
        """Quita un detalle de la lista de detalles."""
        producto = next((p for p in self.detalles if p.id_producto==id), None)
        if(producto):
            self.detalles.remove(producto)

    def validar_detalle_existente(self, id_producto: int) -> bool:
        """Valida la existencia de un detalle en la lista de detalles."""
        detalle = next((d for d in self.detalles if d.id_producto==id_producto), None)
        return True if detalle else False

    def agregar_detalle(self, ordendetalle: OrdenDetalle):
        """Agrega un detalle a la lista de detalles."""
        ordendetalle.actualizar_cantidad(ordendetalle.cantidad)
        self.detalles.append(ordendetalle)

    def actualizar_cantidad_detalle(self, id_producto: int, nueva_cantidad: int):
        """Actualiza la cantidad de un detalle en la lista de detalles."""
        detalle = next((d for d in self.detalles if d.id_producto==id_producto), None)
        if detalle:
            detalle.actualizar_cantidad(nueva_cantidad)
            return True
        return False

    def obtener_lista_detalles(self):
        return self.detalles


    def agregar_detalles_bd(self, orden_detalles: list):
        """Agrega detalles de orden a la base de datos."""
        if orden_detalles:
            try:
                conexion = Conexion()
                cursor = conexion.conectar()
        
                for detalle in orden_detalles:
                    sql = """ INSERT INTO detalle_orden(id_orden, id_producto, cantidad, precio_unitario, subtotal, nota)
                        VALUES (?, ?, ?, ?, ?, ?) """

                    cursor.execute(sql, (
                        detalle.id_orden,
                        detalle.id_producto,
                        detalle.cantidad,
                        detalle.precio_unitario,
                        detalle.subtotal,
                        detalle.nota
                    ))

                conexion.conn.commit()
                # return cursor.lastrowid
            except Exception as e:
                    print("Error al agregar detalle:", e)

    def obtener_detalles_por_orden(self, id_orden):
        """Obtiene detalles de orden de la base de datos."""
        try:
            conexion = Conexion()
            cursor = conexion.conectar()

            sql = "SELECT * FROM detalle_orden WHERE id_orden = ?"
            cursor.execute(sql, (id_orden,))
            rows = cursor.fetchall()
            if rows:
                return [OrdenDetalle(id_detalle=row[0], id_orden=row[1], id_producto=row[2], 
                                     cantidad=row[3], precio_unitario=row[4], nota=row[6]) for row in rows]
            return []

        except Exception as e:
            print("Error al obtener detalles:", e)
