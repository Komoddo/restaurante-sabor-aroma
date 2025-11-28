class OrdenDetalle:
    def __init__(self, id_detalle, id_orden,id_producto, cantidad, precio_unitario, nota=""):
        self.id_detalle = id_detalle
        self.id_orden = id_orden
        self.id_producto = id_producto
        self.cantidad = cantidad
        self.precio_unitario = precio_unitario
        self.subtotal = self.precio_unitario * self.cantidad
        self.nota = nota

    # def __str__(self):
    #     return f"{self.nombre_producto} x {self.cantidad} = S/{self.subtotal:.2f}"

    def actualizar_cantidad(self, nueva_cantidad):
        self.cantidad = nueva_cantidad
        self.subtotal = round(self.cantidad * self.precio_unitario, 2)