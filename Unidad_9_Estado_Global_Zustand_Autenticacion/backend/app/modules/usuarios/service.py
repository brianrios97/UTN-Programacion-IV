from typing import List, Optional
from fastapi import HTTPException, status
from app.core.security import hash_password, verify_password
from app.modules.usuarios.model import Usuario
from app.modules.usuarios.repository import UsuarioRepository
from app.modules.usuarios.schemas import UserCreate


class UsuarioService:
    """Servicio de negocio para la gestión y autenticación de usuarios."""

    def __init__(self, repository: UsuarioRepository):
        self.repository = repository

    def register(self, data: UserCreate) -> Usuario:
        # Validar unicidad de username (RN-02)
        if self.repository.get_by_username(data.username):
            raise HTTPException(
                status_code=status.HTTP_409_CONFLICT,
                detail="El nombre de usuario ya se encuentra registrado",
            )

        # Validar unicidad de email (RN-02)
        if self.repository.get_by_email(data.email):
            raise HTTPException(
                status_code=status.HTTP_409_CONFLICT,
                detail="El correo electrónico ya se encuentra registrado",
            )

        # Hashear la contraseña con bcrypt (RN-01) y asignar rol por defecto "user" (RN-08)
        hashed_pwd = hash_password(data.password)
        nuevo_usuario = Usuario(
            username=data.username,
            full_name=data.full_name,
            email=data.email,
            hashed_password=hashed_pwd,
            role="user",
            disabled=False,
        )
        return self.repository.create(nuevo_usuario)

    def authenticate(self, username: str, password: str) -> Usuario:
        usuario = self.repository.get_by_username(username)
        if not usuario or not verify_password(password, usuario.hashed_password):
            raise HTTPException(
                status_code=status.HTTP_401_UNAUTHORIZED,
                detail="Credenciales inválidas",
                headers={"WWW-Authenticate": "Bearer"},
            )

        # Si el usuario fue desactivado lógicamente (RN-11 / consigna b/c)
        if usuario.disabled:
            raise HTTPException(
                status_code=status.HTTP_400_BAD_REQUEST,
                detail="Cuenta de usuario desactivada",
            )

        return usuario

    def get_by_id(self, user_id: int) -> Usuario:
        usuario = self.repository.get_by_id(user_id)
        if not usuario:
            raise HTTPException(
                status_code=status.HTTP_404_NOT_FOUND,
                detail="Usuario no encontrado",
            )
        return usuario

    def get_by_username(self, username: str) -> Usuario:
        usuario = self.repository.get_by_username(username)
        if not usuario:
            raise HTTPException(
                status_code=status.HTTP_404_NOT_FOUND,
                detail="Usuario no encontrado",
            )
        return usuario

    def list_all(self) -> List[Usuario]:
        return self.repository.get_all()

    def activar(self, user_id: int) -> Usuario:
        usuario = self.get_by_id(user_id)
        usuario.disabled = False
        return self.repository.update(usuario)

    def desactivar(self, user_id: int) -> Usuario:
        usuario = self.get_by_id(user_id)
        usuario.disabled = True
        return self.repository.update(usuario)
