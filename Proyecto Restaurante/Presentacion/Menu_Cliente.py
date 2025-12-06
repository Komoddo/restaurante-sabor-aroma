
# Importa la clase que gestiona las operaciones del cliente
from Servicio.Cliente_Servicio import ClienteServicio

# Importa el modelo Cliente para crear y manipular objetos cliente
from Modelo.Cliente import Cliente

cs = ClienteServicio()    # Crea una instancia del servicio encargado de gestionar clientes en la BD

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
                    print(f"Nombre: {cliente.nombre}")
                    print(f"Apellido: {cliente.apellido}")
                    nombre = cliente.nombre
                    apellido = cliente.apellido

                     # Si no, solicita los datos manualmente
                else:
                    nombre = input("Nombre")
                    apellido = input("Apellido")

                    # Verifica si el cliente ya existe (evita duplicados)
                if not(cs.validar_cliente(nombre=nombre, apellido=apellido)):
                    email = input("Email")
                    telefono = input("Teléfono")

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
                 # Busca clientes escribiendo nombre y apellido
                nombres = input("Ingrese el nombre y apellido del cliente").strip()
                cs.Buscar_cliente(nombres)
                if cs.f_cliente:
                    # Muestra todas las coincidencias encontradas
                    for c in cs.f_cliente:
                        print(f"{c.id_cliente:<3} {c.nombre:<20} {c.apellido:<20}  {c.email}  {c.telefono:<12}")

                    id = int(input("Seleccione el cliente a actualizar: "))
                    # Obtiene el cliente elegido por ID
                    cliente = next((c for c in cs.f_cliente if c.id_cliente == id), None)
                    if(cliente):
                        print(" Deje en blanco los campos que no desea actualizar.")

                        # Permite modificar solo lo que se desea cambiar
                        nuevo_nombre = input(f"Nombre ({cliente.nombre}): ").strip()
                        nuevo_apellido = input(f"Apellido ({cliente.apellido}): ").strip()
                        nuevo_email = input(f"Email ({cliente.email}): ").strip()
                        nuevo_telefono = input(f"Teléfono ({cliente.telefono}): ").strip()

                        # Actualiza solo los campos ingresados
                        cliente.nombre = nuevo_nombre if nuevo_nombre else cliente.nombre
                        cliente.apellido = nuevo_apellido if nuevo_apellido else cliente.apellido
                        cliente.email = nuevo_email if nuevo_email else cliente.email
                        cliente.telefono = nuevo_telefono if nuevo_telefono else cliente.telefono

                        # Guarda el cambio en la base de datos
                        if cs.actualizar_cliente(cliente):
                            print("✔ Cliente actualizado exitosamente.")
                        else:
                            print("❌ Error al actualizar el cliente.")
                else:
                    print("No se encontraron coincidencias.")
            elif opcion == "0":
                return        # Sale del submenú
            else:
                print(" Opción inválida")

        except Exception as e:
            print(f" Error: {e}")              # Captura errores generales para evitar que el programa se cierre