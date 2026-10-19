from fastapi import APIRouter, HTTPException, Path, Query, status
from typing import List, Optional
from . import schemas, services

router = APIRouter(prefix="/proveedores", tags=["Proveedores"])


@router.post(
    "/",
    response_model=schemas.ProveedorRead,
    status_code=status.HTTP_201_CREATED,
    summary="Crear un nuevo proveedor"
)
def alta_proveedor(proveedor: schemas.ProveedorCreate):
    # RN-02: El código del proveedor es único
    existente = services.buscar_por_codigo(proveedor.codigo)
    if existente:
        raise HTTPException(
            status_code=status.HTTP_409_CONFLICT,
            detail="El código de proveedor ya existe"
        )
    return services.crear(proveedor)


@router.get(
    "/",
    response_model=List[schemas.ProveedorRead],
    status_code=status.HTTP_200_OK,
    summary="Listar proveedores con paginación y filtros"
)
def listar_proveedores(
    skip: int = Query(0, ge=0, description="Cantidad de registros a saltar"),
    limit: int = Query(10, ge=1, le=50, description="Cantidad máxima a retornar"),
    activo: Optional[bool] = Query(None, description="Filtrar por estado (True=activos, False=inactivos)")
):
    return services.obtener_todos(skip=skip, limit=limit, activo=activo)


@router.get(
    "/{id}",
    response_model=schemas.ProveedorRead,
    status_code=status.HTTP_200_OK,
    summary="Obtener detalle de un proveedor por ID"
)
def detalle_proveedor(id: int = Path(..., gt=0, description="ID del proveedor")):
    proveedor = services.obtener_por_id(id)
    # RN-04: No se puede consultar un proveedor cuyo id no exista
    if not proveedor:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Proveedor no encontrado"
        )
    return proveedor


@router.put(
    "/{id}",
    response_model=schemas.ProveedorRead,
    status_code=status.HTTP_200_OK,
    summary="Actualizar todos los campos de un proveedor"
)
def actualizar_proveedor(
    proveedor: schemas.ProveedorCreate,
    id: int = Path(..., gt=0, description="ID del proveedor a actualizar")
):
    # RN-04: No se puede actualizar un proveedor cuyo id no exista
    existente = services.obtener_por_id(id)
    if not existente:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Proveedor no encontrado"
        )

    # RN-02: El código es único (verificar si otro proveedor ya usa el nuevo código)
    proveedor_con_codigo = services.buscar_por_codigo(proveedor.codigo)
    if proveedor_con_codigo and proveedor_con_codigo.id != id:
        raise HTTPException(
            status_code=status.HTTP_409_CONFLICT,
            detail="El código de proveedor ya pertenece a otro registro"
        )

    return services.actualizar_total(id, proveedor)


@router.put(
    "/{id}/desactivar",
    response_model=schemas.ProveedorRead,
    status_code=status.HTTP_200_OK,
    summary="Desactivar (borrado lógico) un proveedor"
)
def desactivar_proveedor(id: int = Path(..., gt=0, description="ID del proveedor a desactivar")):
    # RN-04: No se puede desactivar un proveedor cuyo id no exista
    proveedor = services.obtener_por_id(id)
    if not proveedor:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Proveedor no encontrado"
        )

    # RN-05: No se puede desactivar un proveedor que ya está desactivado
    if not proveedor.activo:
        raise HTTPException(
            status_code=status.HTTP_409_CONFLICT,
            detail="El proveedor ya está desactivado"
        )

    return services.desactivar(id)
