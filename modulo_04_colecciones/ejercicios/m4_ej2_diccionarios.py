"""Módulo 4 - Ejercicio 2: tuplas y diccionarios.

Parte de los ejercicios de estudiantes y carrito del curso anterior.
"""


def punto_medio(a: tuple[float, float], b: tuple[float, float]) -> tuple[float, float]:
    """Devuelve el punto medio entre dos puntos (x, y).

    >>> punto_medio((0, 0), (4, 2))
    (2.0, 1.0)
    """
    return ((a[0] + b[0]) / 2, (a[1] + b[1]) / 2)


def contar_palabras(texto: str) -> dict[str, int]:
    """Devuelve cuántas veces aparece cada palabra, en minúsculas.

    >>> contar_palabras("El gato y el perro")
    {'el': 2, 'gato': 1, 'y': 1, 'perro': 1}
    """
    conteo = {}
    for palabra in texto.lower().split():
        conteo[palabra] = conteo.get(palabra, 0) + 1
    return conteo


def invertir(diccionario: dict) -> dict:
    """Devuelve un diccionario nuevo con las claves y los valores intercambiados.

    >>> invertir({"a": 1, "b": 2})
    {1: 'a', 2: 'b'}
    """
    invertido = {}
    for clave, valor in diccionario.items():
        invertido[valor] = clave
    return invertido


def notas_medias(estudiantes: dict[str, list[float]]) -> dict[str, float]:
    """Devuelve la nota media de cada estudiante, redondeada a dos decimales.

    ``estudiantes`` asocia cada nombre con su lista de notas. Un estudiante
    sin notas tiene media 0.0.

    >>> notas_medias({"Ada": [9, 10], "Linus": [5, 6, 8]})
    {'Ada': 9.5, 'Linus': 6.33}
    """
    medias = {}
    for nombre, notas in estudiantes.items():
        if notas:
            media = round(sum(notas) / len(notas), 2)
        else:
            media = 0.0
        medias[nombre] = media
    return medias


def mejor_estudiante(estudiantes: dict[str, list[float]]) -> str | None:
    """Devuelve el nombre del estudiante con la media más alta.

    Con el diccionario vacío devuelve ``None``. En caso de empate, el que
    aparece primero.

    >>> mejor_estudiante({"Ada": [9, 10], "Linus": [5, 6, 8]})
    'Ada'
    """
    if not estudiantes:
        return None
    medias = notas_medias(estudiantes)
    return max(medias, key=medias.get)


def total_carrito(carrito: list[tuple[str, int, float]]) -> float:
    """Devuelve el importe total de un carrito, redondeado a dos decimales.

    Cada elemento del carrito es una tupla (producto, unidades, precio).

    >>> total_carrito([("teclado", 2, 45.0), ("raton", 1, 19.9)])
    109.9
    """
    total = 0 
    for producto, unidades, precio in carrito:
        total += unidades * precio
    return round(total, 2)


def fusionar_inventarios(a: dict[str, int], b: dict[str, int]) -> dict[str, int]:
    """Devuelve un inventario nuevo con las unidades de ``a`` y ``b`` sumadas.

    No modifica ninguno de los dos diccionarios.

    >>> fusionar_inventarios({"teclado": 5, "raton": 2}, {"raton": 3, "monitor": 1})
    {'teclado': 5, 'raton': 5, 'monitor': 1}
    """
    resultado = a.copy()
    for producto, unidades in b.items():
        resultado[producto] = resultado.get(producto, 0) + unidades
    return resultado


def valor_anidado(datos: dict, ruta: str, por_defecto=None):
    """Devuelve el valor situado en ``ruta`` dentro de diccionarios anidados.

    ``ruta`` son claves separadas por puntos. Si alguna clave no existe, o
    se intenta entrar en algo que no es un diccionario, devuelve
    ``por_defecto``.

    >>> pedido = {"cliente": {"direccion": {"ciudad": "Madrid"}}}
    >>> valor_anidado(pedido, "cliente.direccion.ciudad")
    'Madrid'
    >>> valor_anidado(pedido, "cliente.telefono", "sin datos")
    'sin datos'
    """
    actual = datos
    for clave in ruta.split("."):
        if not isinstance(actual, dict) or clave not in actual:
            return por_defecto
        actual = actual[clave]
    return actual
