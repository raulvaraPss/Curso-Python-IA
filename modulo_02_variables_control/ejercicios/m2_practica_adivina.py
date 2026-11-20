"""Módulo 2 - Práctica 2, parte A: adivina el número."""

import random

MINIMO = 1
MAXIMO = 100
MAX_INTENTOS = 7


def evaluar_intento(secreto: int, intento: int) -> str:
    """Compara el intento con el número secreto.

    Devuelve "acierto", "mayor" si el secreto es mayor que el intento o
    "menor" si el secreto es menor.

    >>> evaluar_intento(50, 30)
    'mayor'
    """
    if secreto == intento:
        return "acierto"
    elif secreto > intento:
        return "mayor"
    else:
        return "menor"


def es_intento_valido(texto: str) -> bool:
    """Indica si ``texto`` es un entero entre MINIMO y MAXIMO.

    >>> es_intento_valido("50"), es_intento_valido("abc"), es_intento_valido("101")
    (True, False, False)
    """
    limpio = texto.strip()
    if not limpio.isdecimal():
        return False
    return MINIMO <= int(limpio) <= MAXIMO


def jugar(secreto: int, max_intentos: int = MAX_INTENTOS) -> bool:
    """Juega una partida y devuelve True si el jugador acierta.

    En cada turno pide un número con input(). Una entrada no válida no
    consume intento. Tras cada intento fallido imprime una pista.
    """
    intento_actual = 1
    while intento_actual <= max_intentos:
        texto = input(f"Intento {intento_actual} de {max_intentos}: ")

        if not es_intento_valido(texto):
            print(f"Escribe un número entre {MINIMO} y {MAXIMO}.")
            continue  # vuelve a preguntar sin sumar intento

        resultado = evaluar_intento(secreto, int(texto))
        if resultado == "acierto":
            print(f"¡Correcto! Lo has adivinado en {intento_actual} intentos.")
            return True

        print(f"El número secreto es {resultado}.")
        intento_actual += 1

    print(f"Has agotado los intentos. El número era {secreto}.")
    return False


def main() -> None:
    """Genera un número secreto al azar y lanza una partida."""
    secreto = random.randint(MINIMO, MAXIMO)
    jugar(secreto)


if __name__ == "__main__":
    main()