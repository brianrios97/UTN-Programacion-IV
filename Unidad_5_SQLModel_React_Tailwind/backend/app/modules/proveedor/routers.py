from fastapi import APIRouter, HTTPException, Path, Query, status, Depends
from sqlmodel import Session
from typing import List, Optional
from app.database import get_session
from .models import ProveedorCreate, ProveedorRead
from . import services

router = APIRouter(prefix="/proveedores", tags=["Proveedores"])


# 1. ALTA (POST /proveedores/ -> 201)
@router.post(
    "/", response_model=ProveedorRead, status_code=status.HTTP_201_CREATED,
    summary="Crear un nuevo proveedor"
)
def alta_proveedor(proveedor: ProveedorCreate, session: Session = Depends(get_session)):
    # RN-02: El codigo del proveedor es unico
    existente = services.buscar_por_codigo(session, proveedor.codigo)
    if existente:
        raise HTTPException(
            status_code=status.HTTP_409_CONFLICT,
            detail="El codigo de proveedor ya existe"
        )
    return services.crear(session, proveedor)


# 2. LISTAR (GET /proveedores/ -> 200)
@router.get(
    "/", response_model=List[ProveedorRead], status_code=status.HTTP_200_OK,
    summary="Listar proveedores con paginacion y filtros"
)
def listar_proveedores(
    skip: int = Query(0, ge=0, description="Registros a saltar"),
    limit: int = Query(10, ge=1, le=50, description="Maximo a retornar"),
    activo: Optional[bool] = Query(None, description="Filtrar por estado"),
    session: Session = Depends(get_session),
):
    return services.obtener_todos(session, skip=skip, limit=limit, activo=activo)


# 3. DETALLE (GET /proveedores/{id} -> 200)
@router.get(
    "/{id}", response_model=ProveedorRead, status_code=status.HTTP_200_OK,
    summary="Obtener detalle de un proveedor por ID"
)
def detalle_proveedor(id: int = Path(..., gt=0), session: Session = Depends(get_session)):
    proveedor = services.obtener_por_id(session, id)
    if not proveedor:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Proveedor no encontrado")
    return proveedor


# 4. ACTUALIZAR (PUT /proveedores/{id} -> 200)
@router.put(
    "/{id}", response_model=ProveedorRead, status_code=status.HTTP_200_OK,
    summary="Actualizar todos los campos de un proveedor"
)
def actualizar_proveedor(
    proveedor: ProveedorCreate,
    id: int = Path(..., gt=0),
    session: Session = Depends(get_session),
):
    existente = services.obtener_por_id(session, id)
    if not existente:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Proveedor no encontrado")

    # RN-02: El codigo es unico (otro proveedor no puede tener el mismo codigo)
    proveedor_con_codigo = services.buscar_por_codigo(session, proveedor.codigo)
    if proveedor_con_codigo and proveedor_con_codigo.id != id:
        raise HTTPException(
            status_code=status.HTTP_409_CONFLICT,
            detail="El codigo de proveedor ya pertenece a otro registro"
        )
    return services.actualizar_total(session, id, proveedor)


# 5. BORRADO LOGICO (PUT /proveedores/{id}/desactivar -> 200)
@router.put(
    "/{id}/desactivar", response_model=ProveedorRead, status_code=status.HTTP_200_OK,
    summary="Desactivar proveedor (borrado logico)"
)
def desactivar_proveedor(id: int = Path(..., gt=0), session: Session = Depends(get_session)):
    proveedor = services.obtener_por_id(session, id)
    if not proveedor:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Proveedor no encontrado")

    # RN-05: No se puede desactivar un proveedor ya desactivado
    if not proveedor.activo:
        raise HTTPException(
            status_code=status.HTTP_409_CONFLICT, detail="El proveedor ya esta desactivado"
        )
    return services.desactivar(session, id)
