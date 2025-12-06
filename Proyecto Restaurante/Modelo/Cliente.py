class Cliente: #clase cliente
    def __init__(self, id_cliente=0, nombre=None, apellido=None, email=None, telefono=None):
        self.id_cliente = id_cliente
        self.nombre = nombre
        self.apellido = apellido
        self.email = email
        self.telefono = telefono