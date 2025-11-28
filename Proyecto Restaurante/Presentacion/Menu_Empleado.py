from Servicio.Empleado_Servicio import EmpleadoServicio
from Modelo.Empleado import Empleado

es = EmpleadoServicio()

def submenu_Empleados():
        
    while True:
        es.obtener_Empleados_bd()
        """Submenú para gestión de Empleados."""
        print("\n" + "="*50)
        print("👥 GESTIÓN DE EMPLEADOS")
        print("="*50)

        print("1. Lista de Empleados")
        print("2. Nuevo Empleado")
        print("3. Actualizar Empleado")
        print("0. Cancelar")

        try:
            opcion = input("\nSeleccione una opción: ").strip()

            if opcion == "1":
                """Muestra la lista completa de Empleados."""
                print("\n👥 LISTA DE EMPLEADOS")
                print("=" * 80)
                print(f"{'ID':<10}{'Nombres'+' '+'Apellidos':<30}{'DNI':>20}{'Teléfono':>20}")
                print("=" * 80)
                estructura = es.obtener_empleados_por_cargo_estado()
                if estructura:
                    for cargo, items in estructura.items():
                        print(f"{'📋 '+cargo.upper():>40}")
                        print("=" * 80)
                        for estado, items in items.items():
                            print(f"{estado+(' 🟢' if estado=='activo' else (' 🟡' if estado=='inactivo' else ' 🔴')):>79}")
                            print("-" * 80)
                            for e in items:
                                print(f"{e.id:<10}{(e.nombre +' '+ e.apellido):<30}{e.dni:>20}{e.telefono:>20}")
                                print("-" * 80)
                else:
                    print("sin productos*")
                print("0. Regresar")
                    
            elif opcion == "2":
                print("\n📋 NUEVO EMPLEADO")
                print("-" * 45)
                print("Ingrese DNI: ")
                dni = input("➤  ").strip().lower()
                if not(es.obtener_Empleado_por_dni(dni)):
                    empleado = Empleado()
                    print("Ingrese el nombre: ")
                    empleado.nombre = input("➤  ").strip().lower()
                    print("\nIngrese el Apellido: ")
                    empleado.apellido = input("➤  ").strip().lower()
                    print("\nIngrese el número de telefono: ")
                    empleado.telefono = input("➤  ").strip().lower()
                    print("\nCategorias:")
                    cargos = es.crear_cargos()
                    for i, car in cargos.items():
                        print(f"{i}. {car}")
                    print(f"{len(cargos) + 1}. Nueva categoría")

                    while True:
                        print("\nSeleccione un cargo")
                        car_id = input("➤  ").strip().lower()
                        num_car = len(cargos)
                        try:
                            if car_id in range(1, num_car + 1):
                                empleado.cargo = cargos[car_id]
                                break
                            elif cat_id == num_cat + 1:
                                print("\nNombre de la categoría nueva")
                                empleado.cargo = input("➤  ").strip().lower()
                                if empleado.cargo=="":
                                    print("Asigne un cargo válido")
                                else:
                                    break
                            else:
                                print("Opción inválida")
                        except ValueError:
                            cargo = cat_id
                    
                    id = es.agregar_Empleado_bd(empleado)
                    if not(id):
                        print("Error registrar el Empleado")
                    else:
                         print("✅ registrado con exito")
                else:
                    print("El Empleado ya esta registrado")
            elif opcion == "3":
                print("-" * 45)
                print("\n📋 ACTUALIZACIÒN DE EMPLEADO")
                print("-" * 45)
                print("Ingrese DNI del empleado: ")
                dni = input("➤  ").strip().lower()
                empleado = es.obtener_Empleado_por_dni(dni)
                if empleado:
                    print(" Deje en blanco los campos que no desea actualizar.")
                    nuevo_nombre = input(f"Nombre ({Empleado.nombre}): ").strip()
                    nuevo_apellido = input(f"Apellido ({Empleado.apellido}): ").strip()
                    nuevo_email = input(f"Email ({Empleado.email}): ").strip()
                    nuevo_telefono = input(f"Teléfono ({Empleado.telefono}): ").strip()
                    Empleado.nombre = nuevo_nombre if nuevo_nombre else Empleado.nombre
                    Empleado.apellido = nuevo_apellido if nuevo_apellido else Empleado.apellido
                    Empleado.email = nuevo_email if nuevo_email else Empleado.email
                    Empleado.telefono = nuevo_telefono if nuevo_telefono else Empleado.telefono
                    if es.actualizar_Empleado_bdo(Empleado):
                        print("✔ Empleado actualizado exitosamente.")
                    else:
                        print("❌ Error al actualizar el Empleado.")
                else:
                    print("No se encontró un empleado a este DNI.")
            elif opcion == "0":
                return
            else:
                print(" Opción inválida")

        except Exception as e:
            print(f" Error: {e}")