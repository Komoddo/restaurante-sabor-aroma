class PedidoDetalle:
    def __init__(self, id_detalle, id_pedido,id_producto,
                 cantidad, precio_unitario, subtotal):
        self.id_detalle = id_detalle
        self.id_pedido = id_pedido
        self.id_producto = id_producto
        self.cantidad = cantidad
        self.precio_unitario = precio_unitario
        self.subtotal = round(cantidad * precio_unitario, 2) if subtotal is None else subtotal


