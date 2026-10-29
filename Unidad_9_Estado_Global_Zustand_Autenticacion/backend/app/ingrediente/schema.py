from typing import Annotated
from pydantic import StringConstraints
from sqlmodel import SQLModel

NombreStr = Annotated[str, StringConstraints(strip_whitespace=True, min_length=1)]


class IngredienteBase(SQLModel):
    nombre: NombreStr


class IngredienteCreate(IngredienteBase):
    pass


class IngredienteRead(IngredienteBase):
    id: int


class IngredienteUpdate(SQLModel):
    nombre: NombreStr
