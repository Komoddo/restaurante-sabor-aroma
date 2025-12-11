from base_datos.conexion_db import Conexion                           # Manejo de la conexión a la base de datos           
from Modelo.Orden import Orden                                        # Modelo Orden                                       # Modelo Mesa
from Servicio.OrdenDetalle_Servicio import OrdenDetalleServicio       # Servicio para manejar los detalles de la orden
from Principal import LISTA_ORDENES                                   # Lista que almacena temporalmente todas las órdenes cargadas en memoria durante la ejecución

class OrdenServicio:
    def __init__(self):
        self.ordenes = []                  # Lista interna de órdenes
        self.f_ordenes = []                # Lista interna de órdenes

    def agregar_orden_lista(self, orden:Orden):
        LISTA_ORDENES.append(orden)                 # Agrega la orden a la lista global en memoria

    def crear_orden_bd(self, o: Orden):
        """Crea una nueva orden en la base de datos."""
        try:
            conn = Conexion()                          # Conexión a BD
            cursor = conn.conectar()                   # Cursor para ejecutar SQL
            cursor.execute("""
                INSERT INTO ordenes (id_mesa, id_empleado, id_cliente, fecha_hora, nro_personas, estado, nota, total_parcial)
                VALUES (?, ?, ?, ?, ?, ?, ?, ?)""",
                (o.id_mesa, o.id_empleado, o.id_cliente, o.fecha_hora, o.nro_personas, o.estado, o.nota, o.total))

            conn.commit()                                 # Guarda cambios en BD
            return cursor.lastrowid                       # Retorna ID de la orden creada         
        except Exception as e:
            print("Error al crear orden:", e)
        finally:
            conn.cerrar()                                 # Cierra la conexión

    def actualizar_total_orden_bd(self, o: Orden):
        """Actualiza el total de una orden en la base de datos."""       
        try:
            conexion = Conexion()                           # Conexión a BD
            cursor = conexion.conectar()                    # Cursor para ejecutar SQL

            cursor.execute('''UPDATE ordenes SET total_parcial = ? WHERE id_orden = ? ''', (o.total ,o.id_orden))
            conexion.conn.commit()
            return cursor.rowcount

        except Exception as e:
            print("Error al obtener orden:", e)

    def actualizar_orden_bd(self, o: Orden):
        """Actualiza una orden en la base de datos."""
        try:
            conexion = Conexion()
            cursor = conexion.conectar()

            cursor.execute('''UPDATE ordenes SET
                           id_mesa = ?,
                           nro_personas = ? 
                           WHERE id_orden = ? ''', (o.id_mesa, o.nro_personas ,o.id_orden))
            conexion.conn.commit()
            return cursor.rowcount

        except Exception as e:
            print("Error al obtener orden:", e)

    def obtener_orden_por_id(self, id_orden:int)->Orden:
        """Busca una orden por su ID en la lista de órdenes."""
        orden = None
        if LISTA_ORDENES:
            orden = next((o for o in LISTA_ORDENES if o.id_orden==id_orden),None)
        if orden:
            return orden
        return None

    def obtener_orden_pendiente_por_id(self, id_orden:int)->Orden:
        """Busca una orden por su ID en la lista de órdenes."""
        orden = None
        if LISTA_ORDENES:
            orden = next((o for o in LISTA_ORDENES if o.id_orden==id_orden and o.estado.lower()=="pendiente"),None)
        if orden:
            return orden
        return None
    
    def obtener_orden_pendiente_por_mesa_id(self, id_mesa:int)->Orden:
        """Busca una orden por su ID en la lista de órdenes."""
        orden = None
        if LISTA_ORDENES:
            orden = next((o for o in LISTA_ORDENES if o.id_mesa==id_mesa and o.estado.lower()=="pendiente"),None)
        if orden:
            return orden
        return None

    def obtener_ordenes_bd(self):
        """Obtiene todas las órdenes de la base de datos y actualiza LISTA_ORDENES."""
        try:
            LISTA_ORDENES.clear()          # Limpia lista antes de cargar datos
            ods = OrdenDetalleServicio()       # Servicio para obtener detalles
            conn = Conexion()
            cursor = conn.conectar()
            cursor.execute("SELECT * FROM ordenes")
            rows = cursor.fetchall()                # Obtiene todas las filas

            # return [Orden(*row) for row in rows]
            LISTA_ORDENES.extend([Orden(id_orden=row[0], id_mesa=row[1], id_empleado=row[2], 
                                     id_cliente=row[3], fecha_hora=row[4], nro_personas=row[5],
                                     estado=row[6], nota=row[7], total=row[8]) for row in rows])
            if LISTA_ORDENES:
                for orden in LISTA_ORDENES:
                    detalles = ods.obtener_detalles_por_orden(orden.id_orden)   # Obtiene detalles de la orden
                    if detalles:
                        for detalle in detalles:
                            orden.agregar_detalle(detalle)          # Agrega detalles a la orden
        except Exception as e:
            print("Error al listar ordenes:", e)

    def obtener_ordenes_pendientes(self):
        """Obtiene todas las órdenes pendientes de la lista de ordenes."""
        if LISTA_ORDENES:
            pendientes = [o for o in LISTA_ORDENES if o.estado.lower() == "pendiente"]    # Filtra pendientes
            return pendientes
        return None

    def actualizar_estado_orden_bd(self, id_orden, nuevo_estado):
        """Actualiza el estado de una orden en la base de datos."""
        conn = Conexion()
        cursor = conn.conectar()

        try:    # Actualiza estado de la orden
            cursor.execute("""
            UPDATE ordenes SET estado = ? WHERE id_orden = ?
            """, (nuevo_estado, id_orden))
            conn.commit()     # Guarda cambios
            return cursor.rowcount    # Retorna filas afectadas
        except Exception as ex:
            return None
        finally:
            conn.cerrar()
            
    def validar_orden_completa(self, orden: Orden):
        """Valida que la orden tenga mesa, empleado y cliente asignados."""
        if not orden.id_mesa or not orden.id_empleado or not orden.id_cliente:
            return False     # Retorna False si falta algún dato
        return True           # Retorna True si la orden está completa