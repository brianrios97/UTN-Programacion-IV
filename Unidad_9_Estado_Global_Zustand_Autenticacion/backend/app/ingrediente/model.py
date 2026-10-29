from typing import Optional
from sqlmodel import Field, SQLModel


class Ingrediente(SQLModel, table=True):
    __tablename__ = "ingrediente"

    id: Optional[int] = Field(default=None, primary_key=True)
    nombre: str = Field(index=True, unique=True)
    activo: bool = Field(default=True)  # Borrado lógico (RN-11)
