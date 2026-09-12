# TP Integrador — Programación Orientada a Objetos en Python

**Alumno:** Ríos, Brian Emanuel
**Cátedra:** Programación IV — UTN
**Repositorio:** [https://github.com/brianrios97/UTN-Programacion-IV](https://github.com/brianrios97/UTN-Programacion-IV)

---

## Archivos del proyecto

| Archivo | Descripción |
| :--- | :--- |
| `figuras.py` | Dominio completo (Partes 1 a 4): `Figura`, `Lado`, `Poligono`, `Triangulo`, `Cuadrado`, `PoligonoRegular`, `Etiqueta`, `Taller`, `Exportable` y subclases exportables |
| `parte1_diagnostico.py` | Código de partida entregado por la cátedra, ya corregido con los 8 java-ismos |
| `demo_sintomas.py` | Demostración de 2 síntomas del código original (argumento mutable y alias sin copia) |
| `libreria_externa.py` | Clase `PlanoCAD` de terceros — **NO modificada** |
| `main.py` | Demo ejecutable: crea un `Taller` con figuras, muestra inventario y exportaciones |
| `informe.md` | Diagnóstico de los 8 java-ismos y análisis de decisiones de diseño (máx. 1 carilla) |
| `uml/modelo_final.md` | Diagrama de clases en Mermaid con todas las relaciones del dominio |

---

## Cómo ejecutar

```bash
python main.py           # corre sin errores y muestra el inventario
python demo_sintomas.py  # muestra los 2 síntomas de la Parte 1
```

---

## Conceptos aplicados

| Concepto | Dónde |
| :--- | :--- |
| `@property` + `@setter` | `Lado.longitud` en `figuras.py` |
| `abc.ABC` + `@abstractmethod` | `Figura` y `Poligono` en `figuras.py` |
| `@dataclass(frozen=True)` | `Etiqueta` en `figuras.py` |
| Composición | `Taller` → `Etiqueta` |
| Agregación | `Taller` → `Poligono` |
| Asociación | `Taller` → supervisor |
| `typing.Protocol` | `Exportable` en `figuras.py` |
| Copia defensiva | `Taller.inventario()`, `Poligono.lados()` |
