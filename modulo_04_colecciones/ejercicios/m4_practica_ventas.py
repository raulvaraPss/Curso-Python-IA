"""Módulo 4 - Práctica 4: análisis de ventas en memoria.

Cada venta es un diccionario con las claves "fecha", "vendedor", "region",
"producto", "categoria", "unidades" y "precio". Ninguna función modifica la
lista de ventas que recibe.
"""

from m4_datos_ventas import VENTAS

ANCHO = 44


def importe(venta: dict) -> float:
    """Devuelve el importe de una venta: unidades por precio, con dos decimales.

    >>> importe({"unidades": 3, "precio": 19.9})
    59.7
    """
    return round(venta["unidades"] * venta["precio"], 2)


def total_ventas(ventas: list[dict]) -> float:
    """Devuelve la suma de los importes de todas las ventas, con dos decimales."""
    return round(sum(importe(venta) for venta in ventas), 2)


def filtrar_ventas(ventas: list[dict], *, region: str | None = None,
                   categoria: str | None = None, vendedor: str | None = None,
                   desde: str | None = None, hasta: str | None = None) -> list[dict]:
    """Devuelve las ventas que cumplen todos los criterios indicados.

    Un criterio que vale ``None`` no se aplica. ``desde`` y ``hasta`` son
    fechas ISO y las dos están incluidas en el intervalo.
    """
    iguales = {
        "region": region,
        "categoria": categoria,
        "vendedor": vendedor
    }
    return [
        venta for venta in ventas
        if all(venta[campo] == valor for campo, valor in iguales.items() if valor is not None)
        and (desde is None or venta["fecha"] >= desde)
        and (hasta is None or venta["fecha"] <= hasta)
    ]


def _acumular(ventas: list[dict], campo: str, medida) -> dict:
    """Suma ``medida(venta)`` agrupando las ventas por ``campo``."""
    totales = {}
    for venta in ventas:
        clave = venta[campo]
        totales[clave] = totales.get(clave, 0) + medida(venta)
    return totales


def importe_por(ventas: list[dict], campo: str) -> dict[str, float]:
    """Agrupa las ventas por ``campo`` y devuelve el importe total de cada grupo.

    Los importes van redondeados a dos decimales.

    >>> importe_por([{"region": "Norte", "unidades": 2, "precio": 10.0}], "region")
    {'Norte': 20.0}
    """
    return {clave: round(total, 2) for clave, total in _acumular(ventas, campo, importe).items()}


def unidades_por_producto(ventas: list[dict]) -> dict[str, int]:
    """Devuelve las unidades totales vendidas de cada producto."""
    return _acumular(ventas, "producto", lambda venta: venta["unidades"])


def ranking(ventas: list[dict], campo: str, cantidad: int = 3) -> list[tuple[str, float]]:
    """Devuelve los ``cantidad`` grupos con mayor importe, como tuplas (clave, importe).

    De mayor a menor importe. A igual importe, por orden alfabético de la clave.
    """
    totales = importe_por(ventas, campo)
    ordenados = sorted(totales.items(), key=lambda par: (-par[1], par[0]))
    return ordenados[:cantidad]


def producto_mas_vendido(ventas: list[dict]) -> str | None:
    """Devuelve el producto con más unidades vendidas, o ``None`` si no hay ventas.

    En caso de empate, el primero por orden alfabético.
    """
    unidades = unidades_por_producto(ventas)
    if not unidades:
        return None
    return min(unidades, key=lambda producto: (-unidades[producto], producto))


def ticket_medio(ventas: list[dict]) -> float:
    """Devuelve el importe medio por venta, con dos decimales. Sin ventas, 0.0."""
    if not ventas:
        return 0.0
    return round(total_ventas(ventas) / len(ventas), 2)


def _linea_resumen(etiqueta: str, valor: str) -> str:
    return f"{etiqueta:<30}{valor:>14}"


def _linea_desglose(clave: str, valor: float) -> str:
    return f"  {clave:<28}{valor:>14,.2f}"

def generar_informe(ventas: list[dict]) -> str:
    """Devuelve el informe de ventas como texto, con el formato del enunciado."""
    doble = "=" * ANCHO
    simple = "-" * ANCHO
    lineas = [
        doble,
        "INFORME DE VENTAS".center(ANCHO),
        doble,
        _linea_resumen("Ventas registradas", str(len(ventas))),
        _linea_resumen("Importe total", f"{total_ventas(ventas):,.2f}"),
        _linea_resumen("Ticket medio", f"{ticket_medio(ventas):,.2f}"),
        _linea_resumen("Producto más vendido", producto_mas_vendido(ventas) or "-")]
    desgloses = [("Por región", "region"), ("Por categoría", "categoria"), ("Por vendedor", "vendedor")]
    for titulo, campo in desgloses:
        lineas.append(simple)
        lineas.append(titulo)
        for clave, total in ranking(ventas, campo, cantidad=len(ventas)):
            lineas.append(_linea_desglose(clave, total))
    lineas.append(doble)
    return "\n".join(lineas)


def main():
    print(generar_informe(VENTAS))
    print()
    print("Solo la región Sur, segunda quincena:")
    print(generar_informe(filtrar_ventas(VENTAS, region="Sur", desde="2026-10-16")))


if __name__ == "__main__":
    main()
