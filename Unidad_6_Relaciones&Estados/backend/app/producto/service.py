
from fastapi import HTTPException, status
from sqlalchemy.orm import selectinload
from sqlmodel import Session, select
from app.categoria.model import Categoria, ProductoCategoria
from app.producto.model import Producto
from app.producto.schema import ProductoCreate, ProductoUpdate


def get_all(session: Session) -> list[Producto]:
    """Obtiene todos los productos cargando anticipadamente sus categorías (Eager Loading)."""
    statement = select(Producto).options(selectinload(Producto.categorias))
    return list(session.exec(statement).all())


def get_by_id(session: Session, producto_id: int) -> Producto:
    """Busca un producto por su ID incluyendo sus categorías asociadas o lanza 404."""
    statement = (
        select(Producto)
        .where(Producto.id == producto_id)
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
    """Crea un nuevo producto y asocia las categorías indicadas en categoria_ids."""
    # 1. Separamos los IDs de categorías para tratarlos relacionalmente
    categoria_ids = data.categoria_ids
    producto_dict = data.model_dump(exclude={"categoria_ids"})

    db_producto = Producto.model_validate(producto_dict)

    # 2. Validamos que cada categoría solicitada realmente exista en la DB
    if categoria_ids:
        for cat_id in categoria_ids:
            cat = session.get(Categoria, cat_id)
            if not cat:
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
    """Actualiza los campos de un producto y sus asociaciones de categorías si se especifican."""
    db_producto = get_by_id(session, producto_id)

    # 1. Actualizamos campos escalares
    update_data = data.model_dump(exclude_unset=True, exclude={"categoria_ids"})
    for key, value in update_data.items():
        setattr(db_producto, key, value)

    # 2. Si se envió una nueva lista de categorías, reemplazamos las relaciones
    if data.categoria_ids is not None:
        nuevas_categorias = []
        for cat_id in data.categoria_ids:
            cat = session.get(Categoria, cat_id)
            if not cat:
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


def delete(session: Session, producto_id: int) -> dict[str, str]:
    """Elimina un producto y sus asociaciones intermedias."""
    db_producto = get_by_id(session, producto_id)

    # Limpiamos los registros en la tabla intermedia
    links = session.exec(
        select(ProductoCategoria).where(
            ProductoCategoria.producto_id == producto_id
        )
    ).all()
    for link in links:
        session.delete(link)

    session.delete(db_producto)
    session.commit()
    return {"mensaje": f"Producto con ID {producto_id} eliminado correctamente"}


# =========================================================================
# OPERACIONES ESPECÍFICAS DE LA TABLA INTERMEDIA (Producto_Categoria)
# =========================================================================


def asociar_categoria(
    session: Session, producto_id: int, categoria_id: int
) -> Producto:
    """Vincula un producto a una categoría creando un registro en producto_categoria."""
    # 1. Validar existencia de ambas entidades
    producto = session.get(Producto, producto_id)
    if not producto:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND, detail="Producto no encontrado"
        )

    categoria = session.get(Categoria, categoria_id)
    if not categoria:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND, detail="Categoría no encontrada"
        )

    # 2. Validar que no esté ya asociada (409 Conflict)
    link_existente = session.get(ProductoCategoria, (producto_id, categoria_id))
    if link_existente:
        raise HTTPException(
            status_code=status.HTTP_409_CONFLICT,
            detail=f"El producto {producto_id} ya pertenece a la categoría {categoria_id}",
        )

    # 3. Insertar en la tabla intermedia
    nuevo_link = ProductoCategoria(
        producto_id=producto_id, categoria_id=categoria_id
    )
    session.add(nuevo_link)
    session.commit()
    return get_by_id(session, producto_id)


def desasociar_categoria(
    session: Session, producto_id: int, categoria_id: int
) -> Producto:
    """Elimina la vinculación entre un producto y una categoría."""
    link = session.get(ProductoCategoria, (producto_id, categoria_id))
    if not link:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="La relación entre este producto y esta categoría no existe",
        )

    session.delete(link)
    session.commit()
    return get_by_id(session, producto_id)
