"""Módulo 4 - Ejercicio 6: buscar, filtrar, ordenar y agrupar.

Todas las funciones trabajan con una lista de diccionarios como esta:

    empleados = [
        {"id": 1, "nombre": "Ada", "departamento": "IT", "salario": 52000},
        {"id": 2, "nombre": "Linus", "departamento": "IT", "salario": 48000},
        {"id": 3, "nombre": "Grace", "departamento": "Ventas", "salario": 45000},
    ]

Ninguna función modifica la lista que recibe.
"""


def buscar_por_id(registros: list[dict], identificador: int) -> dict | None:
    """Devuelve el registro cuyo campo "id" coincide, o ``None`` si no existe."""
    for registro in registros:
        if registro.get("id") == identificador:
            return registro
    return None


def nombres(registros: list[dict]) -> list[str]:
    """Devuelve la lista con el campo "nombre" de cada registro, en el mismo orden."""
    return [registro.get("nombre") for registro in registros]


def filtrar(registros: list[dict], campo: str, valor) -> list[dict]:
    """Devuelve los registros en los que ``campo`` vale ``valor``."""
    return [registro for registro in registros if registro.get(campo) == valor]


def ordenar_por(registros: list[dict], campo: str, descendente: bool = False) -> list[dict]:
    """Devuelve una lista nueva con los registros ordenados por ``campo``."""
    return sorted(registros, key=lambda x: x.get(campo), reverse=descendente)


def mejor_pagados(registros: list[dict], cantidad: int = 3) -> list[str]:
    """Devuelve los nombres de los ``cantidad`` empleados con mayor salario.

    De mayor a menor salario. A igual salario, por orden alfabético de nombre.
    """
    ordenados = sorted(registros, key=lambda r: (-r.get("salario", 0), r.get("nombre", "")))
    return [r["nombre"] for r in ordenados[:cantidad]]

def agrupar_por(registros: list[dict], campo: str) -> dict[str, list[dict]]:
    """Agrupa los registros por el valor de ``campo``.

    Devuelve un diccionario que asocia cada valor distinto del campo con la
    lista de registros que lo tienen, en su orden original.
    """
    grupos = {}
    for registro in registros:
        clave = registro[campo]
        if clave not in grupos:
            grupos[clave] = []
        grupos[clave].append(registro)
    return grupos


def salario_medio_por_departamento(registros: list[dict]) -> dict[str, float]:
    """Devuelve el salario medio de cada departamento, con dos decimales."""
    grupos = agrupar_por(registros, "departamento")
    return {
        departamento: round(sum(e["salario"] for e in empleados) / len(empleados), 2)
        for departamento, empleados in grupos.items()
    }


def emparejar(claves: list[str], filas: list[list]) -> list[dict]:
    """Convierte filas de valores en diccionarios usando ``claves`` como nombres de campo.

    Es lo que hace un lector de CSV con la cabecera y las filas.

    >>> emparejar(["id", "nombre"], [[1, "Ada"], [2, "Linus"]])
    [{'id': 1, 'nombre': 'Ada'}, {'id': 2, 'nombre': 'Linus'}]
    """
    return [dict(zip(claves, fila)) for fila in filas]
