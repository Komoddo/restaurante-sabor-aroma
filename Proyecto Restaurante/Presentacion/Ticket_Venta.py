from datetime import datetime
from Servicio.Cliente_Servicio import ClienteServicio
from Servicio.producto_servicio import ProductoServicio
from Servicio.Venta_Servicio import ventaServicio
from Servicio.VentaDetalle_Servicio import DetalleventaServicio
from Servicio.Orden_Servicio import OrdenServicio
from Modelo.Venta import Venta

pes = ventaServicio()
pds = DetalleventaServicio()
cs = ClienteServicio()
ps = ProductoServicio()
ors = OrdenServicio()

def ticket_venta(venta : Venta) -> str:
    orden = ors.obtener_orden_pendiente_por_id(venta.id_orden)
    cliente = cs.obtener_cliente_por_id(orden.id_cliente)
    """Muestra el ticket de venta."""
    print("\n" + "-"*100)
    print(f"{'RESTAURANTE SABOR & AROMA':<50}{'TICKET DE VENTA':>50}")
    print("-"*100)
    print(f"\n{'R.U.C. 11277067965':>100}")
    print(f"\n{'NRO. VENTA: ':>93}{'0'*(7-len(str(venta.id_venta)))+str(venta.id_venta)}")
    print(f"\nCliente: {cliente.nombre + ' ' + cliente.apellido:<41}{'Fecha: '+str(datetime.now().strftime('%Y-%m-%d %H:%M:%S')):>50}")
    print("\n" + "="*100)
    print(f"{'N°':<6}{'Descripción':<30} {'Cantidad':<22} {'Precio Unitario':<18} {'Subtotal':>17}")
    print("="*100)
    for i, detalle in enumerate(venta.detalles, 1):
        producto = ps.obtener_producto_disponible_por_id(detalle.id_producto)
        print(f"{str(i)+'.':<5} {producto.nombre:<28}|      {detalle.cantidad:<15}|       {detalle.precio_unitario:<18.2f}|      {detalle.subtotal:<10.2f}")
        print("-"*100)
    print(f"\n{'Subtotal:':>75} {'S/.':>11} {venta.subtotal:>6.2f}")
    print(f"\n{'Descuento:':>75} {'S/.':>11} {venta.descuento:>6.2f}")
    print(f"\n{'IGV (18%):':>75} {'S/.':>11} {venta.impuestos:>6.2f}")
    print(f"\n{'TOTAL:':>75} {'S/.':>11} {venta.total:>6.2f}")
    print(f"\n{'¡Gracias por confiar en nosotros!':>99}")
    
    # ticket = (
    # f"\n{'-'*100}"
    # f"{'RESTAURANTE SABOR & AROMA':<50}{'TICKET DE VENTA':>50}"
    # f"{'-'*100}"
    # f"\n{'R.U.C. XXXXXXXXXXX':>100}"
    # f"\n{'NRO. venta: ':>93}{'0'*(7-len(str(venta.id_venta)))+str(venta.id_venta)}"
    # f"\nCliente: {cliente.nombre + ' ' + cliente.apellido:<41}{'Fecha: '+str(datetime.now().strftime('%Y-%m-%d %H:%M:%S')):>50}"
    # f"\n{'='*100}"
    # f"{'N°':<6}{'Descripción':<30} {'Cantidad':<22} {'Precio Unitario':<18} {'Subtotal':>17}"
    # f"\n{'='*100}")
    
    # for i, detalle in enumerate(venta.detalles, 1):
    #     producto = ps.obtener_producto_disponible_por_id(detalle.id_producto)
    #     ticket += (f"{str(i)+'.':<5} {producto.nombre:<28}|      {detalle.cantidad:<15}|       {detalle.precio_unitario:<18.2f}|      {detalle.subtotal:<10.2f}"
    #     f"{'-'*100}")
        
    # ticket += (f"\n{'Subtotal:':>75} {'S/.':>11} {venta.subtotal:>6.2f}"
    # f"\n{'Descuento:':>75} {'S/.':>11} {venta.descuento:>6.2f}"
    # f"\n{'IGV:':>75} {'S/.':>11} {venta.impuestos:>6.2f}"
    # f"\n{'TOTAL:':>75} {'S/.':>11} {venta.total:>6.2f}"
    # f"\n{'¡Gracias por confiar en nosotros!':>99}"
    # )
    
    # return ticket
    

                            