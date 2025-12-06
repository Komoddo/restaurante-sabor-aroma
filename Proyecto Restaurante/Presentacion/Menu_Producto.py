from Presentacion.SubMenu_Actualizacion_Precios import submenu_actualizar_precios
from Servicio.producto_servicio import ProductoServicio
from Modelo.Producto import Producto
from Utilitario.Validacion import validar, TipoValidacion


ps = ProductoServicio()

def submenu_productos():
    ps.obtener_productos_bd()
    ps.crear_categorias()

    while True:
        print("\n📦 MENÚ DE PRODUCTOS")
        print("1.  Listado de productos")
        print("2. ➕ Agregar Nuevo producto")
        print("3. ✏️ Actualizar datos de producto")
        print("4. 💰 Actualizar precio de producto")
        print("0. ⬅️ Volver al menú principal")

        opcion = input("Seleccione: ")

        if opcion == "1":
            """Muestra la lista completa de productos."""
            print("\n")
            print("LISTA DE PRODUCTOS")
            print("="*100)
            print(f"{'Nombre':<28}{'Descripción':<43}{'Categoría':<20}{'Precio':<10}{'Disponibilidad':>15}")
            print("="*100)
            if ps.obtener_lista_productos():
                for p in ps.obtener_lista_productos():
                    print(f"► {p.nombre:<25} | {p.descripcion:<40} | {p.categoria:<15} | S/.{p.precio:>6.2f}{('🟢' if p.disponibilidad else '🔴'):>15}")
            else:
                print("No hay productos registrados")   
        elif opcion == "2":
            """Submenú para agregar nuevos productos"""
            print("\n📋 MENÚ: NUEVO PRODUCTO")
            print("-" * 45)
            
            while True:
                print("Nombre del producto: ")
                nombre  = input("➤  ")
                if validar(nombre, TipoValidacion.NOMBRE):
                    break
                print("Formato de nombre inválido")
            producto = ps.validar_producto(nombre)
            
            if not producto:
                print("Descripción: ")
                descripcion = input("➤  ").strip()
                
                while True:
                    print("Precio: S/ ")
                    precio = input("➤  ")
                    if validar(precio, TipoValidacion.PRECIO):
                        precio = float(precio)
                        break
                    print("Formato de precio inválido")
                
                while True:
                    print("\nCategorias:\n")
                    for i, cat in ps.categorias.items():
                        print(f"{i}. {cat}")
                    print(f"{len(ps.categorias) + 1}. Nueva categoría")

                    print("\nSeleccione una categoría: ")
                    cat_id = input("➤  ").strip()
                    if validar(cat_id, TipoValidacion.ENTERO):
                        cat_id = int(cat_id)
                        num_cat = len(ps.categorias)
                        if cat_id in range(1, num_cat + 1):
                            categoria = ps.categorias[cat_id]
                        elif cat_id == num_cat + 1:
                            categoria = input("Nombre de la nueva categoría: ").strip()
                        else:
                            print("Opción inválida")
                        break
                    print("Formato de categoría inválido")
   
                nuevo_producto = Producto(
                    id_producto=0,
                    nombre=nombre,
                    descripcion=descripcion,
                    precio=precio,
                    categoria=categoria)

                print(f"\n📋 RESUMEN DEL NUEVO PRODUCTO:")
                print(f"Nombre: {nombre}")
                print(f"Precio: S/{precio:.2f}")
                print(f"Categoría: {categoria}")

                print("\n¿Confirmar agregado? (s/n): ")
                confirmar = input("➤  ").strip().lower()
                if confirmar == 's':
                    ps.agregar_producto_lst(nuevo_producto)
                    ps.agregar_producto_bd(nuevo_producto)
                    print(f" Producto '{nombre}' agregado exitosamente")
                else:
                    print(" Cancelando...")
            else:
                print(f" Ya existe un producto con el nombre: '{nombre}'")
        elif opcion == "3":
            """Submenú actualizacion de productos."""
            print("\n" + "="*100)
            print("➕ ACTUALIZACIÓN DE PRODUCTOS")
            print("="*100)
            print("\nNombre del producto que desea modificar: ")
            nombre = input("➤  ")
            print("\n")
            print("-" * 100)
            print(f"{'ID':<5}{'Nombre':<24}{'Descripción':<42}{'Categoría':<18}{'Precio':<10}{'Disponibilidad':>15}")
            print("-" * 100)
            productos = ps.buscar_productos(nombre)
            if productos:
                for p in productos:
                    print(f"{'0' if p.id_producto<10 else ''}{(str(p.id_producto)+'.'):<5}{p.nombre:<20} | {p.descripcion:<40} | {p.categoria:<15} | S/{p.precio:>6.2f}{('🟢' if p.disponibilidad else '🔴'):>15}")
            else:
                print("No hay productos registrados")
                continue
            print(f"{'0.':<5} 🔙 Regresar")

            print("\nSeleccione un producto: ")
            id = input("➤  ").strip()
            if (id == "0"):
                print("Cancelando edición de productos...")
            else:
                producto = ps.obtener_producto_por_id(int(id))
                if(producto):
                    while True:
                        print("\nRESUMEN DEL PRODUCTO")
                        print(f"\n1. Nombre: {producto.nombre}")
                        print(f"2. Descripción: {producto.descripcion}")
                        print(f"3. Categoria: {producto.categoria}")
                        print(f"4. Disponibilidad: {'Disponible' if producto.disponibilidad else 'No disponible'}")
                        print("0. ⬅️ Salir")

                        print("\nSeleccione el dato que desea actualizar")
                        opcion = input("➤  ").strip()
                        if opcion=="1":
                            print(f"Nombre nuevo para {producto.nombre}")
                            nombre_nuevo = input("➤  ")
                            while True:
                                if validar(nombre_nuevo, TipoValidacion.NOMBRE):
                                    break
                                print("Formato de nombre inválido")
                            producto.nombre = nombre_nuevo
                            print("Actualizando nombre...")
                        elif opcion=="2":
                            print(f"Descripción nueva para {producto.nombre}")
                            producto.descripcion = input("➤  ").strip()
                            print("Actualizando descripción...")
                        elif opcion=="3":
                            while True:
                                print("\nCategorias:")
                                for i, cat in ps.categorias.items():
                                    print(f"{i}. {cat}")
                                print(f"{len(ps.categorias) + 1}. Nueva categoría")
                                print("\nSeleccione una categoría: ")
                                cat_id = input("➤  ").strip()
                                if validar(cat_id, TipoValidacion.ENTERO):
                                    cat_id = int(cat_id)
                                    num_cat = len(ps.categorias)
                                    if cat_id in range(1, num_cat + 1):
                                        categoria = ps.categorias[cat_id]
                                    elif cat_id == num_cat + 1:
                                        categoria = input("Nombre de la nueva categoría: ").strip()
                                        if not validar(categoria, TipoValidacion.NOMBRE):
                                            print("Formato de nombre inválido")
                                            continue
                                    else:
                                        print("Opción inválida")
                                        continue

                                    producto.categoria = categoria
                                    print("Actualizando categoría...")
                                    break
                                print("Formato de categoría inválido")
                        elif opcion=="4":
                            print("¿Desea cambiar el estado del producto? (s/n)")
                            respuesta = input("➤  ").strip().lower()
                            if respuesta=="s":
                                producto.disponibilidad = False if producto.disponibilidad else True
                                print("Actualizando categoría...")
                        elif opcion=="0":
                            print("¿Desea guardar los cambios realizados? (s/n)")
                            respuesta = input("➤  ").strip().lower()
                            if respuesta=="s":
                                if ps.actualizar_producto_bd(producto):
                                    print("✔️ Producto actualizado con exito")
                                    break
                                else:
                                    print("❌ Error al actualizar el producto")
                                    break
                            else:
                                print("🚶‍♂️ Cancelando cambios...")
                                break
                        else:
                            print("Respuesta inválida")
                else:
                    print("Producto no encontrado")
        elif opcion == "4":
             submenu_actualizar_precios()
        elif opcion == "0":
            break
        else:
            print("Opción inválida.")
