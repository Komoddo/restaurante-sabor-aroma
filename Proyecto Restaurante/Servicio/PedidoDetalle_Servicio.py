from base_datos.conexion_db import Conexion
from Modelo.PedidoDetalle import PedidoDetalle

class DetallePedidoServicio:
    def __init__(self):
        detalles = []

    def agregar_detalles_bd(self, pedido_detalles: list):
        if pedido_detalles:
            try:
                conexion = Conexion()
                cursor = conexion.conectar()
        
                for detalle in pedido_detalles:
                    sql = """ INSERT INTO detalle_pedido(id_pedido, id_producto, cantidad, precio_unitario, subtotal)
                        VALUES (?, ?, ?, ?, ?) """

                    cursor.execute(sql, (
                        detalle.id_pedido,
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

    def obtener_detalles_por_pedido(self, id_pedido):
        try:
            conexion = Conexion()
            cursor = conexion.conectar()

            sql = "SELECT * FROM detalle_pedido WHERE id_pedido = ?"
            cursor.execute(sql, (id_pedido,))
            rows = cursor.fetchall()
            if rows:
                return [PedidoDetalle(id_detalle=row[0], id_pedido=row[1], id_producto=row[2], 
                                     cantidad=row[3], precio_unitario=row[4], subtotal=row[6]) for row in rows]
            return []

        except Exception as e:
            print("Error al obtener detalles:", e)