"""Módulo 3 - Ejercicio 2: parámetros y retorno."""


def potencia(base: float, exponente: float = 2) -> float:
    """Eleva ``base`` a ``exponente``. Sin exponente, eleva al cuadrado.

    >>> potencia(3)
    9
    >>> potencia(2, 10)
    1024
    """
    return base ** exponente


def sumar_todos(*numeros: float) -> float:
    """Suma todos los argumentos recibidos. Sin argumentos devuelve 0.

    >>> sumar_todos(1, 2, 3)
    6
    >>> sumar_todos()
    0
    """
    return sum(numeros)


def crear_usuario(nombre: str, *, activo: bool = True, **extras) -> dict:
    """Devuelve un diccionario con los datos de un usuario.

    Contiene siempre las claves "nombre" y "activo", y además una clave por
    cada argumento adicional que se pase por nombre. ``activo`` solo se puede
    pasar por nombre.

    >>> crear_usuario("Ada")
    {'nombre': 'Ada', 'activo': True}
    >>> crear_usuario("Ada", activo=False, rol="admin")
    {'nombre': 'Ada', 'activo': False, 'rol': 'admin'}
    """
    return {"nombre": nombre, "activo": activo, **extras}
    # También vale en una línea: return {"nombre": nombre, "activo": activo, **extras}


def anadir_elemento(elemento, lista: list | None = None) -> list:
    """Añade ``elemento`` al final de ``lista`` y devuelve la lista.

    Si no se pasa lista, se crea una nueva en cada llamada.

    >>> anadir_elemento(1)
    [1]
    >>> anadir_elemento(2)
    [2]
    >>> anadir_elemento(3, [1, 2])
    [1, 2, 3]
    """
    if lista is None:
        lista = []
    lista.append(elemento)
    return lista


def formatear_nombre(nombre: str, apellido: str, *, mayusculas: bool = False,
                     separador: str = " ") -> str:
    """Une nombre y apellido con el separador indicado.

    Quita los espacios sobrantes de cada parte. Con ``mayusculas=True``
    devuelve el resultado en mayúsculas. Las dos opciones son solo por nombre.

    >>> formatear_nombre(" Ada ", "Lovelace")
    'Ada Lovelace'
    >>> formatear_nombre("Ada", "Lovelace", mayusculas=True, separador=", ")
    'ADA, LOVELACE'
    """
    resultado = f"{nombre.strip()}{separador}{apellido.strip()}"
    if mayusculas:
        resultado = resultado.upper()
    return resultado

def estadisticas(*numeros: float) -> tuple:
    """Devuelve la tupla (cantidad, suma, media) de los números recibidos.

    La media se redondea a dos decimales. Sin números devuelve (0, 0, None).

    >>> estadisticas(2, 4, 9)
    (3, 15, 5.0)
    >>> estadisticas()
    (0, 0, None)
    """
    cantidad = len(numeros)
    suma = sum(numeros)
    media = round(suma / cantidad, 2) if cantidad > 0 else None
    return cantidad, suma, media