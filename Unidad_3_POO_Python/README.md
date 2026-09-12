# Unidad 3: Programación Orientada a Objetos en Python 🐍

**Tecnicatura Universitaria en Programación — Universidad Tecnológica Nacional (UTN)**
**Cátedra:** Programación IV
**Repositorio:** [https://github.com/brianrios97/UTN-Programacion-IV](https://github.com/brianrios97/UTN-Programacion-IV)

---

## 📌 Objetivo

Transformar un módulo escrito con *acento de Java* en Python idiomático, aplicando:

- Encapsulamiento por convención (`_` vs `__`) y `@property`
- Relaciones estructurales: **composición**, **agregación** y **asociación**
- Herencia justificada por dominio
- Contratos con `abc.ABC` / `@abstractmethod` y `typing.Protocol`
- Suite de tests con `pytest`
- Diagrama UML en Mermaid

---

## 📂 Estructura del Proyecto

```
Unidad_3_POO_Python/
├── libreria_externa.py          # Clase PlanoCAD de terceros — NO modificar
├── parte1_corregido.py          # Parte 1: los 8 java-ismos corregidos
├── parte2_taller_etiqueta.py    # Parte 2: Taller + Etiqueta con relaciones OO
├── parte3_jerarquia.py          # Parte 3: jerarquía con abc.ABC y falla temprana
├── parte4_exportable.py         # Parte 4: contrato Exportable con typing.Protocol
├── parte5_tests.py              # Parte 5: suite de 7 tests con pytest
├── informe.md                   # Diagnóstico, decisiones de diseño y UML
└── README.md                    # Este archivo
```

---

## 🚀 Cómo ejecutar

### Requisitos

```bash
pip install pytest mypy
```

### Ejecutar cada módulo

```bash
python parte1_corregido.py
python parte2_taller_etiqueta.py
python parte3_jerarquia.py
python parte4_exportable.py
```

### Ejecutar los tests

```bash
pytest parte5_tests.py -v
```

### Verificación de tipos estáticos (mypy estricto)

```bash
mypy parte4_exportable.py --strict
```

---

## 🛠️ Tecnologías

| Componente | Detalle |
| :--- | :--- |
| Lenguaje | Python 3.12+ |
| Testing | pytest |
| Tipado estático | mypy (modo `--strict`) |
| Contratos abstractos | `abc.ABC`, `@abstractmethod` |
| Contrato estructural | `typing.Protocol` |
| Valor inmutable | `@dataclass(frozen=True)` |
| Documentación UML | Mermaid (en `informe.md`) |
