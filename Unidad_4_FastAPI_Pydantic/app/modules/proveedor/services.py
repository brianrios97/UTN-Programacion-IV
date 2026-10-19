from typing import List, Optional
from .schemas import ProveedorCreate, ProveedorRead, ProveedorUpdate

# "Base de datos" en memoria
db_proveedores: List[ProveedorRead] = []
id_counter = 1

def buscar_por_codigo(codigo: str) -> Optional[ProveedorRead]:
    for p in db_proveedores:
        if p.codigo == codigo:
            return p
    return None


def crear(data: ProveedorCreate) -> ProveedorRead:
    global id_counter
    nuevo = ProveedorRead(id=id_counter, **data.model_dump())
    db_proveedores.append(nuevo)
    id_counter += 1
    return nuevo

def obtener_por_id(id: int) -> Optional[ProveedorRead]:
    for p in db_proveedores:
        if p.id == id:
            return p
    return None

def obtener_todos(skip: int = 0, limit: int = 10, activo: Optional[bool] = None) -> List[ProveedorRead]:
    resultado = db_proveedores

    # Si nos pidieron filtrar por activo (True o False)
    if activo is not None:
        resultado = [p for p in resultado if p.activo == activo]

    # Aplicamos paginación usando "slicing" (rebanado) de Python
    return resultado[skip : skip + limit]

def actualizar_total(id: int, data: ProveedorCreate) -> Optional[ProveedorRead]:
    for index, p in enumerate(db_proveedores):
        if p.id == id:
            actualizado = ProveedorRead(id=id, **data.model_dump())
            db_proveedores[index] = actualizado
            return actualizado
    return None


def desactivar(id: int) -> Optional[ProveedorRead]:
    for index, p in enumerate(db_proveedores):
        if p.id == id:
            p_dict = p.model_dump()
            p_dict["activo"] = False
            actualizado = ProveedorRead(**p_dict)
            db_proveedores[index] = actualizado
            return actualizado
    return None
