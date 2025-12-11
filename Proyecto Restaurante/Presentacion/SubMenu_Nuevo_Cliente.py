from Servicio.Cliente_Servicio import ClienteServicio
from Modelo.Cliente import Cliente
from Utilitario.Validacion import validar, TipoValidacion

cs = ClienteServicio()    # Crea una instancia del servicio encargado de gestionar clientes en la BD

def submenu_nuevo_cliente() -> Cliente:
    """Submenú para gestión de clientes."""    

    while True:
        print("\nIngrese el nombre: ")
        nombre = input("➤  ").strip()
        if validar(nombre, TipoValidacion.NOMBRE):
            break
        print("Nombre inválido")
    
    while True:
        print("\nIngrese el apellido: ")
        apellido = input("➤  ").strip()
        if validar(apellido, TipoValidacion.NOMBRE):
            break
        print("\nApellido inválido")
        
    # Verifica si el cliente ya existe (evita duplicados)
    cliente = cs.validar_cliente(nombre=nombre, apellido=apellido)
    if cliente:
        print("\n✅ El cliente ya esta registrado")
        return cliente
    
    while True:
        print("\nIngrese el email: ")
        email = input("➤  ").strip()
        if not email: break
        if validar(email, TipoValidacion.EMAIL):
            break
        print("\nEmail inválido")
            
    while True:
        print("\nIngrese el teléfono: ")
        telefono = input("➤  ").strip()
        if not telefono: break
        if validar(telefono, TipoValidacion.TELEFONO):
            break
        print("\nTeléfono inválido")
        
    cliente = Cliente(
        nombre=nombre.lower(),
        apellido=apellido.lower(),
        email=email,
        telefono=telefono
    )
    
    # Crea un nuevo objeto Cliente y lo guarda en BD
    id = cs.agregar_cliente_bd(Cliente(
        nombre=nombre,
        apellido=apellido,
        email=email,
        telefono=telefono
    ))
    
    if (id):
        print("\n✅ Cliente registrado")
        cliente.id_cliente = id
        return cliente
    else:
        print("\nError al registrar el cliente")
        return None
            