from sqlmodel import Session, select
from typing import List, Optional
from .models import Categoria, CategoriaCreate


# 1. Crear categoria (INSERT real en base de datos)
def crear(session: Session, data: CategoriaCreate) -> Categoria:
    db_categoria = Categoria.model_validate(data)
    session.add(db_categoria)
    session.commit()
    session.refresh(db_categoria)
    return db_categoria


# 2. Listar con paginacion (SELECT con OFFSET y LIMIT)
def obtener_todas(session: Session, skip: int = 0, limit: int = 10) -> List[Categoria]:
    query = select(Categoria).offset(skip).limit(limit)
    return list(session.exec(query).all())


# 3. Buscar por ID (SELECT WHERE id = ...)
def obtener_por_id(session: Session, id: int) -> Optional[Categoria]:
    return session.get(Categoria, id)


# 4. Actualizar total (UPDATE)
def actualizar_total(session: Session, id: int, data: CategoriaCreate) -> Optional[Categoria]:
    db_categoria = session.get(Categoria, id)
    if not db_categoria:
        return None
    datos_nuevos = data.model_dump()
    for key, value in datos_nuevos.items():
        setattr(db_categoria, key, value)
    session.add(db_categoria)
    session.commit()
    session.refresh(db_categoria)
    return db_categoria


# 5. Borrado logico (desactivar)
def desactivar(session: Session, id: int) -> Optional[Categoria]:
    db_categoria = session.get(Categoria, id)
    if not db_categoria:
        return None
    db_categoria.activo = False
    session.add(db_categoria)
    session.commit()
    session.refresh(db_categoria)
    return db_categoria
