"""Esta clase representa un producto y guarda su información como nombre, precio y disponibilidad."""

class Producto:

    # Inicializa los datos principales del producto
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
    

    # Devuelve una representación sencilla del producto como texto
    def __str__(self):
        return f"{self.nombre} - S/. {self.precio}"
    
     # Devuelve una representación formal del producto (útil para depuración)
    def __repr__(self):
        return f"Producto({self.id_producto}, {self.nombre}, {self.precio})"
    
    # Actualiza el precio del producto
    def actualizar_precio(self, nuevo_precio):
        self.precio = nuevo_precio
    
    # Cambia la disponibilidad del producto (True/False)
    def cambiar_disponibilidad(self, disponible):
        self.disponibilidad = disponible