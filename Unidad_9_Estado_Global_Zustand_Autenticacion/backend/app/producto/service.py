from fastapi import HTTPException, status
from sqlalchemy.orm import selectinload
from sqlmodel import Session, select
from app.categoria.model import Categoria, ProductoCategoria
from app.producto.model import Producto
from app.producto.schema import ProductoCreate, ProductoUpdate


def get_all(session: Session) -> list[Producto]:
    statement = (
        select(Producto)
        .where(Producto.activo == True)
        .options(selectinload(Producto.categorias))
    )
    return list(session.exec(statement).all())


def get_by_id(session: Session, producto_id: int) -> Producto:
    statement = (
        select(Producto)
        .where(Producto.id == producto_id, Producto.activo == True)
        .options(selectinload(Producto.categorias))
    )
    producto = session.exec(statement).first()
    if not producto:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"Producto con ID {producto_id} no encontrado",
        )
    return producto


def create(session: Session, data: ProductoCreate) -> Producto:
    categoria_ids = data.categoria_ids
    producto_dict = data.model_dump(exclude={"categoria_ids"})

    db_producto = Producto.model_validate(producto_dict)
    db_producto.activo = True

    if categoria_ids:
        for cat_id in categoria_ids:
            cat = session.get(Categoria, cat_id)
            if not cat or not cat.activo:
                raise HTTPException(
                    status_code=status.HTTP_404_NOT_FOUND,
                    detail=f"Categoría con ID {cat_id} no existe",
                )
            db_producto.categorias.append(cat)

    session.add(db_producto)
    session.commit()
    session.refresh(db_producto)
    return db_producto


def update(session: Session, producto_id: int, data: ProductoUpdate) -> Producto:
    db_producto = get_by_id(session, producto_id)

    update_data = data.model_dump(exclude_unset=True, exclude={"categoria_ids"})
    for key, value in update_data.items():
        setattr(db_producto, key, value)

    if data.categoria_ids is not None:
        nuevas_categorias = []
        for cat_id in data.categoria_ids:
            cat = session.get(Categoria, cat_id)
            if not cat or not cat.activo:
                raise HTTPException(
                    status_code=status.HTTP_404_NOT_FOUND,
                    detail=f"Categoría con ID {cat_id} no existe",
                )
            nuevas_categorias.append(cat)
        db_producto.categorias = nuevas_categorias

    session.add(db_producto)
    session.commit()
    session.refresh(db_producto)
    return db_producto


def delete(session: Session, producto_id: int) -> None:
    db_producto = get_by_id(session, producto_id)
    # Borrado lógico: no se elimina de la base, se marca como inactivo (RN-11)
    db_producto.activo = False
    session.add(db_producto)
    session.commit()


def asociar_categoria(
    session: Session, producto_id: int, categoria_id: int
) -> Producto:
    producto = get_by_id(session, producto_id)

    categoria = session.get(Categoria, categoria_id)
    if not categoria or not categoria.activo:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND, detail="Categoría no encontrada"
        )

    link_existente = session.get(ProductoCategoria, (producto_id, categoria_id))
    if link_existente:
        raise HTTPException(
            status_code=status.HTTP_409_CONFLICT,
            detail=f"El producto {producto_id} ya pertenece a la categoría {categoria_id}",
        )

    nuevo_link = ProductoCategoria(
        producto_id=producto_id, categoria_id=categoria_id
    )
    session.add(nuevo_link)
    session.commit()
    return get_by_id(session, producto_id)


def desasociar_categoria(
    session: Session, producto_id: int, categoria_id: int
) -> Producto:
    link = session.get(ProductoCategoria, (producto_id, categoria_id))
    if not link:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="La relación entre este producto y esta categoría no existe",
        )

    session.delete(link)
    session.commit()
    return get_by_id(session, producto_id)
