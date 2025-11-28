from Presentacion.Menu_Pedido import menu_pedidos
from Presentacion.Menu_Orden import menu_ordenes
from Presentacion.Menu_gestion import menu_gestion

from Servicio.producto_servicio import ProductoServicio
from Servicio.Cliente_Servicio import ClienteServicio
from Servicio.Empleado_Servicio import EmpleadoServicio
from Servicio.Mesa_Servicio import MesaServicio
from Servicio.Orden_Servicio import OrdenServicio
from base_datos.restaurante_db import RestaurantDB

os = OrdenServicio()
ps = ProductoServicio()
cs = ClienteServicio()
es = EmpleadoServicio()
ms = MesaServicio()

def menu_principal():
    
    RestaurantDB()
    ps.obtener_productos_bd()
    cs.obtener_clientes_bd()
    es.obtener_Empleados_bd()
    ms.obtener_mesas_bd()


    while True:
        print("\n" + "="*45)
        print("SISTEMA DE RESTAURANTE 🍽️")
        print("="*45)
        print("1. 🧾 Gestión de Órdenes")
        print("2. 📋 Gestión de Pedidos")
        print("3. ⚙️ Actualizaciones generales")
        print("0. 🔙 Salir")
        print("-"*45)

        opcion = input("Seleccione una opción: ")
        
        if opcion == "1":
            menu_ordenes()
        elif opcion == "2":
            menu_pedidos()
        elif opcion == "3":
            menu_gestion()
        elif opcion == "0":
            print("Saliendo del sistema...")
            break
        else:
            print("⚠ Opción incorrecta. Intente nuevamente.")