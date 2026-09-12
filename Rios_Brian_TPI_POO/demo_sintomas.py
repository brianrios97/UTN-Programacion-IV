"""demo_sintomas.py -- Demostracion de 2 sintomas de java-ismos en Python.

Muestra el comportamiento PROBLEMATICO del codigo original y
el comportamiento CORRECTO despues de aplicar las inversiones conceptuales.

Uso:
    python demo_sintomas.py
"""


# ============================================================
# SINTOMA 1: Argumento por defecto mutable (java-ismo #4)
# ============================================================
#
# En Java, cada llamada al constructor crea nuevos objetos.
# En Python, el valor por defecto de lados=[] se evalua UNA sola vez
# y se reutiliza: todas las instancias sin argumento comparten la MISMA lista.

print("=" * 60)
print("SINTOMA 1 -- Argumento por defecto mutable")
print("=" * 60)

# --- Version ROTA (acento de Java) ---
class PoligonoRoto:
    def __init__(self, nombre, lados=[]):   # lados=[] compartido entre llamadas
        self._nombre = nombre
        self._lados = lados                 # alias, no copia


p1 = PoligonoRoto("P1")
p2 = PoligonoRoto("P2")
p1._lados.append("lado_extra")             # mutamos el estado de p1...

print(f"\n[ROTO] p1._lados = {p1._lados}")
print(f"[ROTO] p2._lados = {p2._lados}  <- tambien cambio! (mismo objeto)")
print(f"Son el mismo objeto: {p1._lados is p2._lados}")

# --- Version CORREGIDA ---
class PoligonoCorregido:
    def __init__(self, nombre, lados=None):  # None como centinela
        self._nombre = nombre
        self._lados = list(lados) if lados is not None else []   # copia

c1 = PoligonoCorregido("C1")
c2 = PoligonoCorregido("C2")
c1._lados.append("lado_extra")

print(f"\n[OK]   c1._lados = {c1._lados}")
print(f"[OK]   c2._lados = {c2._lados}  -> no se ve afectado")
print(f"Son el mismo objeto: {c1._lados is c2._lados}")


# ============================================================
# SINTOMA 2: Alias sin copia defensiva en getter (java-ismo #6)
# ============================================================
#
# getLados() del codigo original devuelve la lista interna directamente.
# El llamador puede mutarla sin que el poligono "sepa" nada.

print("\n" + "=" * 60)
print("SINTOMA 2 -- Alias sin copia defensiva en getter")
print("=" * 60)

# --- Version ROTA ---
class PoligonoConGetterRoto:
    def __init__(self, lados):
        self._lados = list(lados)

    def getLados(self):          # expone el estado interno directamente
        return self._lados


roto = PoligonoConGetterRoto([10, 20, 30])
referencia = roto.getLados()    # el llamador obtiene la lista real
referencia.clear()              # y la vacia sin avisar

print(f"\n[ROTO] Poligono creado con 3 lados.")
print(f"[ROTO] Despues de getLados().clear(): {roto.getLados()} <- vacio!")

# --- Version CORREGIDA ---
class PoligonoConGetterOK:
    def __init__(self, lados):
        self._lados = list(lados)

    def lados(self) -> list:     # devuelve una copia nueva cada vez
        return list(self._lados)


ok = PoligonoConGetterOK([10, 20, 30])
copia = ok.lados()
copia.clear()

print(f"\n[OK]   Poligono creado con 3 lados.")
print(f"[OK]   Despues de lados().clear(): {ok.lados()} -> intacto")

print("\n[OK] demo_sintomas.py ejecutado sin errores.")
