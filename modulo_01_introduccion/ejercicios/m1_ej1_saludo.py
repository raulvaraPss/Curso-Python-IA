"""Módulo 1 - Ejercicio 1: saludo."""


def saludar(nombre):
    """Devuelve un saludo de bienvenida para ``nombre``.

    El nombre se limpia de espacios sobrantes y se escribe con la inicial de
    cada palabra en mayúscula. Si queda vacío, se saluda a "Anónimo".

    >>> saludar("  ada lovelace ")
    'Hola, Ada Lovelace. ¡Te damos la bienvenida al curso!'
    """
    # split() sin argumentos separa por cualquier espacio y descarta los
    # sobrantes (al inicio, al final y repetidos entre palabras).
    palabras = nombre.split()
    nombre_limpio = " ".join(palabra.capitalize() for palabra in palabras)

    if not nombre_limpio:
        nombre_limpio = "Anónimo"

    return f"Hola, {nombre_limpio}. ¡Te damos la bienvenida al curso!"


def main():
    """Pide el nombre por teclado e imprime el saludo."""
    nombre = input("¿Cómo te llamas? ")
    print(saludar(nombre))


if __name__ == "__main__":
    main()
