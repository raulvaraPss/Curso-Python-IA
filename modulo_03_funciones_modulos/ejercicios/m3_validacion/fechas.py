"""Validación de fechas.

Todas las fechas se reciben como texto en formato ISO: AAAA-MM-DD.
"""

from datetime import date

MAYORIA_DE_EDAD = 18


def es_fecha(texto: str) -> bool:
    """Indica si el texto es una fecha válida en formato ISO.

    Esta función se entrega hecha porque usa ``try``/``except``, que se ve
    en el módulo 6.

    >>> es_fecha("2026-02-28")
    True
    >>> es_fecha("2026-02-30")
    False
    """
    try:
        date.fromisoformat(texto.strip())
    except ValueError:
        return False
    return len(texto.strip()) == 10


def edad(fecha_nacimiento: str, hoy: date | None = None) -> int:
    """Devuelve los años cumplidos a día de ``hoy``.

    ``fecha_nacimiento`` es un texto ISO válido. Si no se indica ``hoy`` se
    usa la fecha actual. Recuerda que quien aún no ha cumplido años este año
    tiene un año menos.

    >>> edad("2000-06-15", date(2026, 6, 14))
    25
    >>> edad("2000-06-15", date(2026, 6, 15))
    26
    """
    if hoy is None:
        hoy = date.today()
    nacimiento = date.fromisoformat(fecha_nacimiento.strip())
    anios = hoy.year - nacimiento.year
    if (hoy.month, hoy.day) < (nacimiento.month, nacimiento.day):
        anios -= 1
    return anios


def es_mayor_de_edad(fecha_nacimiento: str, hoy: date | None = None) -> bool:
    """Indica si la persona ha cumplido ya ``MAYORIA_DE_EDAD`` años.

    >>> es_mayor_de_edad("2008-11-24", date(2026, 11, 23))
    False
    """
    return edad(fecha_nacimiento, hoy) >= MAYORIA_DE_EDAD
