"""Esta clase representa cada detalle del pedido, como producto, cantidad y subtotal."""

class PedidoDetalle:

    # Inicializa los datos del detalle y calcula el subtotal
    def __init__(self, id_detalle, id_pedido,id_producto,
                 cantidad, precio_unitario):
        self.id_detalle = id_detalle
        self.idpedido = id_pedido
        self.id_producto = id_producto
        self.cantidad = cantidad
        self.precio_unitario = precio_unitario
        self.subtotal = round(cantidad * precio_unitario, 2)

    # Devuelve un texto mostrando el producto, cantidad y subtotal
    def __str__(self):
        return f"{self.nombre_producto} x {self.cantidad} = S/{self.subtotal:.2f}"
