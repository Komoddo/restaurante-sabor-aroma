from datetime import datetime
from Modelo.PedidoDetalle import PedidoDetalle

class Pedido:
    def __init__(self, id_pedido, id_orden, impuestos, 
                 descuento, total, metodo_pago, estado="Pagado"):
        self.id_pedido = id_pedido
        self.id_orden = id_orden
        self.fecha = datetime.now()
        self.impuestos = impuestos
        self.descuento = descuento
        self.total = total
        self.metodo_pago = metodo_pago
        self.estado = estado      # Pagado / Anulado
        
        self.detalles = []                  # lista de DetallePedido

    def agregar_detalle(self, detalle: PedidoDetalle):
        self.detalles.append(detalle)

    def __str__(self):
        return f"Pedido #{self.id_pedido} - Total S/{self.total_pagar:.2f} - {self.metodo_pago}"
