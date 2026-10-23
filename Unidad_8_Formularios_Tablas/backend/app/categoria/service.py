from fastapi import HTTPException, status
from sqlmodel import Session, select
from app.categoria.model import Categoria
from app.categoria.schema import CategoriaCreate, CategoriaUpdate


def get_all(session: Session) -> list[Categoria]:
    statement = select(Categoria)
    return list(session.exec(statement).all())


def get_by_id(session: Session, categoria_id: int) -> Categoria:
    categoria = session.get(Categoria, categoria_id)
    if not categoria:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"Categoría con ID {categoria_id} no encontrada",
        )
    return categoria


def create(session: Session, data: CategoriaCreate) -> Categoria:
    existente = session.exec(
        select(Categoria).where(Categoria.nombre == data.nombre)
    ).first()
    if existente:
        raise HTTPException(
            status_code=status.HTTP_409_CONFLICT,
            detail=f"Ya existe una categoría con el nombre '{data.nombre}'",
        )

    db_categoria = Categoria.model_validate(data)
    session.add(db_categoria)
    session.commit()
    session.refresh(db_categoria)
    return db_categoria


def update(session: Session, categoria_id: int, data: CategoriaUpdate) -> Categoria:
    db_categoria = get_by_id(session, categoria_id)

    if data.nombre is not None and data.nombre != db_categoria.nombre:
        existente = session.exec(
            select(Categoria).where(Categoria.nombre == data.nombre)
        ).first()
        if existente:
            raise HTTPException(
                status_code=status.HTTP_409_CONFLICT,
                detail=f"Ya existe otra categoría con el nombre '{data.nombre}'",
            )

    update_data = data.model_dump(exclude_unset=True)
    for key, value in update_data.items():
        setattr(db_categoria, key, value)

    session.add(db_categoria)
    session.commit()
    session.refresh(db_categoria)
    return db_categoria


def delete(session: Session, categoria_id: int) -> None:
    db_categoria = get_by_id(session, categoria_id)
    # Limpiamos las asociaciones en la tabla intermedia mediante el ORM
    db_categoria.productos.clear()
    session.delete(db_categoria)
    session.commit()
