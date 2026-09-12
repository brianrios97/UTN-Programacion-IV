"""parte2_taller_etiqueta.py — Clases Taller y Etiqueta con relaciones OO.

Relaciones implementadas:

  COMPOSICIÓN (Taller ──*── Etiqueta):
    Taller *crea* Etiquetas internamente en __init__ y en agregar_etiqueta().
    Si el Taller deja de existir, sus Etiquetas no tienen sentido fuera de él.
    Multiplicidad: 1 Taller tiene 1..* Etiquetas.

  AGREGACIÓN (Taller ──o── Poligono):
    Taller *recibe* polígonos ya creados mediante agregar_figura(). Los polígonos
    pueden existir sin el Taller y son creados externamente.
    Multiplicidad: 1 Taller tiene 0..* Polígonos.
    Copia defensiva en inventario(): el llamador no puede mutar el estado interno.

  ASOCIACIÓN (Taller ──── supervisor: str):
    Taller *conoce* el nombre del supervisor pero no lo crea ni lo destruye.
    Relación débil y temporal: puede cambiar o ser None.
"""

from __future__ import annotations

from dataclasses import dataclass

from parte3_jerarquia import Lado, Poligono


@dataclass(frozen=True)
class Etiqueta:
    """Par clave-valor inmutable.

    frozen=True:
      - impide la reasignación de atributos post-construcción (AttributeError).
      - habilita el hash automático → se puede usar en sets y como clave de dict.
    """

    clave: str
    valor: str

    def __str__(self) -> str:
        return f"{self.clave}={self.valor}"


class Taller:
    """Taller de geometría que gestiona polígonos y sus etiquetas descriptivas."""

    def __init__(self, nombre: str, ciudad: str) -> None:
        self._nombre = nombre
        self._ciudad = ciudad

        # COMPOSICIÓN: Taller crea las Etiquetas; ellas no existen fuera del Taller.
        self._etiquetas: list[Etiqueta] = [
            Etiqueta("nombre", nombre),
            Etiqueta("ciudad", ciudad),
        ]

        # AGREGACIÓN: los polígonos se agregan desde afuera y pueden existir sin el Taller.
        self._inventario: list[Poligono] = []

        # ASOCIACIÓN: referencia débil; el Taller conoce pero no crea ni destruye al supervisor.
        self._supervisor: str | None = None

    # ---------- propiedades simples ----------

    @property
    def nombre(self) -> str:
        return self._nombre

    @property
    def ciudad(self) -> str:
        return self._ciudad

    # ---------- gestión de etiquetas (COMPOSICIÓN) ----------

    def agregar_etiqueta(self, clave: str, valor: str) -> None:
        """Taller crea la Etiqueta internamente → composición."""
        self._etiquetas.append(Etiqueta(clave, valor))

    def etiquetas(self) -> list[Etiqueta]:
        """Copia defensiva: el llamador no puede mutar la lista interna."""
        return list(self._etiquetas)

    # ---------- gestión de inventario (AGREGACIÓN) ----------

    def agregar_figura(self, figura: Poligono) -> None:
        """Recibe una figura ya creada → agregación."""
        self._inventario.append(figura)

    def inventario(self) -> list[Poligono]:
        """Copia defensiva: devuelve una lista nueva, no la referencia interna."""
        return list(self._inventario)

    def total_figuras(self) -> int:
        return len(self._inventario)

    # ---------- gestión del supervisor (ASOCIACIÓN) ----------

    def asignar_supervisor(self, nombre_supervisor: str) -> None:
        """Asociación: conoce al supervisor por nombre, no lo crea ni lo destruye."""
        self._supervisor = nombre_supervisor

    def supervisor(self) -> str | None:
        return self._supervisor

    def __str__(self) -> str:
        etqs = ", ".join(str(e) for e in self._etiquetas)
        return f"Taller({etqs}, figuras={len(self._inventario)})"


if __name__ == "__main__":
    from parte3_jerarquia import Triangulo, Cuadrado

    taller = Taller("Geometrix", "Córdoba")
    taller.agregar_etiqueta("tipo", "didáctico")
    taller.asignar_supervisor("Prof. García")

    t = Triangulo(lados=[Lado(3), Lado(4), Lado(5)])
    c = Cuadrado(lados=[Lado(5), Lado(5), Lado(5), Lado(5)])
    taller.agregar_figura(t)
    taller.agregar_figura(c)

    print(taller)
    print(f"Inventario: {taller.total_figuras()} figuras")
    print(f"Supervisor: {taller.supervisor()}")

    # Verificar copia defensiva
    inv = taller.inventario()
    inv.clear()
    assert taller.total_figuras() == 2, "La copia defensiva debe proteger el inventario."
    print("✅ Copia defensiva en inventario() verificada.")

    # Verificar que Etiqueta es inmutable
    e = Etiqueta("color", "rojo")
    try:
        e.valor = "azul"  # type: ignore[misc]
    except AttributeError:
        print("✅ Etiqueta es inmutable (frozen=True).")
