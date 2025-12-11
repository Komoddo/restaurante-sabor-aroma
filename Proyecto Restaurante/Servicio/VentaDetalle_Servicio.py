from base_datos.conexion_db import Conexion
from Modelo.VentaDetalle import ventaDetalle

class DetalleventaServicio:
    def __init__(self):
        detalles = []

    def agregar_detalles_bd(self, venta_detalles: list):
        if venta_detalles:
            try:
                conexion = Conexion()
                cursor = conexion.conectar()
        
                for detalle in venta_detalles:
                    sql = """ INSERT INTO detalle_venta(id_venta, id_producto, cantidad, precio_unitario, subtotal)
                        VALUES (?, ?, ?, ?, ?) """

                    cursor.execute(sql, (
                        detalle.id_venta,
                        detalle.id_producto,
                        detalle.cantidad,
                        detalle.precio_unitario,
                        detalle.subtotal
                    ))

                conexion.conn.commit()
                return cursor.lastrowid
            except Exception as e:
                    print("Error al agregar detalle:", e)
                    
            finally:
                conexion.cerrar()

    def obtener_detalles_por_venta(self, id_venta):
        try:
            conexion = Conexion()
            cursor = conexion.conectar()

            sql = "SELECT * FROM detalle_venta WHERE id_venta = ?"
            cursor.execute(sql, (id_venta,))
            rows = cursor.fetchall()
            if rows:
                return [ventaDetalle(id_detalle=row[0], 
                                      id_venta=row[1], 
                                      id_producto=row[2], 
                                     cantidad=row[3], 
                                     precio_unitario=row[4], 
                                     subtotal=row[5]) for row in rows]
            return []

        except Exception as e:
            print("Error al obtener detalles:", e)