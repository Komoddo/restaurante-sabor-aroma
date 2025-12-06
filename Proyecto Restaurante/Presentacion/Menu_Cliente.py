
# Importa la clase que gestiona las operaciones del cliente
from Servicio.Cliente_Servicio import ClienteServicio

# Importa el modelo Cliente para crear y manipular objetos cliente
from Modelo.Cliente import Cliente
from Utilitario.Validacion import validar, TipoValidacion

cs = ClienteServicio()    # Crea una instancia del servicio encargado de gestionar clientes en la BD

def submenu_clientes(cliente:Cliente=None):
    """Submenú para gestión de clientes."""
    while True:
        print("\n" + "="*50)
        print("👥 GESTIÓN DE CLIENTES")
        print("="*50)
        
        print("1. Lista de clientes")
        print("2. Nuevo cliente")
        print("3. Actualizar cliente")
        print("0. Cancelar")

        try:
            opcion = input("\nSeleccione una opción: ").strip()
            
            if opcion == "1":
                """Muestra la lista completa de clientes."""
                print("\n👥 LISTA DE CLIENTES")
                print("-" * 60)
                print(f"{'ID':<3} {'Nombre':<20}    {'Apellido':<20}    {'Email'}     {'Teléfono':<12}")
                print("-" * 60)
                clientes = cs.obtener_lista_clientes()    # Obtiene todos los clientes desde la base de datos
                if clientes:
                    for c in clientes:                  # Recorre cada cliente y lo muestra en tabla
                        print(f"{c.id_cliente:<3} {c.nombre:<20} {c.apellido:<20}  {c.email}  {c.telefono:<12}")
                else:
                    print("No hay clientes registrados")        
            elif opcion == "2":
                print("\n📋 NUEVOS CLIENTES")
                print("-" * 45)

                # Si se recibe un cliente desde otro módulo, usa sus datos
                if cliente:
                    print(f"\nNombre: {cliente.nombre}")
                    print(f"Apellido: {cliente.apellido}")
                    nombre = cliente.nombre
                    apellido = cliente.apellido

                     # Si no, solicita los datos manualmente
                else:
                    while True:
                        print("Ingrese el nombre: ")
                        nombre = input("➤  ").strip()
                        if validar(nombre, TipoValidacion.NOMBRE):
                            break
                        print("Nombre inválido")
                    
                    while True:
                        print("Ingrese el apellido: ")
                        apellido = input("➤  ").strip()
                        if validar(apellido, TipoValidacion.NOMBRE):
                            break
                        print("Apellido inválido")
                # Verifica si el cliente ya existe (evita duplicados)
                if not(cs.validar_cliente(nombre=nombre, apellido=apellido)):
                    while True:
                        print("Ingrese el email: ")
                        email = input("➤  ").strip()
                        if validar(email, TipoValidacion.EMAIL):
                            break
                        print("Email inválido")
                    while True:
                        print("Ingrese el teléfono: ")
                        telefono = input("➤  ").strip()
                        if validar(telefono, TipoValidacion.TELEFONO):
                            break
                        print("Teléfono inválido")
                    
                    # Crea un nuevo objeto Cliente y lo guarda en BD
                    id = cs.agregar_cliente_bd(Cliente(
                        nombre=nombre,
                        apellido=apellido,
                        email=email,
                        telefono=telefono
                    ))
                    if not(id):
                        print("Error registrar el cliente")
                    else:
                        print("Cliente registrado")
                else:
                    print("El cliente ya esta registrado")
                return id             # Devuelve el ID del cliente creado
            elif opcion == "3":
                print("-" * 45)
                print("\n📋 ACTUALIZACIÓN DE CLIENTE")
                print("Ingrese el nombre")
                nombre = input("➤  ")
                print("Ingrese el apellido")
                apellido = input("➤  ")
                # Busca clientes escribiendo nombre y apellido
                cs.Buscar_clientes(nombre, apellido)
                if cs.f_cliente:
                    # Muestra todas las coincidencias encontradas
                    for c in cs.f_cliente:
                        print(f"{c.id_cliente:<3} {c.nombre:<20} {c.apellido:<20}  {c.email}  {c.telefono:<12}")
                    print("0. Cancelar")

                    while True:
                        print("Seleccione un cliente: ")
                        id = input("➤  ").strip()
                        if validar(id, TipoValidacion.ENTERO):
                            id = int(id)
                            break
                        print("ID inválido")
                    # Obtiene el cliente elegido por ID
                    cliente = next((c for c in cs.f_cliente if c.id_cliente == id), None)
                    if(cliente):
                        while True:
                            print(f"\nRESUMEN DEL CLIENTE N° {cliente.id_cliente}")
                            print(f"\n1. Nombre: {cliente.nombre}")
                            print(f"2. Apellido: {cliente.apellido}")
                            print(f"3. Email: {cliente.email}")
                            print(f"3. Teléfono: {cliente.telefono}")
                            print("0. ⬅️ Salir")

                            print("\nSeleccione el dato que desea actualizar")
                            opcion = input("➤  ").strip()
                            if opcion=="1":
                                # Permite modificar solo lo que se desea cambiar
                                print(f"Nombre nuevo: ")
                                nombre_nuevo = input("➤  ")
                                while True:
                                    if validar(nombre_nuevo, TipoValidacion.NOMBRE):
                                        break
                                    print("Formato de nombre inválido")
                                cliente.nombre = nombre_nuevo
                                print("Actualizando nombre...")
                            elif opcion=="2":
                                print(f"Apellido nuevo: ")
                                apellido_nuevo = input("➤  ").strip()
                                while True:
                                    if validar(apellido_nuevo, TipoValidacion.NOMBRE):
                                        break
                                    print("Formato de apellido inválido")
                                cliente.apellido = apellido_nuevo
                                print("Actualizando Apellido...")
                            elif opcion=="3":
                                print(f"Email nuevo:")
                                email_nuevo = input("➤  ").strip()
                                while True:
                                    if validar(email_nuevo, TipoValidacion.EMAIL):
                                        break
                                    print("Formato de nombre inválido")
                                cliente.email = email_nuevo
                                print("Actualizando Email...")
                            elif opcion=="4":
                                print(f"Teléfono nuevo: ")
                                telefono_nuevo = input("➤  ").strip()
                                while True:
                                    if validar(telefono_nuevo, TipoValidacion.TELEFONO):
                                        break
                                    print("Formato de teléfono inválido")
                                cliente.telefono = telefono_nuevo
                                print("Actualizando Teléfono...")
                            elif opcion=="0":
                                print("¿Desea guardar los cambios realizados? (s/n)")
                                respuesta = input("➤  ").strip().lower()
                                if respuesta=="s":
                                    # Guarda el cambio en la base de datos
                                    if cs.actualizar_cliente_bd(cliente):
                                        print("✔️ cliente actualizado con exito")
                                    else:
                                        print("❌ Error al actualizar el cliente")
                                else:
                                    print("🚶‍♂️ Cancelando cambios...")
                                break
                            else:
                                print("Respuesta inválida")
                else:
                    print("No se encontraron coincidencias.")
            elif opcion == "0":
                # Sale del submenú
                break
            else:
                print(" Opción inválida")
        # Captura errores generales para evitar que el programa se cierre
        except Exception as e:
            print(f" Error: {e}")  
        finally:
            cs.obtener_clientes_bd()
