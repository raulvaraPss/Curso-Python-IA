"""Módulo 7 - Ejercicio 1: NumPy.

Todas las funciones se resuelven con operaciones sobre el array completo.
Si escribes un bucle ``for``, hay una forma mejor.
"""

import numpy as np


def crear_rango(inicio: float, fin: float, paso: float) -> np.ndarray:
    """Devuelve un array con los valores desde ``inicio`` hasta ``fin`` sin incluirlo.

    >>> crear_rango(0, 1, 0.25)
    array([0.  , 0.25, 0.5 , 0.75])
    """
    return np.arange(inicio, fin, paso)


def estadisticas(valores) -> dict[str, float]:
    """Devuelve la media, la mediana, la desviación típica, el mínimo y el máximo.

    Las claves son "media", "mediana", "desviacion", "minimo" y "maximo", y
    los valores son ``float`` de Python. La desviación es la poblacional, la
    que calcula NumPy por defecto.

    >>> estadisticas([2, 4, 4, 4, 5, 5, 7, 9])
    {'media': 5.0, 'mediana': 4.5, 'desviacion': 2.0, 'minimo': 2.0, 'maximo': 9.0}
    """
    arr = np.asarray(valores, dtype=float)
    return {
        "media": float(arr.mean()),
        "mediana": float(np.median(arr)),
        "desviacion": float(arr.std()),
        "minimo": float(arr.min()),
        "maximo": float(arr.max()),
    }


def aplicar_iva(precios, tipo: float = 0.21) -> np.ndarray:
    """Devuelve los precios con el IVA aplicado, redondeados a dos decimales.

    >>> aplicar_iva([100, 19.9])
    array([121.  ,  24.08])
    """
    return np.round(np.asarray(precios, dtype=float) * (1 + tipo), 2)


def normalizar(valores) -> np.ndarray:
    """Escala los valores al intervalo [0, 1]: el mínimo pasa a 0 y el máximo a 1.

    Si todos los valores son iguales, devuelve un array de ceros.

    >>> normalizar([10, 20, 30])
    array([0. , 0.5, 1. ])
    """
    arr = np.asarray(valores, dtype=float)
    rango = arr.max() - arr.min()
    if rango == 0:
        return np.zeros_like(arr)
    return (arr - arr.min()) / rango


def mayores_que_la_media(valores) -> np.ndarray:
    """Devuelve solo los valores estrictamente mayores que la media, en su orden.

    >>> mayores_que_la_media([1, 5, 2, 8])
    array([5, 8])
    """
    arr = np.asarray(valores)
    return arr[arr > arr.mean()]


def reemplazar_negativos(valores, sustituto: float = 0) -> np.ndarray:
    """Devuelve una copia en la que cada valor negativo se cambia por ``sustituto``.

    El array original no se modifica.

    >>> reemplazar_negativos([3, -1, 4, -5])
    array([3, 0, 4, 0])
    """
    arr = np.asarray(valores)
    return np.where(arr < 0, sustituto, arr)


def totales(matriz) -> tuple[np.ndarray, np.ndarray]:
    """Devuelve la suma de cada fila y la suma de cada columna de una matriz.

    >>> filas, columnas = totales([[1, 2, 3], [4, 5, 6]])
    >>> filas
    array([ 6, 15])
    >>> columnas
    array([5, 7, 9])
    """
    arr = np.asarray(matriz)
    return arr.sum(axis=1), arr.sum(axis=0)


def importes(unidades, precios) -> np.ndarray:
    """Devuelve el importe de cada venta: unidades por precio, elemento a elemento.

    Lanza ``ValueError`` si las dos secuencias no tienen la misma longitud.

    >>> importes([2, 10], [950.0, 19.9])
    array([1900.,  199.])
    """
    u = np.asarray(unidades)
    p = np.asarray(precios)
    if u.shape != p.shape:
        raise ValueError("unidades y precios deben tener la misma longitud")
    return u * p


def media_movil(valores, ventana: int) -> np.ndarray:
    """Devuelve la media móvil: la media de cada grupo de ``ventana`` valores consecutivos.

    El resultado tiene ``len(valores) - ventana + 1`` elementos.

    >>> media_movil([1, 2, 3, 4, 5], 3)
    array([2., 3., 4.])
    """
    arr = np.asarray(valores, dtype=float)
    pesos = np.ones(ventana) / ventana
    return np.convolve(arr, pesos, mode="valid")
