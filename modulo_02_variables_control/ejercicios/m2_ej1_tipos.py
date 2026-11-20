"""Módulo 2 - Ejercicio 1: tipos de datos y conversiones."""

def nombre_del_tipo(valor) -> str:
    """Devuelve el nombre del tipo de ``valor`` en español.

    "entero", "decimal", "booleano", "texto", "nulo" u "otro".

    >>> nombre_del_tipo(3.5)
    'decimal'
    """
    if valor is None:
        return "nulo"
    if isinstance(valor, bool):      # va ANTES que int, porque True también es int
        return "booleano"
    if isinstance(valor, int):
        return "entero"
    if isinstance(valor, float):
        return "decimal"
    if isinstance(valor, str):
        return "texto"
    return "otro"


def a_entero(texto: str) -> int | None:
    """Convierte ``texto`` a entero. Devuelve None si no es un entero válido.

    Admite espacios alrededor y un signo + o - delante.

    >>> a_entero("  -42 ")
    -42
    >>> a_entero("3.5") is None
    True
    """
    limpio = texto.strip()
    if limpio[:1] in ("+", "-"):
        cifras = limpio[1:]
    else:
        cifras = limpio
    if cifras.isdecimal():
        return int(limpio)
    return None


def casi_iguales(a: float, b: float, tolerancia: float = 1e-9) -> bool:
    """Indica si dos decimales son iguales dentro de una tolerancia absoluta.

    >>> casi_iguales(0.1 + 0.2, 0.3)
    True
    """
    return abs(a - b) <= tolerancia


def media(a: float, b: float, c: float) -> float:
    """Devuelve la media de tres números redondeada a dos decimales.

    >>> media(5, 6, 8)
    6.33
    """
    return round((a + b + c) / 3, 2)


def partir_euros(importe: float) -> tuple[int, int]:
    """Separa un importe en euros y céntimos enteros.

    >>> partir_euros(12.34)
    (12, 34)
    """
    centimos_totales = round(importe * 100)
    euros, centimos = divmod(centimos_totales, 100)
    return euros, centimos

