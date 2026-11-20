"""Módulo 2 - Ejercicio 2: operadores."""


def es_bisiesto(anio: int) -> bool:
    """Indica si un año es bisiesto.

    Es bisiesto si es divisible entre 4, salvo los divisibles entre 100 que
    no lo sean también entre 400.

    >>> es_bisiesto(2024), es_bisiesto(1900), es_bisiesto(2000)
    (True, False, True)
    """
    return anio % 4 == 0 and (anio % 100 != 0 or anio % 400 == 0)


def segundos_a_hms(segundos: int) -> str:
    """Convierte segundos al formato HH:MM:SS.

    >>> segundos_a_hms(3725)
    '01:02:05'
    """
    horas, resto = divmod(segundos, 3600)
    minutos, segs = divmod(resto, 60)
    return f"{horas:02d}:{minutos:02d}:{segs:02d}"


def nombre_o_anonimo(nombre: str | None) -> str:
    """Devuelve el nombre sin espacios sobrantes o "Anónimo" si no hay.

    >>> nombre_o_anonimo("  Ada "), nombre_o_anonimo(""), nombre_o_anonimo(None)
    ('Ada', 'Anónimo', 'Anónimo')
    """
    return (nombre or "").strip() or "Anónimo"


def en_rango(valor: float, minimo: float, maximo: float) -> bool:
    """Indica si ``valor`` está entre ``minimo`` y ``maximo``, ambos incluidos.

    >>> en_rango(5, 1, 10), en_rango(11, 1, 10)
    (True, False)
    """
    return minimo <= valor <= maximo


def es_par(numero: int) -> bool:
    """Indica si un entero es par, también si es negativo.

    >>> es_par(-4), es_par(7)
    (True, False)
    """
    return numero % 2 == 0


def reparto(total: int, personas: int) -> tuple[int, int]:
    """Reparte ``total`` unidades entre ``personas``.

    Devuelve cuántas tocan a cada una y cuántas sobran.

    >>> reparto(17, 5)
    (3, 2)
    """
    return divmod(total, personas)
