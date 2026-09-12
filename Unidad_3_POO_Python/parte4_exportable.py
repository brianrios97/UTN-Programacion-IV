"""parte4_exportable.py — Contrato Exportable con typing.Protocol.

Por qué Protocol y no ABC:

  ABC exige herencia explícita. Para que PlanoCAD (de libreria_externa.py)
  cumpla una ABC, habría que modificar su código o crear un adaptador que
  herede de ella: ambas opciones son invasivas o agregan indirección innecesaria.

  typing.Protocol verifica ESTRUCTURALMENTE: si un objeto tiene el método
  exportar() con la firma correcta, cumple el contrato, sin importar su
  árbol de herencia. PlanoCAD ya tiene exportar() -> str; con Protocol
  lo satisface de forma natural sin ningún cambio en su código.

  Resumen:
    ABC  → «declarás que cumplís» (nominal subtyping)
    Protocol → «demostrás que cumplís» (structural subtyping)

Verificación de tipos estáticos:
    mypy parte4_exportable.py --strict
"""

from __future__ import annotations

from typing import Protocol, runtime_checkable

from libreria_externa import PlanoCAD
from parte3_jerarquia import Cuadrado, Lado, PoligonoRegular, Triangulo


@runtime_checkable
class Exportable(Protocol):
    """Contrato estructural: cualquier objeto con exportar() -> str lo cumple."""

    def exportar(self) -> str:
        """Serializa el objeto en una cadena de texto."""
        ...


# ---------------------------------------------------------------------------
# Subclases de los polígonos propios que cumplen Exportable
# ---------------------------------------------------------------------------

class TrianguloExportable(Triangulo):
    """Triángulo que además satisface el contrato Exportable."""

    def exportar(self) -> str:
        lados_str = ", ".join(str(l.longitud) for l in self.lados())
        return (
            f"Triangulo[nombre={self._nombre!r}, "
            f"lados=({lados_str}), area={self.area():.2f}]"
        )


class CuadradoExportable(Cuadrado):
    """Cuadrado que además satisface el contrato Exportable."""

    def exportar(self) -> str:
        lado = self._lados[0].longitud if self._lados else 0
        return (
            f"Cuadrado[nombre={self._nombre!r}, "
            f"lado={lado}, area={self.area():.2f}]"
        )


class PoligonoRegularExportable(PoligonoRegular):
    """PoligonoRegular que además satisface el contrato Exportable."""

    def exportar(self) -> str:
        lado = self._lados[0].longitud if self._lados else 0
        return (
            f"PoligonoRegular[nombre={self._nombre!r}, "
            f"n={self._cantidad}, lado={lado}, area={self.area():.2f}]"
        )


# ---------------------------------------------------------------------------
# Función genérica que trabaja con cualquier Exportable
# ---------------------------------------------------------------------------

def exportar_todos(exportables: list[Exportable]) -> list[str]:
    """Serializa todos los objetos exportables sin importar su tipo concreto."""
    return [e.exportar() for e in exportables]


if __name__ == "__main__":
    # PlanoCAD cumple Exportable sin heredar de ninguna clase propia
    plano = PlanoCAD("A3-001", "1:50")
    assert isinstance(plano, Exportable), "PlanoCAD debe cumplir Exportable"
    print(f"✅ PlanoCAD cumple Exportable: {plano.exportar()}")

    t = TrianguloExportable(lados=[Lado(3), Lado(4), Lado(5)])
    c = CuadradoExportable(lados=[Lado(7), Lado(7), Lado(7), Lado(7)])
    r = PoligonoRegularExportable("Hexágono", "verde", 4, 6)

    exportables: list[Exportable] = [plano, t, c, r]

    print("\n--- Exportación de todos ---")
    for resultado in exportar_todos(exportables):
        print(f"  {resultado}")
