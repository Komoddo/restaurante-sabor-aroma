from base_datos.conexion_db import Conexion
from Modelo.Pedido import Pedido
from Servicio.PedidoDetalle_Servicio import DetallePedidoServicio
from Principal import LISTA_PEDIDOS

class PedidoServicio:
    def __init__(self):
        pass
    # --------------------------
    #   CREATE
    # --------------------------
    def crear_pedido_bd(self, p : Pedido):
        try:
            conn = Conexion()
            cursor = conn.conectar()
            cursor.execute("""
            INSERT INTO pedidos (
                id_orden, 
                fecha,
                subtotal, 
                impuestos, 
                descuento, 
                total, 
                metodo_pago,
                estado)
            VALUES (?, ?, ?, ?, ?, ?, ?, ?)
        """, (
            p.id_orden, 
            p.fecha, 
            p.subtotal, 
            p.impuestos, 
            p.descuento, 
            p.total, 
            p.metodo_pago,
            p.estado))
            
            conn.commit()
            return cursor.lastrowid
        except Exception as e:
            print("Error al crear orden:", e)
        finally:
            conn.cerrar()

    # --------------------------
    #   READ ALL
    # --------------------------
    def obtener_pedidos_bd(self):
        try:
            LISTA_PEDIDOS.clear()
            pds = DetallePedidoServicio()
            conn = Conexion()
            cursor = conn.conectar()
            cursor.execute("SELECT * FROM pedidos ORDER BY fecha DESC")
            rows = cursor.fetchall()

            LISTA_PEDIDOS.extend([Pedido(id_pedido=row[0], id_orden=row[1], 
                                    fecha=row[2], subtotal=row[3], 
                                    impuestos=row[4], descuento=row[5],
                                    total=row[6], metodo_pago=row[7], 
                                    estado=row[8]) for row in rows])
            if LISTA_PEDIDOS:
                for pedido in LISTA_PEDIDOS:
                    detalles = pds.obtener_detalles_por_pedido(pedido.id_pedido)
                    if detalles:
                        for detalle in detalles:
                            pedido.agregar_detalle(detalle)
        except Exception as e:
            print("Error al listar pedidos:", e)

    def obtener_lista_pedidos(self):
        return LISTA_PEDIDOS


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