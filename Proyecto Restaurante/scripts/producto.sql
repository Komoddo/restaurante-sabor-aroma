CREATE TABLE IF NOT EXISTS productos (
                    idProducto INTEGER PRIMARY KEY AUTOINCREMENT,
                    nombre TEXT NOT NULL,
                    descripcion TEXT NULL,
                    precio REAL NOT NULL,
                    categoria TEXT NOT NULL,
                    estado    BOOLEAN    NOT NULL DEFAULT 1,
                    fecha_registro DATETIME DEFAULT CURRENT_TIMESTAMP
                )