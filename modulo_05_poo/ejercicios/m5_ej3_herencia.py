"""Módulo 5 - Ejercicio 3: herencia y clases abstractas."""

from abc import ABC, abstractmethod


class Empleado(ABC):
    """Clase base abstracta de todos los empleados."""

    def __init__(self, nombre: str):
        self.nombre = nombre

    @abstractmethod
    def salario_mensual(self) -> float:
        """Devuelve el salario bruto de un mes."""

    def descripcion(self) -> str:
        """Devuelve "nombre (Clase): salario €", con dos decimales.

        ``Clase`` es el nombre de la clase real del objeto.

        >>> Fijo("Ada", 36000).descripcion()
        'Ada (Fijo): 3000.00 €'
        """
        return f"{self.nombre} ({type(self).__name__}): {self.salario_mensual():.2f} €"


class Fijo(Empleado):
    """Empleado con un salario anual que se cobra en 12 pagas."""

    def __init__(self, nombre: str, salario_anual: float):
        """Inicializa la parte heredada con ``super()`` y guarda ``salario_anual``."""
        super().__init__(nombre)
        self.salario_anual = salario_anual

    def salario_mensual(self) -> float:
        """Devuelve el salario anual entre 12, con dos decimales."""
        return round(self.salario_anual / 12, 2)


class PorHoras(Empleado):
    """Empleado que cobra por las horas trabajadas en el mes."""

    def __init__(self, nombre: str, horas: float, tarifa: float):
        """Inicializa la parte heredada y guarda ``horas`` y ``tarifa``."""
        super().__init__(nombre)
        self.horas = horas
        self.tarifa = tarifa

    def salario_mensual(self) -> float:
        """Devuelve horas por tarifa, con dos decimales."""
        return round(self.horas * self.tarifa, 2)


class Comercial(Fijo):
    """Empleado fijo que cobra además un porcentaje de lo que vende."""

    def __init__(self, nombre: str, salario_anual: float, ventas: float, comision: float = 5):
        """Inicializa la parte heredada y guarda ``ventas`` y ``comision`` (en %)."""
        super().__init__(nombre, salario_anual)
        self.ventas = ventas
        self.comision = comision

    def salario_mensual(self) -> float:
        """Devuelve el salario de un Fijo más la comisión sobre las ventas.

        Tiene que reutilizar el cálculo de la clase base con ``super()``.

        >>> Comercial("Grace", 24000, ventas=10000).salario_mensual()
        2500.0
        """
        return round(super().salario_mensual() + self.ventas * self.comision / 100, 2)


def coste_mensual(plantilla: list[Empleado]) -> float:
    """Devuelve la suma de los salarios mensuales de la plantilla, con dos decimales.

    >>> coste_mensual([Fijo("Ada", 36000), PorHoras("Linus", 100, 20)])
    5000.0
    """
    return round(sum(empleado.salario_mensual() for empleado in plantilla), 2)



def mejor_pagado(plantilla: list[Empleado]) -> Empleado | None:
    """Devuelve el empleado con mayor salario mensual, o ``None`` sin plantilla."""
    if not plantilla:
        return None
    return max(plantilla, key=lambda empleado: empleado.salario_mensual())
