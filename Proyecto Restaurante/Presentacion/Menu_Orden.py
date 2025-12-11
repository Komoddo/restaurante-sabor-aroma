from datetime import datetime       # Permite manejar fechas y horas en las órdenes

# Importa servicios necesarios para gestionar mesas, órdenes, productos, etc.
from Servicio.Mesa_Servicio import MesaServicio
from Servicio.Orden_Servicio import OrdenServicio
from Servicio.OrdenDetalle_Servicio import OrdenDetalleServicio
from Servicio.Cliente_Servicio import ClienteServicio
from Servicio.producto_servicio import ProductoServicio

# Importa modelos y submenús utilizados dentro del flujo de creación de órdenes
from Modelo.Orden import Orden
from Presentacion.SubMenu_nueva_Orden import submenu_nuevaOrden
from Presentacion.Catalogo_Productos import catalogo_productos
from Presentacion.SubMenu_Seleccion_Mesa import submenu_seleccionMesa

# Instancia de cada servicio necesario para operar en el sistema
ms = MesaServicio()           # Servicio para gestionar mesas
ps = ProductoServicio()       # Servicio para gestionar productos
cs = ClienteServicio()        # Servicio para gestionar clientes
os = OrdenServicio()          # Servicio para gestionar órdenes
ods = OrdenDetalleServicio()  # Servicio para gestionar detalles de órdenes

