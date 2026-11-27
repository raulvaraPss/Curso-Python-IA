"""Módulo 7 - Ejercicio 5: visualización con Matplotlib.

Las funciones crean la figura y la devuelven. No llaman a ``plt.show()``: quien
las usa decide si la muestra, la guarda o la prueba.
"""

from pathlib import Path

import matplotlib.pyplot as plt
import pandas as pd
from matplotlib.figure import Figure


def _barras(ejes, serie: pd.Series, titulo: str, etiqueta_y: str) -> None:
    """Dibuja unas barras en unos ejes ya creados."""
    ejes.bar(serie.index.astype(str), serie.values)
    ejes.set_title(titulo)
    ejes.set_ylabel(etiqueta_y)


def _lineas(ejes, serie: pd.Series, titulo: str, etiqueta_y: str) -> None:
    """Dibuja una línea con marcadores y rejilla en unos ejes ya creados."""
    ejes.plot(serie.index.astype(str), serie.values, marker="o")
    ejes.set_title(titulo)
    ejes.set_ylabel(etiqueta_y)
    ejes.grid(True, alpha=0.3)



def grafico_barras(serie: pd.Series, titulo: str, etiqueta_y: str = "Importe (€)") -> Figure:
    """Devuelve una figura con un gráfico de barras: una barra por elemento de la serie.

    El eje X muestra el índice de la serie. La figura lleva el título y la
    etiqueta del eje Y indicados.
    """
    figura, ejes = plt.subplots(figsize=(8, 5))
    _barras(ejes, serie, titulo, etiqueta_y)
    figura.tight_layout()
    return figura


def grafico_lineas(serie: pd.Series, titulo: str, etiqueta_y: str = "Importe (€)") -> Figure:
    """Devuelve una figura con un gráfico de líneas con un marcador en cada punto.

    Pensado para la evolución mensual: el índice de la serie va en el eje X.
    La figura lleva título, etiqueta del eje Y y rejilla.
    """
    figura, ejes = plt.subplots(figsize=(8, 5))
    _lineas(ejes, serie, titulo, etiqueta_y)
    figura.tight_layout()
    return figura


def histograma(valores, titulo: str, intervalos: int = 10) -> Figure:
    """Devuelve una figura con el histograma de los valores, con ``intervalos`` barras."""
    figura, ejes = plt.subplots(figsize=(8, 5))
    ejes.hist(list(valores), bins=intervalos, edgecolor="white")
    ejes.set_title(titulo)
    ejes.set_ylabel("Frecuencia")
    figura.tight_layout()
    return figura


def panel(por_vendedor: pd.Series, mensual: pd.Series, titulo: str) -> Figure:
    """Devuelve una figura con dos gráficos, uno al lado del otro.

    A la izquierda, barras con el importe por vendedor, con el título
    "Por vendedor". A la derecha, líneas con la evolución mensual, con el
    título "Evolución mensual". ``titulo`` es el título general de la figura.
    """
    figura, (izquierda, derecha) = plt.subplots(1, 2, figsize=(14, 5))
    _barras(izquierda, por_vendedor, "Por vendedor", "Importe (€)")
    _lineas(derecha, mensual, "Evolución mensual", "Importe (€)")
    figura.suptitle(titulo)
    figura.tight_layout()
    return figura


def guardar(figura: Figure, ruta: str | Path) -> Path:
    """Guarda la figura en ``ruta`` como PNG a 150 ppp, cierra la figura y devuelve la ruta.

    Crea la carpeta de destino si no existe.
    """
    ruta = Path(ruta)
    ruta.parent.mkdir(parents=True, exist_ok=True)
    figura.savefig(ruta, dpi=150)
    plt.close(figura)
    return ruta
