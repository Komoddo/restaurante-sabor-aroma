from Presentacion.Menu_Venta import menu_venta                  # Importa el módulo para gestionar ventas
from Presentacion.Menu_Orden import menu_orden                    # Importa el módulo para gestionar órdenes
from Presentacion.Menu_Gestion import menu_gestion                # Importa el módulo para actualizaciones generales
from Presentacion.Menu_Reporte import menu_reporte                # Importa el módulo para generar reportes

from Servicio.producto_servicio import ProductoServicio           # Servicio para manejar productos
from Servicio.Cliente_Servicio import ClienteServicio             # Servicio para manejar clientes
from Servicio.Empleado_Servicio import EmpleadoServicio           # Servicio para manejar empleados
from Servicio.Mesa_Servicio import MesaServicio                   # Servicio para manejar mesas
from Servicio.Orden_Servicio import OrdenServicio                 # Servicio para manejar órdenes
from base_datos.restaurante_db import RestaurantDB
# Clase de inicialización de la base de datos


# Instanciación de los servicios
os = OrdenServicio()           # Servicio de órdenes
ps = ProductoServicio()        # Servicio de productos
cs = ClienteServicio()         # Servicio de clientes
es = EmpleadoServicio()       # Servicio de empleados
ms = MesaServicio()           # Servicio de mesas

def menu_principal():
    
    #Inicializa la base de datos y carga los datos iniciales
    RestaurantDB()                # Crea la conexión y estructura de la BD
    ps.obtener_productos_bd()     # Carga los productos
    cs.obtener_clientes_bd()      # Carga los clientes
    es.obtener_Empleados_bd()     # Carga los empleados
    ms.obtener_mesas_bd()         # Carga las mesas disponibles


    while True:
        # Muestra el menú principal del sistema
        print("\n" + "-"*100)
        print("RESTAURANTE SABOR & AROMA 🍽️")
        print("-"*100)
        print("\n1. 🧾 Gestión de Órdenes")
        print("2. 📋 Gestión de ventas")
        print(f"3. {'🛠️ '} Actualizaciones generales")
        print("4. 📊 Reportes (SQL & Gráficos)")
        print("0. 🔙 Salir del sistema")
        # print("\n" + "-"*100)

        print("\nSeleccione una opción: ")
        opcion = input("➤  ").strip()
        
        if opcion == "1":
             # Accede al submenú de órdenes
            menu_orden()
        elif opcion == "2":
            # Accede al submenú de ventas
            menu_venta()
        elif opcion == "3":
             # Accede al submenú de gestión general
            menu_gestion()
        elif opcion == "4":
            # Accede al submenú de reportes
            menu_reporte()
        elif opcion == "0":
            # Sale del sistema
            print("\ndesea salir del sistema? (s/n)")
            respuesta = input().strip().lower()
            if respuesta == "s":
                print("\nSaliendo del sistema...")
                break
        else:
            # Maneja opción inválida
            print("❌ Opción incorrecta")