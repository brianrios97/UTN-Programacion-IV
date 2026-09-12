"""main.py — Demo ejecutable del dominio completo.

Corre sin errores y muestra el inventario del Taller.

Uso:
    python main.py
"""

from figuras import (
    CuadradoExportable,
    Etiqueta,
    Lado,
    PoligonoRegular,
    PoligonoRegularExportable,
    Taller,
    TrianguloExportable,
    exportar_todos,
)
from libreria_externa import PlanoCAD


def main() -> None:
    # --- Crear el Taller (composición + asociación) ---
    taller = Taller("Geometrix", "Córdoba")
    taller.asignar_supervisor("Prof. García")
    taller.agregar_etiqueta("tipo", "didáctico")

    # --- Crear figuras y agregarlas (agregación) ---
    t = TrianguloExportable("Triángulo rojo", "rojo", [Lado(3), Lado(4), Lado(5)])
    c = CuadradoExportable("Cuadrado azul", "azul", [Lado(6), Lado(6), Lado(6), Lado(6)])
    r = PoligonoRegularExportable("Hexágono verde", "verde", 3, 6)

    taller.agregar_figura(t)
    taller.agregar_figura(c)
    taller.agregar_figura(r)

    # --- Mostrar inventario ---
    print("=" * 50)
    print(f"  {taller}")
    print(f"  Supervisor: {taller.supervisor()}")
    print("=" * 50)
    print("\n[=] Inventario del Taller:\n")
    for fig in taller.inventario():
        print(f"  {fig}")
        print(f"    perimetro = {fig.perimetro():.2f}")
        print(f"    area      = {fig.area():.4f}")

    # --- Exportar con Protocol ---
    plano = PlanoCAD("A3-001", "1:50")
    exportables = [t, c, r, plano]

    print("\n[>] Exportacion (Protocol Exportable):\n")
    for resultado in exportar_todos(exportables):
        print(f"  {resultado}")

    # --- Mostrar etiquetas ---
    print("\n[i] Etiquetas del Taller:\n")
    for e in taller.etiquetas():
        print(f"  {e}")

    print("\n[OK] main.py ejecutado sin errores.")


if __name__ == "__main__":
    main()
