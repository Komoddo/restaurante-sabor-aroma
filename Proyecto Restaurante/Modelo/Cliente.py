
"""Módulo Modelo: entidad cliente"""

class Cliente: #clase cliente
    def __init__(self, id_cliente=0, nombre=None, apellido=None, email=None, telefono=None):
        self.id_cliente = id_cliente
        self.nombre = nombre
        self.apellido = apellido
        self.email = email
        self.telefono = telefono

    def __str__(self): # es un string modificado
        return f"Cliente({self.id_cliente}, {self.nombre} {self.apellido}, {self.email})"

    def get_info(self):
        return {
            'id_cliente': self.id_cliente,
            'nombre': self.nombre,
            'apellido': self.apellido,
            'email': self.email,
            'telefono': self.telefono
        }