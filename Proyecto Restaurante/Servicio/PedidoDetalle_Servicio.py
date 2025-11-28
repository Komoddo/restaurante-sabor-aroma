from base_datos.conexion_db import Conexion
from Modelo.PedidoDetalle import PedidoDetalle

class DetallePedidoServicio:
    def __init__(self):
        detalles = []

    def agregar_detalle(self, detalle: PedidoDetalle):
        conn = Conexion()
        cursor = conn.cursor()
        cursor.execute("""
            INSERT INTO detalles_pedido (pedido_id, producto_id, cantidad, subtotal)
            VALUES (?, ?, ?, ?)
        """, (detalle.pedido_id, detalle.producto_id,
              detalle.cantidad, detalle.subtotal))
        conn.commit()

    def obtener_detalles(self, pedido_id):
        self.cursor.execute("""
            SELECT * FROM detalles_pedido WHERE pedido_id=?
        """, (pedido_id,))
        rows = self.cursor.fetchall()
        return [
            PedidoDetalle(id=r[0], pedido_id=r[1], producto_id=r[2], cantidad=r[3], subtotal=r[4])
            for r in rows
        ]