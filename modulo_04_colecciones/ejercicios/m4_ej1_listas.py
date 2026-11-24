"""Módulo 4 - Ejercicio 1: listas."""


def extremos(lista: list) -> tuple:
    """Devuelve una tupla con el primer y el último elemento de la lista.

    Con la lista vacía devuelve ``(None, None)``.

    >>> extremos([4, 8, 15])
    (4, 15)
    >>> extremos([7])
    (7, 7)
    """
    if not lista:
        return (None, None)
    return (lista[0], lista[-1])


def rotar(lista: list, posiciones: int = 1) -> list:
    """Devuelve una lista nueva con los elementos desplazados a la izquierda.

    Los que salen por el principio entran por el final. ``posiciones`` puede
    ser mayor que la longitud de la lista. No modifica la lista original.

    >>> rotar([1, 2, 3, 4, 5], 2)
    [3, 4, 5, 1, 2]
    >>> rotar([1, 2, 3], 4)
    [2, 3, 1]
    """
    if not lista:
        return []
    n = posiciones % len(lista)
    return lista[n:] + lista[:n]


def segundo_mayor(numeros: list[float]) -> float | None:
    """Devuelve el segundo valor más alto, sin contar repetidos.

    Si no hay al menos dos valores distintos devuelve ``None``.

    >>> segundo_mayor([4, 42, 15, 42])
    15
    >>> segundo_mayor([5, 5]) is None
    True
    """
    distintos = sorted(set(numeros), reverse=True)
    if len(distintos) < 2:
        return None 
    return distintos[1]


def trocear(lista: list, tamano: int) -> list[list]:
    """Divide la lista en trozos de ``tamano`` elementos.

    El último trozo puede ser más corto.

    >>> trocear([1, 2, 3, 4, 5], 2)
    [[1, 2], [3, 4], [5]]
    """
    trozos = []
    for inicio in range(0, len(lista), tamano):
        trozos.append(lista[inicio:inicio + tamano])
    return trozos


def sin_duplicados(lista: list) -> list:
    """Devuelve una lista nueva sin repetidos, conservando el orden de aparición.

    >>> sin_duplicados([3, 1, 3, 2, 1])
    [3, 1, 2]
    """
    vistos = set()
    resultado = []
    for elemento in lista:
        if elemento not in vistos:
            vistos.add(elemento)
            resultado.append(elemento)
    return resultado


def insertar_ordenado(ordenada: list[float], valor: float) -> list[float]:
    """Devuelve una lista nueva con ``valor`` insertado en su sitio.

    ``ordenada`` está en orden ascendente y no se modifica.

    >>> insertar_ordenado([1, 3, 5], 4)
    [1, 3, 4, 5]
    """
    resultado = ordenada.copy()
    for i, elemento in enumerate(resultado):
        if valor < elemento:
            resultado.insert(i, valor)
            return resultado
    resultado.append(valor)
    return resultado


def crear_tablero(filas: int, columnas: int, valor=0) -> list[list]:
    """Devuelve una matriz de ``filas`` x ``columnas`` rellena con ``valor``.

    Cada fila tiene que ser una lista independiente de las demás.

    >>> crear_tablero(2, 3)
    [[0, 0, 0], [0, 0, 0]]
    """
    tablero = []
    for _ in range(filas):
        tablero.append([valor] * columnas)
    return tablero
