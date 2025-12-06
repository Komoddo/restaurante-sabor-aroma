from datetime import datetime
from Modelo.PedidoDetalle import PedidoDetalle

class Pedido:
    def __init__(self, id_pedido, id_orden, fecha, subtotal, impuestos, 
                 descuento, total, metodo_pago, estado):
        self.id_pedido = id_pedido
        self.id_orden = id_orden
        self.fecha = datetime.now().strftime("%Y-%m-%d %H:%M:%S") if fecha is None else fecha
        self.subtotal = subtotal
        self.impuestos = impuestos
        self.descuento = descuento
        self.total = total
        self.metodo_pago = "efectivo" if metodo_pago is None else metodo_pago
        self.estado = "pagado" if estado is None else estado    # Pagado / Anulado
        
        self.detalles = []                  # lista de DetallePedido

    def agregar_detalle(self, detalle: PedidoDetalle):
        self.detalles.append(detalle)
        self.actualizar_calculos()
        
    def agregar_detalles(self, detalles : list):
        if detalles:
            for pd in detalles:
                pd.id_pedido = self.id_pedido
                self.detalles.append(pd)
        self.actualizar_calculos()

    def actualizar_calculos(self):
        self.subtotal = round(sum(d.subtotal for d in self.detalles), 2)
        self.impuestos = round(self.subtotal * 0.18, 2)
        self.total = round(self.subtotal + self.impuestos - self.descuento, 2)
