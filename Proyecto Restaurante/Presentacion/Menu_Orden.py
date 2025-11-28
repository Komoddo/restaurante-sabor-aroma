from datetime import datetime
from Servicio.Mesa_Servicio import MesaServicio
from Servicio.Orden_Servicio import OrdenServicio
from Servicio.OrdenDetalle_Servicio import OrdenDetalleServicio
from Servicio.Cliente_Servicio import ClienteServicio
from Servicio.producto_servicio import ProductoServicio
from Modelo.Orden import Orden
from Presentacion.SubMenu_nueva_Orden import submenu_nuevaOrden
from Presentacion.Catalogo_Productos import catalogo_productos
from Presentacion.subMenu_Seleccion_Mesa import submenu_seleccionMesa


ms = MesaServicio()
ps = ProductoServicio()
cs = ClienteServicio()
os = OrdenServicio()
ods = OrdenDetalleServicio()

def menu_ordenes():

    os.obtener_ordenes_bd()
    nueva_orden = Orden()

    while True:
        print("\n🧾 MENÚ DE ÓRDENES")
        print("1. Crear nueva orden")
        print("2. Agregar productos a la orden")
        print("3. Ver detalles de la orden")
        print("4. Cerrar nueva orden")
        print("5. Gestionar órdenes pendientes")
        print("0. Volver")

        opcion = input("Seleccione: ")

        if opcion == "1":
            
            try:
                nueva_orden = submenu_nuevaOrden()
                if(nueva_orden.id_orden):
                    print(f"{' ☑️ '} Orden {nueva_orden.id_orden} en la mesa Nro. {ms.obtener_mesa_por_id(nueva_orden.id_mesa).numero}")
            except Exception as e:
                print(f"{' ⚠️ '} Ocurrió un error:", e)

            finally:
                ms.obtener_mesas_bd()
                cs.obtener_clientes_bd()   
        elif opcion == "2":
            if(nueva_orden.id_orden):
                detalles = catalogo_productos()
                if(detalles):
                    nueva_orden.detalles.clear()
                    nueva_orden.agregar_detalles(detalles)
                    ods.agregar_detalles_bd(detalles)
                    os.actualizar_total_orden_bd(nueva_orden)
                    print("✔ Productos agregados a la orden.")
            else:
                print("No existe una orden asociada. Primero cree una orden")          
        elif opcion == "3":
            """Muestra el contenido actual de la orden"""
            if not nueva_orden.id_orden:
                print("Cree una orden para continuar")
                continue
            if not nueva_orden.detalles:
                print("🛒 La orden esta vacia. Agregue productos para visualizarlos")
                continue
            cliente = cs.obtener_cliente_por_id(nueva_orden.id_cliente)
            mesa = ms.obtener_mesa_por_id(nueva_orden.id_mesa)
            print("\n" + "="*80)
            print(f"🛒 ORDEN NRO. {nueva_orden.id_orden}")
            print(f"Fecha: {datetime.strptime(nueva_orden.fecha_hora, '%Y-%m-%d %H:%M:%S')}")
            print(f"Cliente: {cliente.nombre} {cliente.apellido}")
            print(f"Mesa asignada: {mesa.numero:<10} Nro. personas: {nueva_orden.nro_personas:<10}")
            print(f"Estado: {nueva_orden.estado}")
            print("="*80)
            for detalle in nueva_orden.detalles:
                producto = ps.obtener_producto_disponible_por_id(detalle.id_producto)
                print(f"• {producto.nombre:<25} |  {detalle.nota if detalle.nota else 'sin detalles':<30}  |  S/{detalle.precio_unitario:>6.2f} x {detalle.cantidad} = S/{detalle.subtotal:>8.2f}")
            print("-" * 80)
            print(f"TOTAL: S/{nueva_orden.total:.2f}")
            print("¡Gracias por confiar en nosotros!")
            print("="*80)
        elif opcion == "4":
                if not nueva_orden.id_orden:
                    print("No existe una orden creada")
                print(f"✔ Orden creada {nueva_orden.id_orden}")
                break
        elif opcion == "5":

            while True:
                print("\n👥 LISTA DE ORDENES PENDIENTES")
                print("-" * 90)
                print(f"{'ID':<8} {'Mesa':<15}    {'Cliente':<30}    {'Fecha':<18}     {'Total':>10}")
                print("-" * 90)
                pendientes = os.obtener_ordenes_pendientes()
                if pendientes:
                    for op in pendientes:
                        mesa = ms.obtener_mesa_por_id(op.id_mesa)
                        cliente = cs.obtener_cliente_por_id(op.id_cliente)
                        print(f"{op.id_orden:<6}  mesa {mesa.numero:<12} | {cliente.nombre} {cliente.apellido:<26} | {op.fecha_hora:<24} | S/{op.total:>6.2f}")
                    print("0. Regresar")

                    print("\nSeleccione una orden: ")
                    id = input("➤  ").strip().lower()
                    if (id == "0"):
                        print("Saliendo...")
                        break
                    else:
                        orden = os.obtener_orden_pendiente_por_id(int(id))
                        if orden:
                            while True:
                                mesa = ms.obtener_mesa_por_id(orden.id_mesa)
                                cliente = cs.obtener_cliente_por_id(orden.id_cliente)

                                print(f"\n🛒 ORDEN PENDIENTE N° {orden.id_orden} MESA {mesa.numero}")
                                print("-"*80)
                                print(f"Fecha: {datetime.strptime(orden.fecha_hora, '%Y-%m-%d %H:%M:%S')}")
                                print(f"Cliente: {cliente.nombre} {cliente.apellido}")
                                print(f"Mesa asignada: {mesa.numero:<10} Nro. personas: {orden.nro_personas:<10}")
                                print(f"Estado: {orden.estado}")
                                print("="*80)
                                print("\n1. Ver detalles")
                                print("2. Reasignar mesa")
                                print("3. Reasignar detalles")
                                print("4. cancelar orden")
                                print("0. Volver")

                                print("\nSeleccione una opción: ")
                                opcion = input("➤  ").strip().lower()
                                try:
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
                                    elif opcion == "2":
                                        _orden = submenu_seleccionMesa()
                                        if _orden:
                                            ms.actualizar_estado(orden.id_mesa, "disponible")
                                            orden.id_mesa=_orden.id_mesa
                                            orden.nro_personas=_orden.nro_personas
                                            ms.actualizar_estado(orden.id_mesa, "ocupado")
                                            if os.actualizar_orden_bd(orden):
                                                print("✅ Orden actualizada")
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
                                    elif opcion == "4":
                                        print(f"Seguro que desea cancelar la orden de la mesa {mesa.numero}? (s/n): ")
                                        opcion = input("➤  ").strip().lower()
                                        if opcion=="s":
                                            if os.actualizar_estado(orden.id_orden, "cancelado"):
                                                ms.actualizar_estado(orden.id_mesa, "disponible")
                                                print(f"✅ orden {orden.id_orden} cancelada con éxito")
                                            else:
                                                print("⚠️ Error al cancelar la orden")
                                        else: continue
                                    elif opcion == "0": break

                                except Exception as e:
                                    print("Ocurrió un error:", e)
                                finally:
                                    os.obtener_ordenes_bd()
                                    ms.obtener_mesas_bd()
                                    cs.obtener_clientes_bd()
                        else:
                            print("Error al consultar la orden seleccionada")   
                else:
                    print("No hay productos registrados")
        elif opcion == "0": break
        else:
            print("Opción inválida.")
