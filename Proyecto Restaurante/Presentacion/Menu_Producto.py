# Importa el submenú para actualizar precios de productos
from Presentacion.SubMenu_Actualizacion_Precios import submenu_actualizar_precios
# Importa el servicio que maneja operaciones CRUD de productos
from Servicio.producto_servicio import ProductoServicio
# Importa la clase Producto que define la estructura de los productos
from Modelo.Producto import Producto
# Crea la instancia del servicio para gestionar productos

# Crea una instancia de la clase ProductoServicio
# Esto permite usar todos los métodos de ProductoServicio (agregar, actualizar, listar, eliminar productos)
# Es decir, 'ps' es un objeto que representa el servicio de productos y nos facilita interactuar con la base de datos

ps = ProductoServicio()

def submenu_productos():
    """Interfaz para la gestión de productos del restaurante."""
    # Carga los productos desde la base de datos
    ps.obtener_productos_bd()
    ps.crear_categorias()

    while True:
        # Menú principal de productos
        print("\n📦 MENÚ DE PRODUCTOS")
        print("1.  Listado de productos")
        print("2. ➕ Agregar Nuevo producto")
        print("3. ✏️ Actualizar datos de producto")
        print("4. 💰 Actualizar precio de producto")
        print("0. ⬅️ Volver al menú principal")

        opcion = input("Seleccione: ")

        if opcion == "1":
            """Muestra la lista completa de productos."""
            print("\n" + "*"*90)
            print("LISTA DE PRODUCTOS")
            print("*"*100)
            print(f"{'Nombre':<28}{'Descripción':<43}{'Categoría':<20}{'Precio':<10}{'Disponibilidad':>15}")
            print("-" * 100)
            if ps.obtener_lista_productos():
                # Muestra cada producto con su información
                for p in ps.obtener_lista_productos():
                            print(f"► {p.nombre:<25} | {p.descripcion:<40} | {p.categoria:<15} | S/.{p.precio:>6.2f}{('🟢' if p.disponibilidad else '🔴'):>15}")
            else:
                print("No hay productos registrados")   
        elif opcion == "2":
            """Submenú para agregar nuevos productos"""
            print("\n📋 AGREGAR NUEVOS PRODUCTOS")
            print("-" * 45)

            nombre = input("Nombre del producto: ").strip()
            producto = ps.validar_producto(nombre)
            if not producto:
                descripcion = input("Descripción: ").strip()
                precio = float(input("Precio: S/ "))

                # Selección o creación de categoría
                print("\nCategorias:")
                for i, cat in ps.categorias.items():
                    print(f"{i}. {cat}")
                print(f"{len(ps.categorias) + 1}. Nueva categoría")

                cat_id = int(input("\nSeleccione una categoría: ").strip())
                num_cat = len(ps.categorias)
                try:
                    if cat_id in range(1, num_cat + 1):
                        categoria = ps.categorias[cat_id]
                    elif cat_id == num_cat + 1:
                        categoria = input("Nombre de la nueva categoría: ").strip()
                    else:
                        print(" Opción inválida")
                except ValueError:
                    categoria = cat_id  # Permitir entrada directa

                # Crear objeto Producto y mostrar resumen
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

                confirmar = input("\n¿Confirmar agregado? (s/n): ").lower()
                if confirmar == 's':
                    # Agrega el producto a la lista y a la BD
                    ps.agregar_producto_lst(nuevo_producto)
                    ps.agregar_producto_bd(nuevo_producto)
                    print(f" Producto '{nombre}' agregado exitosamente")
                else:
                    print(" Agregado cancelado")
            else:
                print(f" Ya existe un producto con el nombre: '{nombre}'")
        elif opcion == "3":
            """Submenú actualizacion de productos."""
            print("\n" + "="*100)
            print("➕ ACTUALIZACIÓN DE PRODUCTOS")
            print("="*100)
            print("\nNombre del producto que desea modificar: ")
            nombre = input("➤  ").strip().lower()
            print("\n")
            print("-" * 100)
            print(f"{'ID':<6}{'Nombre':<28}{'Descripción':<42}{'Categoría':<18}{'Precio':<10}{'Disponibilidad':>15}")
            print("-" * 100)
            productos = ps.buscar_productos(nombre)
            if productos:
                for p in productos:
                    print(f"{'0' if p.id_producto<10 else ''}{(str(p.id_producto)+'.'):<6}{p.nombre:<25} | {p.descripcion:<40} | {p.categoria:<15} | S/{p.precio:>6.2f}{('🟢' if p.disponibilidad else '🔴'):>15}")
            else:
                print("No hay productos registrados")
            print("0. 🔙 Regresar")

            print("\nSeleccione un producto: ")
            id = input("➤  ").strip().lower()
            if (id == "0"):
                print("Cancelando edición de productos...")
            else:
                producto_seleccionado = ps.obtener_producto_por_id(int(id))
                if(producto_seleccionado):
                
                    while True:
                        # Muestra detalles del producto seleccionado
                        print("\nRESUMEN DEL PRODUCTO")
                        print(f"\n1. Nombre: {producto_seleccionado.nombre}")
                        print(f"2. Descripción: {producto_seleccionado.descripcion}")
                        print(f"3. Categoria: {producto_seleccionado.categoria}")
                        print(f"4. Disponibilidad: {'Disponible' if producto_seleccionado.disponibilidad else 'No disponible'}")
                        print("0. ⬅️ Salir")

                        print("\nSeleccione el dato que desea actualizar")
                        opcion = input("➤  ").strip().lower()
                        if opcion=="1":
                            print(f"Nombre nuevo para {producto_seleccionado.nombre}")
                            nombre_nuevo = input("➤  ").strip().lower()
                            producto_seleccionado.nombre = nombre_nuevo
                            print("Actualizando nombre...")
                        elif opcion=="2":
                            print(f"Descripción nueva para {producto_seleccionado.nombre}")
                            descripcion_nueva = input("➤  ").strip().lower()
                            producto_seleccionado.descripcion = descripcion_nueva
                            print("Actualizando descripción...")
                        elif opcion=="3":
                            print("\nCategorias:")
                            for i, cat in ps.categorias.items():
                                print(f"{i}. {cat}")
                            print(f"{len(ps.categorias) + 1}. Nueva categoría")
                            cat_id = int(input("\nSeleccione una categoría: ").strip())
                            num_cat = len(ps.categorias)
                            try:
                                if cat_id in range(1, num_cat + 1):
                                    categoria = ps.categorias[cat_id]
                                elif cat_id == num_cat + 1:
                                    categoria = input("Nombre de la nueva categoría: ").strip()
                                else:
                                    print("Opción inválida")
                                    continue

                                producto_seleccionado.categoria = categoria
                                print("Actualizando categoría...")
                            except ValueError:
                                categoria = cat_id  # Permitir entrada directa
                        elif opcion=="4":
                            print("¿Desea cambiar el estado del producto? (s/n)")
                            respuesta = input("➤  ").strip().lower()
                            if respuesta=="s":
                                producto_seleccionado.disponibilidad = False if producto_seleccionado.disponibilidad else True
                                print("Actualizando categoría...")
                        elif opcion=="0":
                            print("¿Desea guardar los cambios realizados? (s/n)")
                            respuesta = input("➤  ").strip().lower()
                            if respuesta=="s":
                                if ps.actualizar_producto_bd(producto_seleccionado):
                                    print("✔️ Producto actualizado con exito")
                                    break
                                else:
                                    print("❌ Error al actualizar el producto")
                                    break
                            else:
                                print("🚶‍♂️ Saliendo...")
                                break
                        else:
                            print("Respuesta inválida")
                else:
                    print("Producto no encontrado")
        elif opcion == "4":
             # Llama al submenú para actualizar precios
             submenu_actualizar_precios()
        elif opcion == "0":
            break
        else:
            print("Opción inválida.")
