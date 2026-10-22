from fastapi import APIRouter, Depends, status
from sqlmodel import Session
from app.core.database import get_session
from app.producto.schema import (
    ProductoCreate,
    ProductoReadWithCategorias,
    ProductoUpdate,
)
from app.producto import service

router = APIRouter(prefix="/productos", tags=["Productos"])


@router.get(
    "/",
    response_model=list[ProductoReadWithCategorias],
    summary="Listar todos los productos con sus categorías",
)
def listar_productos(session: Session = Depends(get_session)):
    return service.get_all(session)


@router.get(
    "/{producto_id}",
    response_model=ProductoReadWithCategorias,
    summary="Obtener un producto por ID con sus categorías",
)
def obtener_producto(producto_id: int, session: Session = Depends(get_session)):
    return service.get_by_id(session, producto_id)


@router.post(
    "/",
    response_model=ProductoReadWithCategorias,
    status_code=status.HTTP_201_CREATED,
    summary="Crear un nuevo producto",
)
def crear_producto(data: ProductoCreate, session: Session = Depends(get_session)):
    return service.create(session, data)


@router.put(
    "/{producto_id}",
    response_model=ProductoReadWithCategorias,
    summary="Actualizar un producto existente",
)
def actualizar_producto(
    producto_id: int,
    data: ProductoUpdate,
    session: Session = Depends(get_session),
):
    return service.update(session, producto_id, data)


@router.delete(
    "/{producto_id}",
    status_code=status.HTTP_200_OK,
    summary="Eliminar un producto",
)
def eliminar_producto(producto_id: int, session: Session = Depends(get_session)):
    return service.delete(session, producto_id)


# =========================================================================
# ENDPOINTS RELACIONALES N:N (Producto <-> Categoría)
# =========================================================================


@router.post(
    "/{producto_id}/categorias/{categoria_id}",
    response_model=ProductoReadWithCategorias,
    status_code=status.HTTP_201_CREATED,
    summary="Asociar una categoría a un producto (N:N)",
)
def asociar_categoria(
    producto_id: int,
    categoria_id: int,
    session: Session = Depends(get_session),
):
    return service.asociar_categoria(session, producto_id, categoria_id)


@router.delete(
    "/{producto_id}/categorias/{categoria_id}",
    response_model=ProductoReadWithCategorias,
    status_code=status.HTTP_200_OK,
    summary="Desasociar una categoría de un producto",
)
def desasociar_categoria(
    producto_id: int,
    categoria_id: int,
    session: Session = Depends(get_session),
):
    return service.desasociar_categoria(session, producto_id, categoria_id)
