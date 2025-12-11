from base_datos.conexion_db import Conexion

class RestaurantDB:
    def __init__(self):
        self.conn = Conexion()
        self.cursor = self.conn.conectar()
        self.create_tables()

    def create_tables(self):
        
        # Tabla de clientes
        self.cursor.execute('''
            CREATE TABLE IF NOT EXISTS clientes (
                id          INTEGER PRIMARY KEY AUTOINCREMENT,
                nombre      TEXT NOT NULL,
                apellido    TEXT NOT NULL,
                email       TEXT,
                telefono    TEXT,
                f_registro DATETIME DEFAULT CURRENT_TIMESTAMP
            )
        ''')
        
        # Tabla de productos
        self.cursor.execute('''
                CREATE TABLE IF NOT EXISTS productos (
                    id_producto      INTEGER PRIMARY KEY AUTOINCREMENT,
                    nombre          TEXT NOT NULL,
                    descripcion     TEXT NULL,
                    precio          REAL NOT NULL,
                    categoria       TEXT NOT NULL,
                    disponibilidad  BOOLEAN DEFAULT 1,
                    f_registro      DATETIME DEFAULT CURRENT_TIMESTAMP
            )
        ''')

        # Tabla de mesas
        self.cursor.execute('''
            CREATE TABLE IF NOT EXISTS mesas (
                id          INTEGER PRIMARY KEY AUTOINCREMENT,
                numero      INTEGER NOT NULL UNIQUE,
                capacidad   INTEGER,
                estado      TEXT DEFAULT 'disponible'
            )
        ''')

        # Tabla Empleados
        self.cursor.execute("""
        CREATE TABLE IF NOT EXISTS empleados(
            id          INTEGER PRIMARY KEY AUTOINCREMENT,
            nombre      TEXT NOT NULL,
            apellido    TEXT NOT NULL,
            dni         TEXT UNIQUE NOT NULL,
            cargo       TEXT,
            telefono    TEXT,
            estado      TEXT    DEFAULT 'activo'                         
        )
        """)

        # Tabla de ventas
        self.cursor.execute('''
            CREATE TABLE IF NOT EXISTS ventas (
                id_venta       INTEGER PRIMARY KEY AUTOINCREMENT,
                id_orden        INTEGER,
                fecha           DATETIME NOT NULL,
                subtotal        REAL NOT NULL,
                impuestos       REAL,            
                descuento       REAL DEFAULT 0,
                total           REAL NOT NULL,
                metodo_pago     TEXT,
                estado          TEXT,                     
                FOREIGN KEY (id_orden) REFERENCES ordenes (id_orden)
            )
        ''')  

        # Tabla de detalle_venta
        self.cursor.execute('''
            CREATE TABLE IF NOT EXISTS detalle_venta(
                id_detalle      INTEGER PRIMARY KEY AUTOINCREMENT,
                id_venta        INTEGER NOT NULL,
                id_producto      INTEGER NOT NULL,
                cantidad        INTEGER NOT NULL,
                precio_unitario REAL NOT NULL,
                subtotal        REAL NOT NULL,
                FOREIGN KEY(id_venta) REFERENCES ventas(id_venta),
                FOREIGN KEY(id_producto) REFERENCES productos(id_producto)
            )
        ''')

        # tabla de ordenes
        self.cursor.execute('''
            CREATE TABLE IF NOT EXISTS ordenes (
                id_orden        INTEGER PRIMARY KEY AUTOINCREMENT,
                id_mesa         INTEGER,
                id_empleado     INTEGER NOT NULL,
                id_cliente      INTEGER,
                fecha_hora      TEXT,
                nro_personas    INTEGER DEFAULT 1,
                estado          TEXT NOT NULL,   -- Pendiente, En cocina, Preparado
                nota            TEXT,
                total_parcial   REAL DEFAULT 0,
                FOREIGN KEY(id_mesa) REFERENCES Mesas(id),
                FOREIGN KEY(id_empleado) REFERENCES empleados(id),
                FOREIGN KEY(id_cliente) REFERENCES clientes(id)
            )
        ''')

        #Tabla de detalle orden
        self.cursor.execute('''
            CREATE TABLE IF NOT EXISTS detalle_orden (
                id_detalle      INTEGER PRIMARY KEY AUTOINCREMENT,
                id_orden        INTEGER NOT NULL,
                id_producto     INTEGER NOT NULL,
                cantidad        INTEGER NOT NULL,
                precio_unitario REAL NOT NULL,
                subtotal        REAL NOT NULL,
                nota            TEXT,
                FOREIGN KEY(id_orden) REFERENCES ordenes(id_orden),
                FOREIGN KEY(id_producto) REFERENCES productos(id_producto)
            )
        ''')

        # Tabla de auditoría de precios
        self.cursor.execute('''
            CREATE TABLE IF NOT EXISTS auditoria_precios (
                id_auditoria    INTEGER PRIMARY KEY AUTOINCREMENT,
                fecha_cambio    DATE NOT NULL,
                id_producto     INTEGER NOT NULL,
                precio_anterior REAL,
                precio_nuevo    REAL NOT NULL,
                fecha_registro  DATETIME DEFAULT CURRENT_TIMESTAMP,
                FOREIGN KEY (id_producto) REFERENCES productos (id_producto)       
            )
        ''')
        self.conn.commit()
        