# Modelo Final — Diagrama UML

Dominio completo del TP Integrador POO en Python.

```mermaid
classDiagram
    class Figura {
        <<abstract>>
        #_nombre str
        #_color str
        +nombre() str
        +color() str
        +area()* float
    }

    class Lado {
        -_longitud float
        +longitud() float
        +longitud(valor float)
    }

    class Poligono {
        <<abstract>>
        -_lados list
        -_observaciones list
        +lados_esperados()* int
        +area()* float
        +perimetro() float
        +lados() list
        +agregar_observacion(texto)
    }

    class Triangulo {
        +lados_esperados() int
        +area() float
    }

    class Cuadrado {
        +lados_esperados() int
        +area() float
    }

    class PoligonoRegular {
        -_cantidad int
        +lados_esperados() int
        +area() float
    }

    class Etiqueta {
        <<dataclass frozen>>
        +clave str
        +valor str
    }

    class Taller {
        -_nombre str
        -_ciudad str
        -_etiquetas list
        -_inventario list
        -_supervisor str
        +agregar_figura(figura)
        +inventario() list
        +agregar_etiqueta(clave, valor)
        +etiquetas() list
        +asignar_supervisor(nombre)
    }

    class Exportable {
        <<Protocol>>
        +exportar()* str
    }

    class PlanoCAD {
        +identificador str
        +escala str
        +exportar() str
    }

    Figura <|-- Poligono : herencia
    Poligono <|-- Triangulo : herencia
    Poligono <|-- Cuadrado : herencia
    Poligono <|-- PoligonoRegular : herencia
    Poligono "1" *-- "1..*" Lado : composición

    Taller "1" *-- "1..*" Etiqueta : composición
    Taller "1" o-- "0..*" Poligono : agregación
    Taller ..> Taller : asoc. supervisor

    Exportable <.. PlanoCAD : cumple estructuralmente
    Exportable <.. Triangulo : cumple estructuralmente
    Exportable <.. Cuadrado : cumple estructuralmente
```

## Notas del diagrama

| Relación | Tipo | Descripción |
| :--- | :--- | :--- |
| `Figura → Poligono` | Herencia | Poligono extiende Figura abstracta |
| `Poligono → Lado` | Composición | Poligono crea y posee sus Lados |
| `Taller → Etiqueta` | Composición | Taller crea las Etiquetas internamente |
| `Taller → Poligono` | Agregación | Taller recibe polígonos ya creados |
| `Taller → supervisor` | Asociación | Referencia débil a un nombre externo |
| `PlanoCAD → Exportable` | Protocol | Cumple estructuralmente sin heredar |
