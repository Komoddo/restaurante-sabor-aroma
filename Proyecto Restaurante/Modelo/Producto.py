class Producto:
    def __init__(self, 
                 id_producto=None, 
                 nombre=None, 
                 descripcion=None, 
                 precio=None, 
                 categoria=None, 
                 disponibilidad=True):
        self.id_producto = id_producto
        self.nombre = nombre
        self.descripcion = descripcion
        self.precio = precio
        self.categoria = categoria
        self.disponibilidad = disponibilidad
    
    def __str__(self):
        return f"{self.nombre} - S/. {self.precio}"
    
    def __repr__(self):
        return f"Producto({self.id_producto}, {self.nombre}, {self.precio})"
    
    def actualizar_precio(self, nuevo_precio):
        self.precio = nuevo_precio
    
    def cambiar_disponibilidad(self, disponible):
        self.disponibilidad = disponible