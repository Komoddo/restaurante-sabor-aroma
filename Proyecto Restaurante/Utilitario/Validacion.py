from enum import Enum
import re
from datetime import datetime

class TipoValidacion(Enum):
    ENTERO = "entero"
    PRECIO = "precio"
    DNI = "dni"
    EMAIL = "email"
    NOMBRE = "nombre"
    FECHA = "fecha"
    TELEFONO = "telefono"

def validar_entero(valor):
    try:
        return int(valor) >= 0
    except:
        return False

def validar_precio(valor):
    try:
        return float(valor) >= 0
    except:
        return False

def validar_dni(valor):
    return bool(re.fullmatch(r"\d{8}", valor))

def validar_email(valor):
    return bool(re.fullmatch(r"[^@]+@[^@]+\.[^@]+", valor))

def validar_nombre(valor):
    return bool(re.fullmatch(r"[A-Za-záéíóúÁÉÍÓÚñÑ ]{2,50}", valor))

def validar_fecha(valor):
    try:
        datetime.strptime(valor, "%Y-%m-%d")  # Formato AAAA-MM-DD
        return True
    except:
        return False

def validar_telefono(valor):
    return bool(re.fullmatch(r"9\d{8}", valor))  # Ej: 9XXXXXXXX


def validar(valor, tipo: TipoValidacion):
    valor = valor.strip()
    
    if tipo == TipoValidacion.ENTERO:
        return validar_entero(valor)
    
    if tipo == TipoValidacion.PRECIO:
        return validar_precio(valor)

    elif tipo == TipoValidacion.DNI:
        return validar_dni(valor)

    elif tipo == TipoValidacion.EMAIL:
        return validar_email(valor)

    elif tipo == TipoValidacion.NOMBRE:
        return validar_nombre(valor)

    elif tipo == TipoValidacion.FECHA:
        return validar_fecha(valor)

    elif tipo == TipoValidacion.TELEFONO:
        return validar_telefono(valor)

    return False

