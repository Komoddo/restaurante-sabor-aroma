from base_datos.conexion_db import Conexion

class AuditoriaPrecioServicio:
    def __init__(self):
          pass

    """Inserta los cambios de precios de productos en la base de datos."""
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