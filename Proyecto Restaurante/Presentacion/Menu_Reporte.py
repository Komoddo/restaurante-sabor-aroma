from Presentacion import SubMenu_ReporteVenta
from Presentacion import SubMenu_ReporteOrden
from Presentacion import SubMenu_ReporteProducto


def menu_reporte():
    while True:
            print("\n" + "-"*100)
            print("REPORTES GENERALES 📊")
            print("-"*100)
            print("\n1. 🧾 Reporte de ventas")
            print("2. 📋 Reporte de ordenes")
            print("3. ⚙️ Reporte de productos")
            print("0. 🔙 Salir")
            print("\n" + "-"*100)

            print("\nSeleccione una opción: ")
            opcion = input("➤  ").strip()

            if opcion == "1":
                SubMenu_ReporteVenta()
            elif opcion == "2":
                SubMenu_ReporteOrden()
            elif opcion == "3":
                SubMenu_ReporteProducto()
            elif opcion == "4":
                ()
            elif opcion == "0":
                print("Saliendo del sistema...")
                break
            else:
                print("⚠ Opción incorrecta. Intente nuevamente.")