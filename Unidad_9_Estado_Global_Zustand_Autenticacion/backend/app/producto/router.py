from fastapi import APIRouter, Depends, Response, status
from sqlmodel import Session
from app.core.database import get_session
from app.core.deps import get_current_active_user, require_role
from app.modules.usuarios.model import Usuario
from app.producto import service
from app.producto.schema import (
    ProductoCreate,
    ProductoReadWithCategorias,
    ProductoUpdate,
)

router = APIRouter(prefix="/productos", tags=["Productos"])


@router.get(
    "/",
    response_model=list[ProductoReadWithCategorias],
    summary="Listar todos los productos activos (usuario autenticado)",
)
def listar_productos(
    session: Session = Depends(get_session),
    current_user: Usuario = Depends(get_current_active_user),
):
    return service.get_all(session)


@router.get(
    "/{producto_id}",
    response_model=ProductoReadWithCategorias,
    summary="Obtener producto por ID (usuario autenticado)",
)
def obtener_producto(
    producto_id: int,
    session: Session = Depends(get_session),
    current_user: Usuario = Depends(get_current_active_user),
):
    return service.get_by_id(session, producto_id)


@router.post(
    "/",
    response_model=ProductoReadWithCategorias,
    status_code=status.HTTP_201_CREATED,
    summary="Crear producto (solo admin)",
)
def crear_producto(
    data: ProductoCreate,
    session: Session = Depends(get_session),
    admin: Usuario = Depends(require_role(["admin"])),
):
    return service.create(session, data)


@router.put(
    "/{producto_id}",
    response_model=ProductoReadWithCategorias,
    summary="Actualizar producto (solo admin)",
)
def actualizar_producto(
    producto_id: int,
    data: ProductoUpdate,
    session: Session = Depends(get_session),
    admin: Usuario = Depends(require_role(["admin"])),
):
    return service.update(session, producto_id, data)


@router.delete(
    "/{producto_id}",
    status_code=status.HTTP_204_NO_CONTENT,
    summary="Eliminar lógicamente un producto (solo admin)",
)
def eliminar_producto(
    producto_id: int,
    session: Session = Depends(get_session),
    admin: Usuario = Depends(require_role(["admin"])),
):
    service.delete(session, producto_id)
    return Response(status_code=status.HTTP_204_NO_CONTENT)


@router.post(
    "/{producto_id}/categorias/{categoria_id}",
    response_model=ProductoReadWithCategorias,
    status_code=status.HTTP_201_CREATED,
    summary="Asociar categoría a producto (solo admin)",
)
def asociar_categoria(
    producto_id: int,
    categoria_id: int,
    session: Session = Depends(get_session),
    admin: Usuario = Depends(require_role(["admin"])),
):
    return service.asociar_categoria(session, producto_id, categoria_id)


@router.delete(
    "/{producto_id}/categorias/{categoria_id}",
    response_model=ProductoReadWithCategorias,
    status_code=status.HTTP_200_OK,
    summary="Desasociar categoría de producto (solo admin)",
)
def desasociar_categoria(
    producto_id: int,
    categoria_id: int,
    session: Session = Depends(get_session),
    admin: Usuario = Depends(require_role(["admin"])),
):
    return service.desasociar_categoria(session, producto_id, categoria_id)
