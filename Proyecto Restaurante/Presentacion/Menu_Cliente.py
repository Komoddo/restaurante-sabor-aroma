
# Importa la clase que gestiona las operaciones del cliente
from Servicio.Cliente_Servicio import ClienteServicio

# Importa el modelo Cliente para crear y manipular objetos cliente
from Modelo.Cliente import Cliente
from Utilitario.Validacion import validar, TipoValidacion
from Presentacion.SubMenu_Nuevo_Cliente import submenu_nuevo_cliente


cs = ClienteServicio()    # Crea una instancia del servicio encargado de gestionar clientes en la BD

def submenu_clientes(cliente:Cliente=None):
    """Submenú para gestión de clientes."""
    while True:
        print("\n" + "-"*100)
        print("👥 GESTIÓN DE CLIENTES")
        print("-"*100)
        print("\n1. Lista de clientes")
        print("2. Nuevo cliente")
        print("3. Actualizar cliente")
        print("0. Salir")

        try:
            print("\nSeleccione una opción: ")
            opcion = input("➤  ").strip()
            
            if opcion == "1":
                """Muestra la lista completa de clientes."""
                print("\n" + "-" * 100)
                print("👥 LISTA DE CLIENTES")
                print("=" * 100)
                print(f"{'ID':<8} {'Nombres y apellidos':<40}    {'Email':<30}     {'Teléfono':<12}")
                print("=" * 100)
                clientes = cs.obtener_lista_clientes()    # Obtiene todos los clientes desde la base de datos
                if clientes:
                    for c in clientes:                  # Recorre cada cliente y lo muestra en tabla
                        print(f"{'0' if c.id_cliente<10 else ''}{(str(c.id_cliente)+'.'):<8}{c.nombre + ' ' + c.apellido:<40}{c.email:<38}{c.telefono:<12}")
                else:
                    print("No hay clientes registrados")        
            elif opcion == "2":
                submenu_nuevo_cliente()
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
                                while True:
                                    print(f"Nombre nuevo: ")
                                    nombre_nuevo = input("➤  ")
                                    if validar(nombre_nuevo, TipoValidacion.NOMBRE):
                                        break
                                    print("Formato de nombre inválido")
                                cliente.nombre = nombre_nuevo
                                print("Actualizando nombre...")
                            elif opcion=="2":
                                while True:
                                    print(f"Apellido nuevo: ")
                                    apellido_nuevo = input("➤  ").strip()
                                    if validar(apellido_nuevo, TipoValidacion.NOMBRE):
                                        break
                                    print("Formato de apellido inválido")
                                cliente.apellido = apellido_nuevo
                                print("Actualizando Apellido...")
                            elif opcion=="3":
                                while True:
                                    print(f"Email nuevo:")
                                    email_nuevo = input("➤  ").strip()
                                    if validar(email_nuevo, TipoValidacion.EMAIL):
                                        break
                                    print("Formato de nombre inválido")
                                cliente.email = email_nuevo
                                print("Actualizando Email...")
                            elif opcion=="4":
                                while True:
                                    print(f"Teléfono nuevo: ")
                                    telefono_nuevo = input("➤  ").strip()
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
