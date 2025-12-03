from enum import Enum

class TipoDato(Enum):
    ENTERO = "int"
    FLOTANTE = "float"
    BOOLEANO = "bool"
    CADENA = "str"
    NULO = "none"

def validar_entrada(tipo_dato:TipoDato, cadena:str):
    cadena = cadena.strip()
    # if tipo_dato==TipoDato.ENTERO:
    #     if cadena.isdigit() or (cadena.startswith('-') and cadena[1:].isdigit()):
    #         return True
    # elif TipoDato == TipoDato.ENTERO:
    # elif TipoDato == TipoDato.ENTERO:
        