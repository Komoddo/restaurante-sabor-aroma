from Modelo.Producto import Producto
from Servicio.producto_servicio import ProductoServicio
from base_datos.conexion_db import Conexion

class AuditoriaPrecioServicio:
    def __init__(self):
          pass

    # def actualizar_precios_por_fecha(self, fecha_efectiva: str, ajustes: Dict[str, float]):
    #     """Actualiza precios con fecha efectiva."""
    #     try:
    #         # Actualizar precios inmediatamente
    #         actualizados = 0
    #         for i, (nombre, descripcion, precio, categoria) in enumerate(self.catalogo):
    #             if nombre in ajustes:
    #                 nuevo_precio = ajustes[nombre]
    #                 self.catalogo[i] = (nombre, descripcion, nuevo_precio, categoria)
    #                 actualizados += 1
    #                 print(f" {nombre}: S/{precio:.2f} → S/{nuevo_precio:.2f}")

    #         # Registrar cambios en BD
    #         self.registrar_cambio_precios_bd(fecha_efectiva, ajustes)
    #         print(f" Se actualizaron {actualizados} productos")
    #         return True

    #     except Exception as e:
    #         print(f" Error al actualizar precios: {e}")
    #         return False
        

    def registrar_cambio_precios_bd(self, auditoria_precios:list):
        """Registra cambios de precios en la base de datos para auditoría."""
        try:
            conn = Conexion()
            cursor = conn.conectar()

            for ap in auditoria_precios:
                cursor.execute('''
                    INSERT INTO auditoria_precios
                    (fecha_cambio, id_producto, precio_anterior, precio_nuevo)
                    VALUES (?, ?, ?, ?)
                ''', (ap.fecha_cambio, ap.id_producto, ap.precio_anterior, ap.precio_nuevo))
                if not (cursor.lastrowid):
                    return False        
            
            conn.commit()
            return True
        except Exception as e:
            print(f" Error al registrar cambios de precios: {e}")
        finally:
            conn.cerrar()