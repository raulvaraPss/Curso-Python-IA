"""Módulo 3 - Ejercicio 3: ámbito, cierres y funciones como argumento."""


def crear_contador(inicio: int = 0):
    """Devuelve una función que cuenta: cada llamada devuelve el siguiente número.

    El primer valor devuelto es ``inicio + 1``. Cada contador tiene su propia
    cuenta. No se pueden usar variables globales.

    >>> contador = crear_contador()
    >>> contador(), contador(), contador()
    (1, 2, 3)
    """
    cuenta = inicio

    def contador():
        nonlocal cuenta
        cuenta += 1
        return cuenta

    return contador


def multiplicador(factor: float):
    """Devuelve una función que multiplica su argumento por ``factor``.

    >>> triple = multiplicador(3)
    >>> triple(10)
    30
    """
    # También vale: return lambda numero: numero * factor

    def multiplicar(numero):
        return numero * factor
    return multiplicar


def aplicar(funcion, valores: list) -> list:
    """Devuelve una lista nueva con el resultado de aplicar ``funcion`` a cada valor.

    No modifica la lista original.

    >>> aplicar(abs, [-1, 2, -3])
    [1, 2, 3]
    """
    # En el módulo 4 veremos la forma idiomática: [funcion(valor) for valor in valores]

    resultado = []
    for valor in valores:
        resultado.append(funcion(valor))
    return resultado


def componer(f, g):
    """Devuelve una función que calcula ``f(g(x))``.

    >>> incrementar_y_duplicar = componer(lambda x: x * 2, lambda x: x + 1)
    >>> incrementar_y_duplicar(5)
    12
    """
    def compuesta(x):
        return f(g(x))
    return compuesta

def ordenar_por_longitud(palabras: list[str]) -> list[str]:
    """Devuelve una lista nueva con las palabras ordenadas de más corta a más larga.

    Las palabras de igual longitud conservan su orden original.

    >>> ordenar_por_longitud(["manzana", "uva", "kiwi"])
    ['uva', 'kiwi', 'manzana']
    """
    return sorted(palabras, key=len)


def mas_caro(productos: list[tuple]) -> tuple | None:
    """Devuelve el producto de mayor precio de una lista de tuplas (nombre, precio).

    Con la lista vacía devuelve ``None``.

    >>> mas_caro([("teclado", 45.0), ("monitor", 189.0), ("raton", 19.9)])
    ('monitor', 189.0)
    """
    if not productos:
        return None
    return max(productos, key=lambda producto: producto[1])