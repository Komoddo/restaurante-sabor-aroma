
"""Esta clase guarda y maneja los datos de un cliente."""

# Inicializa el objeto cliente asignando sus datos básicos al momento de crearlo
class Cliente: 
    def __init__(self, id_cliente=0, nombre=None, apellido=None, email=None, telefono=None):
        self.id_cliente = id_cliente
        self.nombre = nombre
        self.apellido = apellido
        self.email = email
        self.telefono = telefono

   # Devuelve un texto que muestra los datos principales del cliente cuando se imprime el objeto
    def __str__(self): 
        return f"Cliente({self.id_cliente}, {self.nombre} {self.apellido}, {self.email})"

    # Devuelve los datos del cliente organizados en un diccionario (clave : valor)
    def get_info(self):
        return {
            'id_cliente': self.id_cliente,
            'nombre': self.nombre,
            'apellido': self.apellido,
            'email': self.email,
            'telefono': self.telefono
        }