from datetime import datetime
from Servicio.Cliente_Servicio import ClienteServicio
from Servicio.producto_servicio import ProductoServicio
from Servicio.Mesa_Servicio import MesaServicio
from Servicio.Pedido_Servicio import PedidoServicio
from Servicio.PedidoDetalle_Servicio import DetallePedidoServicio
from Servicio.Orden_Servicio import OrdenServicio
from Modelo.Pedido import Pedido
from Modelo.PedidoDetalle import PedidoDetalle
from Presentacion.Ticket_Pedido import ticket_pedido

pes = PedidoServicio()
pds = DetallePedidoServicio()
ors = OrdenServicio()
ms = MesaServicio()
cs = ClienteServicio()
ps = ProductoServicio()


"""Irterfaz para la gestion de los pedidos"""
def menu_pedido():
    while True:
        
        
        print("\n🍽 MENÚ DE PEDIDOS")
        print("1. Generar pedido desde orden")
        print("2. Ver pedidos recientes")
        print("0. Volver")

        opcion = input("Opción: ")       
        
        if opcion == "1":
            ors.obtener_ordenes_bd()
            print("\n👥 LISTA DE ORDENES PENDIENTES")
            print("-" * 90)
            print(f"{'Mesa':<15}    {'Cliente':<30}    {'Fecha':<18}     {'Total':>10}")
            print("-" * 90)
            pendientes = ors.obtener_ordenes_pendientes()
            if pendientes:
                for op in pendientes:
                    mesa = ms.obtener_mesa_por_id(op.id_mesa)
                    cliente = cs.obtener_cliente_por_id(op.id_cliente)
                    print(f"mesa {mesa.numero:<12} | {cliente.nombre} {cliente.apellido:<26} | {op.fecha_hora:<24} | S/{op.total:>6.2f}")
                print("0. Regresar")
                print("\nSeleccione la mesa: ")
                id = input("➤  ").strip().lower()
                
                if (id == "0"):
                    print("Saliendo...")
                    break
                else:
                    orden = ors.obtener_orden_pendiente_por_id(int(id))
                    if orden:
                        mesa = ms.obtener_mesa_por_id(orden.id_mesa)
                        print("\n" + "="*80)
                        cliente = cs.obtener_cliente_por_id(orden.id_cliente)
                        print(f"🛒 ORDEN N° {orden.id_orden} MESA {mesa.numero}")
                        print("="*80)
                        print(f"Fecha: {datetime.strptime(orden.fecha_hora, '%Y-%m-%d %H:%M:%S')}")
                        print(f"Cliente: {cliente.nombre} {cliente.apellido}")
                        print(f"Mesa asignada: {mesa.numero:<10} Nro. personas: {orden.nro_personas:<10}")
                        print(f"Estado: {orden.estado}")

                        print(f"\nDesea generar un pedido de la orden {orden.id_orden}? (s/n): ")
                        opcion = input("➤  ").strip().lower()
                        
                        if opcion=="s":
                            pedido_nuevo = Pedido(
                                id_pedido=0,
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
                                    pedido_nuevo.agregar_detalle(PedidoDetalle(
                                        id_detalle=0,
                                        id_pedido=0,
                                        id_producto=do.id_producto,
                                        cantidad=do.cantidad,
                                        precio_unitario=do.precio_unitario
                                ))
                                
                            pedido_nuevo.id_pedido = pes.crear_pedido_bd(pedido_nuevo)
                            if pedido_nuevo.id_pedido:
                                for detalle in pedido_nuevo.detalles:
                                    detalle.id_pedido = pedido_nuevo.id_pedido
                                if pds.agregar_detalles_bd(pedido_nuevo.detalles):
                                    if ors.actualizar_estado_orden_bd(orden.id_orden, "preparado"):
                                         if ms.actualizar_estado_mesa_bd(orden.id_mesa, "disponible"):
                                            print("✅ Pedido creado con éxito")
                            else:
                                print("⚠️ Error al crear el pedido")
                            
                            ticket_pedido(pedido_nuevo)
                        else: continue
        elif opcion == "2":
            """Muestra la lista completa pedidos."""
            pes.obtener_pedidos_bd()
            
            print("\n")
            print("LISTA DE PEDIDOS")
            print("="*100)
            print(f"{'ID':<5}{'Orden':<10}{'Subtotal':<12}{'IGV':<10}{'Descuento':<15}{'Total':<12}{'Método Pago':<18}{'Estado':<10}{'Fecha':>8}")
            print("="*100)
            pedidos = pes.obtener_lista_pedidos()
            if pedidos:
                for p in pedidos:
                    print(f"► {p.id_pedido:<5}{p.id_orden:<5}|  {p.subtotal:<8.2f}|  {p.impuestos:<10.2f}|  {p.descuento:<10.2f}|  {p.total:<10.2f}|  {p.metodo_pago:<15}|  {('🟢' if p.estado.lower()=='pagado' else '🔴'):<5}{datetime.strptime(p.fecha,'%Y-%m-%d %H:%M:%S').date()}")
            else:
                print("No hay productos registrados")  

        elif opcion == "0":
            break
        else:
            print("Opción no válida.")
