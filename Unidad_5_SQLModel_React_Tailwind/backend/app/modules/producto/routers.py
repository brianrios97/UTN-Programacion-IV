from fastapi import APIRouter, HTTPException, Path, Query, status, Depends
from sqlmodel import Session
from typing import List
from app.database import get_session
from .models import Producto, ProductoCreate, ProductoRead, ProductoUpdate
from . import services

router = APIRouter(prefix="/productos", tags=["Productos"])


# 1. ALTA DE PRODUCTO (POST /productos/ -> 201)
@router.post(
    "/", response_model=ProductoRead, status_code=status.HTTP_201_CREATED, summary="Crear un nuevo producto"
)
def alta_producto(producto: ProductoCreate, session: Session = Depends(get_session)):
    return services.crear(session, producto)


# 2. LISTAR PRODUCTOS (GET /productos/ -> 200)
@router.get(
    "/", response_model=List[ProductoRead], status_code=status.HTTP_200_OK, summary="Listar productos con paginación"
)
def listar_productos(
    skip: int = Query(0, ge=0),
    limit: int = Query(10, le=50),
    session: Session = Depends(get_session)
):
    return services.obtener_todos(session, skip=skip, limit=limit)


# 3. DETALLE DE PRODUCTO (GET /productos/{id} -> 200)
@router.get(
    "/{id}", response_model=ProductoRead, status_code=status.HTTP_200_OK, summary="Obtener producto por ID"
)
def detalle_producto(id: int = Path(..., gt=0), session: Session = Depends(get_session)):
    producto = services.obtener_por_id(session, id)
    # RN-04: 404 si no existe
    if not producto:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND, detail="Producto no encontrado"
        )
    return producto


# 4. ACTUALIZACIÓN TOTAL (PUT /productos/{id} -> 200)
@router.put(
    "/{id}", response_model=ProductoRead, status_code=status.HTTP_200_OK, summary="Actualizar todos los datos de un producto"
)
def actualizar_producto(
    producto: ProductoCreate,
    id: int = Path(..., gt=0),
    session: Session = Depends(get_session)
):
    # RN-04: 404 si no existe
    actualizado = services.actualizar_total(session, id, producto)
    if not actualizado:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND, detail="Producto no encontrado"
        )
    return actualizado


# 5. BORRADO LÓGICO / DESACTIVAR (PUT /productos/{id}/desactivar -> 200)
@router.put(
    "/{id}/desactivar",
    response_model=ProductoRead,
    status_code=status.HTTP_200_OK,
    summary="Desactivar producto (borrado lógico)"
)
def desactivar_producto(id: int = Path(..., gt=0), session: Session = Depends(get_session)):
    desactivado = services.desactivar(session, id)
    if not desactivado:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND, detail="Producto no encontrado"
        )
    return desactivado


# 6. ELIMINAR FÍSICO (DELETE /productos/{id} -> 200)
@router.delete(
    "/{id}",
    status_code=status.HTTP_200_OK,
    summary="Eliminar producto de la base de datos"
)
def eliminar_producto(id: int = Path(..., gt=0), session: Session = Depends(get_session)):
    # RN-04 y RN-05: Eliminar de base de datos o 404 si no existe
    eliminado = services.eliminar(session, id)
    if not eliminado:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND, detail="Producto no encontrado"
        )
    return {"message": "Producto eliminado exitosamente"}
