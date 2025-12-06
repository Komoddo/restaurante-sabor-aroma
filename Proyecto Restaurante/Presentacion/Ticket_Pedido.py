from datetime import datetime
from Servicio.Cliente_Servicio import ClienteServicio
from Servicio.producto_servicio import ProductoServicio
from Servicio.Mesa_Servicio import MesaServicio
from Servicio.Pedido_Servicio import PedidoServicio
from Servicio.PedidoDetalle_Servicio import DetallePedidoServicio
from Servicio.Orden_Servicio import OrdenServicio
from Modelo.Pedido import Pedido
from Modelo.PedidoDetalle import PedidoDetalle

pes = PedidoServicio()
pds = DetallePedidoServicio()
cs = ClienteServicio()
ps = ProductoServicio()
ors = OrdenServicio()

def ticket_pedido(pedido):
    orden = ors.obtener_orden_pendiente_por_id(pedido.id_orden)
    cliente = cs.obtener_cliente_por_id(orden.id_cliente)
    """Muestra el ticket de pedido."""
    print("\n" + "-"*100)
    print(f"{'RESTAURANTE SABOR & AROMA':<50}{'ORDEN DE PEDIDO':>50}")
    print("-"*100)
    print(f"\n{'R.U.C. XXXXXXXXXXX':>100}")
    print(f"\n{'NRO. PEDIDO: ':>93}{'0'*(7-len(str(pedido.id_pedido)))+str(pedido.id_pedido)}")
    print(f"\nCliente: {cliente.nombre + ' ' + cliente.apellido:<41}{'Fecha: '+str(datetime.now().strftime('%Y-%m-%d %H:%M:%S')):>50}")
    print("\n" + "="*100)
    print(f"{'N°':<6}{'Descripción':<30} {'Cantidad':<22} {'Precio Unitario':<18} {'Subtotal':>17}")
    print("="*100)
    for i, detalle in enumerate(pedido.detalles, 1):
        producto = ps.obtener_producto_disponible_por_id(detalle.id_producto)
        print(f"{str(i)+'.':<5} {producto.nombre:<28}|      {detalle.cantidad:<15}|       {detalle.precio_unitario:<18.2f}|      {detalle.subtotal:<10.2f}")
        print("-"*100)
    print(f"\n{'Subtotal:':>75} {'S/.':>11} {pedido.subtotal:>6.2f}")
    print(f"\n{'Descuento:':>75} {'S/.':>11} {pedido.descuento:>6.2f}")
    print(f"\n{'IGV:':>75} {'S/.':>11} {pedido.impuestos:>6.2f}")
    print(f"\n{'TOTAL:':>75} {'S/.':>11} {pedido.total:>6.2f}")
    print(f"\n{'¡Gracias por confiar en nosotros!':>99}")

                            