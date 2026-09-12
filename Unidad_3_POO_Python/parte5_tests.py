"""parte5_tests.py — Suite de tests pytest para el TP Integrador POO.

Cómo ejecutar:
    pytest parte5_tests.py -v

Cada test verifica UNA decisión de diseño, no un getter.
"""

from __future__ import annotations

import math

import pytest

from libreria_externa import PlanoCAD
from parte2_taller_etiqueta import Etiqueta, Taller
from parte3_jerarquia import (
    Cuadrado,
    Figura,
    Lado,
    Poligono,
    PoligonoRegular,
    Triangulo,
)
from parte4_exportable import (
    CuadradoExportable,
    Exportable,
    TrianguloExportable,
    exportar_todos,
)


# ---------------------------------------------------------------------------
# Test 1: Falla temprana — Figura y Poligono son abstractos
# ---------------------------------------------------------------------------

class TestFallaTempranaABC:
    """abc.ABC convierte instanciar directamente en TypeError inmediato."""

    def test_figura_no_se_puede_instanciar(self) -> None:
        with pytest.raises(TypeError):
            Figura("test", "rojo")  # type: ignore[abstract]

    def test_poligono_no_se_puede_instanciar(self) -> None:
        with pytest.raises(TypeError):
            Poligono("test", "rojo")  # type: ignore[abstract]


# ---------------------------------------------------------------------------
# Test 2: Copia defensiva
# ---------------------------------------------------------------------------

class TestCopiaDefensiva:
    """Mutar la lista retornada no debe alterar el estado interno."""

    def test_lados_devuelve_copia(self) -> None:
        t = Triangulo(lados=[Lado(3), Lado(4), Lado(5)])
        copia = t.lados()
        copia.append(Lado(99))
        assert len(t.lados()) == 3, "La mutación de la copia no debe afectar al polígono"

    def test_taller_inventario_devuelve_copia(self) -> None:
        taller = Taller("TestTaller", "Rosario")
        taller.agregar_figura(Triangulo(lados=[Lado(3), Lado(4), Lado(5)]))
        inv = taller.inventario()
        inv.clear()
        assert taller.total_figuras() == 1, "Vaciar la copia no debe afectar al inventario"


# ---------------------------------------------------------------------------
# Test 3: Argumento por defecto mutable — java-ismo #4 corregido
# ---------------------------------------------------------------------------

class TestDefaultNoCompartido:
    """Dos instancias sin lados explícitos NO deben compartir la misma lista."""

    def test_triangulos_con_default_no_comparten_lados(self) -> None:
        t1 = Triangulo()
        t2 = Triangulo()
        t1._lados.append(Lado(5))  # mutación directa del estado interno
        assert len(t2.lados()) == 0, "El default mutable corregido: t2 no se ve afectado"


# ---------------------------------------------------------------------------
# Test 4: Protocol Exportable — PlanoCAD cumple sin heredar
# ---------------------------------------------------------------------------

class TestProtocolExportable:
    """typing.Protocol verifica estructuralmente sin requerir herencia."""

    def test_planocad_es_exportable(self) -> None:
        plano = PlanoCAD("B1")
        assert isinstance(plano, Exportable)

    def test_planocad_no_hereda_de_figura(self) -> None:
        assert not issubclass(PlanoCAD, Figura)

    def test_exportar_todos_mezcla_planocad_y_poligonos(self) -> None:
        plano = PlanoCAD("C2", "1:200")
        t = TrianguloExportable(lados=[Lado(3), Lado(4), Lado(5)])
        resultados = exportar_todos([plano, t])
        assert len(resultados) == 2
        assert "PlanoCAD" in resultados[0]
        assert "Triangulo" in resultados[1]


# ---------------------------------------------------------------------------
# Test 5: Etiqueta inmutable — @dataclass(frozen=True)
# ---------------------------------------------------------------------------

class TestEtiquetaInmutable:
    """frozen=True impide cualquier reasignación de atributos."""

    def test_etiqueta_no_se_puede_mutar(self) -> None:
        e = Etiqueta("tipo", "regular")
        with pytest.raises((AttributeError, TypeError)):
            e.valor = "irregular"  # type: ignore[misc]

    def test_etiqueta_es_hashable(self) -> None:
        """frozen=True habilita el hash automático."""
        e1 = Etiqueta("color", "rojo")
        e2 = Etiqueta("color", "rojo")
        assert e1 == e2
        assert hash(e1) == hash(e2)
        assert len({e1, e2}) == 1  # se pueden usar en sets


# ---------------------------------------------------------------------------
# Test 6: Área correcta con fórmulas reales
# ---------------------------------------------------------------------------

class TestAreaCorrecta:
    """Verifica que las implementaciones de area() sean numéricamente correctas."""

    def test_area_triangulo_heron(self) -> None:
        # 3-4-5: área exacta = 6.0
        t = Triangulo(lados=[Lado(3), Lado(4), Lado(5)])
        assert abs(t.area() - 6.0) < 1e-9

    def test_area_cuadrado(self) -> None:
        c = Cuadrado(lados=[Lado(4), Lado(4), Lado(4), Lado(4)])
        assert abs(c.area() - 16.0) < 1e-9

    def test_area_hexagono_regular(self) -> None:
        h = PoligonoRegular("Hexágono", "azul", 2, 6)
        esperado = (6 * 4) / (4 * math.tan(math.pi / 6))
        assert abs(h.area() - esperado) < 1e-9


# ---------------------------------------------------------------------------
# Test 7: Lado rechaza longitudes inválidas
# ---------------------------------------------------------------------------

class TestLadoValidacion:
    """Validación en __init__ de Lado (java-ismo #2 corregido)."""

    def test_lado_rechaza_cero(self) -> None:
        with pytest.raises(ValueError):
            Lado(0)

    def test_lado_rechaza_negativo(self) -> None:
        with pytest.raises(ValueError):
            Lado(-5)

    def test_lado_acepta_positivo(self) -> None:
        l = Lado(3.5)
        assert l.longitud == 3.5
