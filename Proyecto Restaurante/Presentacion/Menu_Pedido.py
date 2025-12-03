import datetime
from Servicio.Cliente_Servicio import ClienteServicio
from Servicio.Mesa_Servicio import MesaServicio
from Servicio.Pedido_Servicio import PedidoServicio
from Servicio.Orden_Servicio import OrdenServicio
from Servicio.OrdenDetalle_Servicio import OrdenDetalleServicio
from Modelo.Pedido import Pedido
from Modelo.PedidoDetalle import PedidoDetalle

ps = PedidoServicio()
os = OrdenServicio()
ms = MesaServicio()
cs = ClienteServicio()

"""Irterfaz para la gestion de los pedidos"""
def menu_pedidos():
    while True:
        print("\n🍽 MENÚ DE PEDIDOS")
        print("1. Generar pedido desde orden")
        print("2. Ver pedidos recientes")
        print("0. Volver")

        opcion = input("Opción: ")
        if opcion == "1":
            print("\n👥 LISTA DE ORDENES PENDIENTES")
            print("-" * 90)
            print(f"{'Mesa':<15}    {'Cliente':<30}    {'Fecha':<18}     {'Total':>10}")
            print("-" * 90)
            pendientes = os.obtener_ordenes_pendientes()
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
                    orden = os.obtener_orden_pendiente_por_id(int(id))
                    if orden:
                        mesa = ms.obtener_mesa_por_id(orden.id_mesa)
                        cliente = cs.obtener_cliente_por_id(orden.id_cliente)
                        print(f"\n🛒 ORDEN N° {orden.id_orden} MESA {mesa.numero}")
                        print("-"*80)
                        print(f"Fecha: {datetime.strptime(orden.fecha_hora, '%Y-%m-%d %H:%M:%S')}")
                        print(f"Cliente: {cliente.nombre} {cliente.apellido}")
                        print(f"Mesa asignada: {mesa.numero:<10} Nro. personas: {orden.nro_personas:<10}")
                        print(f"Estado: {orden.estado}")
                        print("="*80)

                        print(f"Desea generar un pedido de la orden {orden.id_orden}? (s/n): ")
                        opcion = input("➤  ").strip().lower()
                        if opcion=="s":
                            
                            # Actualizamos informacion de orden
                            if os.actualizar_estado_pedido_bd(orden.id_orden, "preparado"):
                                if ms.actualizar_estado_mesa_bd(orden.id_mesa, "disponible"):
                                    if ps.agregar_pedido_bd(pedido):
                                print(f"✅ orden {orden.id_orden} cancelada con éxito")
                            else:
                                print("⚠️ Error al cancelar la orden")
                        else: continue

                        """Muestra el ticket de pedido."""
                        print("\n" + "="*60)
                        print("🐾 VETERINARIA HUELLITAS - TICKET DE VENTA")
                        print("="*60)
                        print(f"Fecha: {venta['fecha'].strftime('%d/%m/%Y %H:%M:%S')}")
                        print(f"Cliente: {venta['cliente']}")
                        print("-" * 60)

                        for nombre, precio, cantidad, _ in venta["items"]:
                            subtotal = precio * cantidad
                            print(f"{nombre:<35} {cantidad:>3} x S/{precio:>6.2f} = S/{subtotal:>8.2f}")

                        print("-" * 60)
                        print(f"Subtotal: {venta['subtotal']:>46.2f}")
                        if venta['descuento_pct'] > 0:
                            descuento_monto = venta['subtotal'] - venta['total']
                            print(f"Descuento ({venta['descuento_pct']:.0f}%): {descuento_monto:>38.2f}")
                        print(f"TOTAL: S/{venta['total']:>45.2f}")
                        print("="*60)
                        print("¡Gracias por confiar en nosotros! 🐾")
        elif opcion == "2":
            pedidos = pedido_servicio.listar()

            print("\nLISTA DE PEDIDOS")
            for p in pedidos:
                print(f"- Pedido {p.id_pedido}  Total: S/{p.total}  Estado: {p.estado}")

        elif opcion == "0":
            break
        else:
            print("Opción no válida.")
