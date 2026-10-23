from fastapi import APIRouter, Depends, status, Response
from sqlmodel import Session
from app.core.database import get_session
from app.categoria.schema import CategoriaCreate, CategoriaRead, CategoriaUpdate
from app.categoria import service

router = APIRouter(prefix="/categorias", tags=["Categorías"])


@router.get(
    "/",
    response_model=list[CategoriaRead],
    summary="Listar todas las categorías",
)
def listar_categorias(session: Session = Depends(get_session)):
    return service.get_all(session)


@router.get(
    "/{categoria_id}",
    response_model=CategoriaRead,
    summary="Obtener categoría por ID",
)
def obtener_categoria(categoria_id: int, session: Session = Depends(get_session)):
    return service.get_by_id(session, categoria_id)


@router.post(
    "/",
    response_model=CategoriaRead,
    status_code=status.HTTP_201_CREATED,
    summary="Crear una nueva categoría",
)
def crear_categoria(data: CategoriaCreate, session: Session = Depends(get_session)):
    return service.create(session, data)


@router.put(
    "/{categoria_id}",
    response_model=CategoriaRead,
    summary="Actualizar una categoría",
)
def actualizar_categoria(
    categoria_id: int,
    data: CategoriaUpdate,
    session: Session = Depends(get_session),
):
    return service.update(session, categoria_id, data)


@router.delete(
    "/{categoria_id}",
    status_code=status.HTTP_204_NO_CONTENT,
    summary="Eliminar una categoría (Responde 204 No Content)",
)
def eliminar_categoria(
    categoria_id: int, session: Session = Depends(get_session)
):
    service.delete(session, categoria_id)
    return Response(status_code=status.HTTP_204_NO_CONTENT)
