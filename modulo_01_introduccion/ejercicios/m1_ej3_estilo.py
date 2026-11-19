"""Módulo 1 - Ejercicio 3: código con estilo.

La función de abajo funciona, pero ignora PEP 8. Reescríbela siguiendo las
indicaciones del enunciado sin cambiar su comportamiento.
"""

def PrecioFinal(P, i = 21, d = 0):
    x = P - P * d / 100
    y = x + x * i / 100
    return round(y, 2)
