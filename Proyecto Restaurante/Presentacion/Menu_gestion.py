from Presentacion.Menu_Cliente import submenu_clientes
from Presentacion.Menu_Empleado import submenu_Empleados
from Presentacion.Menu_Producto import submenu_productos


def menu_gestion():
        """Menú especializado para gestionar todas las actualizaciones."""
        while True:
            print("\n" + "="*60)
            print("🔄 MENÚ DE ACTUALIZACIONES - RESTAURANTE")
            print("="*60)
            print("1. 💰 Gestionar Productos")
            print("2. 📦 Gestionar Clientes")
            print("3. 👥 Gestionar Empleado")
            print("4. 👥 Gestionar Mesas")
            print("0. ⬅️  Volver al Menú Principal")
            print("="*60)

            try:
                opcion = input("Seleccione una opción: ").strip()

                if opcion == "1":
                    submenu_productos()
                    break
                elif opcion == "2":
                    submenu_clientes()
                    break
                elif opcion == "3":
                    submenu_Empleados()
                    break
                    
                elif opcion == "4":
                    continue
                    # submenu_mesas()
                elif opcion == "0":
                    print("Regresando al menú principal...")
                    break
                else:
                    print(" Opción inválida. Intente de nuevo.")

            except Exception as e:
                print(f" Error: {e}")