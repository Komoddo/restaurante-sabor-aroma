class AuditoriaPrecio:
    def __init__(self, id_auditoria: int=None,
        fecha_cambio: str = None,
        id_producto: int = None,
        precio_anterior: float = None,
        precio_nuevo: float = None,
        fecha_registro: str = None):

        self.id_auditoria = id_auditoria
        self.fecha_cambio = fecha_cambio
        self.id_producto = id_producto
        self.precio_anterior = precio_anterior
        self.precio_nuevo = precio_nuevo
        self.fecha_registro = fecha_registro

    # def __repr__(self):
    #     return (
    #         f"AuditoriaPrecio(id={self.id}, fecha_cambio='{self.fecha_cambio}', "
    #         f"idProducto={self.idProducto}, precio_anterior={self.precio_anterior}, "
    #         f"precio_nuevo={self.precio_nuevo}, fecha_registro='{self.fecha_registro}')"
    #     )