def menu_orden():
    """Menú principal para la gestión de órdenes del sistema."""

    os.obtener_ordenes_bd()   # Carga todas las órdenes desde la base de datos
    nueva_orden = Orden()     # Crea una orden vacía para iniciar el flujo

    while True:
        # --- INTERFAZ DEL MENÚ ---
        print("\n" + "-"*100)
        print("🧾 MENÚ DE ÓRDENES")
        print("-"*100)
        print("\n1. Crear nueva orden")
        print("2. Agregar productos a la orden")
        print("3. Ver detalles de la orden")
        print("4. Finalizar nueva orden")
        print("5. Gestionar órdenes pendientes")
        print("0. Volver")
        
        print("\nSeleccione una opción: ")
        opcion = input("➤  ").strip()

        # 1. CREAR NUEVA ORDEN
        if opcion == "1":
            
            try:
                 # Abre submenú donde se elige mesa, cliente y personas
                nueva_orden = submenu_nuevaOrden()

                # Si se creó correctamente la orden
                if(nueva_orden.id_orden):
                    print(f"\n{'✅'} Orden {nueva_orden.id_orden} en la mesa Nro. {ms.obtener_mesa_por_id(nueva_orden.id_mesa).numero}")
            except Exception as e:
                print(f"\n{'⚠️'} Ocurrió un error:", e)

            finally:
                # Se actualiza la información local para mantener coherencia
                ms.obtener_mesas_bd()   
        # 2. AGREGAR PRODUCTOS A LA ORDEN
        elif opcion == "2":
            if(nueva_orden.id_orden):                           # Verifica que exista una orden activa
                detalles = catalogo_productos()                 # Abre catálogo y devuelve detalles seleccionados
                if(detalles):
                    nueva_orden.detalles.clear()                # Limpia los detalles actuales
                    nueva_orden.agregar_detalles(detalles)      # Añade los nuevos detalles
                    ods.agregar_detalles_bd(detalles)           # Guarda detalles en la BD
                    os.actualizar_total_orden_bd(nueva_orden)   # Recalcula el total de la orden
                    print("\n✔ Productos agregados a la orden.")
            else:
                print("\nNo existe una orden asociada. Primero cree una orden")   
        # 3. MOSTRAR DETALLES DE LA ORDEN       
        elif opcion == "3":
            """Muestra el contenido actual de la orden"""
            # Validaciones básicas
            if not nueva_orden.id_orden:
                print("\nCree una orden para continuar")
                continue
            if not nueva_orden.detalles:
                print("\n🛒 La orden esta vacia. Agregue productos para visualizarlos")
                continue
            cliente = cs.obtener_cliente_por_id(nueva_orden.id_cliente)
            mesa = ms.obtener_mesa_por_id(nueva_orden.id_mesa)

            # --- ENCABEZADO ---
            print("\n" + "="*80)
            print(f"🛒 ORDEN NRO. {nueva_orden.id_orden}")
            print(f"Fecha: {datetime.strptime(nueva_orden.fecha_hora, '%Y-%m-%d %H:%M:%S')}")
            print(f"Cliente: {cliente.nombre} {cliente.apellido}")
            print(f"Mesa asignada: {mesa.numero:<10} Nro. personas: {nueva_orden.nro_personas:<10}")
            print(f"Estado: {nueva_orden.estado}")
            print("="*80)

            # --- DETALLES DE PRODUCTOS ---
            for detalle in nueva_orden.detalles:
                producto = ps.obtener_producto_disponible_por_id(detalle.id_producto)
                print(f"• {producto.nombre:<25} |  {detalle.nota if detalle.nota else 'sin detalles':<30}  |  S/{detalle.precio_unitario:>6.2f} x {detalle.cantidad} = S/{detalle.subtotal:>8.2f}")
            print("-" * 80)
            print(f"\nTOTAL: S/{nueva_orden.total:.2f}")
            print("\n¡Gracias por confiar en nosotros!")
            print("="*80)
        # 4. CERRAR ORDEN (FINALIZAR CREACIÓN)   
        elif opcion == "4":
                if not nueva_orden.id_orden:
                    print("\nNo existe una orden creada")
                print(f"\n✔ Orden creada {nueva_orden.id_orden}")
                break        
        # 5. GESTIONAR ÓRDENES PENDIENTES
        elif opcion == "5":

            while True:
                print("\n👥 LISTA DE ORDENES PENDIENTES")
                print("-" * 100)
                print(f"{'ID':<8} {'Mesa':<15}    {'Cliente':<30}    {'Fecha':<18}     {'Total':>10}")
                print("-" * 100)
                pendientes = os.obtener_ordenes_pendientes()
                if pendientes:
                    # Imprime cada orden pendiente
                    for op in pendientes:
                        mesa = ms.obtener_mesa_por_id(op.id_mesa)
                        cliente = cs.obtener_cliente_por_id(op.id_cliente)
                        print(f"{op.id_orden:<6}  mesa {mesa.numero:<12} | {cliente.nombre} {cliente.apellido:<26} | {op.fecha_hora:<24} | S/{op.total:>6.2f}")
                    print("0. Regresar")

                    print("\nSeleccione una orden: ")
                    id = input("➤  ").strip().lower()
                    if (id == "0"):
                        print("\nSaliendo...")
                        break
                    else:
                        while True:
                            orden = os.obtener_orden_pendiente_por_id(int(id))
                            if orden:
                                mesa = ms.obtener_mesa_por_id(orden.id_mesa)
                                cliente = cs.obtener_cliente_por_id(orden.id_cliente)
                                
                                print("\n" + "-"*80)
                                print(f"🛒 ORDEN PENDIENTE N° {orden.id_orden} MESA {mesa.numero}")
                                print("-"*80)
                                print(f"\nFecha: {datetime.strptime(orden.fecha_hora, '%Y-%m-%d %H:%M:%S')}")
                                print(f"Cliente: {cliente.nombre} {cliente.apellido}")
                                print(f"Mesa asignada: {mesa.numero:<10} Nro. personas: {orden.nro_personas:<10}")
                                print(f"Estado: {orden.estado}")

                                 # --- SUBMENÚ DE ÓRDENES PENDIENTES ---
                                print("\n1. Ver detalles")
                                print("2. Reasignar mesa")
                                print("3. Reasignar detalles")
                                print("4. Cancelar orden")
                                print("0. Volver")

                                print("\nSeleccione una opción: ")
                                opcion = input("➤  ").strip().lower()
                                try:
                                     # Mostrar detalles
                                    if opcion == "1":
                                        print("="*80)
                                        if not (orden.detalles):
                                            print("Sin detalles")
                                            print("="*80)
                                            continue
                                        for detalle in orden.detalles:
                                            producto = ps.obtener_producto_disponible_por_id(detalle.id_producto)
                                            print(f"• {producto.nombre:<25} |  {detalle.nota if detalle.nota else 'sin detalles*':<30}  |  S/{detalle.precio_unitario:>6.2f} x {detalle.cantidad} = S/{detalle.subtotal:>8.2f}")
                                        print("-" * 80)
                                        print(f"TOTAL: S/{orden.total:.2f}")

                                     # Reasignar mesa
                                    elif opcion == "2":
                                        _orden = submenu_seleccionMesa()
                                        if _orden:
                                            ms.actualizar_estado_mesa_bd(orden.id_mesa, "disponible")
                                            orden.id_mesa=_orden.id_mesa
                                            orden.nro_personas=_orden.nro_personas
                                            ms.actualizar_estado_mesa_bd(orden.id_mesa, "ocupado")
                                            if os.actualizar_orden_bd(orden):
                                                print("✅ Orden actualizada")

                                    # Reasignar detalles (aún no implementado)           
                                    elif opcion == "3": pass
                                        # if(nueva_orden.id_orden):
                                        #     detalles = catalogo_productos()
                                        #     if(detalles):
                                        #         nueva_orden.detalles.clear()
                                        #         nueva_orden.agregar_detalles(detalles)
                                        #         ods.agregar_detalles_bd(detalles)
                                        #         os.actualizar_total_orden_bd(nueva_orden)
                                        #         print("✔ Productos agregados a la orden.")
                                        # else:
                                        #     print("No existe una orden asociada. Primero cree una orden")

                                    # Cancelar orden
                                    elif opcion == "4":
                                        print(f"\nSeguro que desea cancelar la orden de la mesa {mesa.numero}? (s/n): ")
                                        opcion = input("➤  ").strip().lower()
                                        if opcion=="s":
                                            if os.actualizar_estado_orden_bd(orden.id_orden, "cancelado"):
                                                ms.actualizar_estado_mesa_bd(orden.id_mesa, "disponible")
                                                print(f"\n✅ orden {orden.id_orden} cancelada con éxito")
                                            else:
                                                print("\n⚠️ Error al cancelar la orden")
                                        else: 
                                            continue
                                    elif opcion == "0":
                                        break
                                except Exception as e:
                                    print("\nOcurrió un error:", e)
                                finally:
                                     # Actualiza datos locales tras cada operación
                                    os.obtener_ordenes_bd()
                                    ms.obtener_mesas_bd()
                                    cs.obtener_clientes_bd()
                            else:
                                break  
                else:
                    print("\nNo hay ordenes pendientes registradas")
                    break
      # 0. SALIR DEL MENÚ
        elif opcion == "0": break
        # OPCIÓN INVÁLIDA
        else:
            print("\nOpción inválida.")
