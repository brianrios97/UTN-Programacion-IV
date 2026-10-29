from typing import List
from fastapi import APIRouter, Depends, HTTPException, Response, status
from sqlmodel import Session
from app.core.database import get_session
from app.core.deps import get_current_active_user, require_role
from app.ingrediente.schema import (
    IngredienteCreate,
    IngredienteRead,
    IngredienteUpdate,
)
from app.ingrediente.service import IngredienteService
from app.modules.usuarios.model import Usuario

router = APIRouter(prefix="/ingredientes", tags=["Ingredientes"])


def get_service(session: Session = Depends(get_session)) -> IngredienteService:
    return IngredienteService(session)


@router.get(
    "/",
    response_model=List[IngredienteRead],
    summary="Listar todos los ingredientes activos (usuario autenticado)",
)
def get_ingredientes(
    service: IngredienteService = Depends(get_service),
    current_user: Usuario = Depends(get_current_active_user),
):
    return service.get_all()


@router.get(
    "/{id}",
    response_model=IngredienteRead,
    summary="Obtener ingrediente por ID (usuario autenticado)",
)
def get_ingrediente_by_id(
    id: int,
    service: IngredienteService = Depends(get_service),
    current_user: Usuario = Depends(get_current_active_user),
):
    ingrediente = service.get_by_id(id)
    if not ingrediente:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"Ingrediente con id {id} no encontrado",
        )
    return ingrediente


@router.post(
    "/",
    response_model=IngredienteRead,
    status_code=status.HTTP_201_CREATED,
    summary="Crear ingrediente (solo admin)",
)
def create_ingrediente(
    data: IngredienteCreate,
    service: IngredienteService = Depends(get_service),
    admin: Usuario = Depends(require_role(["admin"])),
):
    try:
        return service.create(data)
    except ValueError as e:
        raise HTTPException(status_code=status.HTTP_409_CONFLICT, detail=str(e))


@router.put(
    "/{id}",
    response_model=IngredienteRead,
    summary="Actualizar ingrediente (solo admin)",
)
def update_ingrediente(
    id: int,
    data: IngredienteUpdate,
    service: IngredienteService = Depends(get_service),
    admin: Usuario = Depends(require_role(["admin"])),
):
    try:
        updated = service.update(id, data)
        if not updated:
            raise HTTPException(
                status_code=status.HTTP_404_NOT_FOUND,
                detail=f"Ingrediente con id {id} no encontrado",
            )
        return updated
    except ValueError as e:
        raise HTTPException(status_code=status.HTTP_409_CONFLICT, detail=str(e))


@router.delete(
    "/{id}",
    status_code=status.HTTP_204_NO_CONTENT,
    summary="Eliminar lógicamente un ingrediente (solo admin)",
)
def delete_ingrediente(
    id: int,
    service: IngredienteService = Depends(get_service),
    admin: Usuario = Depends(require_role(["admin"])),
):
    deleted = service.delete(id)
    if not deleted:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"Ingrediente con id {id} no encontrado",
        )
    return Response(status_code=status.HTTP_204_NO_CONTENT)
