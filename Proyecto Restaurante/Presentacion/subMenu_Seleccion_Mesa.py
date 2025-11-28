from Modelo.Orden import Orden
from Servicio.Mesa_Servicio import MesaServicio

ms = MesaServicio()

def submenu_seleccionMesa() -> Orden:
    try:
        print("Ingrese el número de personas: ")
        num_personas = input("➤  ").strip().lower()
        print(f"\n MESAS DISPONIBLES PARA {num_personas} PERSONA(S)")
        print("="*65)
        print(f"{'ID':<8}     {'Mesa':<12}     {'Capacidad':<12}       {'Estado':<15}")
        print("-"*65)        
        mesas_disponibles = ms.obtener_mesas_disponibles(int(num_personas))
        if mesas_disponibles:
            for md in mesas_disponibles:
                print(f"{md.id_mesa:<8}    mesa {md.numero:<12}    {md.capacidad:<12}      {md.estado:<15}")
                print("-"*65)
            print(f"Total: {len(mesas_disponibles)} mesa(s) disponible(s)")
            print("🔙 0. Regresar")
        else:
            print(f"\n❌ No hay mesas disponibles para {num_personas} persona(s)")
            return None
            
    except ValueError:
        print("⚠️ Cantidad inválida")
        return None
    
    try:
        mesa_seleccionada = None
        while True:
            try:
                print("Seleccione una mesa: ")
                mesa_num = input("➤  ").strip().lower()
                if mesa_num=="0":
                    return None
                mesa_seleccionada = ms.obtener_mesa_por_id(int(mesa_num))
                if mesa_seleccionada:
                    id_mesa = mesa_seleccionada.id_mesa
                    nro_personas = num_personas
                    print("✅ Mesa agregada a la orden")
                    return Orden(
                        id_mesa=id_mesa,
                        nro_personas=nro_personas
                    )
                else:
                    print("❌ Mesa no disponible. Intente nuevamente.")
            except ValueError:
                print("❌ Ingrese un número válido.")
    except ValueError:
        print("⚠️ Cantidad inválida")