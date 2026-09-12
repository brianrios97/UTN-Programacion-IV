"""parte1_corregido.py — El dominio Figura / Polígono / Lado, corregido.

Los 8 java-ismos del módulo de partida eliminados:

  1. Getters preventivos sin lógica  → acceso directo al atributo protegido.
  2. getter/setter Bean              → @property + @longitud.setter con validación.
  3. Atributo de clase mutable       → catalogo = [] eliminado del cuerpo de clase.
  4. Argumentos por defecto mutables → None + list() dentro del cuerpo.
  5. super().__init__() omitido      → llamada explícita a super().
  6. Alias sin copia defensiva       → list(lados) al recibir; list() al devolver.
  7. Bucle acumulador manual         → sum() con expresión generadora.
  8. Sobrecarga de constructor       → __init__ con keyword args y defaults.

Ruido sintáctico también limpiado (punto y coma, == True, + en lugar de f-string,
type hint mentiroso -> int que retornaba str).

Nota: area() sigue siendo concreta aquí. La conversión a @abstractmethod
(falla temprana) se aplica en la Parte 3 al introducir abc.ABC.
"""

import math


class Figura:
    def __init__(self, nombre: str, color: str) -> None:
        self._nombre = nombre
        self._color = color
        # Java-ismo #1 eliminado: sin getNombre() ni getColor() como métodos.
        # El atributo _nombre es accesible desde subclases; si se necesita
        # lógica en el acceso, se agrega @property en ese momento.

    def area(self) -> float:
        return 0.0


class Lado:
    def __init__(self, longitud: float) -> None:
        # Validación también en __init__ para que el objeto nazca consistente.
        if longitud <= 0:
            raise ValueError("La longitud debe ser positiva")
        self._longitud = longitud

    @property                                  # Java-ismo #2: @property reemplaza getLongitud()
    def longitud(self) -> float:
        return self._longitud

    @longitud.setter                           # Java-ismo #2: setter reemplaza setLongitud()
    def longitud(self, valor: float) -> None:
        if valor <= 0:
            raise ValueError("La longitud debe ser positiva")
        self._longitud = valor

    def __repr__(self) -> str:
        return f"Lado({self._longitud})"


class Poligono(Figura):
    # Java-ismo #3 eliminado: sin catalogo = [] como atributo de clase mutable.

    def __init__(
        self,
        nombre: str,
        color: str,
        lados: list[Lado] | None = None,          # Java-ismo #4: None en vez de []
        observaciones: list[str] | None = None,   # Java-ismo #4
    ) -> None:
        super().__init__(nombre, color)            # Java-ismo #5: super() correcto
        # Java-ismo #6: copia defensiva al recibir la colección
        self._lados: list[Lado] = list(lados) if lados is not None else []
        self._observaciones: list[str] = list(observaciones) if observaciones is not None else []

    def lados_esperados(self) -> int:
        return 0

    def perimetro(self) -> float:
        return sum(lado.longitud for lado in self._lados)  # Java-ismo #7: sum + generator

    def area(self) -> float:
        return 0.0

    def agregar_observacion(self, texto: str) -> None:
        self._observaciones.append(texto)

    def lados(self) -> list[Lado]:
        return list(self._lados)                   # Java-ismo #6: copia defensiva al exponer


class Triangulo(Poligono):
    # Java-ismo #8: constructor simple con keyword args, sin ramas isinstance.
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
        a = self._lados[0].longitud
        b = self._lados[1].longitud
        c = self._lados[2].longitud
        s = (a + b + c) / 2
        return math.sqrt(s * (s - a) * (s - b) * (s - c))


class Cuadrado(Poligono):
    # Java-ismo #8: constructor simple con keyword args.
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
    """Polígono de N lados de igual longitud.

    La decisión sobre si esta herencia es necesaria en Python se toma en la Parte 3.
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
    activo = True
    if activo:                                                              # ruido: == True
        t = Triangulo("Triángulo", "rojo", [Lado(3), Lado(4), Lado(5)])   # ruido: ;
        c = Cuadrado("Cuadrado", "azul", [Lado(2), Lado(2), Lado(2), Lado(2)])
        print(f"Perímetro del triángulo: {t.perimetro()}")                 # ruido: +
        print(f"Perímetro del cuadrado:  {c.perimetro()}")
        t.agregar_observacion("revisar el vértice A")
        r = PoligonoRegular("Pentágono", "verde", 4, 5)
        print(f"Perímetro del pentágono: {r.perimetro()}")
        print(f"Área del pentágono:      {r.area():.2f}")
