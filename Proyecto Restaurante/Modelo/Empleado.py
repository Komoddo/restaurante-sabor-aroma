class Empleado:
    def __init__(self, id=0, nombre="", apellido="", dni="", cargo="", telefono="", estado="activo"):
        self.id = id
        self.nombre = nombre
        self.apellido = apellido
        self.dni = dni
        self.cargo = cargo
        self.telefono = telefono
        self.estado = estado   # activo/inactivo/retirado  