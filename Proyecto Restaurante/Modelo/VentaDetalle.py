"""Esta clase representa cada detalle del venta, como producto, cantidad y subtotal."""

class ventaDetalle:

    # Inicializa los datos del detalle y calcula el subtotal
    def __init__(self, id_detalle, id_venta,id_producto,
                 cantidad, precio_unitario, subtotal):
        self.id_detalle = id_detalle
        self.id_venta = id_venta
        self.id_producto = id_producto
        self.cantidad = cantidad
        self.precio_unitario = precio_unitario
        self.subtotal = round(cantidad * precio_unitario, 2) if subtotal is 0.0 else subtotal


