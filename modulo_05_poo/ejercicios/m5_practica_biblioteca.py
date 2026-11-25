"""Módulo 5 - Práctica 5: modelo de dominio de una biblioteca.

Clases del modelo:

    Material (abstracta)      lo que se puede prestar
    ├── Libro
    ├── Revista
    └── Dvd
    Socio                     quien toma prestado
    Prestamo                  un material prestado a un socio en una fecha
    Biblioteca                el catálogo, los socios y los préstamos (composición)
"""

from abc import ABC, abstractmethod
from dataclasses import dataclass, field
from datetime import date, timedelta


class Material(ABC):
    """Clase base abstracta de todo lo que se puede prestar."""

    def __init__(self, codigo: str, titulo: str, anio: int):
        """Guarda ``codigo``, ``titulo`` y ``anio``. El material empieza disponible.

        La disponibilidad se guarda en el atributo interno ``_disponible``.
        """
        self.codigo = codigo
        self.titulo = titulo
        self.anio = anio
        self._disponible = True

    @property
    def disponible(self) -> bool:
        """Indica si el material se puede prestar. Solo lectura."""
        return self._disponible

    @property
    @abstractmethod
    def dias_prestamo(self) -> int:
        """Días que se puede tener prestado este tipo de material."""

    def prestar(self) -> None:
        """Marca el material como no disponible.

        Lanza ``ValueError`` si ya estaba prestado.
        """
        if not self._disponible:
            raise ValueError(f"{self.codigo} ya está prestado")
        self._disponible = False

    def devolver(self) -> None:
        """Marca el material como disponible.

        Lanza ``ValueError`` si no estaba prestado.
        """
        if self._disponible:
            raise ValueError(f"{self.codigo} no está prestado")
        self._disponible = True

    def __str__(self) -> str:
        """Devuelve "[codigo] titulo (anio)"."""
        return f"[{self.codigo}] {self.titulo} ({self.anio})"

    def __repr__(self) -> str:
        """Devuelve "Clase('codigo', 'titulo')" con el nombre de la clase real."""
        return f"{type(self).__name__}({self.codigo!r}, {self.titulo!r})"

    def __eq__(self, otro) -> bool:
        """Dos materiales son iguales si tienen el mismo código.

        Si ``otro`` no es un Material, devuelve ``NotImplemented``.
        """
        if not isinstance(otro, Material):
            return NotImplemented
        return self.codigo == otro.codigo

    def __hash__(self) -> int:
        return hash(self.codigo)


class Libro(Material):
    """Un libro. Se presta 21 días."""

    def __init__(self, codigo: str, titulo: str, anio: int, autor: str):
        """Inicializa la parte heredada y guarda ``autor``."""
        super().__init__(codigo, titulo, anio)
        self.autor = autor

    @property
    def dias_prestamo(self) -> int:
        return 21

    def __str__(self) -> str:
        """Añade el autor a la descripción heredada: "[codigo] titulo (anio), de autor"."""
        return f"{super().__str__()}, de {self.autor}"


class Revista(Material):
    """Una revista. Se presta 7 días."""

    def __init__(self, codigo: str, titulo: str, anio: int, numero: int):
        """Inicializa la parte heredada y guarda ``numero``."""
        super().__init__(codigo, titulo, anio)
        self.numero = numero

    @property
    def dias_prestamo(self) -> int:
        return 7

    def __str__(self) -> str:
        """Añade el número: "[codigo] titulo (anio), n.º numero"."""
        return f"{super().__str__()}, n.º {self.numero}"


class Dvd(Material):
    """Un DVD. Se presta 3 días. No redefine ``__str__``."""

    def __init__(self, codigo: str, titulo: str, anio: int, minutos: int):
        """Inicializa la parte heredada y guarda ``minutos``."""
        super().__init__(codigo, titulo, anio)
        self.minutos = minutos

    @property
    def dias_prestamo(self) -> int:
        return 3


@dataclass
class Socio:
    """Una persona que puede tomar materiales en préstamo.

    Campos: ``numero`` (int), ``nombre`` (str) y ``prestados``, la lista de
    materiales que tiene en este momento, que empieza vacía y es propia de
    cada socio.
    """

    MAX_PRESTAMOS = 3

    numero: int
    nombre: str
    prestados: list[Material] = field(default_factory=list)


    def puede_tomar_prestado(self) -> bool:
        """Indica si el socio tiene menos de ``MAX_PRESTAMOS`` materiales."""
        return len(self.prestados) < self.MAX_PRESTAMOS


@dataclass
class Prestamo:
    """Un material prestado a un socio en una fecha.

    Campos: ``material`` (Material), ``socio`` (Socio) y ``fecha`` (date).
    """

    material: Material
    socio: Socio
    fecha: date

    @property
    def fecha_devolucion(self) -> date:
        """Fecha límite: la del préstamo más los días que permite el material."""
        return self.fecha + timedelta(days=self.material.dias_prestamo)

    def dias_de_retraso(self, hoy: date) -> int:
        """Días transcurridos desde la fecha límite. Si no ha vencido, 0."""
        return max(0, (hoy - self.fecha_devolucion).days)

    def esta_vencido(self, hoy: date) -> bool:
        """Indica si ``hoy`` es posterior a la fecha límite."""
        return hoy > self.fecha_devolucion


