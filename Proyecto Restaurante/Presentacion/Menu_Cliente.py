from Servicio.Cliente_Servicio import ClienteServicio
from Modelo.Cliente import Cliente

cs = ClienteServicio()

def submenu_clientes(cliente:Cliente=None):
        """Submenú para gestión de clientes."""
        print("\n" + "="*50)
        print("👥 GESTIÓN DE CLIENTES")
        print("="*50)
        
        print("1. Lista de clientes")
        print("2. Nuevo cliente")
        print("3. Actualizar datos de cliente")
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
                    print(f"Nombre: {cliente.nombre}")
                    print(f"Apellido: {cliente.apellido}")
                    nombre = cliente.nombre
                    apellido = cliente.apellido
                else:
                    nombre = input("Nombre")
                    apellido = input("Apellido")
                if not(cs.validar_cliente(nombre=nombre, apellido=apellido)):
                    email = input("Email")
                    telefono = input("Teléfono")
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
                nombres = input("Ingrese el nombre y apellido del cliente").strip()
                cs.Buscar_cliente(nombres)
                if cs.f_cliente:
                    for c in cs.f_cliente:
                        print(f"{c.id_cliente:<3} {c.nombre:<20} {c.apellido:<20}  {c.email}  {c.telefono:<12}")

                    id = int(input("Seleccione el cliente a actualizar: "))
                    cliente = next((c for c in cs.f_cliente if c.id_cliente == id), None)
                    if(cliente):
                        print(" Deje en blanco los campos que no desea actualizar.")
                        nuevo_nombre = input(f"Nombre ({cliente.nombre}): ").strip()
                        nuevo_apellido = input(f"Apellido ({cliente.apellido}): ").strip()
                        nuevo_email = input(f"Email ({cliente.email}): ").strip()
                        nuevo_telefono = input(f"Teléfono ({cliente.telefono}): ").strip()

                        cliente.nombre = nuevo_nombre if nuevo_nombre else cliente.nombre
                        cliente.apellido = nuevo_apellido if nuevo_apellido else cliente.apellido
                        cliente.email = nuevo_email if nuevo_email else cliente.email
                        cliente.telefono = nuevo_telefono if nuevo_telefono else cliente.telefono

                        if cs.actualizar_cliente(cliente):
                            print("✔ Cliente actualizado exitosamente.")
                        else:
                            print("❌ Error al actualizar el cliente.")
                else:
                    print("No se encontraron coincidencias.")
            elif opcion == "0":
                return
            else:
                print(" Opción inválida")

        except Exception as e:
            print(f" Error: {e}")