"""Importación de entidades y servicios de los módulos correspondientes"""
from Modelo.Cliente import Cliente
from Modelo.Empleado import Empleado
from Modelo.Producto import Producto
from Servicio.Cliente_Servicio import ClienteServicio
from Servicio.Empleado_Servicio import EmpleadoServicio
from Servicio.producto_servicio import ProductoServicio

"""Se crean instancias de los servicios correspondientes"""
cs = ClienteServicio()
es = EmpleadoServicio()
ps = ProductoServicio()


"""
Lista de entidades de clientes, empleados, productos y mesas.
Con formato válido para inserción en base de datos.
"""

clientes = [
    Cliente(nombre="Diego", apellido="Ramírez", email="diego.ramirez@example.com", telefono="900200001"),
    Cliente(nombre="Lucía", apellido="Gutiérrez", email="lucia.gutierrez@example.com", telefono="900200002"),
    Cliente(nombre="Pedro", apellido="Torres", email="pedro.torres@example.com", telefono="900200003"),
    Cliente(nombre="Elena", apellido="Salazar", email="elena.salazar@example.com", telefono="900200004"),
    Cliente(nombre="Juan", apellido="Flores", email="juan.flores@example.com", telefono="900200005"),
    Cliente(nombre="María", apellido="Castro", email="maria.castro@example.com", telefono="900200006"),
    Cliente(nombre="Carlos", apellido="Rivas", email="carlos.rivas@example.com", telefono="900200007"),
    Cliente(nombre="Ana", apellido="Gómez", email="ana.gomez@example.com", telefono="900200008"),
    Cliente(nombre="Luis", apellido="Soto", email="luis.soto@example.com", telefono="900200009"),
    Cliente(nombre="Marta", apellido="Paredes", email="marta.paredes@example.com", telefono="900200010"),
    Cliente(nombre="Jorge", apellido="Herrera", email="jorge.herrera@example.com", telefono="900200011"),
    Cliente(nombre="Sofía", apellido="Aguilar", email="sofia.aguilar@example.com", telefono="900200012"),
    Cliente(nombre="Hugo", apellido="Navarro", email="hugo.navarro@example.com", telefono="900200013"),
    Cliente(nombre="Isabel", apellido="Vargas", email="isabel.vargas@example.com", telefono="900200014"),
    Cliente(nombre="Renato", apellido="Rojas", email="renato.rojas@example.com", telefono="900200015"),
    Cliente(nombre="Daniela", apellido="Quispe", email="daniela.quispe@example.com", telefono="900200016"),
    Cliente(nombre="Ricardo", apellido="Mendoza", email="ricardo.mendoza@example.com", telefono="900200017"),
    Cliente(nombre="Patricia", apellido="Cárdenas", email="patricia.cardenas@example.com", telefono="900200018"),
    Cliente(nombre="Andrés", apellido="Ponce", email="andres.ponce@example.com", telefono="900200019"),
    Cliente(nombre="Gabriela", apellido="Vera", email="gabriela.vera@example.com", telefono="900200020"),
    Cliente(nombre="Henry", apellido="Montoya", email="henry.montoya@example.com", telefono="900200021"),
    Cliente(nombre="Valeria", apellido="Lozano", email="valeria.lozano@example.com", telefono="900200022"),
    Cliente(nombre="Adrián", apellido="Peña", email="adrian.pena@example.com", telefono="900200023"),
    Cliente(nombre="Rosa", apellido="Chávez", email="rosa.chavez@example.com", telefono="900200024"),
    Cliente(nombre="Samuel", apellido="Prieto", email="samuel.prieto@example.com", telefono="900200025"),
    Cliente(nombre="Carmen", apellido="Delgado", email="carmen.delgado@example.com", telefono="900200026"),
    Cliente(nombre="Tomás", apellido="Villanueva", email="tomas.villanueva@example.com", telefono="900200027"),
    Cliente(nombre="Silvia", apellido="Arévalo", email="silvia.arevalo@example.com", telefono="900200028"),
    Cliente(nombre="Rodrigo", apellido="Valencia", email="rodrigo.valencia@example.com", telefono="900200029"),
    Cliente(nombre="Estefanía", apellido="Cruz", email="estefania.cruz@example.com", telefono="900200030"),
    Cliente(nombre="Mauricio", apellido="Pacheco", email="mauricio.pacheco@example.com", telefono="900200031"),
    Cliente(nombre="Paola", apellido="Linares", email="paola.linares@example.com", telefono="900200032"),
    Cliente(nombre="Fernando", apellido="Mejía", email="fernando.mejia@example.com", telefono="900200033"),
    Cliente(nombre="Nadia", apellido="Salas", email="nadia.salas@example.com", telefono="900200034"),
    Cliente(nombre="Gustavo", apellido="Reyes", email="gustavo.reyes@example.com", telefono="900200035"),
    Cliente(nombre="Ruth", apellido="Cornejo", email="ruth.cornejo@example.com", telefono="900200036"),
    Cliente(nombre="Fabián", apellido="Ibáñez", email="fabian.ibanez@example.com", telefono="900200037"),
    Cliente(nombre="Leticia", apellido="Poma", email="leticia.poma@example.com", telefono="900200038"),
    Cliente(nombre="Óscar", apellido="Vásquez", email="oscar.vasquez@example.com", telefono="900200039"),
    Cliente(nombre="Liliana", apellido="Arce", email="liliana.arce@example.com", telefono="900200040"),
    Cliente(nombre="Raúl", apellido="Sánchez", email="raul.sanchez@example.com", telefono="900200041"),
    Cliente(nombre="Jimena", apellido="Maldonado", email="jimena.maldonado@example.com", telefono="900200042"),
    Cliente(nombre="Sebastián", apellido="Bravo", email="sebastian.bravo@example.com", telefono="900200043"),
    Cliente(nombre="Karen", apellido="Fuentes", email="karen.fuentes@example.com", telefono="900200044"),
    Cliente(nombre="Álvaro", apellido="Núñez", email="alvaro.nunez@example.com", telefono="900200045"),
    Cliente(nombre="Bianca", apellido="Peralta", email="bianca.peralta@example.com", telefono="900200046"),
    Cliente(nombre="Franco", apellido="Barrios", email="franco.barrios@example.com", telefono="900200047"),
    Cliente(nombre="Lorena", apellido="Huamán", email="lorena.huaman@example.com", telefono="900200048"),
    Cliente(nombre="Eduardo", apellido="Rengifo", email="eduardo.rengifo@example.com", telefono="900200049"),
    Cliente(nombre="Tatiana", apellido="Silva", email="tatiana.silva@example.com", telefono="900200050")
]


