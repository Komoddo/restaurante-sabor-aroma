from base_datos.conexion_db import Conexion
from Modelo.Pedido import Pedido
from datetime import datetime

class PedidoServicio:
    def __init__(self):
        self.clientes = []
        self.f_cliente = []

    # --------------------------
    #   CREATE
    # --------------------------
    def agregar_pedido_bd(p : Pedido):
        conn = Conexion()
        cursor = conn.cursor()
        
        fecha = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

        cursor.execute("""
            INSERT INTO pedidos (
                id_orden, 
                fecha, 
                impuestos, 
                descuento, 
                total, 
                metodo_pago,
                estado)
            VALUES (?, ?, ?, ?, ?, ?, ?)
        """, (
            p.id_orden, 
            p.fecha, 
            p.impuestos, 
            p.descuento, 
            p.total, 
            p.metodo_pago,
            p.estado))

        conn.commit()
        return cursor.lastrowid   # retorna el ID generado

    # --------------------------
    #   READ ALL
    # --------------------------
    def obtener_pedidos(self):
        self.cursor.execute("SELECT * FROM pedidos")
        rows = self.cursor.fetchall()
        return [self._fila_a_pedido(r) for r in rows]

    # --------------------------
    #   READ ONE BY ID
    # --------------------------
    def obtener_pedido_por_id(self, pedido_id):
        self.cursor.execute("SELECT * FROM pedidos WHERE id=?", (pedido_id,))
        row = self.cursor.fetchone()
        return self._fila_a_pedido(row) if row else None

    # --------------------------
    #   UPDATE
    # --------------------------
    def actualizar_pedido(self, pedido: Pedido):
        self.cursor.execute("""
            UPDATE pedidos
            SET cliente_id=?, mesa_id=?, empleado_id=?, total=?, fecha=?
            WHERE id=?
        """, (pedido.cliente_id, pedido.mesa_id, pedido.empleado_id,
              pedido.total, pedido.fecha, pedido.id))

        self.conn.commit()
        return self.cursor.rowcount  # cuántas filas se actualizaron

    # --------------------------
    #   DELETE
    # --------------------------
    def eliminar_pedido(self, pedido_id):
        self.cursor.execute("DELETE FROM pedidos WHERE id=?", (pedido_id,))
        self.conn.commit()
        return self.cursor.rowcount

    # --------------------------
    #   UTILIDAD: convertir fila → objeto
    # --------------------------
    def _fila_a_pedido(self, r):
        return Pedido(
            id=r[0],
            cliente_id=r[1],
            mesa_id=r[2],
            empleado_id=r[3],
            total=r[4],
            fecha=r[5]
        )