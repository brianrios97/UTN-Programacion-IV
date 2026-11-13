from sqlmodel import Session, select
from typing import List, Optional
from .models import Proveedor, ProveedorCreate


# 1. Crear proveedor (INSERT real en base de datos)
def crear(session: Session, data: ProveedorCreate) -> Proveedor:
    db_proveedor = Proveedor.model_validate(data)
    session.add(db_proveedor)
    session.commit()
    session.refresh(db_proveedor)
    return db_proveedor


# 2. Listar con paginacion y filtro opcional por activo
def obtener_todos(
    session: Session,
    skip: int = 0,
    limit: int = 10,
    activo: Optional[bool] = None,
) -> List[Proveedor]:
    query = select(Proveedor)
    if activo is not None:
        query = query.where(Proveedor.activo == activo)
    query = query.offset(skip).limit(limit)
    return list(session.exec(query).all())


# 3. Buscar por ID
def obtener_por_id(session: Session, id: int) -> Optional[Proveedor]:
    return session.get(Proveedor, id)


# 4. Buscar por codigo (unicidad)
def buscar_por_codigo(session: Session, codigo: str) -> Optional[Proveedor]:
    query = select(Proveedor).where(Proveedor.codigo == codigo)
    return session.exec(query).first()


# 5. Actualizar total (UPDATE)
def actualizar_total(session: Session, id: int, data: ProveedorCreate) -> Optional[Proveedor]:
    db_proveedor = session.get(Proveedor, id)
    if not db_proveedor:
        return None
    datos_nuevos = data.model_dump()
    for key, value in datos_nuevos.items():
        setattr(db_proveedor, key, value)
    session.add(db_proveedor)
    session.commit()
    session.refresh(db_proveedor)
    return db_proveedor


# 6. Borrado logico (desactivar)
def desactivar(session: Session, id: int) -> Optional[Proveedor]:
    db_proveedor = session.get(Proveedor, id)
    if not db_proveedor:
        return None
    db_proveedor.activo = False
    session.add(db_proveedor)
    session.commit()
    session.refresh(db_proveedor)
    return db_proveedor
