"""Módulo 3 - Ejercicio 1: definición de funciones.

Basado en el ejercicio de áreas del curso anterior: tres funciones pequeñas
y una que las coordina.
"""

import math


def area_circulo(radio: float) -> float:
    """Devuelve el área de un círculo, redondeada a dos decimales.

    >>> area_circulo(1)
    3.14
    """
    return round(math.pi * radio ** 2, 2)


def area_rectangulo(base: float, altura: float) -> float:
    """Devuelve el área de un rectángulo.

    >>> area_rectangulo(3, 4)
    12
    """
    return base * altura


def area_triangulo(base: float, altura: float) -> float:
    """Devuelve el área de un triángulo.

    >>> area_triangulo(3, 4)
    6.0
    """
    return base * altura / 2


def calcular_area(figura: str, *, radio=None, base=None, altura=None):
    """Calcula el área de la figura indicada usando las funciones anteriores.

    ``figura`` puede ser "circulo", "rectangulo" o "triangulo", en mayúsculas
    o minúsculas. Las medidas se pasan solo por nombre. Devuelve ``None`` si
    la figura no se conoce o si falta alguna de las medidas que necesita.

    >>> calcular_area("circulo", radio=1)
    3.14
    >>> calcular_area("Rectangulo", base=3, altura=4)
    12
    >>> calcular_area("triangulo", base=3) is None
    True
    """

    figura = figura.lower()

    if figura == "circulo":
        if radio is None:
            return None
        return area_circulo(radio)
    elif figura in ("rectangulo", "triangulo"):
        if base is None or altura is None:
            return None
        if figura == "rectangulo":
            return area_rectangulo(base, altura)
        else:
            return area_triangulo(base, altura)
    return None


def minimo_y_maximo(*numeros):
    """Devuelve una tupla (mínimo, máximo) con los números recibidos.

    Si no se recibe ningún número devuelve ``(None, None)``.

    >>> minimo_y_maximo(4, 8, 15)
    (4, 15)
    >>> minimo_y_maximo()
    (None, None)
    """
    if not numeros:
        return(None, None)
    return (min(numeros), max(numeros)) 


def describir(funcion) -> str:
    """Devuelve "nombre: primera línea del docstring" de la función recibida.

    Si la función no tiene docstring devuelve "nombre: sin documentar".

    >>> describir(area_rectangulo)
    'area_rectangulo: Devuelve el área de un rectángulo.'
    """
    doc = funcion.__doc__
    if not doc:
        return f"{funcion.__name__}: sin documentar"
    primera_linea = doc.strip().splitlines()[0]
    return f"{funcion.__name__}: {primera_linea}"