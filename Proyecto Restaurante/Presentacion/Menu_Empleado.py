from Servicio.Empleado_Servicio import EmpleadoServicio
from Modelo.Empleado import Empleado
from Utilitario.Validacion import validar, TipoValidacion

es = EmpleadoServicio()

def submenu_Empleados():
        
    while True:
        es.obtener_Empleados_bd()
        """Submenú para gestión de Empleados."""
        
        print("\n" + "-"*100)
        print("👥 GESTIÓN DE EMPLEADOS")
        print("-"*100)
        print("\n1. Lista de Empleados")
        print("2. Nuevo Empleado")
        print("3. Actualizar Empleado")
        print("0. Salir")

        try:
            print("\nSeleccione una opción: ")
            opcion = input("➤  ").strip()

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
                    print("sin empleados")               
            elif opcion == "2":
                print("\n📋 MENÚ: NUEVO EMPLEADO")
                print("-" * 45)
                while True:
                    print("Ingrese DNI: ")
                    dni  = input("➤  ").strip()
                    if validar(dni, TipoValidacion.DNI):
                        break
                    print("❗ Formato de DNI inválido")
                
                if not es.obtener_Empleado_por_dni(dni):
                    
                    while True:
                        print("Ingrese el nombre: ")
                        nombre  = input("➤  ").strip()
                        if validar(nombre, TipoValidacion.NOMBRE):
                            break
                        print("❗ Formato de nombre inválido")
                        
                    while True:
                        print("Ingrese el apellido: ")
                        apellido = input("➤  ").strip()
                        if validar(apellido, TipoValidacion.NOMBRE):
                            break
                        print("❗ Formato de Apellido inválido")

                    while True:
                        print("Ingrese el número de telefono: ")
                        telefono  = input("➤  ")
                        if not telefono:
                            break
                        if validar(telefono, TipoValidacion.TELEFONO):
                            break
                        print("❗ Formato de teléfono inválido")                    
                    
                    while True:
                        print("\nCARGOS:")
                        cargos = es.crear_cargos()
                        for i, car in cargos.items():
                            print(f"{i}. {car}")
                        print(f"{len(cargos) + 1}. Nuevo cargo")

                        print("\nSeleccione un cargo")
                        cat_id = input("➤  ").strip()
                        if validar(cat_id, TipoValidacion.ENTERO):
                            cat_id = int(cat_id)
                            num_cat = len(cargos)
                            if cat_id in range(1, num_cat + 1):
                                cargo = cargos[cat_id]
                            elif cat_id == num_cat + 1:
                                print("\nNombre del nuevo cargo")
                                cargo = input("➤  ").strip()
                                if cargo=="":
                                    print("Asigne un cargo válido")
                            else:
                                print("Opción inválida")
                            break
                        print("❗ Formato de cargo inválido")
                    
                    nuevo_empleado = Empleado(
                        id=0,
                        nombre=nombre,
                        apellido=apellido,
                        dni=dni,
                        cargo=cargo,
                        telefono=telefono)
                    
                    print("\n📋 RESUMEN DEL NUEVO EMPLEADO:")
                    print(f"\n{'Nombre:':>10}  {nombre}")
                    print(f"{'Apellido:':>10}  {apellido}")
                    print(f"{'DNI:':>10}  {dni}")
                    print(f"{'Cargo:':>10}  {cargo}")
                    print(f"{'Teléfono:':>10}  {telefono}")

                    print("\n¿Confirmar agregado? (s/n): ")
                    confirmar = input("➤  ").strip().lower()
                    if confirmar == 's':
                        if es.agregar_empleado_bd(nuevo_empleado):
                            print(f"✅ Empleado agregado exitosamente")
                        else:
                            print("❌ Error registrar el Empleado")
                    else:
                        print("Cancelando...")
                else:
                    print("El Empleado ya esta registrado")
                    
            elif opcion == "3":
                """Submenú actualizacion de empleado."""
                print("\n" + "="*100)
                print("🔄 ACTUALIZACIÓN DE EMPLEADOS")
                print("="*100)
                
                while True:
                    print("\nDNI del empleado que desea modificar: ")
                    dni = input("➤  ").strip()
                    if validar(dni, TipoValidacion.DNI):
                        break
                    print("Formato de DNI inválido")                
                
                empleado = es.obtener_Empleado_por_dni(dni)
                if not empleado:
                    print("No se encontraron coincidencias.")
                    continue
                
                while True:
                    print(f"\n📋 RESUMEN DEL EMPLEADO")
                    print(f"\n1. {'Nombre:':>10}  {empleado.nombre}")
                    print(f"2. {'Apellido:':>10}  {empleado.apellido}")
                    print(f"3. {'Cargo:':>10}  {empleado.cargo}")
                    print(f"4. {'Teléfono:':>10}  {empleado.telefono}")
                    print(f"5. {'Estado:':>10}  {empleado.estado}")
                    print(f"0. ⬅️ {'Salir':>7}")
                    
                    print("\nSeleccione el dato que desea actualizar:")
                    opcion = input("➤  ").strip()
                    if opcion=="1":
                        while True:
                            print(f"Nombre nuevo")
                            nombre_nuevo = input("➤  ")
                            if validar(nombre_nuevo, TipoValidacion.NOMBRE):
                                break
                            print("Formato de nombre inválido")
                        empleado.nombre = nombre_nuevo
                        print("Actualizando nombre...")
                        
                    elif opcion=="2":
                        while True:
                            print(f"Apellido nuevo")
                            apellido_nuevo = input("➤  ")
                            if validar(apellido_nuevo, TipoValidacion.NOMBRE):
                                break
                            print("Formato de apellido inválido")
                        empleado.apellido = apellido_nuevo
                        print("Actualizando apellido...")
                        
                    elif opcion=="3":
                        while True:
                            print("\nCARGOS:")
                            cargos = es.crear_cargos()
                            for i, car in cargos.items():
                                print(f"{i}. {car}")
                            print(f"{len(cargos) + 1}. Nuevo cargo")

                            print("\nSeleccione un cargo:")
                            cat_id = input("➤  ").strip()
                            if validar(cat_id, TipoValidacion.ENTERO):
                                cat_id = int(cat_id)
                                num_cat = len(cargos)
                                if cat_id in range(1, num_cat + 1):
                                    cargo = cargos[cat_id]
                                elif cat_id == num_cat + 1:
                                    print("\nNombre del nuevo cargo")
                                    cargo = input("➤  ").strip()
                                    if cargo=="":
                                        print("Asigne un cargo válido")
                                else:
                                    print("Opción inválida")
                                empleado.cargo = cargo
                                break
                            print("❗ Formato de cargo inválido")
                    elif opcion=="4":
                        while True:
                            print(f"Teléfono nuevo: ")
                            telefono_nuevo = input("➤  ").strip()
                            if validar(telefono_nuevo, TipoValidacion.TELEFONO):
                                break
                            print("Formato de teléfono inválido")
                        empleado.telefono = telefono_nuevo
                        print("Actualizando Teléfono...")
                    elif opcion=="5":
                        while True:
                            print("\nESTADOS:\n")
                            estados = es.crear_estados()
                            for i, est in estados.items():
                                print(f"{i}. {est}")

                            print("\nSeleccione un estado:")
                            est_id = input("➤  ").strip()
                            if validar(est_id, TipoValidacion.ENTERO):
                                est_id = int(est_id)
                                num_est = len(estados)
                                if est_id in range(1, num_est + 1):
                                    estado = estados[est_id]
                                else:
                                    print("Opción inválida")
                                empleado.estado = estado
                                break
                            print("❗ Formato de estado inválido")
                    elif opcion=="0":
                        print("¿Desea guardar los cambios realizados? (s/n):")
                        respuesta = input("➤  ").strip().lower()
                        if respuesta=="s":
                            if es.actualizar_Empleado_bd(empleado):
                                print("✔️ empleado actualizado con exito")
                                break
                            else:
                                print("❌ Error al actualizar el empleado")
                                break
                        else:
                            print("🚶‍♂️ Cancelando cambios...")
                            break
                    else:
                        print("Respuesta inválida")
            elif opcion == "0":
                return
            else:
                print(" Opción inválida")

        except Exception as e:
            print(f" Error: {e}")
            
        finally:
            es.obtener_Empleados_bd()