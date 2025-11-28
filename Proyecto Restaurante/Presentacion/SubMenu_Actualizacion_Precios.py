from datetime import datetime
from Servicio.producto_servicio import ProductoServicio
from Servicio.AuditoriaPrecio_Servicio import AuditoriaPrecioServicio
from Modelo.AuditoriaPrecio import AuditoriaPrecio

ps = ProductoServicio()
aps = AuditoriaPrecioServicio()

def submenu_actualizar_precios():
    """Submenú interactivo para actualizar precios."""
    print("\n" + "="*50)
    print("💰 ACTUALIZACIÓN DE PRECIOS")
    print("="*50)
    # Mostrar productos actuales
    print("\n📋 PRODUCTOS ACTUALES:")
    print("-" * 60)
    print(f"{'ID':<3} {'Nombre':<20}     {'Categoría'}     {'Precio':<12}")
    print("-" * 60)
    productos = ps.obtener_lista_productos_disponibles()
    if productos:
        for p in productos:
                    print(f"{p.id_producto}   {p.nombre:<25}   |   {p.categoria:<45}  |   S/{p.precio:>6.2f}")
    else:
        print("No hay productos registrados")   
    print("\n¿Cómo desea actualizar los precios?")
    print("1. Actualizar precio de un producto específico")
    print("2. Aplicar aumento/descuento porcentual por categoría")
    print("0. Cancelar")
    try:
        opcion = input("\nSeleccione una opción: ").strip()
        if opcion == "1":
            """Actualiza el precio de un producto específico."""
            print("\n🎯 ACTUALIZAR PRECIO INDIVIDUAL")
            print("-" * 40)
            nombre = input("Ingrese nombre: ")
            print("\n👥 LISTA DE PRODUCTOS")
            print("-" * 60)
            print(f"{'Nro.':<3} {'Nombre':<20}       {'Categoría'}     {'Precio':<12}")
            print("-" * 60)
            productos = ps.buscar_productos(nombre)
            if productos:
                for p in productos:
                    print(f"{'0' if p.id_producto<10 else ''}{p.id_producto}.  {p.nombre:<25}   |    {p.categoria:<45}  |   S/{p.precio:>6.2f}")
            
                id = input(f"Seleccione un producto").strip()
                if (id == "0"):
                    print("Cancelando selección de productos...")
                else:
                    producto = ps.obtener_producto_disponible_por_id(int(id))
                    if(producto):
                        print(f"\n✅ Producto encontrado:")
                        print(f"Nombre: {producto.nombre}")
                        print(f"Precio actual: S/{producto.precio:.2f}")
                        print(f"Categoría: {producto.categoria}")
                        confirmar = input(f"\n¿Desea actualizar el precio de '{producto.nombre}'? (s/n): ").lower()
                        if confirmar != 's':
                            print(" Operación cancelada")
                            return
                        try:
                            nuevo_precio = float(input(f"Ingrese el nuevo precio (actual: S/{producto.precio:.2f}): "))
                            if nuevo_precio <= 0:
                                print(" El precio debe ser mayor a 0")
                                return
                            # Mostrar resumen del cambio
                            diferencia = nuevo_precio - producto.precio
                            porcentaje = (diferencia / producto.precio) * 100
                            print(f"\n RESUMEN DEL CAMBIO:")
                            print(f"Producto: {producto.nombre}")
                            print(f"Precio anterior: S/{producto.precio:.2f}")
                            print(f"Precio nuevo: S/{nuevo_precio:.2f}")
                            print(f"Diferencia: S/{diferencia:+.2f} ({porcentaje:+.1f}%)")
                            aplicar = input("\n¿Aplicar cambio? (s/n): ").lower()
                            if aplicar == 's':
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
                                    print(" Precio actualizado exitosamente")
                                else:
                                    print(" Error al actualizar precio")
                            else:
                                print(" Cambio cancelado")
                        except ValueError:
                            print(" Precio inválido")
            else:
                print("No hay productos registrados")
            print("0. <- REGRESAR")
        elif opcion == "2":
            """Aplica un ajuste porcentual a toda una categoría."""
            print("\n ACTUALIZACIÓN POR CATEGORÍA")
            print("-" * 40)
            print("\nCategorías disponibles:")
            categorias = ps.crear_categorias()
            productos = ps.obtener_lista_productos_disponibles()
            if(categorias):
                for i, categoria in categorias.items():
                    nro_productos = len([p for p in productos if p.categoria==categoria])
                    print(f"\n{i}. {categoria}: ({nro_productos} productos)")
                    print("-" * 40)
            else:
                print("Vacio")
            print("0. <- REGRESAR")
            
            try:
                opcion = input("\nSeleccione el número de categoría: ").strip()
                if opcion != "0":
                    id = int(opcion)
                    if(id in categorias):    
                        categoria_seleccionada = categorias[id]
                        productos_categoria = ps.filtrar_productos_por_categoria(categoria_seleccionada)
                        print(f"\n Productos en '{categoria_seleccionada}':")
                        for p in productos_categoria:
                            print(f"• {p.nombre:<25}  | • {p.descripcion:<25}  | S/{p.precio:.2f}")
                        porcentaje = float(input(f"\nIngrese el porcentaje de ajuste (+/- ej: 10 para aumentar 10%, -5 para reducir 5%): "))
                        print(f"\n VISTA PREVIA - Ajuste del {porcentaje:+.1f}%:")
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
                            print(f"• {p.nombre:<25}  | • {p.descripcion:<25}  | S/{p.precio:.2f}")
                        confirmar = input(f"\n¿Aplicar ajuste del {porcentaje:+.1f}% a {len(productos_categoria)} productos? (s/n): ").lower()
                        if confirmar == 's':
                            if(aps.registrar_cambio_precios_bd(auditorias)):
                                if(ps.actualizar_precio_producto_bd(productos_categoria)):
                                    print(f" Precios de categoría '{categoria_seleccionada}' actualizados")
                            else:
                                print(" Error al actualizar precios")
                        else:
                            auditorias.clear()
                            productos_categoria.clear()
                            print(" Cambios cancelados")
                    else:
                        print(" Selección inválida")
                else:
                    return
            except (ValueError, IndexError):
                print(" Entrada inválida")
        elif opcion == "0":
            return
        else:
            print("❌ Opción inválida")
    except Exception as e:
        print(f"❌ Error: {e}")
    finally:
        ps.obtener_productos_bd()