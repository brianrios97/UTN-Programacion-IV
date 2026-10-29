from typing import Optional, List
from sqlmodel import Session, select
from app.modules.usuarios.model import Usuario


class UsuarioRepository:
    """Repositorio para la persistencia y consultas de usuarios."""

    def __init__(self, session: Session):
        self.session = session

    def get_by_id(self, user_id: int) -> Optional[Usuario]:
        return self.session.get(Usuario, user_id)

    def get_by_username(self, username: str) -> Optional[Usuario]:
        statement = select(Usuario).where(Usuario.username == username)
        return self.session.exec(statement).first()

    def get_by_email(self, email: str) -> Optional[Usuario]:
        statement = select(Usuario).where(Usuario.email == email)
        return self.session.exec(statement).first()

    def get_all(self) -> List[Usuario]:
        statement = select(Usuario)
        return list(self.session.exec(statement).all())

    def create(self, usuario: Usuario) -> Usuario:
        self.session.add(usuario)
        self.session.commit()
        self.session.refresh(usuario)
        return usuario

    def update(self, usuario: Usuario) -> Usuario:
        self.session.add(usuario)
        self.session.commit()
        self.session.refresh(usuario)
        return usuario
