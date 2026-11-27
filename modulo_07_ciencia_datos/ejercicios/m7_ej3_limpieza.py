"""Módulo 7 - Ejercicio 3: limpieza de datos.

Se trabaja con ``datos/ventas_sucias.csv``, leído con todas las columnas como
texto. Ninguna función modifica el DataFrame que recibe.
"""

from pathlib import Path

import pandas as pd

COLUMNAS_TEXTO = ["vendedor", "region", "producto", "categoria"]


def cargar_en_bruto(ruta: str | Path) -> pd.DataFrame:
    """Lee el CSV con todas las columnas como texto, sin que pandas interprete nada.

    Las celdas vacías quedan como valores ausentes.
    """
    return pd.read_csv(ruta, dtype=str, encoding="utf-8")


def contar_ausentes(df: pd.DataFrame) -> dict[str, int]:
    """Devuelve cuántos valores ausentes tiene cada columna. Solo las que tienen alguno."""
    ausentes = df.isna().sum()
    return {columna: int(n) for columna, n in ausentes[ausentes > 0].items()}


def normalizar_texto(df: pd.DataFrame, columnas: list[str] = COLUMNAS_TEXTO) -> pd.DataFrame:
    """Devuelve una copia con las columnas indicadas sin espacios sobrantes y con la inicial en mayúscula.

    "  ada " y "ADA" pasan a ser "Ada". Los valores ausentes siguen ausentes.
    """
    resultado = df.copy()
    for columna in columnas:
        resultado[columna] = resultado[columna].str.strip().str.capitalize()
    return resultado



def convertir_tipos(df: pd.DataFrame) -> pd.DataFrame:
    """Devuelve una copia con ``fecha``, ``unidades`` y ``precio`` convertidos.

    - ``fecha``: fecha a partir del formato "AAAA-MM-DD". Lo que no lo cumple queda ausente.
    - ``unidades``: número. Lo que no es un número queda ausente.
    - ``precio``: número. Admite coma decimal: "29,5" es 29.5.
    """
    resultado = df.copy()
    resultado["fecha"] = pd.to_datetime(resultado["fecha"], format="%Y-%m-%d", errors="coerce")
    resultado["unidades"] = pd.to_numeric(resultado["unidades"], errors="coerce")
    resultado["precio"] = pd.to_numeric(resultado["precio"].str.replace(",", ".", regex=False), errors="coerce")
    return resultado


def quitar_duplicados(df: pd.DataFrame) -> pd.DataFrame:
    """Devuelve el DataFrame sin filas repetidas. Se conserva la primera de cada grupo."""
    return df.drop_duplicates(keep="first")


def rellenar_region(df: pd.DataFrame, valor: str = "Sin región") -> pd.DataFrame:
    """Devuelve una copia en la que las regiones ausentes se sustituyen por ``valor``."""
    return df.assign(region=df["region"].fillna(valor))


def limpiar(df: pd.DataFrame) -> pd.DataFrame:
    """Aplica toda la limpieza y devuelve un DataFrame listo para analizar.

    Pasos, en este orden:

    1. Normalizar el texto.
    2. Quitar duplicados.
    3. Convertir los tipos.
    4. Rellenar las regiones ausentes con "Sin región".
    5. Descartar las filas sin fecha, sin vendedor, sin unidades o sin precio,
       y las que tienen unidades o precio menores o iguales que cero.
    6. Dejar ``unidades`` como entero y renumerar el índice desde 0.
    """
    resultado = normalizar_texto(df)
    resultado = quitar_duplicados(resultado)
    resultado = convertir_tipos(resultado)
    resultado = rellenar_region(resultado)
    resultado = resultado.dropna(subset=["fecha", "vendedor", "unidades", "precio"])
    resultado = resultado[(resultado["unidades"] > 0) & (resultado["precio"] > 0)]
    resultado = resultado.astype({"unidades": int})
    return resultado.reset_index(drop=True)
