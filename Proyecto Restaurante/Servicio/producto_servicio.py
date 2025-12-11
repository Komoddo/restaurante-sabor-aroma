from typing import List
from base_datos.conexion_db import Conexion
from Modelo.Producto import Producto
from Principal import LISTA_PRODUCTOS

class ProductoServicio:
    def __init__(self):
        # self.catalogo = {}
        self.categorias = {}

    # --------------------------
    #   CREATE
    # --------------------------
    
    # Agrega producto a la lista general
    def agregar_producto_lst(self, producto: Producto):
        LISTA_PRODUCTOS.append(producto)
    
    # Devuelve la lista de productos general
    def obtener_lista_productos(self):
        return LISTA_PRODUCTOS
    
    def obtener_lista_productos_disponibles(self):
        """Devuelve la lista de productos disponibles."""
        disponibles = [pd for pd in LISTA_PRODUCTOS if pd.disponibilidad]
        return disponibles

    def agregar_producto_bd(self, producto: Producto):
        """Agrega un producto a la base de datos y devuelve su ID."""
        conn = Conexion()
        cursor = conn.conectar()

        try:
            cursor.execute("""
            INSERT INTO productos (nombre, descripcion, precio, categoria, disponibilidad)
            VALUES (?, ?, ?, ?, ?)
            """, (producto.nombre, producto.descripcion, producto.precio,
              producto.categoria, producto.disponibilidad))
            
            conn.commit()
            return cursor.lastrowid
        except Exception as ex:
            conn.rollback()
        finally:
            conn.cerrar()

    #   Leer todos los productos de la base de datos
    def obtener_productos_bd(self):
        """Obtiene todos los productos de la base de datos y actualiza LISTA_PRODUCTOS."""
        LISTA_PRODUCTOS.clear()
        conn = Conexion()
        cursor = conn.conectar()

        try:
            cursor.execute("SELECT * FROM productos ORDER BY LOWER(nombre)")
            filas = cursor.fetchall()
            if not filas:
                return []
            LISTA_PRODUCTOS.clear()
            return LISTA_PRODUCTOS.extend([Producto(id_producto=row[0], nombre=row[1], 
                                     descripcion=row[2], precio=row[3], 
                                     categoria=row[4], disponibilidad=row[5]) for row in filas])
        except Exception as ex:
            return []
        finally:
            conn.cerrar()

    def obtener_producto_por_id_bd(self, producto_id: int):
        """Obtiene un producto por su ID."""
        conn = Conexion()
        cursor = conn.conectar()

        cursor.execute("SELECT * FROM productos WHERE id=?", (producto_id,))
        row = cursor.fetchone()
        return self._fila_a_producto(row) if row else None

    def obtener_producto_por_id(self, id: int):
        """Busca un producto por su ID en la lista de productos."""
        if(LISTA_PRODUCTOS):
            producto = next((p for p in LISTA_PRODUCTOS if p.id_producto==id),None)
        return producto

    def obtener_producto_disponible_por_id(self, id: int):
        """Busca un producto por su ID en la lista de productos."""
        if(LISTA_PRODUCTOS):
            producto = next((p for p in LISTA_PRODUCTOS if (p.id_producto==id and p.disponibilidad)),None)
        return producto
    
    # --------------------------
    #   UPDATE
    # --------------------------
    def actualizar_producto_bd(self, producto: Producto):
        """Actualiza un producto en la base de datos."""
        conn = Conexion()
        cursor = conn.conectar()

        cursor.execute("""
            UPDATE productos
            SET nombre=?, descripcion=?, categoria=?, disponibilidad=?
            WHERE id_producto=?
        """, (producto.nombre, producto.descripcion,
              producto.categoria, producto.disponibilidad, producto.id_producto))

        conn.commit()
        return cursor.rowcount

    def actualizar_precio_producto_bd(self, productos:list):
        """Actualiza el precio de un producto en la base de datos."""
        conn = Conexion()
        cursor = conn.conectar()

        try:
            for p in productos:
                cursor.execute("""
                    UPDATE productos
                    SET precio=?
                    WHERE id_producto=?
                """, (p.precio, p.id_producto))

            conn.commit()
            if(cursor.rowcount):
                return True
            return False
        except Exception as ex:
            return None
        finally:
            conn.cerrar()

    def crear_categorias(self):
        """Crea un diccionario de categorías con números consecutivos."""
        categorias = sorted({p.categoria for p in LISTA_PRODUCTOS})
        self.categorias = {i: c for i, c in enumerate(categorias, start=1)}
        return self.categorias

    def filtrar_productos_por_categoria(self, categoria:str):
        """Filtra productos por categoría."""
        if LISTA_PRODUCTOS:
            productos_por_categoria = [p for p in LISTA_PRODUCTOS if p.categoria==categoria and p.disponibilidad]
            return productos_por_categoria

    def _fila_a_producto(self, r):
        """Convierte una fila de la base de datos en un objeto Producto."""
        return Producto(
            id_producto=r[0],
            nombre=r[1],
            descripcion=r[2],
            precio=r[3],
            categoria=r[4],
            disponibilidad=r[5]
        )
    
    def validar_producto(self, nombre:str) -> Producto:
        """Busca un producto que coincida con el nombre en la lista de productos."""
        producto = next((p for p in LISTA_PRODUCTOS if nombre.strip().lower()==p.nombre.lower()),None)
        return producto
         
    def buscar_productos(self, nombre:str) -> List[Producto]:
        """Busca un producto que coincida con el nombre en la lista de productos."""
        productos = [p for p in LISTA_PRODUCTOS if nombre.strip().lower() in p.nombre.lower()]
        return productos
    
    def buscar_productos_disponibles(self, nombre:str) -> List[Producto]:
        """Busca un producto que coincida con el nombre en la lista de productos."""
        productos = [p for p in LISTA_PRODUCTOS if nombre.strip().lower() in p.nombre.lower() and p.disponibilidad]
        return productos
         
    def obtener_catalogo(self):
        """Obtiene el catálogo de productos."""
        if LISTA_PRODUCTOS:
            catalogo = [p for p in LISTA_PRODUCTOS if p.disponibilidad]
        categorizados = {}
        for item in catalogo:
            categoria = item.categoria
            if categoria not in categorizados:
                categorizados[categoria] = []
            categorizados[categoria].append(item)
        return categorizados
        