# Importaciones de servicios y modelos usados en el catálogo
from Modelo.OrdenDetalle import OrdenDetalle
from Servicio.producto_servicio import ProductoServicio
from Servicio.Orden_Servicio import OrdenServicio
from Servicio.OrdenDetalle_Servicio import OrdenDetalleServicio
from Utilitario.Validacion import validar, TipoValidacion

os = OrdenServicio()              # servicio para manejar órdenes

ps = ProductoServicio()           # servicio para manejar productos
ods = OrdenDetalleServicio()      # servicio para manejar detalles de la orden

def catalogo_productos():

    """Interfaz de selección de productos: ver, buscar, agregar o quitar."""
    while True:
        # Menú de productos
        print("\n" + "-"*100)
        print("SELECCION DE PRODUCTOS")
        print("-"*100)
        print("1. Ver Carta de productos")
        print("2. Buscar producto")
        print("3. Quitar producto")
        print("0. Salir")
        
        print("\nSeleccione una opción: ")
        opcion = input("➤  ").strip()
        
        if opcion == "1":
            """Muestra el catálogo completo de productos."""
            print("\n")
            print("CATÁLOGO PRODUCTOS")
            print("="*90)
            print(f"{'ID':<6}{'Nombre':<25}{'Descripción':<45}{'Precio':>10}")
            estructura = ps.obtener_catalogo()     # obtiene productos agrupados por categoría
            if(estructura):
                # Itera por cada categoría y sus productos
                for categoria, items in estructura.items():
                    print("="*90)
                    print(f"📋 {categoria.upper()}")
                    print("=" * 90)
                     # Muestra cada producto con su id, nombre, descripción y precio
                    for p in items:
                        print(f"{'0' if p.id_producto<1<0 else ''}{p.id_producto}{'.':<3}{p.nombre:<25} | {p.descripcion[:30]+'...':<40}|    S/{p.precio:>6.2f}")
            else:
                print("sin productos*")
            print("0. Salir")

            # Selección de producto por id
            while True:
                print("\nSeleccione un producto: ")
                id = input("➤  ").strip()
                if validar(id, TipoValidacion.ENTERO):
                    id = int(id)
                    break
                print("\nIngrese un número válido")
            if not id:
                print("\nCancelando selección de productos...")
            else:
                producto_seleccionado = ps.obtener_producto_disponible_por_id(int(id))
                if(producto_seleccionado):
                    # Si ya existe en la orden, preguntar si se desea actualizar la cantidad
                    if ods.validar_detalle_existente(producto_seleccionado.id_producto):
                        print("El producto ya fue agregado anteriormente ¿Desea actualizar la cantidad? (s/n)")
                        respuesta = input("➤  ").strip().lower()
                        if respuesta == "s":
                            while True:
                                print(f"\nIngrese la cantidad de {producto_seleccionado.nombre}: ")
                                cantidad = input("➤  ").strip()
                                if validar(cantidad, TipoValidacion.ENTERO):
                                    cantidad = int(cantidad)  
                                    break
                                print("Ingrese una cantidad válida")
                                
                            ods.actualizar_cantidad_detalle(producto_seleccionado.id_producto, cantidad)
                            print(f"Cantidad de {producto_seleccionado.nombre} actualizada con éxito")
                    else:
                         # Agregar nuevo detalle al orden
                        while True:
                            print(f"\nIngrese la cantidad de {producto_seleccionado.nombre}: ")
                            cantidad = input("➤  ").strip()
                            if validar(cantidad, TipoValidacion.ENTERO):
                                cantidad = int(cantidad)  
                                break
                            print("Ingrese una cantidad válida")
                        nota = input("Ingrese una nota especial para este producto (o presione Enter para omitir): ").strip()
                        while True:
                            print(f"\nIngrese un precio especial (o presione Enter para omitir):")
                            precio = input("➤  ").strip()
                            if not precio: break
                            if validar(precio, TipoValidacion.PRECIO):
                                precio = float(precio)
                                break
                            print("Ingrese un precio válido")
                        ods.agregar_detalle(OrdenDetalle(
                                id_detalle=0,
                                id_orden=0,
                                id_producto=producto_seleccionado.id_producto,
                                cantidad=cantidad,  
                                precio_unitario=producto_seleccionado.precio if not precio else float(precio),
                                nota=nota))
                        print(f"{producto_seleccionado.nombre} agregado con éxito")
                else:
                    print("Producto no disponible. Intente nuevamente.")             
        
        elif opcion == "2":
            print("\n" + "-"*100)
            print("BÚSQUEDA DE PRODUCTOS")
            print("-"*100)
            nombre = input("\nIngrese nombre: ")
            print("\n👥 LISTA DE PRODUCTOS")
            print("-" * 90)
            print(f"{'ID':<6}{'Nombre':<25}{'Descripción':<40}{'Precio':>10} {'Categoría':>15}")
            print("-" * 90)
            productos = ps.buscar_productos_disponibles(nombre)
            if productos:
                for p in productos:
                        print(f"{'0' if p.id_producto<1<0 else ''}{p.id_producto}{'.':<3}{p.nombre:<25} | {p.descripcion:<40} | S/{p.precio:>6.2f} | {p.categoria:>15}")
                        print("-"*90)    
            else:
                print("\nNo hay productos registrados")
            print("0. Salir")
            
            if len(productos)==1:
                producto_seleccionado = productos[0]
                if ods.validar_detalle_existente(producto_seleccionado.id_producto):
                    print("\nEl producto ya fue agregado anteriormente ¿Desea actualizar la cantidad? (s/n)")
                    respuesta = input().strip().lower()
                    if respuesta == "s":
                        cantidad = int(input(f"\nIngrese la nueva cantidad de {producto_seleccionado.nombre}: ").strip())
                        if cantidad > 0:
                            ods.actualizar_cantidad_detalle(producto_seleccionado.id_producto, cantidad)
                            print(f"\nCantidad de {producto_seleccionado.nombre} actualizada con éxito")
                        else:
                            print("\nCantidad inválida. Operación cancelada.")
                    else:
                        cantidad = int(input(f"\nIngrese la cantidad de {producto_seleccionado.nombre} a agregar: ").strip())
                        if cantidad > 0:
                            nota = input("\nIngrese una nota especial para este producto (o presione Enter para omitir): ").strip()
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
                 # Si hay varios, permitir seleccionar por id
                while True:
                    print("\nSeleccione un producto: ")
                    id = input("➤  ").strip()
                    if validar(id, TipoValidacion.ENTERO):
                        id = int(id)
                        break
                    print("\nIngrese un número válido")
                if (id == 0):
                    print("\nCancelando selección de productos...")
                else:
                    producto_seleccionado = ps.obtener_producto_disponible_por_id(id)
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
                print("\n" + "="*100)
                print("PRODUCTOS SELECCIONADOS")
                print("="*100)
                 # Obtiene los objetos Producto correspondientes a cada detalle
                detalle_producto = [ps.obtener_producto_disponible_por_id(d.id_producto) for d in ods.detalles]
                for p in detalle_producto:
                    print(f"{'0' if p.id_producto<10 else ''}{p.id_producto}. {p.nombre:<25} | {p.descripcion:<45} | S/{p.precio:>6.2f}   {p.categoria:<20}")
                print("0. Salir")

                # Seleccionar id para quitar
                iden = input(f"\nSeleccione el producto que desea quitar de la orden: ").strip()
                if (iden == "0"):
                    print("\nCancelando selección de productos...")
                    continue
                else:
                    if(ods.validar_detalle_existente(int(iden.strip()))):
                        ods.quitar_detalle_por_id(int(iden))
                        print(f"\n{producto_seleccionado.nombre} quitado de la orden")
                    else:
                        print("\nIngrese un número válido")
            else:
                print("\nNo hay productos seleccionados")
        
        elif opcion == "0":
            detalles = ods.obtener_lista_detalles()
            if not (detalles):
                print("\nNo se agregaron productos")
                opcion = input("\n¿Salir? (s/n): ")
                if opcion == "s":
                    print("\nSaliendo del sistema...")
                    return None
                continue
            else:
                return detalles
        
        else:
            print("\n⚠ Opción incorrecta. Intente nuevamente.")


    