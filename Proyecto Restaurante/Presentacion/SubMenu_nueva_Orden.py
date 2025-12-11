from Servicio.Orden_Servicio import OrdenServicio
from Servicio.OrdenDetalle_Servicio import OrdenDetalleServicio
from Servicio.Cliente_Servicio import ClienteServicio
from Servicio.Mesa_Servicio import MesaServicio
from Servicio.Empleado_Servicio import EmpleadoServicio
from Modelo.Empleado import Empleado
from Modelo.Orden import Orden
from Modelo.Cliente import Cliente
from Modelo.OrdenDetalle import OrdenDetalle
from Presentacion.Menu_Cliente import submenu_clientes
from Presentacion.SubMenu_Seleccion_Mesa import submenu_seleccionMesa
from Presentacion.SubMenu_Nuevo_Cliente import submenu_nuevo_cliente
from Utilitario.Validacion import validar, TipoValidacion

# from Principal import LISTA_PRODUCTOS, LISTA_CLIENTES, LISTA_EMPLEADOS, LISTA_MESAS

ms = MesaServicio()
os = OrdenServicio()
ds = OrdenDetalleServicio()
cs = ClienteServicio()
es = EmpleadoServicio()

def submenu_nuevaOrden():

    orden = Orden()
    while True:
        print("\n" + "-"*100)
        print("🧾  PROCESAR ORDENES")
        print("-"*100)
        print("\n1.🍽️  Seleccionar mesa")
        print("2.🧑 Seleccionar Cliente")
        print("3.👨‍💼 Seleccionar Empleado")
        print("0.🔙 Volver")

        print("\nSeleccione una opción: ")
        opcion = input("➤  ").strip()
        
        if opcion == "1":
            _orden = submenu_seleccionMesa()
            if _orden:
                orden.id_mesa = _orden.id_mesa
                orden.nro_personas = _orden.nro_personas
        
        elif opcion == "2":
            print("\n" + "-"*100)
            print("🧾 SELECCION DE CLIENTE")
            print("-"*100)
            cliente = submenu_nuevo_cliente()
            if(cliente):
                orden.id_cliente = cliente.id_cliente
                cs.obtener_clientes_bd()
                print("\n✅ Cliente agregado a la orden")
            else:
                print("\n⚠️ Error al seleccionar cliente")
                
        elif opcion == "3":
            print(f"\nLISTA DE EMPLEADO")        
            cargos = es.obtener_empleados_por_cargo()
            if not(cargos):
                print("⚠️ Lista de empleados vacia")
                continue
            mozos = cargos["mozo"]
            print("-"*100)
            print(f"📋 Mozos")
            print("="*100)
            print(f"{'ID':<17}{'Nombre':<30}{'Apellido':<25}{'DNI':>15}")
            print("="*100)
            for m in mozos:
                print(f"{m.id}{'.':<15}{m.nombre:<25}|     {m.apellido:<20}|     {m.dni:>15}") 
            
            print("\nSeleccione un empleado: ")
            id = input("➤  ").strip()
            while True:
                if validar(id, TipoValidacion.ENTERO):
                    id = int(id)
                    break
                print("\nIngrese un número válido")
            
            empleado_seleccionado = es.obtener_empleado_por_id(id)
            if empleado_seleccionado:
                orden.id_empleado = empleado_seleccionado.id
                print("\n✅ Empleado agregado a la orden")
            else:
                print("\n❌ Empleado no disponible. Intente nuevamente.")

        elif opcion == "0":
            if(os.validar_orden_completa(orden=orden)):
                print("\n¿Registrar orden? (s/n)")
                respuesta = input().strip().lower()
                if respuesta == "s":
                    orden.id_orden = os.crear_orden_bd(orden)
                    if(orden.id_orden):
                        os.agregar_orden_lista(orden)
                        ms.actualizar_estado_mesa_bd(orden.id_mesa,"Ocupado")
                        print("\nCreando orden de venta...")
                        return orden
                    else:
                        print("\n❌ Error al registrar la orden")
            else:
                print("\n❌ La orden esta imcompleta. Llene todos los datos solicitados")
                print("\nINFORMACION FALTANTE")
                if not orden.id_mesa:
                    print("\nMesa")
                if not orden.id_cliente:
                    print("\nCliente")
                if not orden.id_empleado:
                    print("\nEmpleado")
                print("\ndesea continuar llenando la orden? (s/n)")
                respuesta = input().strip().lower()
                if respuesta != "s":
                    print("\nCancelando orden...")
                    return Orden()
        
        else:
            print("\nOpción inválida.")

