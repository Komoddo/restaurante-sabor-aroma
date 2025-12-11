from Modelo.Orden import Orden
from Servicio.Mesa_Servicio import MesaServicio
from Utilitario.Validacion import validar, TipoValidacion

ms = MesaServicio()

def submenu_seleccionMesa() -> Orden:
    try:
        print("\n" + "-"*100)
        print("SELECCION DE MESA 🍽️")
        print("-"*100)
        while True:
            print("\nIngrese el número de personas: ")
            num_personas = input("➤  ").strip()
            if num_personas!="0":
                if validar(num_personas, TipoValidacion.ENTERO):
                    num_personas = int(num_personas)
                    break
            print("❗ Entrada inválida")
            
        print("\n" + "-"*100)
        print(f"MESAS DISPONIBLES PARA {num_personas} PERSONA(S)")
        print("="*100)
        print(f"{'ID':<28}{'Mesa':<27}{'Capacidad':<25}{'Estado':>18}")
        print("="*100)        
        mesas_disponibles = ms.obtener_mesas_disponibles(num_personas)
        if mesas_disponibles:
            for md in mesas_disponibles:
                print(f"{'0' if md.id_mesa<10 else ''}{md.id_mesa}{'.':<12}|            mesa {md.numero:<15}|           {md.capacidad:<20}|         {md.estado:<25}")
            print(f"\nTotal: {len(mesas_disponibles)} mesa(s) disponible(s)")
            print("0. Salir")
        else:
            print(f"\n❌ No hay mesas disponibles para {num_personas} persona(s)")
            return None

        while True:
            print("\nSeleccione una mesa: ")
            mesa_num = input("➤  ").strip()
            if mesa_num=="0": 
                print("\n❌ Cancelando...")
                return None
            if validar(mesa_num, TipoValidacion.ENTERO):
                mesa_num = int(mesa_num)
                if mesa_num in (m.id_mesa for m in mesas_disponibles):
                    break
            print("\n❗ Entrada inválida")
            
        mesa_seleccionada = ms.obtener_mesa_por_id(mesa_num)
        if mesa_seleccionada:
            print("\n✅ Mesa agregada a la orden")
            return Orden(
                id_mesa = mesa_seleccionada.id_mesa,
                nro_personas = num_personas
            )
        else:
            print("\n❌ Mesa no disponible. Intente nuevamente.")
    except ValueError:
        print("\n⚠️ Cantidad inválida")