from enum import Enum
from datetime import datetime
from Modelo.OrdenDetalle import OrdenDetalle

# class EstadoOrden(Enum):
#     PENDIENTE = "Pendiente"
#     PAGADO = "preparado"
#     ANULADO = "cancelado"

class Orden:
    def __init__(self, 
                 id_orden, 
                 id_mesa, 
                 id_empleado, 
                 id_cliente, 
                 fecha_hora,
                 nro_personas,
                 estado, 
                 nota, 
                 total):
        self.id_orden = id_orden
        self.id_mesa = id_mesa
        self.id_empleado = id_empleado
        self.id_cliente = id_cliente
        self.fecha_hora = datetime.now().strftime("%Y-%m-%d %H:%M:%S") if fecha_hora is None else fecha_hora
        self.nro_personas = 1 if nro_personas==0 else nro_personas
        self.estado = "pendiente" if estado is None else estado
        self.nota = nota
        self.total = total
        
        self.detalles = []             # lista de DetalleOrden

    def agregar_detalles(self, detalles : list):
        if detalles:
            for od in detalles:
                od.id_orden = self.id_orden
                self.detalles.append(od)
        self.actualizar_total()

    def agregar_detalle(self, detalle: OrdenDetalle):
        self.detalles.append(detalle)
        self.actualizar_total()

    def actualizar_total(self):
        self.total = round(sum(d.subtotal for d in self.detalles), 2)

    def cambiar_estado(self, nuevo_estado: str):
        self.estado = nuevo_estado

    def __str__(self):
        return f"Orden #{self.id_orden} - Mesa {self.id_mesa} - Total S/{self.total:.2f} - {self.estado.value}"
