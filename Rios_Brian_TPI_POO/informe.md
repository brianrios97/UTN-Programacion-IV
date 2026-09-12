# Informe — TP Integrador POO en Python

**Alumno:** Ríos, Brian Emanuel | **Cátedra:** Programación IV — UTN

---

## Parte 1 — Los 8 Java-ismos

| # | Java-ismo | Línea(s) | Inversión conceptual | Corrección |
|---|:---|:---|:---|:---|
| 1 | Getters preventivos sin lógica (`getNombre`, `getColor`) | 28–33 | *Consenting adults*: si no hay lógica, el atributo protegido se accede directo | Eliminar; acceso a `_nombre` |
| 2 | getter/setter Bean con lógica (`getLongitud`, `setLongitud`) | 43–49 | Java obliga `setX()`/`getX()`; Python usa `@property` con la misma sintaxis de atributo | `@property longitud` + `@longitud.setter` |
| 3 | Atributo de clase mutable (`catalogo = []`) | 55 | `static` en Java es explícito; en Python es un "static accidental" que crece sin control | Eliminar; no era necesario |
| 4 | Argumentos por defecto mutables (`lados=[]`) | 58 | En Python los defaults se evalúan una vez y se comparten entre llamadas | `lados=None` → `list(lados) if lados is not None else []` |
| 5 | `super().__init__()` omitido | 60–61 | Java lo exige el compilador; Python no, pero sin él el MRO falla en ABC | `super().__init__(nombre, color)` |
| 6 | Alias sin copia defensiva (`self._lados = lados`) | 63 + 84 | El llamador puede mutar el estado interno sin que el objeto lo sepa | `list(lados)` al recibir; `list(self._lados)` al exponer |
| 7 | Bucle acumulador manual | 71–75 | Python idiomático usa `sum()` + expresión generadora: más declarativo | `sum(l.longitud for l in self._lados)` |
| 8 | Sobrecarga de constructor con `isinstance` *(no estaba en el checklist)* | 91–97 | Java no tiene keyword args; Python los tiene nativos → sin ramas `isinstance` | `__init__(nombre="triángulo", color="negro", lados=None)` |

---

## Parte 2 — Taller y Etiqueta

- **Composición** `Taller → Etiqueta`: `Taller.__init__()` crea las `Etiqueta`s internamente. Si el Taller desaparece, sus etiquetas no tienen sentido. `frozen=True` hace a `Etiqueta` inmutable y hashable.
- **Agregación** `Taller → Poligono`: los polígonos se crean fuera y se pasan via `agregar_figura()`. Pueden existir sin el Taller.
- **Asociación** `Taller → supervisor`: referencia débil a un nombre externo; el Taller no crea ni destruye al supervisor.
- **Copia defensiva**: `inventario()` y `etiquetas()` devuelven `list(...)` para proteger el estado interno.

## Parte 3 — ABC y Falla Temprana

`Figura` y `Poligono` pasan a ser `abc.ABC`. `area()` y `lados_esperados()` se declaran `@abstractmethod`: Python lanza `TypeError` al intentar instanciar cualquier subclase que no los implemente. **PoligonoRegular mantiene la herencia**: ES-UN Poligono por dominio y comportamiento, no por truco de compilador.

## Parte 4 — Protocol Exportable

`typing.Protocol` es un contrato **estructural**: si un objeto tiene `exportar() -> str`, cumple el contrato sin heredar. `PlanoCAD` (código de terceros, no modificable) lo satisface automáticamente. Una `ABC` no alcanzaría porque exigiría herencia explícita.
