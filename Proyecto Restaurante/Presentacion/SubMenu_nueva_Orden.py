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

# from Principal import LISTA_PRODUCTOS, LISTA_CLIENTES, LISTA_EMPLEADOS, LISTA_MESAS

ms = MesaServicio()
os = OrdenServicio()
ds = OrdenDetalleServicio()
cs = ClienteServicio()
es = EmpleadoServicio()

def submenu_nuevaOrden():

    orden = Orden()
    while True:
        print("\n🧾 PROCESAR ORDENES")
        print("1.🍽️ Seleccionar mesa")
        print("2.🧑 Seleccionar Cliente")
        print("3.👩‍🍳 Seleccionar Empleado")
        print("0.🔙 Volver")

        print("Seleccione un opción: ")
        opcion = input("➤  ").strip().lower()
        if opcion == "1":
            _orden = submenu_seleccionMesa()
            if _orden:
                orden.id_mesa = _orden.id_mesa
                orden.nro_personas = _orden.nro_personas
        elif opcion == "2":
            print("nombre del cliente: ")
            nombre = input("➤  ").strip().lower()
            print("Apellido del cliente: ")
            apellido = input("➤  ").strip().lower()
            cliente = cs.validar_cliente(nombre, apellido)
            if(cliente):
                orden.id_cliente = cliente.id_cliente
                print("✅ Cliente agregado a la orden")
            else:
                print("⚠️ El cliente no esta registrado")
                print("Registre al cliente")
                id = submenu_clientes(Cliente(nombre=nombre, apellido=apellido))
                if(id):
                    orden.id_cliente = id
                    print("✅ Cliente agregado a la orden")    
        elif opcion == "3":
            print(f"\nLISTA DE EMPLEADO")
            print("="*50)
            print(f"{'ID':<10}{'Nombre':<20}{'Apellido':<20}{'DNI':<15}")
            print("-"*50)        
            cargos = es.obtener_empleados_por_cargo()
            if not(cargos):
                print("⚠️ Lista de empleados vacia")
                continue
            mozos = cargos["Mozo"]
            print(f"📋 Mozos")
            print("-" * 40)
            for m in mozos:
                print(f"• {m.id:<10}    {m.nombre:<20} | {m.apellido:<20} |  {m.dni:>10}") 
            
            try:
                id = None
                while True:
                    try:
                        id = int(input("\nSeleccione un empleado: ").strip())
                        empleado_seleccionado = es.obtener_empleado_por_id(id)
                        if empleado_seleccionado:
                            orden.id_empleado = empleado_seleccionado.id
                            print("✅ Empleado agregado a la orden")
                            break
                        else:
                            print("❌ Empleado no disponible. Intente nuevamente.")
                    except ValueError:
                        print("❌ Ingrese un número válido.")
            except ValueError:
                print("⚠️ Número inválida")

            # orden = orden_servicio.obtener_por_id(id_orden)
            # detalles = detalle_servicio.obtener_por_orden(id_orden)

            # print(f"\nORDEN #{orden.id_orden}")
            # print(f"Cliente: {orden.id_cliente}  Estado: {orden.estado}")

            # for d in detalles:
            #     print(f"- Producto {d.id_producto}: x{d.cantidad} (S/{d.precio_unitario})")
        elif opcion == "0":
            if(os.validar_orden_completa(orden=orden)):
                print("¿Registrar orden? (s/n)")
                respuesta = input().strip().lower()
                if respuesta == "s":
                    orden.id_orden = os.crear_orden_bd(orden)
                    if(orden.id_orden):
                        os.agregar_orden_lista(orden)
                        ms.actualizar_estado(orden.id_mesa,"Ocupado")
                        print("Creando orden de pedido...")
                        return orden
                    else:
                        print("❌ Error al registrar la orden")
            else:
                print("❌ La orden esta imcompleta. Llene todos los datos solicitados")
                print("INFORMACION FALTANTE")
                if orden.id_mesa is None:
                    print("Mesa")
                if not orden.id_cliente:
                    print("Cliente")
                if not orden.id_empleado:
                    print("Falta asignar un empleado")
                print("desea continuar llenando la orden? (s/n)")
                respuesta = input().strip().lower()
                if respuesta != "s":
                    print("Cancelando orden...")
                    return Orden()
        else:
            print("Opción inválida.")