class Biblioteca:
    """El catálogo, los socios y los préstamos en curso.

    Usa composición: contiene un diccionario de materiales por código, un
    diccionario de socios por número y una lista de préstamos. Ninguno de
    los tres es accesible directamente desde fuera.
    """

    def __init__(self, nombre: str):
        """Guarda el nombre y crea ``_materiales``, ``_socios`` y ``_prestamos`` vacíos."""
        self.nombre = nombre
        self._materiales = {}
        self._socios = {}
        self._prestamos = []

    # ------------------------------------------------------------- catálogo
    def anadir_material(self, material: Material) -> None:
        """Añade un material al catálogo.

        Lanza ``ValueError`` si ya hay un material con ese código.
        """
        if material.codigo in self._materiales:
            raise ValueError(f"Ya existe un material con el código {material.codigo}")
        self._materiales[material.codigo] = material

    def buscar(self, codigo: str) -> Material | None:
        """Devuelve el material con ese código, o ``None`` si no existe."""
        return self._materiales.get(codigo)

    def buscar_por_titulo(self, texto: str) -> list[Material]:
        """Devuelve los materiales cuyo título contiene el texto.

        No distingue mayúsculas de minúsculas. El resultado va ordenado por título.
        """
        texto = texto.lower()
        encontrados = [m for m in self._materiales.values() if texto in m.titulo.lower()]
        return sorted(encontrados, key=lambda m: m.titulo)

    def disponibles(self) -> list[Material]:
        """Devuelve los materiales disponibles, ordenados por código."""
        libres = [m for m in self._materiales.values() if m.disponible]
        return sorted(libres, key=lambda m: m.codigo)

    def __len__(self) -> int:
        """Devuelve el número de materiales del catálogo."""
        return len(self._materiales)

    def __contains__(self, codigo: str) -> bool:
        """Indica si hay un material con ese código."""
        return codigo in self._materiales

    def __iter__(self):
        """Recorre los materiales del catálogo en el orden en que se añadieron."""
        return iter(self._materiales.values())

    # --------------------------------------------------------------- socios
    def registrar_socio(self, nombre: str) -> Socio:
        """Crea un socio con el siguiente número libre, lo guarda y lo devuelve.

        Los números empiezan en 1 y son consecutivos.
        """
        nuevo = Socio(len(self._socios) + 1, nombre)
        self._socios[nuevo.numero] = nuevo
        return nuevo

    def socio(self, numero: int) -> Socio | None:
        """Devuelve el socio con ese número, o ``None`` si no existe."""
        return self._socios.get(numero)

    # ------------------------------------------------------------ préstamos
    def prestar(self, codigo: str, numero_socio: int, fecha: date) -> Prestamo:
        """Presta un material a un socio y devuelve el préstamo creado.

        Lanza ``ValueError`` con uno de estos mensajes, comprobados en este orden:

        - "No existe el material <codigo>"
        - "No existe el socio <numero>"
        - "<nombre> ha alcanzado el máximo de préstamos"
        - el de ``Material.prestar`` si el material ya está prestado

        Si todo es correcto: marca el material como prestado, lo añade a la
        lista del socio y guarda el préstamo.
        """
        material = self.buscar(codigo)
        if material is None:
            raise ValueError(f"No existe el material {codigo}")
        socio = self.socio(numero_socio)
        if socio is None:
            raise ValueError(f"No existe el socio {numero_socio}")
        if not socio.puede_tomar_prestado():
            raise ValueError(f"{socio.nombre} ha alcanzado el máximo de préstamos")
        material.prestar()
        socio.prestados.append(material)
        prestamo = Prestamo(material, socio, fecha)
        self._prestamos.append(prestamo)
        return prestamo

    def devolver(self, codigo: str) -> Prestamo:
        """Registra la devolución de un material y devuelve el préstamo cerrado.

        Lanza ``ValueError`` con el mensaje "No hay ningún préstamo de <codigo>"
        si ese material no está prestado. Si lo está: lo marca como
        disponible, lo quita de la lista del socio y elimina el préstamo.
        """
        for prestamo in self._prestamos:
            if prestamo.material.codigo == codigo:
                prestamo.material.devolver()
                prestamo.socio.prestados.remove(prestamo.material)
                self._prestamos.remove(prestamo)
                return prestamo
        raise ValueError(f"No hay ningún préstamo de {codigo}")

    @property
    def prestamos(self) -> tuple:
        """Tupla con los préstamos en curso, en el orden en que se hicieron."""
        return tuple(self._prestamos)

    def prestamos_vencidos(self, hoy: date) -> list[Prestamo]:
        """Devuelve los préstamos vencidos, del que lleva más retraso al que menos."""
        vencidos = [p for p in self._prestamos if p.esta_vencido(hoy)]
        return sorted(vencidos, key=lambda p: p.dias_de_retraso(hoy), reverse=True)

    def resumen(self) -> str:
        """Devuelve "nombre: N materiales, D disponibles, S socios"."""
        return (
            f"{self.nombre}: {len(self)} materiales, "
            f"{len(self.disponibles())} disponibles, {len(self._socios)} socios"
        )
