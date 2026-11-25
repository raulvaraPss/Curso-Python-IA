"""Módulo 5 - Ejercicio 1: clases, objetos y constructores."""


class Rectangulo:
    """Un rectángulo definido por su base y su altura."""

    def __init__(self, base: float, altura: float):
        """Guarda la base y la altura en los atributos ``base`` y ``altura``."""
        self.base = base
        self.altura = altura

    def area(self) -> float:
        """Devuelve el área.

        >>> Rectangulo(3, 4).area()
        12
        """
        return self.base * self.altura

    def perimetro(self) -> float:
        """Devuelve el perímetro.

        >>> Rectangulo(3, 4).perimetro()
        14
        """
        return 2 * (self.base + self.altura)

    def es_cuadrado(self) -> bool:
        """Indica si la base y la altura son iguales."""
        return self.base == self.altura

    def escalar(self, factor: float) -> "Rectangulo":
        """Devuelve un rectángulo NUEVO con las medidas multiplicadas por ``factor``.

        El rectángulo original no cambia.
        """
        return Rectangulo(self.base * factor, self.altura * factor)


class Contador:
    """Un contador con paso configurable.

    Es la versión con clase del cierre ``crear_contador`` del módulo 3.
    """

    def __init__(self, inicio: int = 0, paso: int = 1):
        """Guarda el valor inicial en ``valor`` y el paso en ``paso``.

        El contador recuerda además su valor inicial para poder reiniciarse.
        """
        self.inicio = inicio
        self.paso = paso
        self.valor = inicio

    def incrementar(self) -> int:
        """Suma el paso al valor y devuelve el valor nuevo.

        >>> contador = Contador()
        >>> contador.incrementar(), contador.incrementar()
        (1, 2)
        """
        self.valor += self.paso
        return self.valor

    def reiniciar(self) -> None:
        """Devuelve el valor al inicial."""
        self.valor = self.inicio


class Tarea:
    """Una tarea pendiente con etiquetas."""

    def __init__(self, titulo: str, etiquetas: list[str] | None = None):
        """Guarda el título sin espacios alrededor y deja la tarea sin completar.

        Atributos: ``titulo``, ``completada`` (empieza en ``False``) y
        ``etiquetas``. Si no se pasan etiquetas, cada tarea tiene su propia
        lista vacía.
        """
        self.titulo = titulo.strip()
        self.completada = False
        self.etiquetas = list(etiquetas) if etiquetas is not None else []

    def completar(self) -> None:
        """Marca la tarea como completada."""
        self.completada = True

    def etiquetar(self, etiqueta: str) -> None:
        """Añade la etiqueta en minúsculas si la tarea no la tiene ya."""
        etiqueta = etiqueta.lower()
        if etiqueta not in self.etiquetas:
            self.etiquetas.append(etiqueta)

    def resumen(self) -> str:
        """Devuelve "[x] título" si está completada y "[ ] título" si no.

        >>> Tarea("Comprar pan").resumen()
        '[ ] Comprar pan'
        """
        marca = "x" if self.completada else " "
        return f"[{marca}] {self.titulo}"
