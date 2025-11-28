class Mesa:
    def __init__(self, id=None, numero=0, capacidad=0, estado="disponible"):
        self.id_mesa = id
        self.numero = numero
        self.capacidad = capacidad
        self.estado = estado