"""Módulo 6 - Ejercicio 1: lectura y escritura de ficheros de texto.

Todas las rutas pueden llegar como ``str`` o como ``Path``. Todos los
ficheros se abren con ``with`` y con ``encoding="utf-8"``.
"""

from pathlib import Path


def contar_lineas(ruta) -> int:
    """Devuelve el número de líneas del fichero.

    Tiene que recorrer el fichero línea a línea, sin cargarlo entero en memoria.
    """
    contador = 0
    with open(ruta, encoding="utf-8") as fichero:
        for _ in fichero:          # línea a línea, sin cargarlo entero
            contador += 1
    return contador


def leer_lineas_utiles(ruta) -> list[str]:
    """Devuelve las líneas del fichero sin espacios ni saltos alrededor.

    Descarta las líneas vacías y las que empiezan por ``#``.
    """
    utiles = []
    with open(ruta, encoding="utf-8") as fichero:
        for linea in fichero:
            limpia = linea.strip()
            if limpia and not limpia.startswith("#"):
                utiles.append(limpia)
    return utiles


def escribir_lineas(ruta, lineas: list[str]) -> None:
    """Escribe cada elemento de la lista en una línea del fichero.

    Si el fichero existe, se sustituye su contenido. Si la carpeta no existe,
    se crea. Cada línea, incluida la última, termina en salto de línea.
    """
    ruta = Path(ruta)
    ruta.parent.mkdir(parents=True, exist_ok=True)   # crea la carpeta si falta
    with open(ruta, "w", encoding="utf-8") as fichero:
        for linea in lineas:
            fichero.write(linea + "\n")


def anadir_linea(ruta, linea: str) -> None:
    """Añade una línea al final del fichero sin borrar lo que hubiera.

    Si el fichero no existe, lo crea.
    """
    with open(ruta, "a", encoding="utf-8") as fichero:
        fichero.write(linea + "\n")


def buscar(ruta, texto: str) -> list[tuple[int, str]]:
    """Devuelve las líneas que contienen el texto, sin distinguir mayúsculas.

    Cada resultado es una tupla (número de línea, línea sin el salto final).
    La primera línea del fichero es la 1.
    """
    resultados = []
    buscado = texto.lower()
    with open(ruta, encoding="utf-8") as fichero:
        for numero, linea in enumerate(fichero, start=1):
            linea = linea.rstrip("\n")
            if buscado in linea.lower():
                resultados.append((numero, linea))
    return resultados


def numerar(origen, destino) -> int:
    """Copia ``origen`` en ``destino`` anteponiendo a cada línea su número.

    El formato de cada línea es "  1: texto", con el número alineado a la
    derecha en tres caracteres. Devuelve el número de líneas copiadas.
    """
    copiadas = 0
    with open(origen, encoding="utf-8") as entrada, open(destino, "w", encoding="utf-8") as salida:
        for numero, linea in enumerate(entrada, start=1):
            texto = linea.rstrip("\n")
            salida.write(f"{numero:>3}: {texto}\n")
            copiadas = numero
    return copiadas


def ficheros_por_extension(carpeta, extension: str) -> list[str]:
    """Devuelve, ordenados, los nombres de los ficheros de la carpeta con esa extensión.

    ``extension`` se recibe sin punto. No busca en subcarpetas.

    >>> ficheros_por_extension(".", "no_existe")
    []
    """
    return sorted(
        ruta.name for ruta in Path(carpeta).glob(f"*.{extension}") if ruta.is_file()
    )
