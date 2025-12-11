from datetime import datetime                                       # Para manejar fechas y horas
from Servicio.Cliente_Servicio import ClienteServicio               # Servicio que maneja operaciones sobre clientes
from Servicio.Mesa_Servicio import MesaServicio                     # Servicio que maneja operaciones sobre mesas
from Servicio.Venta_Servicio import ventaServicio                 # Servicio que maneja operaciones sobre ventas
from Servicio.Orden_Servicio import OrdenServicio                   # Servicio que maneja operaciones sobre órdenes
from Servicio.VentaDetalle_Servicio import DetalleventaServicio
from Modelo.Venta import Venta                                    # Modelo venta: estructura de datos del venta
from Modelo.VentaDetalle import ventaDetalle                      # Modelo ventaDetalle: estructura de los detalles de venta
from Servicio.producto_servicio import ProductoServicio
from Presentacion.Ticket_Venta import ticket_venta
from Utilitario.Validacion import validar, TipoValidacion

ves = ventaServicio()        # Instancia para gestionar ventas 
vds = DetalleventaServicio()
ors = OrdenServicio()         # Instancia para gestionar órdenes
ms = MesaServicio()          # Instancia para gestionar mesas
cs = ClienteServicio()       # Instancia para gestionar clientes
ps = ProductoServicio()


"""Irterfaz para la gestion de los ventas"""
def menu_venta():
    while True:
        ors.obtener_ordenes_bd()
        print("\n" + "-"*100)
        print("🍽 MENÚ DE VENTAS")
        print("-"*100)
        print("\n1. Generar venta desde orden")
        print("2. Ver ventas recientes")
        print("3. Anular venta")
        print("0. Volver")
        print("\n" + "-"*100)
        
        print("\nSeleccione una opción: ")
        opcion = input("➤  ").strip()    
        
        if opcion == "1":
            print("\n👥 LISTA DE ORDENES PENDIENTES")
            print("-" * 90)
            print(f"{'Mesa':<15}    {'Cliente':<30}    {'Fecha':<18}     {'Total':>10}")
            print("-" * 90)
            pendientes = ors.obtener_ordenes_pendientes() # Obtener todas las órdenes pendientes
            if pendientes:
                for op in pendientes:
                    mesa = ms.obtener_mesa_por_id(op.id_mesa)   # Obtener información de la mesa
                    cliente = cs.obtener_cliente_por_id(op.id_cliente)   # Obtener información del cliente
                    print(f"mesa {mesa.numero:<12} | {cliente.nombre} {cliente.apellido:<26} | {op.fecha_hora:<24} | S/{op.total:>6.2f}")
                print("0. Regresar")
                
                while True:
                    print("\nSeleccione la mesa: ")
                    nro_mesa = input("➤  ").strip().lower()
                    if validar(nro_mesa, TipoValidacion.ENTERO):
                        nro_mesa = int(nro_mesa)
                        break
                    print("Ingrese un número válido")
                
                if (nro_mesa==0):
                    print("Saliendo...")
                    break
                else:
                    mesa = ms.obtener_mesa_por_numero(nro_mesa)
                    orden = ors.obtener_orden_pendiente_por_mesa_id(mesa.id_mesa)
                    if orden:
                        
                        print("\n" + "="*80)
                        cliente = cs.obtener_cliente_por_id(orden.id_cliente)

                        # Mostrar detalles de la orden seleccionada
                        print(f"\n🛒 ORDEN N° {orden.id_orden} MESA {mesa.numero}")
                        print("-"*80)
                        print(f"Fecha: {datetime.strptime(orden.fecha_hora, '%Y-%m-%d %H:%M:%S')}")
                        print(f"Cliente: {cliente.nombre} {cliente.apellido}")
                        print(f"Mesa asignada: {mesa.numero:<10} Nro. personas: {orden.nro_personas:<10}")
                        print(f"Estado: {orden.estado}")


                        # Confirmar si se desea generar venta desde esta orden
                        print(f"Desea generar un venta de la orden {orden.id_orden}? (s/n): ")
                        opcion = input("➤  ").strip().lower()
                        
                        if opcion=="s":
                            venta_nuevo = Venta(
                                id_venta=0,
                                id_orden = orden.id_orden,
                                fecha=None,
                                subtotal = orden.total,
                                impuestos = 0.0,
                                descuento = 0.0,
                                total = 0.0,
                                metodo_pago = "efectivo",
                                estado = "pagado"
                                )
                                                      
                            for do in orden.detalles:
                                    venta_nuevo.agregar_detalle(ventaDetalle(
                                        id_detalle=0,
                                        id_venta=0,
                                        id_producto=do.id_producto,
                                        cantidad=do.cantidad,
                                        precio_unitario=do.precio_unitario,
                                        subtotal=do.subtotal
                                ))
                                
                            venta_nuevo.id_venta = ves.crear_venta_bd(venta_nuevo)
                            if venta_nuevo.id_venta:
                                for detalle in venta_nuevo.detalles:
                                    detalle.id_venta = venta_nuevo.id_venta
                                if vds.agregar_detalles_bd(venta_nuevo.detalles):
                                    if ors.actualizar_estado_orden_bd(orden.id_orden, "preparado"): # Actualizar estado de la orden y de la mesa
                                         if ms.actualizar_estado_mesa_bd(orden.id_mesa, "disponible"):
                                            # ves.guardar_venta_archivo(ticket)
                                            print("\n✅ venta creado con éxito")
                                            ticket_venta(venta_nuevo)
                            else:
                                print("⚠️ Error al crear el venta")
                        else: continue
        
        elif opcion == "2":
            """Muestra la lista completa ventas."""
            ves.obtener_ventas_bd()
            
            print("\n")
            print(f"{'LISTA DE VENTAS'}{'Pagado 🟢':>71} {'Anulado 🔴'}")
            print("="*100)
            print(f"{'ID':<5}{'Mesa':<10}{'Subtotal':<12}{'IGV':<10}{'Descuento':<15}{'Total':<12}{'Método Pago':<18}{'Estado':<10}{'Fecha':>8}")
            print("="*100)
            ventas = ves.obtener_lista_ventas()
            if ventas:
                for p in ventas:
                    orden = ors.obtener_orden_por_id(p.id_orden)
                    mesa = ms.obtener_mesa_por_id(orden.id_mesa)
                    print(f"{p.id_venta}{'.':<3} Mesa {mesa.numero:<3}|{p.subtotal:>7.2f}   |{p.impuestos:>6.2f}   |{p.descuento:>7.2f}    |{p.total:>9.2f}    |    {p.metodo_pago:<14}|   {('🟢' if p.estado.lower()=='pagado' else '🔴'):<6}{datetime.strptime(p.fecha,'%Y-%m-%d %H:%M:%S').date()}")
            else:
                print("No hay ventas registradas")  

        elif opcion == "3":
            break
        elif opcion == "0":
            break
        else:
            print("Opción no válida.")
