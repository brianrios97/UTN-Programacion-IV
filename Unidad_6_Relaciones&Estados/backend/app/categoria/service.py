from fastapi import HTTPException, status
from sqlmodel import Session, select
from app.categoria.model import Categoria, ProductoCategoria
from app.categoria.schema import CategoriaCreate, CategoriaUpdate


def get_all(session: Session) -> list[Categoria]:
    """Obtiene el listado completo de categorías."""
    statement = select(Categoria)
    return list(session.exec(statement).all())


def get_by_id(session: Session, categoria_id: int) -> Categoria:
    """Busca una categoría por su ID o lanza 404 si no existe."""
    categoria = session.get(Categoria, categoria_id)
    if not categoria:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"Categoría con ID {categoria_id} no encontrada",
        )
    return categoria


def create(session: Session, data: CategoriaCreate) -> Categoria:
    """Crea una nueva categoría validando que el nombre no esté duplicado (409 Conflict)."""
    # 1. Regla de negocio: unicidad del nombre
    existente = session.exec(
        select(Categoria).where(Categoria.nombre == data.nombre)
    ).first()
    if existente:
        raise HTTPException(
            status_code=status.HTTP_409_CONFLICT,
            detail=f"Ya existe una categoría con el nombre '{data.nombre}'",
        )

    # 2. Instanciamos el modelo y persistimos
    db_categoria = Categoria.model_validate(data)
    session.add(db_categoria)
    session.commit()
    session.refresh(db_categoria)
    return db_categoria


def update(session: Session, categoria_id: int, data: CategoriaUpdate) -> Categoria:
    """Actualiza los campos de una categoría existente."""
    db_categoria = get_by_id(session, categoria_id)

    # Si se intenta cambiar el nombre, verificamos que no colisione con otra
    if data.nombre is not None and data.nombre != db_categoria.nombre:
        existente = session.exec(
            select(Categoria).where(Categoria.nombre == data.nombre)
        ).first()
        if existente:
            raise HTTPException(
                status_code=status.HTTP_409_CONFLICT,
                detail=f"Ya existe otra categoría con el nombre '{data.nombre}'",
            )

    # Aplicamos solo los campos enviados
    update_data = data.model_dump(exclude_unset=True)
    for key, value in update_data.items():
        setattr(db_categoria, key, value)

    session.add(db_categoria)
    session.commit()
    session.refresh(db_categoria)
    return db_categoria


def delete(session: Session, categoria_id: int) -> dict[str, str]:
    """Elimina una categoría y limpia sus vínculos en la tabla intermedia."""
    db_categoria = get_by_id(session, categoria_id)

    # Limpiamos las referencias en la tabla intermedia producto_categoria
    links = session.exec(
        select(ProductoCategoria).where(
            ProductoCategoria.categoria_id == categoria_id
        )
    ).all()
    for link in links:
        session.delete(link)

    # Eliminamos la categoría
    session.delete(db_categoria)
    session.commit()
    return {"mensaje": f"Categoría con ID {categoria_id} eliminada con éxito"}
