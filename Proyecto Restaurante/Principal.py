from typing import List
from Modelo.Producto import Producto
from Modelo.Cliente import Cliente
from Modelo.Empleado import Empleado
from Modelo.Mesa import Mesa
from Modelo.Orden import Orden
from Modelo.Venta import Venta


# Listas globales que funcionan como "base de datos en memoria"
LISTA_PRODUCTOS: List[Producto] = []
LISTA_CLIENTES: List[Cliente] = []
LISTA_EMPLEADOS: List[Empleado] = []
LISTA_MESAS: List[Mesa] = []
LISTA_ORDENES: List[Orden] = []
LISTA_VENTAS: List[Venta] = []