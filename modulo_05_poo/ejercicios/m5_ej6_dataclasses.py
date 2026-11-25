"""Módulo 5 - Ejercicio 6: dataclasses y composición.

En este ejercicio las clases se escriben enteras: no hay plantilla. El
enunciado está en ejercicios/README.md.
"""

import math
from dataclasses import dataclass, field


@dataclass(frozen=True)
class Punto:
    x: float = 0.0
    y: float = 0.0

    def distancia(self, otro: "Punto") -> float:
        return round(math.dist((self.x, self.y), (otro.x, otro.y)), 2)


@dataclass
class LineaPedido:
    producto: str
    unidades: int
    precio: float

    def __post_init__(self):
        if self.unidades <= 0:
            raise ValueError("Las unidades deben ser positivas")

    @property
    def importe(self) -> float:
        return round(self.unidades * self.precio, 2)


@dataclass
class Pedido:
    numero: int
    cliente: str
    lineas: list[LineaPedido] = field(default_factory=list)

    def anadir(self, producto: str, unidades: int, precio: float) -> LineaPedido:
        linea = LineaPedido(producto, unidades, precio)
        self.lineas.append(linea)
        return linea

    @property
    def total(self) -> float:
        return round(sum(linea.importe for linea in self.lineas), 2)

    def __len__(self) -> int:
        return len(self.lineas)

    def productos(self) -> list[str]:
        return sorted(set(linea.producto for linea in self.lineas))