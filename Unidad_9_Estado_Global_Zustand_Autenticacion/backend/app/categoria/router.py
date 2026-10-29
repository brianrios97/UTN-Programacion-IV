from fastapi import APIRouter, Depends, Response, status
from sqlmodel import Session
from app.categoria import service
from app.categoria.schema import CategoriaCreate, CategoriaRead, CategoriaUpdate
from app.core.database import get_session
from app.core.deps import get_current_active_user, require_role
from app.modules.usuarios.model import Usuario

router = APIRouter(prefix="/categorias", tags=["Categorías"])


@router.get(
    "/",
    response_model=list[CategoriaRead],
    summary="Listar todas las categorías activas (usuario autenticado)",
)
def listar_categorias(
    session: Session = Depends(get_session),
    current_user: Usuario = Depends(get_current_active_user),
):
    return service.get_all(session)


@router.get(
    "/{categoria_id}",
    response_model=CategoriaRead,
    summary="Obtener categoría por ID (usuario autenticado)",
)
def obtener_categoria(
    categoria_id: int,
    session: Session = Depends(get_session),
    current_user: Usuario = Depends(get_current_active_user),
):
    return service.get_by_id(session, categoria_id)


@router.post(
    "/",
    response_model=CategoriaRead,
    status_code=status.HTTP_201_CREATED,
    summary="Crear una nueva categoría (solo admin)",
)
def crear_categoria(
    data: CategoriaCreate,
    session: Session = Depends(get_session),
    admin: Usuario = Depends(require_role(["admin"])),
):
    return service.create(session, data)


@router.put(
    "/{categoria_id}",
    response_model=CategoriaRead,
    summary="Actualizar una categoría (solo admin)",
)
def actualizar_categoria(
    categoria_id: int,
    data: CategoriaUpdate,
    session: Session = Depends(get_session),
    admin: Usuario = Depends(require_role(["admin"])),
):
    return service.update(session, categoria_id, data)


@router.delete(
    "/{categoria_id}",
    status_code=status.HTTP_204_NO_CONTENT,
    summary="Eliminar lógicamente una categoría (solo admin)",
)
def eliminar_categoria(
    categoria_id: int,
    session: Session = Depends(get_session),
    admin: Usuario = Depends(require_role(["admin"])),
):
    service.delete(session, categoria_id)
    return Response(status_code=status.HTTP_204_NO_CONTENT)