empleados = [
    Empleado(nombre="Diego", apellido="Ramírez", dni="40000001", cargo="mozo", telefono="900100001", estado="activo"),
    Empleado(nombre="Lucía", apellido="Gutiérrez", dni="40000002", cargo="cajero", telefono="900100002", estado="inactivo"),
    Empleado(nombre="Pedro", apellido="Torres", dni="40000003", cargo="limpieza", telefono="900100003", estado="activo"),
    Empleado(nombre="Elena", apellido="Salazar", dni="40000004", cargo="cocinero", telefono="900100004", estado="retirado"),
    Empleado(nombre="Juan", apellido="Flores", dni="40000005", cargo="mozo", telefono="900100005", estado="activo"),
    Empleado(nombre="María", apellido="Castro", dni="40000006", cargo="cajero", telefono="900100006", estado="activo"),
    Empleado(nombre="Carlos", apellido="Rivas", dni="40000007", cargo="limpieza", telefono="900100007", estado="inactivo"),
    Empleado(nombre="Ana", apellido="Gómez", dni="40000008", cargo="cocinero", telefono="900100008", estado="activo"),
    Empleado(nombre="Luis", apellido="Soto", dni="40000009", cargo="mozo", telefono="900100009", estado="retirado"),
    Empleado(nombre="Marta", apellido="Paredes", dni="40000010", cargo="cajero", telefono="900100010", estado="activo"),
    Empleado(nombre="Jorge", apellido="Herrera", dni="40000011", cargo="limpieza", telefono="900100011", estado="activo"),
    Empleado(nombre="Sofía", apellido="Aguilar", dni="40000012", cargo="cocinero", telefono="900100012", estado="inactivo"),
    Empleado(nombre="Hugo", apellido="Navarro", dni="40000013", cargo="mozo", telefono="900100013", estado="activo"),
    Empleado(nombre="Isabel", apellido="Vargas", dni="40000014", cargo="cajero", telefono="900100014", estado="retirado"),
    Empleado(nombre="Renato", apellido="Rojas", dni="40000015", cargo="limpieza", telefono="900100015", estado="activo"),
    Empleado(nombre="Daniela", apellido="Quispe", dni="40000016", cargo="cocinero", telefono="900100016", estado="activo"),
    Empleado(nombre="Ricardo", apellido="Mendoza", dni="40000017", cargo="mozo", telefono="900100017", estado="inactivo"),
    Empleado(nombre="Patricia", apellido="Cárdenas", dni="40000018", cargo="cajero", telefono="900100018", estado="activo"),
    Empleado(nombre="Andrés", apellido="Ponce", dni="40000019", cargo="limpieza", telefono="900100019", estado="retirado"),
    Empleado(nombre="Gabriela", apellido="Vera", dni="40000020", cargo="cocinero", telefono="900100020", estado="activo"),
    Empleado(nombre="Henry", apellido="Montoya", dni="40000021", cargo="mozo", telefono="900100021", estado="activo"),
    Empleado(nombre="Valeria", apellido="Lozano", dni="40000022", cargo="cajero", telefono="900100022", estado="inactivo"),
    Empleado(nombre="Adrián", apellido="Peña", dni="40000023", cargo="limpieza", telefono="900100023", estado="activo"),
    Empleado(nombre="Rosa", apellido="Chávez", dni="40000024", cargo="cocinero", telefono="900100024", estado="activo"),
    Empleado(nombre="Samuel", apellido="Prieto", dni="40000025", cargo="mozo", telefono="900100025", estado="retirado")
]


