"""Módulo 7 - Ejercicio 2: pandas, cargar, inspeccionar y seleccionar.

Las ventas tienen las columnas fecha, vendedor, region, producto, categoria,
unidades y precio. Ninguna función modifica el DataFrame que recibe.
"""

from pathlib import Path

import pandas as pd


def crear_dataframe(ventas: list[dict]) -> pd.DataFrame:
    """Crea un DataFrame a partir de una lista de diccionarios como la del Módulo 4.

    La columna ``fecha`` llega como texto ISO y debe quedar como fecha.

    >>> df = crear_dataframe([{"fecha": "2026-10-01", "vendedor": "Ada", "unidades": 2, "precio": 950.0}])
    >>> df.loc[0, "fecha"].year
    2026
    """
    df = pd.DataFrame(ventas)
    df["fecha"] = pd.to_datetime(df["fecha"])
    return df


def cargar_ventas(ruta: str | Path) -> pd.DataFrame:
    """Lee un CSV de ventas en UTF-8 y devuelve el DataFrame con ``fecha`` como fecha."""
    return pd.read_csv(ruta, encoding="utf-8", parse_dates=["fecha"])


def con_importe(df: pd.DataFrame) -> pd.DataFrame:
    """Devuelve una copia con la columna ``importe``: unidades por precio.

    El DataFrame original no cambia.
    """
    return df.assign(importe=df["unidades"] * df["precio"])


def resumen(df: pd.DataFrame) -> dict:
    """Devuelve un diccionario con los datos básicos del DataFrame.

    Claves: "filas" (int), "columnas" (lista de nombres), "desde" y "hasta"
    (primera y última fecha, como texto "AAAA-MM-DD") y "unidades" (int, total).
    """
    return {
        "filas": len(df),
        "columnas": list(df.columns),
        "desde": df["fecha"].min().strftime("%Y-%m-%d"),
        "hasta": df["fecha"].max().strftime("%Y-%m-%d"),
        "unidades": int(df["unidades"].sum()),
    }


def ventas_de(df: pd.DataFrame, vendedor: str) -> pd.DataFrame:
    """Devuelve las filas de un vendedor."""
    return df[df["vendedor"] == vendedor]


def filtrar(df: pd.DataFrame, *, region: str | None = None, categorias: list[str] | None = None,
            unidades_minimas: int = 0) -> pd.DataFrame:
    """Devuelve las filas que cumplen todos los criterios indicados.

    - ``region``: si no es ``None``, solo esa región.
    - ``categorias``: si no es ``None``, solo las categorías de la lista.
    - ``unidades_minimas``: solo ventas con al menos esas unidades.
    """
    mascara = df["unidades"] >= unidades_minimas
    if region is not None:
        mascara &= df["region"] == region
    if categorias is not None:
        mascara &= df["categoria"].isin(categorias)
    return df[mascara]


def mayores_ventas(df: pd.DataFrame, n: int = 3) -> pd.DataFrame:
    """Devuelve las ``n`` ventas de mayor importe, de mayor a menor.

    El resultado tiene solo las columnas fecha, vendedor, producto e importe.
    """
    return con_importe(df).nlargest(n, "importe")[["fecha", "vendedor", "producto", "importe"]]


def productos(df: pd.DataFrame) -> list[str]:
    """Devuelve la lista de productos distintos, en orden alfabético."""
    return sorted(df["producto"].unique().tolist())


def precio_medio_por_categoria(df: pd.DataFrame) -> dict[str, float]:
    """Devuelve el precio unitario medio de cada categoría, redondeado a dos decimales."""
    return df.groupby("categoria")["precio"].mean().round(2).to_dict()
