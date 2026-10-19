from sqlmodel import Session, select
from typing import List, Optional
from .models import Producto, ProductoCreate, ProductoUpdate


# 1. Crear producto (Persistencia real con INSERT)
def crear(session: Session, data: ProductoCreate) -> Producto:
    db_producto = Producto.model_validate(data)
    session.add(db_producto)
    session.commit()
    session.refresh(db_producto)
    return db_producto


# 2. Listar productos con paginación (SELECT con OFFSET y LIMIT)
def obtener_todos(session: Session, skip: int = 0, limit: int = 10) -> List[Producto]:
    query = select(Producto).offset(skip).limit(limit)
    return list(session.exec(query).all())


# 3. Buscar por ID (SELECT WHERE id = ...)
def obtener_por_id(session: Session, id: int) -> Optional[Producto]:
    return session.get(Producto, id)


# 4. Actualizar producto (UPDATE)
def actualizar_total(session: Session, id: int, data: ProductoCreate) -> Optional[Producto]:
    producto_db = session.get(Producto, id)
    if not producto_db:
        return None

    # Actualizamos los datos del objeto existente
    datos_nuevos = data.model_dump()
    for key, value in datos_nuevos.items():
        setattr(producto_db, key, value)

    session.add(producto_db)
    session.commit()
    session.refresh(producto_db)
    return producto_db


# 5. Borrado lógico (Desactivar)
def desactivar(session: Session, id: int) -> Optional[Producto]:
    producto_db = session.get(Producto, id)
    if not producto_db:
        return None

    producto_db.activo = False
    session.add(producto_db)
    session.commit()
    session.refresh(producto_db)
    return producto_db


# 6. Eliminar físico (DELETE FROM producto WHERE id = ...)
def eliminar(session: Session, id: int) -> bool:
    producto_db = session.get(Producto, id)
    if not producto_db:
        return False

    session.delete(producto_db)
    session.commit()
    return True
