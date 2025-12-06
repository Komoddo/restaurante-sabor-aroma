# Importa la fecha y hora actual para registrar cuándo se crea el pedido
from datetime import datetime
# Importa la clase PedidoDetalle para poder agregar detalles al pedido
from Modelo.PedidoDetalle import PedidoDetalle

"""Esta clase representa un pedido y almacena su información y sus detalles."""
class Pedido:

    # Inicializa los datos principales del pedido al momento de crearlo
    def __init__(self, id_pedido, id_orden, impuestos, 
                 descuento, total, metodo_pago, estado="Pagado"):
        self.id_pedido = id_pedido
        self.id_orden = id_orden
        self.fecha = datetime.now()     # guarda la fecha y hora actual
        self.impuestos = impuestos
        self.descuento = descuento
        self.total = total
        self.metodo_pago = metodo_pago
        self.estado = estado      # puede ser Pagado o Anulado
        
        self.detalles = []                   # aquí se guardan los detalles del pedido

    # Agrega un objeto PedidoDetalle a la lista de detalles
    def agregar_detalle(self, detalle: PedidoDetalle):
        self.detalles.append(detalle)

    # Muestra el pedido como un texto más fácil de leer
    def __str__(self):
        return f"Pedido #{self.id_pedido} - Total S/{self.total_pagar:.2f} - {self.metodo_pago}"
