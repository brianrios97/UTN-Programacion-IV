from typing import List
from fastapi import APIRouter, Depends, Response, status
from fastapi.security import OAuth2PasswordRequestForm
from app.core.config import settings
from app.core.deps import get_current_active_user, get_usuario_service, require_role
from app.core.security import create_access_token
from app.modules.usuarios.model import Usuario
from app.modules.usuarios.schemas import MessageResponse, Token, UserCreate, UserPublic
from app.modules.usuarios.service import UsuarioService

router = APIRouter(prefix="/auth", tags=["Autenticación"])


@router.post(
    "/register",
    response_model=UserPublic,
    status_code=status.HTTP_201_CREATED,
    summary="Registrar un nuevo usuario (rol 'user')",
)
def register(
    data: UserCreate,
    service: UsuarioService = Depends(get_usuario_service),
) -> Usuario:
    return service.register(data)


@router.post(
    "/token",
    response_model=Token,
    summary="Iniciar sesión con OAuth2 form y emitir cookie HttpOnly",
)
def login(
    response: Response,
    form_data: OAuth2PasswordRequestForm = Depends(),
    service: UsuarioService = Depends(get_usuario_service),
):
    usuario = service.authenticate(form_data.username, form_data.password)

    # Crear token JWT con datos relevantes (username como sub y rol)
    access_token = create_access_token(
        data={"sub": usuario.username, "role": usuario.role}
    )

    # Almacenar en cookie HttpOnly (RN-03)
    response.set_cookie(
        key="access_token",
        value=access_token,
        httponly=True,
        samesite="lax",
        secure=False,  # False en desarrollo local HTTP
        max_age=settings.ACCESS_TOKEN_EXPIRE_MINUTES * 60,
    )

    return {"access_token": access_token, "token_type": "bearer"}


@router.post(
    "/logout",
    response_model=MessageResponse,
    summary="Cerrar sesión eliminando la cookie HttpOnly",
)
def logout(response: Response):
    response.delete_cookie(
        key="access_token",
        httponly=True,
        samesite="lax",
    )
    return {"mensaje": "Sesión cerrada correctamente"}


@router.get(
    "/me",
    response_model=UserPublic,
    summary="Obtener perfil del usuario autenticado actual",
)
def get_me(
    current_user: Usuario = Depends(get_current_active_user),
) -> Usuario:
    return current_user


# Endpoints de administración de usuarios (solo rol admin)
admin_router = APIRouter(prefix="/admin/usuarios", tags=["Admin - Usuarios"])


@admin_router.get(
    "",
    response_model=List[UserPublic],
    summary="Listar todos los usuarios (solo admin)",
)
def list_usuarios(
    admin: Usuario = Depends(require_role(["admin"])),
    service: UsuarioService = Depends(get_usuario_service),
) -> List[Usuario]:
    return service.list_all()


@admin_router.post(
    "/{id}/activar",
    response_model=UserPublic,
    summary="Activar usuario desactivado (solo admin)",
)
def activar_usuario(
    id: int,
    admin: Usuario = Depends(require_role(["admin"])),
    service: UsuarioService = Depends(get_usuario_service),
) -> Usuario:
    return service.activar(id)


@admin_router.post(
    "/{id}/desactivar",
    response_model=UserPublic,
    summary="Desactivar usuario lógicamente (solo admin)",
)
def desactivar_usuario(
    id: int,
    admin: Usuario = Depends(require_role(["admin"])),
    service: UsuarioService = Depends(get_usuario_service),
) -> Usuario:
    return service.desactivar(id)
