from datetime import datetime
from base_datos.conexion_db import Conexion
from Modelo.Venta import Venta
from Servicio.VentaDetalle_Servicio import DetalleventaServicio
from Principal import LISTA_VENTAS

class ventaServicio:
    def __init__(self):
        pass
    # --------------------------
    #   CREATE
    # --------------------------
    def crear_venta_bd(self, p : Venta):
        try:
            conn = Conexion()
            cursor = conn.conectar()
            cursor.execute("""
            INSERT INTO ventas (
                id_orden, 
                fecha,
                subtotal, 
                impuestos, 
                descuento, 
                total, 
                metodo_pago,
                estado)
            VALUES (?, ?, ?, ?, ?, ?, ?, ?)
        """, (
            p.id_orden, 
            p.fecha, 
            p.subtotal, 
            p.impuestos, 
            p.descuento, 
            p.total, 
            p.metodo_pago,
            p.estado))
            
            conn.commit()
            return cursor.lastrowid
        except Exception as e:
            print("Error al crear orden:", e)
        finally:
            conn.cerrar()

    # --------------------------
    #   READ ALL
    # --------------------------
    def obtener_ventas_bd(self):
        """Obtiene todas las ventas de la base de datos y actualiza LISTA_VENTAS."""
        try:
            LISTA_VENTAS.clear()
            vds = DetalleventaServicio()
            conn = Conexion()
            cursor = conn.conectar()
            cursor.execute("SELECT * FROM ventas ORDER BY fecha DESC")
            rows = cursor.fetchall()

            LISTA_VENTAS.extend([Venta(id_venta=row[0], id_orden=row[1], 
                                    fecha=row[2], subtotal=row[3], 
                                    impuestos=row[4], descuento=row[5],
                                    total=row[6], metodo_pago=row[7], 
                                    estado=row[8]) for row in rows])
            if LISTA_VENTAS:
                for venta in LISTA_VENTAS:
                    detalles = vds.obtener_detalles_por_venta(venta.id_venta)
                    if detalles:
                        for detalle in detalles:
                            venta.agregar_detalle(detalle)
        except Exception as e:
            print("Error al listar ventas:", e)

    def obtener_lista_ventas(self):
        return LISTA_VENTAS

    def actualizar_venta(self, venta: Venta):
        """Actualiza una venta en la base de datos."""
        conn = Conexion()
        cursor = conn.conectar()
        cursor.execute("""
            UPDATE ventas
            SET cliente_id=?, mesa_id=?, empleado_id=?, total=?, fecha=?
            WHERE id=?
        """, (venta.cliente_id, venta.mesa_id, venta.empleado_id,
              venta.total, venta.fecha, venta.id))
        self.conn.commit()
        return self.cursor.rowcount  # cuántas filas se actualizaron

    def guardar_venta_archivo(self, ticket: str):
        """Guarda una venta en archivo de texto."""
        try:
            archivo = f"datos/ventas_{datetime.now().strftime('%Y%m%d')}.txt"
            with open(archivo, 'a', encoding='utf-8') as f:
                f.write(ticket + '\n')
        except Exception as e:
            print(f" Error al guardar venta en archivo: {e}")