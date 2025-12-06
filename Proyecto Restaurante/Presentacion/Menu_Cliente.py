from Servicio.Cliente_Servicio import ClienteServicio
from Modelo.Cliente import Cliente
from Utilitario.Validacion import validar, TipoValidacion

cs = ClienteServicio()

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
                clientes = cs.obtener_lista_clientes()
                if clientes:
                    for c in clientes:
                        print(f"{c.id_cliente:<3} {c.nombre:<20} {c.apellido:<20}  {c.email}  {c.telefono:<12}")
                else:
                    print("No hay clientes registrados")        
            elif opcion == "2":
                print("\n📋 NUEVOS CLIENTES")
                print("-" * 45)
                if cliente:
                    print(f"\nNombre: {cliente.nombre}")
                    print(f"Apellido: {cliente.apellido}")
                    nombre = cliente.nombre
                    apellido = cliente.apellido
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
                return id
            elif opcion == "3":
                print("-" * 45)
                print("\n📋 ACTUALIZACIÓN DE CLIENTE")
                print("Ingrese el nombre")
                nombre = input("➤  ")
                print("Ingrese el apellido")
                apellido = input("➤  ")
                cs.Buscar_clientes(nombre, apellido)
                if cs.f_cliente:
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
                break
            else:
                print(" Opción inválida")

        except Exception as e:
            print(f" Error: {e}")  
        finally:
            cs.obtener_clientes_bd()