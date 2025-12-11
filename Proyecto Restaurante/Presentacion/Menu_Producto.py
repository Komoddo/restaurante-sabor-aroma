# Importa el submenú para actualizar precios de productos
from Presentacion.SubMenu_Actualizacion_Precios import submenu_actualizar_precios
# Importa el servicio que maneja operaciones CRUD de productos
from Servicio.producto_servicio import ProductoServicio
# Importa la clase Producto que define la estructura de los productos
from Modelo.Producto import Producto
from Utilitario.Validacion import validar, TipoValidacion
# Crea la instancia del servicio para gestionar productos
# Crea una instancia de la clase ProductoServicio
# Esto permite usar todos los métodos de ProductoServicio (agregar, actualizar, listar, eliminar productos)
# Es decir, 'ps' es un objeto que representa el servicio de productos y nos facilita interactuar con la base de datos
ps = ProductoServicio()

def submenu_productos():
    """Interfaz para la gestión de productos del restaurante."""
    # Carga los productos desde la base de datos
    
    while True:
        ps.obtener_productos_bd()
        ps.crear_categorias()
        # Menú principal de productos
        print("\n" + "-"*100)
        print("📦 MENÚ DE PRODUCTOS")
        print("-"*100)
        print("\n1.🍝 Listado de productos")
        print("2. ➕ Nuevo producto")
        print("3. ✏️ Actualizar producto")
        print("4. 💰 Actualizar precios")
        print("0. ⬅️ Salir")

        print("\nSeleccione una opción: ")
        opcion = input("➤  ").strip()

        if opcion == "1":
            """Muestra la lista completa de productos."""
            print("\n" + "-"*100)
            print("LISTA DE PRODUCTOS")
            print("="*100)
            print(f"{'Nombre':<30}{'Descripción':<32}{'Categoría':<20}{'Precio':<6}{'Estado':>12}")
            print("="*100)
            if ps.obtener_lista_productos():
                # Muestra cada producto con su información
                for p in ps.obtener_lista_productos():
                    print(f"► {p.nombre:<25}|   {p.descripcion[:20]+'...':<25}|     {p.categoria:<15}|   S/. {p.precio:>6.2f}{('🟢' if p.disponibilidad else '🔴'):>7}")
            else:
                print("No hay productos registrados")   
        elif opcion == "2":
            """Submenú para agregar nuevos productos"""
            print("\n" + "-"*100)
            print("📋 MENÚ: NUEVO PRODUCTO")
            print("-"*100)
            
            while True:
                print("\nNombre del producto: ")
                nombre  = input("➤  ").strip()
                if validar(nombre, TipoValidacion.NOMBRE):
                    break
                print("Formato de nombre inválido")
            producto = ps.validar_producto(nombre)
            
            if not producto:
                print("\nDescripción: ")
                descripcion = input("➤  ").strip()
                
                while True:
                    print("\nPrecio S/: ")
                    precio = input("➤  ")
                    if validar(precio, TipoValidacion.PRECIO):
                        precio = float(precio)
                        break
                    print("Formato de precio inválido")
                # Selección o creación de categoría
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

                print("\n" + "-"*100)
                print("RESUMEN DEL PRODUCTO")
                print("-"*100)
                print(f"\n1. {'Nombre:':>15}  {nuevo_producto.nombre}")
                print(f"2. {'Descripción:':>15}  {nuevo_producto.descripcion}")
                print(f"3. {'Categoria:':>15}  {nuevo_producto.categoria}")
                print(f"4. {'Disponibilidad:':>15}  {'🟢' if nuevo_producto.disponibilidad else '🔴'}")
                print("\n¿Confirmar agregado? (s/n): ")
                confirmar = input("➤  ").strip().lower()
                if confirmar == 's':
                    # Agrega el producto a la lista y a la BD
                    ps.agregar_producto_lst(nuevo_producto)
                    ps.agregar_producto_bd(nuevo_producto)
                    print(f"\nProducto '{nombre}' agregado exitosamente")
                else:
                    print("\nCancelando...")
            else:
                print(f"\nYa existe un producto con el nombre: '{nombre}'")
        elif opcion == "3":
            """Submenú actualizacion de productos."""
            print("\n" + "-"*100)
            print("➕ ACTUALIZACIÓN DE PRODUCTOS")
            print("-"*100)
            print("\nNombre del producto que desea modificar: ")
            nombre = input("➤  ").strip()
            print("\n" + "-"*100)
            print("LISTA DE PRODUCTOS")
            print("="*100)
            print(f"{'ID':<5}{'Nombre':<29}{'Descripción':<28}{'Categoría':<20}{'Precio':<6}{'Estado':>12}")
            print("="*100)
            productos = ps.buscar_productos(nombre)
            if productos:
                for p in productos:
                    print(f"{'0' if p.id_producto<10 else ''}{(str(p.id_producto)+'.'):<5}{p.nombre:<25}|   {p.descripcion[:20]+'...':<25}|    {p.categoria:<15}|  S/. {p.precio:>6.2f}{('🟢' if p.disponibilidad else '🔴'):>6}")
            else:
                print("No hay productos registrados")
                continue
            print(f"{'0.':<4} Salir")

            print("\nSeleccione un producto: ")
            id = input("➤  ").strip()
            if (id == "0"):
                print("Cancelando edición de productos...")
            else:
                producto = ps.obtener_producto_por_id(int(id))
                if(producto):
                    while True:
                        # Muestra detalles del producto seleccionado
                        print("\n" + "-"*100)
                        print("RESUMEN DEL PRODUCTO")
                        print("-"*100)
                        print(f"\n1. {'Nombre:':>15} {producto.nombre}")
                        print(f"2. {'Descripción:':>15} {producto.descripcion}")
                        print(f"3. {'Categoria:':>15} {producto.categoria}")
                        print(f"4. {'Disponibilidad:':>15} {'🟢' if producto.disponibilidad else '🔴'}")
                        print(f"0. {'Salir':>15}")

                        print("\nSeleccione el dato que desea actualizar:")
                        opcion = input("➤  ").strip()
                        if opcion=="1":
                            while True:
                                print(f"\nNombre nuevo para {producto.nombre}")
                                nombre_nuevo = input("➤  ")
                                if validar(nombre_nuevo, TipoValidacion.NOMBRE):
                                    break
                                print("\nFormato de nombre inválido")
                            producto.nombre = nombre_nuevo
                            print("\nActualizando nombre...")
                        elif opcion=="2":
                            print(f"\nDescripción nueva para {producto.nombre}")
                            producto.descripcion = input("➤  ").strip()
                            print("\nActualizando descripción...")
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
                                        categoria = input("\nNombre de la nueva categoría: ").strip()
                                        if not validar(categoria, TipoValidacion.NOMBRE):
                                            print("\nFormato de nombre inválido")
                                            continue
                                    else:
                                        print("\npción inválida")
                                        continue

                                    producto.categoria = categoria
                                    print("\nActualizando categoría...")
                                    break
                                print("\nFormato de categoría inválido")
                        elif opcion=="4":
                            print("\n¿Desea cambiar el estado del producto? (s/n)")
                            respuesta = input("➤  ").strip().lower()
                            if respuesta=="s":
                                producto.disponibilidad = False if producto.disponibilidad else True
                                print("\nActualizando categoría...")
                        elif opcion=="0":
                            print("\n¿Desea guardar los cambios realizados? (s/n)")
                            respuesta = input("➤  ").strip().lower()
                            if respuesta=="s":
                                if ps.actualizar_producto_bd(producto):
                                    print("\n✔️ Producto actualizado con exito")
                                    break
                                else:
                                    print("\n❌ Error al actualizar el producto")
                                    break
                            else:
                                print("\n🚶‍♂️ Cancelando cambios...")
                                break
                        else:
                            print("\nRespuesta inválida")
                else:
                    print("\nProducto no encontrado")
        elif opcion == "4":
             # Llama al submenú para actualizar precios
             submenu_actualizar_precios()
        elif opcion == "0":
            break
        else:
            print("\nOpción inválida.")
