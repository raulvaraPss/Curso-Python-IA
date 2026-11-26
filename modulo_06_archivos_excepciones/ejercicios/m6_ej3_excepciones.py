"""Módulo 6 - Ejercicio 3: excepciones."""


def a_entero(texto, por_defecto=None):
    """Convierte a entero con ``int()``. Si no se puede, devuelve ``por_defecto``.

    Es la versión con ``try``/``except`` de la función del módulo 2. Tiene que
    funcionar también si ``texto`` es ``None``.

    >>> a_entero("42"), a_entero("abc"), a_entero(None, 0)
    (42, None, 0)
    """
    try:
        return int(texto)
    except (ValueError, TypeError):      # "abc" → ValueError, None → TypeError
        return por_defecto


def dividir(a: float, b: float) -> float | None:
    """Devuelve ``a / b``, o ``None`` si ``b`` es cero.

    Solo captura la división por cero: cualquier otro error tiene que subir.
    """
    try:
        return a / b
    except ZeroDivisionError:            # solo esto; "10" / 2 sigue lanzando TypeError
        return None


def leer_o_vacio(ruta) -> str:
    """Devuelve el contenido del fichero, o la cadena vacía si no existe."""
    try:
        with open(ruta, encoding="utf-8") as fichero:
            return fichero.read()
    except FileNotFoundError:
        return ""


def validar_edad(edad) -> int:
    """Devuelve la edad si es válida y, si no, lanza una excepción.

    - ``TypeError`` si no es un ``int`` (un ``bool`` tampoco vale).
    - ``ValueError`` si no está entre 0 y 130, ambos incluidos. El mensaje
      tiene que contener el valor recibido.

    >>> validar_edad(36)
    36
    """
    if not isinstance(edad, int) or isinstance(edad, bool):
        raise TypeError(f"La edad tiene que ser un entero, no {type(edad).__name__}")
    if not 0 <= edad <= 130:
        raise ValueError(f"Edad fuera de rango (0-130): {edad}")
    return edad


class ErrorDeCuenta(Exception):
    """Base de los errores de una cuenta."""


class ImporteNoValido(ErrorDeCuenta):
    """El importe no es positivo."""


class SaldoInsuficiente(ErrorDeCuenta):
    """El importe supera el saldo disponible."""
    def __init__(self, saldo, importe):
        self.saldo = saldo
        self.importe = importe
        super().__init__(f"Saldo insuficiente: hay {saldo} y se piden {importe}")


def retirar(saldo: float, importe: float) -> float:
    """Devuelve el saldo que queda tras retirar el importe.

    Lanza ``ImporteNoValido`` si el importe no es positivo y
    ``SaldoInsuficiente`` si supera el saldo.

    >>> retirar(100, 30)
    70
    """
    if importe <= 0:
        raise ImporteNoValido(f"El importe tiene que ser positivo: {importe}")
    if importe > saldo:
        raise SaldoInsuficiente(saldo, importe)
    return saldo - importe


def convertir_todos(textos: list[str]) -> tuple[list[float], list[str]]:
    """Convierte cada texto a ``float`` y separa los que no se pueden convertir.

    Devuelve una tupla (números, textos rechazados). Un texto no válido no
    interrumpe el proceso de los siguientes.

    >>> convertir_todos(["1.5", "x", "2"])
    ([1.5, 2.0], ['x'])
    """
    numeros = []
    rechazados = []
    for texto in textos:
        try:                             # el try va DENTRO del bucle
            numeros.append(float(texto))
        except ValueError:
            rechazados.append(texto)
    return numeros, rechazados


def ejecutar(accion, registro: list[str]):
    """Llama a ``accion()`` anotando lo que ocurre en la lista ``registro``.

    Añade "inicio" antes de llamar; después "ok" si termina bien o "error"
    si lanza cualquier excepción; y "fin" en todos los casos. Devuelve lo que
    devuelva la acción. Si la acción falla, la excepción tiene que seguir
    subiendo después de anotar "error" y "fin".
    """
    registro.append("inicio")
    try:
        resultado = accion()
    except Exception:
        registro.append("error")
        raise                            # vuelve a lanzar la misma excepción
    else:
        registro.append("ok")
        return resultado
    finally:
        registro.append("fin") 


class ErrorDeConfiguracion(Exception):
    """La configuración no es válida."""


def puerto_configurado(configuracion: dict) -> int:
    """Devuelve el puerto de la configuración como entero.

    Si falta la clave "puerto" o su valor no se puede convertir a entero,
    lanza ``ErrorDeConfiguracion`` encadenada con la excepción original
    mediante ``raise ... from``.

    >>> puerto_configurado({"puerto": "8080"})
    8080
    """
    try:
        return int(configuracion["puerto"])
    except KeyError as error:
        raise ErrorDeConfiguracion("Falta la clave 'puerto'") from error
    except ValueError as error:
        raise ErrorDeConfiguracion(
            f"El puerto no es un entero: {configuracion['puerto']!r}"
        ) from error