productos = [
    Producto(nombre="Café Americano", descripcion="Café caliente sin azúcar", precio=4.50, categoria="bebida", disponibilidad=1),
    Producto(nombre="Café Expreso", descripcion="Café intenso en taza pequeña", precio=5.20, categoria="bebida", disponibilidad=1),
    Producto(nombre="Té de Manzanilla", descripcion="Infusión relajante de manzanilla", precio=3.80, categoria="bebida", disponibilidad=1),
    Producto(nombre="Jugo de Naranja", descripcion="Jugo natural recién exprimido", precio=6.00, categoria="bebida", disponibilidad=1),
    Producto(nombre="Chocolate Caliente", descripcion="Bebida caliente a base de cacao", precio=5.90, categoria="bebida", disponibilidad=0),
    Producto(nombre="Inca Kola 500ml", descripcion="Bebida gaseosa dulce peruana", precio=4.20, categoria="bebida", disponibilidad=1),
    Producto(nombre="Coca Cola 500ml", descripcion="Gaseosa estándar de cola", precio=4.20, categoria="bebida", disponibilidad=1),
    Producto(nombre="Limonada", descripcion="Refresco de limón natural", precio=5.50, categoria="bebida", disponibilidad=0),
    Producto(nombre="Agua Mineral", descripcion="Botella de agua sin gas", precio=2.50, categoria="bebida", disponibilidad=1),
    Producto(nombre="Emoliente", descripcion="Bebida tradicional caliente de hierbas", precio=3.50, categoria="bebida", disponibilidad=1),
    Producto(nombre="Torta de Chocolate", descripcion="Porción de torta cremosa de chocolate", precio=7.50, categoria="postre", disponibilidad=1),
    Producto(nombre="Pie de Limón", descripcion="Postre dulce y ácido con merengue", precio=6.80, categoria="postre", disponibilidad=1),
    Producto(nombre="Gelatina de Fresa", descripcion="Gelatina tradicional sabor fresa", precio=3.00, categoria="postre", disponibilidad=1),
    Producto(nombre="Flan Casero", descripcion="Flan de leche con caramelo", precio=4.80, categoria="postre", disponibilidad=0),
    Producto(nombre="Helado de Vainilla", descripcion="Helado cremoso sabor vainilla", precio=5.20, categoria="postre", disponibilidad=1),
    Producto(nombre="Crema Volteada", descripcion="Postre peruano a base de huevo", precio=6.00, categoria="postre", disponibilidad=1),
    Producto(nombre="Mazamorra Morada", descripcion="Postre tradicional peruano de maíz morado", precio=4.50, categoria="postre", disponibilidad=1),
    Producto(nombre="Arroz con Leche", descripcion="Postre cremoso de arroz con leche", precio=4.50, categoria="postre", disponibilidad=0),
    Producto(nombre="Brownie", descripcion="Brownie de chocolate con nueces", precio=6.40, categoria="postre", disponibilidad=1),
    Producto(nombre="Tres Leches", descripcion="Bizcocho empapado en mezcla de leches", precio=7.80, categoria="postre", disponibilidad=1),
    Producto(nombre="Menú Criollo", descripcion="Plato del día estilo criollo", precio=12.50, categoria="menú", disponibilidad=1),
    Producto(nombre="Menú Vegetariano", descripcion="Plato del día sin proteína animal", precio=11.00, categoria="menú", disponibilidad=1),
    Producto(nombre="Menú Económico", descripcion="Opción económica con plato principal", precio=9.50, categoria="menú", disponibilidad=1),
    Producto(nombre="Pollo Guisado", descripcion="Plato de pollo en salsa acompañado de arroz", precio=13.80, categoria="menú", disponibilidad=0),
    Producto(nombre="Seco de Carne", descripcion="Guiso de carne con frijoles y arroz", precio=15.00, categoria="menú", disponibilidad=1),
    Producto(nombre="Ají de Gallina", descripcion="Plato peruano de gallina desmenuzada y crema amarilla", precio=14.50, categoria="menú", disponibilidad=1),
    Producto(nombre="Lomo Saltado", descripcion="Carne salteada con cebolla y papas fritas", precio=16.50, categoria="menú", disponibilidad=1),
    Producto(nombre="Bistec a lo Pobre", descripcion="Bistec con huevo, plátano y papas", precio=18.00, categoria="menú", disponibilidad=1),
    Producto(nombre="Tallarin Saltado", descripcion="Tallarines con carne salteada al wok", precio=14.00, categoria="menú", disponibilidad=0),
    Producto(nombre="Chanfainita", descripcion="Guiso peruano con mote y papa", precio=12.80, categoria="menú", disponibilidad=1),
    Producto(nombre="Papa a la Huancaína", descripcion="Rodajas de papa con salsa huancaína", precio=8.00, categoria="entrada", disponibilidad=1),
    Producto(nombre="Causa Limeña", descripcion="Causa rellena con pollo o atún", precio=9.50, categoria="entrada", disponibilidad=1),
    Producto(nombre="Leche de Tigre", descripcion="Jugo de ceviche con pescado picado", precio=10.00, categoria="entrada", disponibilidad=1),
    Producto(nombre="Ensalada Rusa", descripcion="Ensalada fría de papa, zanahoria y arvejas", precio=7.00, categoria="entrada", disponibilidad=0),
    Producto(nombre="Tequeños", descripcion="Rollos crocantes rellenos de queso", precio=9.00, categoria="entrada", disponibilidad=1),
    Producto(nombre="Anticuchos", descripcion="Brochetas de corazón de res marinadas", precio=12.00, categoria="entrada", disponibilidad=1),
    Producto(nombre="Chicharrón de Pescado", descripcion="Trozo de pescado frito crocante", precio=14.50, categoria="entrada", disponibilidad=1),
    Producto(nombre="Sopa Wantán", descripcion="Caldo oriental con wantanes", precio=11.00, categoria="entrada", disponibilidad=1),
    Producto(nombre="Tamal Criollo", descripcion="Tamal de pollo estilo peruano", precio=6.20, categoria="entrada", disponibilidad=0),
    Producto(nombre="Palta Rellena", descripcion="Aguacate relleno con pollo", precio=9.20, categoria="entrada", disponibilidad=1),
    Producto(nombre="Mote con Queso", descripcion="Plato tradicional serrano", precio=5.00, categoria="entrada", disponibilidad=1),
    Producto(nombre="Sopa de Pollo", descripcion="Sopa casera con verduras", precio=8.50, categoria="entrada", disponibilidad=1),
    Producto(nombre="Choclo con Queso", descripcion="Choclo tierno acompañado con queso fresco", precio=7.50, categoria="entrada", disponibilidad=1),
    Producto(nombre="Yuca Frita", descripcion="Porción de yuca crocante", precio=6.70, categoria="entrada", disponibilidad=1),
    Producto(nombre="Ensalada Mixta", descripcion="Ensalada de verduras frescas", precio=6.90, categoria="entrada", disponibilidad=1)
]

"""Método para inserción de clientes en base de datos"""
def add_cliente():
    for c in clientes:
        cs.agregar_cliente_bd(c)

"""Método para inserción de empleados en base de datos"""
def add_empleado():
    for e in empleados:
        es.agregar_empleado_bd(e)

"""Método para inserción de productos en base de datos"""
def add_producto():
    for p in productos:
        ps.agregar_producto_bd(p)

def add_database():
    add_cliente()
    add_empleado()
    add_producto()


