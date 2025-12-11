from datetime import datetime
from Servicio.producto_servicio import ProductoServicio
from Servicio.AuditoriaPrecio_Servicio import AuditoriaPrecioServicio
from Modelo.AuditoriaPrecio import AuditoriaPrecio
from Utilitario.Validacion import validar, TipoValidacion

ps = ProductoServicio()
aps = AuditoriaPrecioServicio()

def submenu_actualizar_precios():
    """Submenú interactivo para actualizar precios."""
    while True:    
        print("\n" + "-"*100)
        print("💰 ACTUALIZACIÓN DE PRECIOS")
        print("-"*100)
        print("\n1. Actualizar precio de un producto específico")
        print("2. Aplicar aumento/descuento porcentual por categoría")
        print("0. Salir")
        try:
            print("\nSeleccione una opción:")
            opcion = input("➤  ").strip()
            
            if opcion == "1":
                """Actualiza el precio de un producto específico."""
                print("\n" + "-"*100)
                print("🎯 ACTUALIZACIÓN DE PRECIO INDIVIDUAL")
                print("-"*100)

                print("\nNombre del producto: ")
                nombre = input("➤  ").strip()

                print("\n" + "-"*100)
                print("RESULTADOS DE BÚSQUEDA")
                print("=" * 100)
                print(f"{'Nro.':<3} {'Nombre':<20}       {'Categoría'}     {'Precio':<12}")
                print("=" * 100)
                productos = ps.buscar_productos(nombre)
                if productos:
                    for p in productos:
                        print(f"{'0' if p.id_producto<10 else ''}{p.id_producto}.  {p.nombre:<25}   |    {p.categoria:<45}  |   S/{p.precio:>6.2f}")
                
                    while True:
                        print("\nSeleccione un producto: ")
                        id = input("➤  ").strip()
                        if validar(id, TipoValidacion.ENTERO):
                            break
                        print("\nFormato de entrada inválida")
                    
                    if id == "0":
                        print("Cancelando selección de productos...")
                    else:
                        producto = ps.obtener_producto_disponible_por_id(int(id))
                        if producto:
                            print("\n" + "-"*100)
                            print("✅ PRODUCTO ENCONTRADO")
                            print("-"*100)
                            print(f"\n1. {'Nombre:':>17} {producto.nombre}")
                            print(f"3. {'Precio actual:':>17} {producto.precio:.2f}")
                            print(f"4. {'Categoría:':>17} {producto.categoria}")
                            print(f"4. {'Disponibilidad:':>17} {'🟢' if producto.disponibilidad else '🔴'}")

                            print(f"\n¿Desea actualizar el precio de '{producto.nombre}'? (s/n): ")
                            confirmar = input("➤  ").strip().lower()
                            if confirmar != 's':
                                print("Operación cancelada")
                                return
                            try:
                                while True:
                                    print("\nIngrese el nuevo precio S/:")
                                    nuevo_precio = input("➤  ")
                                    if validar(nuevo_precio, TipoValidacion.PRECIO):
                                        nuevo_precio = float(nuevo_precio)
                                        break
                                    print("Formato de precio inválido")

                                # Mostrar resumen del cambio
                                diferencia = abs( nuevo_precio - producto.precio)
                                porcentaje = (diferencia / producto.precio) * 100

                                print("\n" + "-"*100)
                                print("✅ RESUMEN PRECIO ACTUALIZADO")
                                print("-"*100)
                                print(f"\n1. {'Nombre:':>17} {producto.nombre}")
                                print(f"3. {'Precio anterior:':>17} {producto.precio:.2f}")
                                print(f"3. {'Precio nuevo:':>17} {nuevo_precio:.2f}")
                                print(f"4. {'Diferencia:':>17} {diferencia:.2f} ({porcentaje:.1f}%)")

                                print("\n¿Aplicar cambio de precio? (s/n): ")
                                confirmar = input("➤  ").strip().lower()
                                if confirmar == 's':
                                    fecha_actual = datetime.now().strftime('%Y-%m-%d')
                                    auditoria = AuditoriaPrecio(
                                        fecha_cambio = fecha_actual,
                                        id_producto = producto.id_producto,
                                        precio_anterior = producto.precio,
                                        precio_nuevo = nuevo_precio
                                    )
                                    if aps.registrar_cambio_precios_bd([auditoria]):
                                        producto.precio = nuevo_precio
                                        ps.actualizar_precio_producto_bd([producto])
                                        print("\n ✅ Precio actualizado exitosamente")
                                    else:
                                        print("\nError al actualizar precio")
                                else:
                                    print("\nCambio cancelado")
                            except ValueError:
                                print("\nPrecio inválido")
                        else:
                            print("\nProducto no encontrado")
                else:
                    print("\nNo hay productos registrados")
                    break
            elif opcion == "2":
                """Aplica un ajuste porcentual a toda una categoría."""
                print("\n" + "-"*100)
                print("💰 ACTUALIZACIONES DE PRECIOS POR CATEGORÍA")
                print("-"*100)
                print("\nCategorías disponibles:\n")
                categorias = ps.crear_categorias()
                productos = ps.obtener_lista_productos_disponibles()
                if(categorias):
                    for i, categoria in categorias.items():
                        nro_productos = len([p for p in productos if p.categoria==categoria])
                        if nro_productos > 0:
                            print(f"{i}.{categoria:>13}: {nro_productos} productos")
                else:
                    print("Sin categorías")
                print(f"0.{'Salir':>13}")

                try:
                    while True:
                        print("\nSeleccione una categoría: ")
                        id = input("➤  ").strip()
                        if validar(id, TipoValidacion.ENTERO):
                            id = int(id)
                            if id in categorias:
                                break
                        print("Entrada inválida")

                    if id == 0:
                        print("Cancelando...")
                        break
 
                    categoria_seleccionada = categorias[id]
                    productos_categoria = ps.filtrar_productos_por_categoria(categoria_seleccionada)
                    print("\n" + "="*100)
                    print(f"PRODUCTOS EN LA CATEGORÍA '{categoria_seleccionada.upper()}'")
                    print("="*100)
                    for p in productos_categoria:
                        print(f"► {p.nombre:<30}|       {p.descripcion:<40}|{'S/':>10}{p.precio:>8.2f}")
                    
                    while True:
                        print("\nIngrese el porcentaje de ajuste (+/- ej: 10 para aumentar 10%, -5 para reducir 5%):")
                        porcentaje = input("➤  ")
                        if validar(porcentaje, TipoValidacion.DECIMAL):
                            porcentaje = float(porcentaje)
                            break
                        print("Formato de entrada inválido")
                    
                    print("\n" + "="*100)
                    print(f"VISTA PREVIA - AJUSTE DEL {porcentaje:+.1f}%:")
                    print("="*100)
                    auditorias = []
                    for p in productos_categoria:
                        nuevo_precio = p.precio * (1 + porcentaje / 100)
                        auditorias.append(AuditoriaPrecio(
                            fecha_cambio = datetime.now().strftime('%Y-%m-%d'),
                            id_producto=p.id_producto,
                            precio_anterior=p.precio,
                            precio_nuevo=nuevo_precio
                        ))
                        p.precio = nuevo_precio
                        print(f"► {p.nombre:<30}|       {p.descripcion:<40}|{'S/':>10}{p.precio:>8.2f}")
                    print(f"\n¿Aplicar ajuste del {porcentaje:+.1f}% a {len(productos_categoria)} producto(s)? (s/n):")
                    confirmar = input("➤  ").strip().lower()
                    if confirmar == 's':
                        if(aps.registrar_cambio_precios_bd(auditorias)):
                            if(ps.actualizar_precio_producto_bd(productos_categoria)):
                                print(f"\n✅ Precios de la categoría '{categoria_seleccionada}' actualizados")
                        else:
                            print("\n❌ Error al actualizar precios")
                    else:
                        auditorias.clear()
                        productos_categoria.clear()
                        print("\n❌ Cancelando actualización...")
                except (ValueError, IndexError):
                    print("\n❌ Entrada inválida")
            elif opcion == "0":
                return
            else:
                print("\n❌ Opción inválida")
        except Exception as e:
            print(f"\n❌ Error: {e}")
        finally:
            ps.obtener_productos_bd()