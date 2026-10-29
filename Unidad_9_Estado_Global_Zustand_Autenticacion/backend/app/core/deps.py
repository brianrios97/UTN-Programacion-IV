from typing import List, Optional
from fastapi import Depends, HTTPException, Request, status
from fastapi.security import OAuth2PasswordBearer
from sqlmodel import Session
from app.core.database import get_session
from app.core.security import decode_access_token
from app.modules.usuarios.model import Usuario
from app.modules.usuarios.repository import UsuarioRepository
from app.modules.usuarios.service import UsuarioService


class OAuth2PasswordBearerWithCookie(OAuth2PasswordBearer):
    """
    Esquema OAuth2 extendido que extrae el token JWT prioritariamente
    de la cookie HttpOnly 'access_token', y como alternativa de la cabecera
    'Authorization: Bearer <token>'.
    """

    def __init__(self, tokenUrl: str, auto_error: bool = True):
        super().__init__(tokenUrl=tokenUrl, auto_error=auto_error)

    async def __call__(self, request: Request) -> Optional[str]:
        # 1. Buscar en la cookie HttpOnly
        token = request.cookies.get("access_token")
        if token:
            return token

        # 2. Buscar en la cabecera Authorization
        header_auth = request.headers.get("Authorization")
        if header_auth and header_auth.startswith("Bearer "):
            return header_auth[7:].strip()

        if self.auto_error:
            raise HTTPException(
                status_code=status.HTTP_401_UNAUTHORIZED,
                detail="No autenticado",
                headers={"WWW-Authenticate": "Bearer"},
            )
        return None


# Instancia del esquema OAuth2
oauth2_scheme = OAuth2PasswordBearerWithCookie(
    tokenUrl="/api/v1/auth/token",
    auto_error=False
)


def get_usuario_service(session: Session = Depends(get_session)) -> UsuarioService:
    repo = UsuarioRepository(session)
    return UsuarioService(repo)


def get_current_user(
    token: Optional[str] = Depends(oauth2_scheme),
    session: Session = Depends(get_session),
) -> Usuario:
    """
    Valida el token JWT y recupera el usuario correspondiente de la base de datos.
    Lanza 401 si no hay token, si está expirado o si la firma es inválida.
    """
    if not token:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="No autenticado",
            headers={"WWW-Authenticate": "Bearer"},
        )

    payload = decode_access_token(token)
    if not payload or "sub" not in payload:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Token inválido o expirado",
            headers={"WWW-Authenticate": "Bearer"},
        )

    username: str = payload["sub"]
    repo = UsuarioRepository(session)
    usuario = repo.get_by_username(username)
    if not usuario:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Usuario no encontrado",
            headers={"WWW-Authenticate": "Bearer"},
        )

    return usuario


def get_current_active_user(
    current_user: Usuario = Depends(get_current_user),
) -> Usuario:
    """
    Verifica que el usuario autenticado no esté desactivado lógicamente.
    Devuelve 400 'Cuenta de usuario desactivada' según la consigna.
    """
    if current_user.disabled:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="Cuenta de usuario desactivada",
        )
    return current_user


def require_role(allowed_roles: List[str]):
    """
    Fábrica de dependencias RBAC (Role-Based Access Control).
    Exige que el usuario activo posea uno de los roles autorizados;
    de lo contrario responde con 403 Forbidden.
    """
    def role_checker(
        current_user: Usuario = Depends(get_current_active_user),
    ) -> Usuario:
        if current_user.role not in allowed_roles:
            raise HTTPException(
                status_code=status.HTTP_403_FORBIDDEN,
                detail="Operación no permitida para su rol",
            )
        return current_user

    return role_checker
