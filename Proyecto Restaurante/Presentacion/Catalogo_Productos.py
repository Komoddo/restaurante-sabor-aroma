from Modelo import Producto
from Modelo.OrdenDetalle import OrdenDetalle
from Servicio.producto_servicio import ProductoServicio
from Servicio.Orden_Servicio import OrdenServicio
from Servicio.OrdenDetalle_Servicio import OrdenDetalleServicio

ps = ProductoServicio()
ods = OrdenDetalleServicio()

def catalogo_productos():
    while True:
        print("\n" + "="*45)
        print("SELECCION DE PRODUCTOS")
        print("="*45)
        print("1. Ver Carta de productos")
        print("2. Buscar producto")
        print("3. Quitar producto")
        print("0. Salir")
        print("-"*45)
        
        opcion = input("Seleccione una opción: ")
        
        if opcion == "1":
            """Muestra el catálogo completo de productos."""
            print("\n")
            print("CATÁLOGO PRODUCTOS")
            print("="*90)
            print(f"{'ID':<6}{'Nombre':<25}{'Descripción':<40}{'Precio':>10}")
            estructura = ps.obtener_catalogo()
            if(estructura):
                for categoria, items in estructura.items():
                    print("="*90)
                    print(f"📋 {categoria.upper()}")
                    print("=" * 90)
                    for p in items:
                        print(f"{'0' if p.id_producto<1<0 else ''}{p.id_producto}{'.':<3}{p.nombre:<25} | {p.descripcion:<40} | S/{p.precio:>6.2f}")
                        # print("-"*90)
            else:
                print("sin productos*")
            print("0. <- REGRESAR")

            id = input(f"➡️ Seleccione un producto: ").strip()
            if (id == "0"):
                print("Cancelando selección de productos...")
            else:
                producto_seleccionado = ps.obtener_producto_disponible_por_id(int(id))
                if(producto_seleccionado):
                    if ods.validar_detalle_existente(producto_seleccionado.id_producto):
                        print("El producto ya fue agregado anteriormente ¿Desea actualizar la cantidad? (S/N)")
                        respuesta = input("➤  ").strip().lower()
                        if respuesta == "s":
                            cantidad = int(input(f"Ingrese la nueva cantidad de {producto_seleccionado.nombre}: ").strip())
                            if cantidad > 0:
                                ods.actualizar_cantidad_detalle(producto_seleccionado.id_producto, cantidad)
                                print(f"Cantidad de {producto_seleccionado.nombre} actualizada con éxito")
                            else:
                                print("Cantidad inválida. Operación cancelada.")
                    else:
                        cantidad = int(input(f"Ingrese la cantidad de {producto_seleccionado.nombre} a agregar: ").strip())
                        if cantidad > 0:
                            nota = input("Ingrese una nota especial para este producto (o presione Enter para omitir): ").strip()
                            precio = input("Ingrese un precio especial (o presione Enter para omitir): ").strip()
                            ods.agregar_detalle(OrdenDetalle(
                                id_detalle=0,
                                id_orden=0,
                                id_producto=producto_seleccionado.id_producto,
                                cantidad=cantidad,  
                                precio_unitario=producto_seleccionado.precio if not precio else float(precio),
                                nota=nota))
                            print(f"{producto_seleccionado.nombre} agregado con éxito")
                        else:
                            print("Cantidad inválida. Operación cancelada.")
                else:
                    print("Producto no disponible. Intente nuevamente.")             
        elif opcion == "2":
            nombre = input("Ingrese nombre: ")
            print("\n👥 LISTA DE PRODUCTOS")
            print("-" * 90)
            print(f"{'ID':<6}{'Nombre':<25}{'Descripción':<40}{'Precio':>10} {'Categoría':>15}")
            print("-" * 90)
            productos = ps.buscar_productos(nombre)
            if productos:
                for p in items:
                        print(f"{'0' if p.id_producto<1<0 else ''}{p.id_producto}{'.':<3}{p.nombre:<25} | {p.descripcion:<40} | S/{p.precio:>6.2f} | {p.categoria>15}")
                        print("-"*90)    
            else:
                print("No hay productos registrados")
            print("0. <- REGRESAR")

            if len(productos)==1:
                if ods.validar_detalle_existente(productos[0].id_producto):
                    print("El producto ya fue agregado anteriormente ¿Desea actualizar la cantidad? (s/n)")
                    respuesta = input().strip().lower()
                    if respuesta == "s":
                        cantidad = int(input(f"Ingrese la nueva cantidad de {producto_seleccionado.nombre}: ").strip())
                        if cantidad > 0:
                            ods.actualizar_cantidad_detalle(producto_seleccionado.id_producto, cantidad)
                            print(f"Cantidad de {producto_seleccionado.nombre} actualizada con éxito")
                        else:
                            print("Cantidad inválida. Operación cancelada.")
                    else:
                        cantidad = int(input(f"Ingrese la cantidad de {producto_seleccionado.nombre} a agregar: ").strip())
                        if cantidad > 0:
                            nota = input("Ingrese una nota especial para este producto (o presione Enter para omitir): ").strip()
                            ods.agregar_detalle(OrdenDetalle(
                                id_detalle=0,
                                id_orden=0,
                                id_producto=producto_seleccionado.id_producto,
                                cantidad=cantidad,  
                                precio_unitario=producto_seleccionado.precio,
                                nota=nota))
                            print(f"{producto_seleccionado.nombre} agregado con éxito")
                        else:
                            print("Cantidad inválida. Operación cancelada.")
                else:
                    cantidad = int(input(f"Ingrese la cantidad de {producto_seleccionado.nombre} a agregar: ").strip())
                    if cantidad > 0:
                        nota = input("Ingrese una nota especial para este producto (o presione Enter para omitir): ").strip()
                        ods.agregar_detalle(OrdenDetalle(
                            id_detalle=0,
                            id_orden=0,
                            id_producto=producto_seleccionado.id_producto,
                            cantidad=cantidad,  
                            precio_unitario=producto_seleccionado.precio,
                            nota=nota))
                        print(f"{producto_seleccionado.nombre} agregado con éxito")
                    else:
                        print("Cantidad inválida. Operación cancelada.")
            else:
                id = input(f"Seleccione un producto").strip()
                if (id == "0"):
                    print("Cancelando selección de productos...")
                else:
                    producto_seleccionado = ps.obtener_producto_disponible_por_id(int(id))
                    if(producto_seleccionado):
                        if ods.validar_detalle_existente(producto_seleccionado.id_producto):
                            print("El producto ya fue agregado anteriormente ¿Desea actualizar la cantidad? (s/n)")
                            respuesta = input("➤  ").strip().lower()
                            if respuesta == "s":
                                cantidad = int(input(f"Ingrese la nueva cantidad de {producto_seleccionado.nombre}: ").strip())
                                if cantidad > 0:
                                    ods.actualizar_cantidad_detalle(producto_seleccionado.id_producto, cantidad)
                                    print(f"Cantidad de {producto_seleccionado.nombre} actualizada con éxito")
                                else:
                                    print("Cantidad inválida. Operación cancelada.")
                            else:
                                continue
                        else:
                            cantidad = int(input(f"Ingrese la cantidad de {producto_seleccionado.nombre} a agregar: ").strip())
                            if cantidad > 0:
                                nota = input("Ingrese una nota especial para este producto (o presione Enter para omitir): ").strip()
                                ods.agregar_detalle(OrdenDetalle(
                                    id_detalle=0,
                                    id_orden=0,
                                    id_producto=producto_seleccionado.id_producto,
                                    cantidad=cantidad,  
                                    precio_unitario=producto_seleccionado.precio,
                                    nota=nota))
                                print(f"{producto_seleccionado.nombre} agregado con éxito")
                            else:
                                print("Cantidad inválida. Operación cancelada.")
                    else:
                        print("Producto no disponible. Intente nuevamente.")    
        elif opcion == "3":
            """Muestra los productos agregados a la orden."""
            if(ods.detalles):
                print("\n" + "="*60)
                print("PRODUCTOS SELECCIONADOS")
                print("="*60)
                detalle_producto = [ps.obtener_producto_disponible_por_id(d.id_producto) for d in ods.detalles]
                for p in detalle_producto:
                    print(f"{'0' if p.id_producto<10 else ''}{p.id_producto}. {p.nombre:<25} | {p.descripcion:<45} | S/{p.precio:>6.2f}   {p.categoria:<20}")
                print("0. <- REGRESAR")

                iden = input(f"Seleccione el producto que desea quitar de la orden: ").strip()
                if (iden == "0"):
                    print("Cancelando selección de productos...")
                    continue
                else:
                    if(ods.validar_detalle_existente(int(iden.strip()))):
                        ods.quitar_detalle_por_id(int(iden))
                        print(f"{producto_seleccionado.nombre} quitado de la orden")
                    else:
                        print("Ingrese un número válido")
            else:
                print("No hay productos seleccionados")
        elif opcion == "0":
            detalles = ods.obtener_lista_detalles()
            if not (detalles):
                print("No se agregaron productos")
                opcion = input("¿Salir? (s/n): ")
                if opcion == "s":
                    print("Saliendo del sistema...")
                    return None
                continue
            else:
                return detalles
        else:
            print("⚠ Opción incorrecta. Intente nuevamente.")


    