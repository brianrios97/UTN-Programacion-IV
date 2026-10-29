from typing import Optional
from sqlmodel import Field, SQLModel


class Usuario(SQLModel, table=True):
    __tablename__ = "usuario"

    id: Optional[int] = Field(default=None, primary_key=True)
    username: str = Field(unique=True, index=True, min_length=3, max_length=50)
    full_name: str = Field(min_length=1, max_length=100)
    email: str = Field(unique=True, index=True, min_length=5, max_length=150)
    hashed_password: str = Field(min_length=8)
    role: str = Field(default="user")  # "user" o "admin"
    disabled: bool = Field(default=False)  # Borrado l?gico de usuarios
