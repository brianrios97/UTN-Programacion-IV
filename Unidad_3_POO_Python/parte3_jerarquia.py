"""parte3_jerarquia.py — Jerarquía con abc.ABC y falla temprana.

Decisiones de diseño aplicadas:

  - Figura pasa a ser abc.ABC: no se puede instanciar directamente.
  - area() se declara @abstractmethod tanto en Figura como en Poligono:
    toda subclase concreta DEBE implementarlo o Python lanza TypeError
    al intentar instanciarla (falla temprana vs. retorno silencioso).
  - lados_esperados() también es @abstractmethod: fuerza la contrato
    en Triangulo, Cuadrado y PoligonoRegular.

Decisión sobre PoligonoRegular (Parte 3):
  Se MANTIENE la herencia de Poligono porque un polígono regular
  ES-UN polígono tanto por dominio como por comportamiento: tiene
  lados, perímetro y área calculables con las mismas reglas que
  cualquier Poligono. La herencia no es un truco de compilador;
  aporta duck typing seguro dentro de la jerarquía.
"""

from __future__ import annotations

import math
from abc import ABC, abstractmethod


class Figura(ABC):
    """Superclase abstracta del dominio geométrico."""

    def __init__(self, nombre: str, color: str) -> None:
        self._nombre = nombre
        self._color = color

    @property
    def nombre(self) -> str:
        return self._nombre

    @property
    def color(self) -> str:
        return self._color

    @abstractmethod
    def area(self) -> float:
        """Cada figura concreta debe calcular su propia área.

        Falla temprana: Python lanza TypeError si una subclase no implementa
        este método e intenta ser instanciada.
        """
        ...


class Lado:
    """Segmento con longitud estrictamente positiva."""

    def __init__(self, longitud: float) -> None:
        if longitud <= 0:
            raise ValueError(f"La longitud debe ser positiva, se recibió {longitud!r}")
        self._longitud = longitud

    @property
    def longitud(self) -> float:
        return self._longitud

    @longitud.setter
    def longitud(self, valor: float) -> None:
        if valor <= 0:
            raise ValueError("La longitud debe ser positiva")
        self._longitud = valor

    def __repr__(self) -> str:
        return f"Lado({self._longitud})"


class Poligono(Figura):
    """Polígono abstracto.

    Impone que sus subclases concretas implementen area() y lados_esperados().
    """

    def __init__(
        self,
        nombre: str,
        color: str,
        lados: list[Lado] | None = None,
        observaciones: list[str] | None = None,
    ) -> None:
        super().__init__(nombre, color)
        self._lados: list[Lado] = list(lados) if lados is not None else []
        self._observaciones: list[str] = list(observaciones) if observaciones is not None else []

    @abstractmethod
    def lados_esperados(self) -> int:
        """Cuántos lados debe tener este tipo de polígono."""
        ...

    @abstractmethod
    def area(self) -> float:
        """Cálculo de área específico de la subclase."""
        ...

    def perimetro(self) -> float:
        return sum(lado.longitud for lado in self._lados)

    def agregar_observacion(self, texto: str) -> None:
        self._observaciones.append(texto)

    def lados(self) -> list[Lado]:
        """Copia defensiva: el llamador no puede mutar la lista interna."""
        return list(self._lados)

    def __repr__(self) -> str:
        return (
            f"{self.__class__.__name__}("
            f"nombre={self._nombre!r}, lados={len(self._lados)})"
        )


class Triangulo(Poligono):
    """Triángulo. Implementa area() con la fórmula de Herón."""

    def __init__(
        self,
        nombre: str = "triángulo",
        color: str = "negro",
        lados: list[Lado] | None = None,
    ) -> None:
        super().__init__(nombre, color, lados)

    def lados_esperados(self) -> int:
        return 3

    def area(self) -> float:
        if len(self._lados) != 3:
            return 0.0
        a, b, c = (lado.longitud for lado in self._lados)
        s = (a + b + c) / 2
        return math.sqrt(s * (s - a) * (s - b) * (s - c))


class Cuadrado(Poligono):
    """Cuadrado de cuatro lados iguales."""

    def __init__(
        self,
        nombre: str = "cuadrado",
        color: str = "negro",
        lados: list[Lado] | None = None,
    ) -> None:
        super().__init__(nombre, color, lados)

    def lados_esperados(self) -> int:
        return 4

    def area(self) -> float:
        if len(self._lados) != 4:
            return 0.0
        return self._lados[0].longitud ** 2


class PoligonoRegular(Poligono):
    """Polígono regular de N lados de igual longitud.

    Hereda de Poligono porque un polígono regular ES-UN polígono: comparte
    el mismo modelo de dominio (lados, perímetro, área) y el mismo protocolo
    de comportamiento. La herencia no es ceremonial: es una generalización
    correcta justificada por el dominio.
    """

    def __init__(self, nombre: str, color: str, medida: float, cantidad: int) -> None:
        super().__init__(nombre, color, [Lado(medida) for _ in range(cantidad)])
        self._cantidad = cantidad

    def lados_esperados(self) -> int:
        return self._cantidad

    def area(self) -> float:
        if not self._lados:
            return 0.0
        l = self._lados[0].longitud
        n = self._cantidad
        return (n * l ** 2) / (4 * math.tan(math.pi / n))


if __name__ == "__main__":
    # Verificar falla temprana al intentar instanciar clases abstractas
    try:
        Figura("test", "rojo")  # type: ignore[abstract]
    except TypeError as exc:
        print(f"✅ Figura no se puede instanciar: {exc}")

    try:
        Poligono("test", "rojo")  # type: ignore[abstract]
    except TypeError as exc:
        print(f"✅ Poligono no se puede instanciar: {exc}")

    t = Triangulo(lados=[Lado(3), Lado(4), Lado(5)])
    c = Cuadrado(lados=[Lado(6), Lado(6), Lado(6), Lado(6)])
    r = PoligonoRegular("Hexágono", "azul", 3, 6)

    figuras: list[Poligono] = [t, c, r]
    for fig in figuras:
        print(f"{fig}: perímetro={fig.perimetro():.2f}, área={fig.area():.2f}")
