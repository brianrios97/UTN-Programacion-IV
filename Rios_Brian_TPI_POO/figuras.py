"""figuras.py — Dominio completo del TP Integrador POO (Partes 1 a 4).

Contiene:
  Parte 1 (corregida): Figura, Lado, Poligono, Triangulo, Cuadrado, PoligonoRegular
  Parte 2: Etiqueta (@dataclass frozen) y Taller (composición/agregación/asociación)
  Parte 3: Figura y Poligono como abc.ABC con falla temprana (@abstractmethod)
  Parte 4: Exportable (typing.Protocol) — PlanoCAD cumple sin herencia
"""

from __future__ import annotations

import math
from abc import ABC, abstractmethod
from dataclasses import dataclass
from typing import Protocol, runtime_checkable

# ============================================================
# PARTE 1 + PARTE 3 — Jerarquía de figuras con ABC
# ============================================================

class Figura(ABC):
    """Superclase abstracta. No se puede instanciar directamente."""

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
        """Falla temprana: toda subclase concreta DEBE implementar area()."""
        ...


class Lado:
    """Segmento con longitud estrictamente positiva."""

    def __init__(self, longitud: float) -> None:
        if longitud <= 0:
            raise ValueError(f"La longitud debe ser positiva, recibí {longitud!r}")
        self._longitud = longitud

    @property                          # java-ismo #2 corregido: @property en vez de getLongitud()
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
    """Polígono abstracto. Impone area() y lados_esperados() a las subclases."""

    def __init__(
        self,
        nombre: str,
        color: str,
        lados: list[Lado] | None = None,          # java-ismo #4 corregido: None en vez de []
        observaciones: list[str] | None = None,
    ) -> None:
        super().__init__(nombre, color)             # java-ismo #5 corregido: super() llamado
        self._lados: list[Lado] = list(lados) if lados is not None else []      # #6: copia
        self._observaciones: list[str] = list(observaciones) if observaciones is not None else []

    @abstractmethod
    def lados_esperados(self) -> int: ...

    @abstractmethod
    def area(self) -> float: ...

    def perimetro(self) -> float:
        return sum(lado.longitud for lado in self._lados)   # java-ismo #7: sum + generator

    def agregar_observacion(self, texto: str) -> None:
        self._observaciones.append(texto)

    def lados(self) -> list[Lado]:
        return list(self._lados)       # java-ismo #6 corregido: copia defensiva al exponer

    def __repr__(self) -> str:
        return f"{self.__class__.__name__}(nombre={self._nombre!r}, lados={len(self._lados)})"


class Triangulo(Poligono):
    """Triángulo. Implementa area() con la fórmula de Herón."""

    def __init__(
        self,
        nombre: str = "triángulo",
        color: str = "negro",
        lados: list[Lado] | None = None,
    ) -> None:
        super().__init__(nombre, color, lados)   # java-ismo #8: sin ramas isinstance

    def lados_esperados(self) -> int:
        return 3

    def area(self) -> float:
        if len(self._lados) != 3:
            return 0.0
        a, b, c = (l.longitud for l in self._lados)
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
    """Polígono regular de N lados iguales.

    Mantiene herencia de Poligono: un polígono regular ES-UN polígono tanto
    por dominio (tiene lados, perímetro, área) como por comportamiento.
    No es un truco de compilador; aporta duck typing seguro en la jerarquía.
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


# ============================================================
# PARTE 2 — Etiqueta (composición) y Taller
# ============================================================

@dataclass(frozen=True)
class Etiqueta:
    """Par clave-valor inmutable.

    frozen=True: impide reasignar atributos, habilita hash automático.
    """
    clave: str
    valor: str

    def __str__(self) -> str:
        return f"{self.clave}={self.valor}"


class Taller:
    """Taller de geometría con tres tipos de relaciones OO.

    COMPOSICIÓN  → Etiqueta  (Taller crea y posee las etiquetas)
    AGREGACIÓN   → Poligono  (los polígonos se pasan desde afuera)
    ASOCIACIÓN   → supervisor: str  (referencia débil, no lo crea)
    """

    def __init__(self, nombre: str, ciudad: str) -> None:
        self._nombre = nombre
        self._ciudad = ciudad
        self._etiquetas: list[Etiqueta] = [          # COMPOSICIÓN
            Etiqueta("nombre", nombre),
            Etiqueta("ciudad", ciudad),
        ]
        self._inventario: list[Poligono] = []        # AGREGACIÓN
        self._supervisor: str | None = None          # ASOCIACIÓN

    @property
    def nombre(self) -> str:
        return self._nombre

    # ---------- COMPOSICIÓN: Taller crea las Etiquetas ----------
    def agregar_etiqueta(self, clave: str, valor: str) -> None:
        self._etiquetas.append(Etiqueta(clave, valor))

    def etiquetas(self) -> list[Etiqueta]:
        return list(self._etiquetas)                 # copia defensiva

    # ---------- AGREGACIÓN: recibe polígonos ya creados ----------
    def agregar_figura(self, figura: Poligono) -> None:
        self._inventario.append(figura)

    def inventario(self) -> list[Poligono]:
        return list(self._inventario)                # copia defensiva

    def total_figuras(self) -> int:
        return len(self._inventario)

    # ---------- ASOCIACIÓN: conoce al supervisor, no lo crea -----
    def asignar_supervisor(self, nombre_supervisor: str) -> None:
        self._supervisor = nombre_supervisor

    def supervisor(self) -> str | None:
        return self._supervisor

    def __str__(self) -> str:
        etqs = ", ".join(str(e) for e in self._etiquetas)
        return f"Taller({etqs}, figuras={len(self._inventario)})"


# ============================================================
# PARTE 4 — Contrato Exportable con typing.Protocol
# ============================================================

@runtime_checkable
class Exportable(Protocol):
    """Contrato estructural: cualquier objeto con exportar() -> str lo cumple.

    Por qué Protocol y no ABC: PlanoCAD (libreria_externa.py) no se puede
    modificar. ABC exigiría herencia explícita; Protocol verifica
    estructuralmente sin tocar el código de terceros.
    """

    def exportar(self) -> str: ...


class TrianguloExportable(Triangulo):
    def exportar(self) -> str:
        lados_str = ", ".join(str(l.longitud) for l in self.lados())
        return f"Triangulo[nombre={self._nombre!r}, lados=({lados_str}), area={self.area():.2f}]"


class CuadradoExportable(Cuadrado):
    def exportar(self) -> str:
        lado = self._lados[0].longitud if self._lados else 0
        return f"Cuadrado[nombre={self._nombre!r}, lado={lado}, area={self.area():.2f}]"


class PoligonoRegularExportable(PoligonoRegular):
    def exportar(self) -> str:
        lado = self._lados[0].longitud if self._lados else 0
        return (
            f"PoligonoRegular[nombre={self._nombre!r}, "
            f"n={self._cantidad}, lado={lado}, area={self.area():.2f}]"
        )


def exportar_todos(exportables: list[Exportable]) -> list[str]:
    """Función genérica que trabaja con cualquier Exportable."""
    return [e.exportar() for e in exportables]
