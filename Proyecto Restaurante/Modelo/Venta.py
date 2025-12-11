# Importa la fecha y hora actual para registrar cuándo se crea el venta
from datetime import datetime
# Importa la clase ventaDetalle para poder agregar detalles al venta
from Modelo.VentaDetalle import ventaDetalle

"""Esta clase representa un venta y almacena su información y sus detalles."""
class Venta:
    # Inicializa los datos principales del venta al momento de crearlo
    def __init__(self, id_venta, id_orden, fecha, subtotal, impuestos, 
                 descuento, total, metodo_pago, estado):
        self.id_venta = id_venta
        self.id_orden = id_orden
        self.fecha = datetime.now().strftime("%Y-%m-%d %H:%M:%S") if fecha is None else fecha  #guarda la fecha y hora actual
        self.subtotal = subtotal
        self.impuestos = impuestos
        self.descuento = descuento
        self.total = total
        self.metodo_pago = "efectivo" if metodo_pago is None else metodo_pago
        self.estado = "pagado" if estado is None else estado    # puede ser Pagado o Anulado
        
        self.detalles = []                   # aquí se guardan los detalles del venta

    # Agrega un objeto ventaDetalle a la lista de detalles
    def agregar_detalle(self, detalle: ventaDetalle):
        self.detalles.append(detalle)
        self.actualizar_calculos()
        
    def agregar_detalles(self, detalles : list):
        if detalles:
            for pd in detalles:
                pd.id_venta = self.id_venta
                self.detalles.append(pd)
        self.actualizar_calculos()

    def actualizar_calculos(self):
        self.subtotal = round(sum(d.subtotal for d in self.detalles), 2)
        self.impuestos = round(self.subtotal * 0.18, 2)
        self.total = round(self.subtotal + self.impuestos - self.descuento, 2)
