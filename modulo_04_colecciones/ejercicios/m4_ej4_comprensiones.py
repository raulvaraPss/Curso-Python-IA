"""Módulo 4 - Ejercicio 4: comprensiones.

Cada función se resuelve con una sola línea ``return`` que contiene una
comprensión o una expresión generadora.
"""


def cuadrados_de_pares(limite: int) -> list[int]:
    """Devuelve los cuadrados de los números pares entre 0 y ``limite``, incluido.

    >>> cuadrados_de_pares(6)
    [0, 4, 16, 36]
    """
    return [x**2 for x in range(limite + 1) if x % 2 == 0]


def longitudes(palabras: list[str]) -> dict[str, int]:
    """Devuelve un diccionario que asocia cada palabra con su longitud.

    >>> longitudes(["uva", "kiwi"])
    {'uva': 3, 'kiwi': 4}
    """
    return {palabra: len(palabra) for palabra in palabras}


def iniciales(nombres: list[str]) -> set[str]:
    """Devuelve el conjunto de iniciales, en mayúscula, de los nombres no vacíos.

    >>> sorted(iniciales(["ada", "Alan", "grace", ""]))
    ['A', 'G']
    """
    return {nombre[0].upper() for nombre in nombres if nombre}


def limpiar(textos: list[str]) -> list[str]:
    """Devuelve los textos sin espacios alrededor y en minúsculas.

    Descarta los que quedan vacíos.

    >>> limpiar(["  Ada ", "", "LINUS", "   "])
    ['ada', 'linus']
    """
    return [texto.strip().lower() for texto in textos if texto.strip()]


def filtrar_por_precio(precios: dict[str, float], maximo: float) -> dict[str, float]:
    """Devuelve los productos cuyo precio es menor o igual que ``maximo``.

    >>> filtrar_por_precio({"teclado": 45.0, "raton": 19.9, "monitor": 189.0}, 50)
    {'teclado': 45.0, 'raton': 19.9}
    """
    return {producto: precio for producto, precio in precios.items() if precio <= maximo}


def aplanar(matriz: list[list]) -> list:
    """Devuelve una lista con todos los elementos de una lista de listas.

    >>> aplanar([[1, 2], [3], [], [4, 5]])
    [1, 2, 3, 4, 5]
    """
    return [elemento for fila in matriz for elemento in fila]


def trasponer(matriz: list[list]) -> list[list]:
    """Devuelve la matriz traspuesta: las filas pasan a ser columnas.

    Todas las filas tienen la misma longitud. Con la matriz vacía devuelve
    una lista vacía.

    >>> trasponer([[1, 2, 3], [4, 5, 6]])
    [[1, 4], [2, 5], [3, 6]]
    """
    return [list(columna) for columna in zip(*matriz)]


def suma_de_importes(lineas: list[dict]) -> float:
    """Devuelve la suma de ``unidades * precio`` de todas las líneas, con dos decimales.

    >>> suma_de_importes([{"unidades": 2, "precio": 45.0}, {"unidades": 1, "precio": 19.9}])
    109.9
    """
    return round(sum(linea["unidades"] * linea["precio"] for linea in lineas), 2)
