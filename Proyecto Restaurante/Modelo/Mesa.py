"""Esta clase representa una mesa del restaurante y guarda sus datos principales."""

class Mesa:

     # Inicializa la mesa asignando su id, número, capacidad y estado
    def __init__(self, id=None, numero=0, capacidad=0, estado="disponible"):
        self.id_mesa = id
        self.numero = numero
        self.capacidad = capacidad
        self.estado = estado