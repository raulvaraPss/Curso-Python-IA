"""Módulo 5 - Ejercicio 5: encapsulación y propiedades."""


class CuentaBancaria:
    """Una cuenta cuyo saldo solo cambia con ingresos y retiradas."""

    def __init__(self, titular: str, saldo_inicial: float = 0.0):
        """Guarda el titular y el saldo. Lanza ``ValueError`` si el saldo es negativo.

        El saldo se guarda en ``_saldo`` y los movimientos en ``_movimientos``,
        que empieza vacía.
        """
        if saldo_inicial < 0:
            raise ValueError("El saldo inicial no puede ser negativo")
        self.titular = titular
        self._saldo = saldo_inicial
        self._movimientos = []

    @property
    def saldo(self) -> float:
        """Saldo actual. Es de solo lectura."""
        return self._saldo

    @property
    def movimientos(self) -> tuple:
        """Tupla con los importes de los movimientos: positivos los ingresos y
        negativos las retiradas."""
        return tuple(self._movimientos)

    def ingresar(self, importe: float) -> None:
        """Suma el importe al saldo. Lanza ``ValueError`` si no es positivo."""
        if importe <= 0:
            raise ValueError("El importe debe ser positivo")
        self._saldo += importe
        self._movimientos.append(importe)

    def retirar(self, importe: float) -> None:
        """Resta el importe del saldo.

        Lanza ``ValueError`` si el importe no es positivo o si supera el saldo.
        """
        if importe <= 0:
            raise ValueError("El importe debe ser positivo")
        if importe > self._saldo:
            raise ValueError("El importe no puede superar el saldo")
        self._saldo -= importe
        self._movimientos.append(-importe)


class Producto:
    """Un producto con precio validado y precio con IVA calculado."""

    IVA = 21

    def __init__(self, nombre: str, precio: float):
        """Guarda el nombre y el precio. El precio tiene que pasar por el setter."""
        self.nombre = nombre
        self.precio = precio  

    @property
    def precio(self) -> float:
        """Precio sin IVA."""
        return self._precio

    @precio.setter
    def precio(self, valor: float) -> None:
        """Lanza ``ValueError`` si el valor es negativo."""
        if valor < 0:
            raise ValueError("El precio no puede ser negativo")
        self._precio = valor

    @property
    def precio_con_iva(self) -> float:
        """Precio con el IVA de la clase aplicado, con dos decimales. Solo lectura.

        >>> Producto("Teclado", 100).precio_con_iva
        121.0
        """
        return round(self._precio * (1 + self.IVA / 100), 2)


class Temperatura:
    """Una temperatura que se puede leer y escribir en dos escalas."""

    CERO_ABSOLUTO = -273.15

    def __init__(self, celsius: float = 0.0):
        """Guarda la temperatura. Tiene que pasar por el setter de ``celsius``."""
        self.celsius = celsius

    @property
    def celsius(self) -> float:
        """Temperatura en grados Celsius."""
        return self._celsius

    @celsius.setter
    def celsius(self, valor: float) -> None:
        """Lanza ``ValueError`` si el valor es menor que ``CERO_ABSOLUTO``."""
        if valor < self.CERO_ABSOLUTO:
            raise ValueError("El valor debe ser mayor o igual que el cero absoluto")
        self._celsius = valor

    @property
    def fahrenheit(self) -> float:
        """Temperatura en grados Fahrenheit: C * 9 / 5 + 32, con dos decimales.

        >>> Temperatura(100).fahrenheit
        212.0
        """
        return round(self._celsius * 9 / 5 + 32, 2)

    @fahrenheit.setter
    def fahrenheit(self, valor: float) -> None:
        """Convierte a Celsius y asigna a través de la propiedad ``celsius``."""
        self.celsius = (valor - 32) * 5 / 9
