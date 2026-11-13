from fastapi import APIRouter, HTTPException, Path, Query, status, Depends
from sqlmodel import Session
from typing import List
from app.database import get_session
from .models import CategoriaCreate, CategoriaRead
from . import services

router = APIRouter(prefix="/categorias", tags=["Categorias"])


# 1. ALTA (POST /categorias/ -> 201)
@router.post(
    "/", response_model=CategoriaRead, status_code=status.HTTP_201_CREATED,
    summary="Crear una nueva categoria"
)
def alta_categoria(categoria: CategoriaCreate, session: Session = Depends(get_session)):
    return services.crear(session, categoria)


# 2. LISTAR (GET /categorias/ -> 200)
@router.get(
    "/", response_model=List[CategoriaRead], status_code=status.HTTP_200_OK,
    summary="Listar categorias con paginacion"
)
def listar_categorias(
    skip: int = Query(0, ge=0),
    limit: int = Query(10, le=50),
    session: Session = Depends(get_session),
):
    return services.obtener_todas(session, skip=skip, limit=limit)


# 3. DETALLE (GET /categorias/{id} -> 200)
@router.get(
    "/{id}", response_model=CategoriaRead, status_code=status.HTTP_200_OK,
    summary="Obtener categoria por ID"
)
def detalle_categoria(id: int = Path(..., gt=0), session: Session = Depends(get_session)):
    categoria = services.obtener_por_id(session, id)
    if not categoria:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Categoria no encontrada")
    return categoria


# 4. ACTUALIZAR (PUT /categorias/{id} -> 200)
@router.put(
    "/{id}", response_model=CategoriaRead, status_code=status.HTTP_200_OK,
    summary="Actualizar todos los datos de una categoria"
)
def actualizar_categoria(
    categoria: CategoriaCreate,
    id: int = Path(..., gt=0),
    session: Session = Depends(get_session),
):
    actualizada = services.actualizar_total(session, id, categoria)
    if not actualizada:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Categoria no encontrada")
    return actualizada


# 5. BORRADO LOGICO (PUT /categorias/{id}/desactivar -> 200)
@router.put(
    "/{id}/desactivar", response_model=CategoriaRead, status_code=status.HTTP_200_OK,
    summary="Desactivar categoria (borrado logico)"
)
def borrado_logico(id: int = Path(..., gt=0), session: Session = Depends(get_session)):
    desactivada = services.desactivar(session, id)
    if not desactivada:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Categoria no encontrada")
    return desactivada
