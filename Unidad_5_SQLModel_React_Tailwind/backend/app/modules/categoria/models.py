from sqlmodel import SQLModel, Field
from typing import Optional


# 1. Campos base con validaciones
class CategoriaBase(SQLModel):
    codigo: str = Field(
        min_length=1,
        schema_extra={"example": "MUE-01"},
    )
    descripcion: str = Field(min_length=3, schema_extra={"example": "Muebles de Oficina"})
    activo: bool = Field(default=True)


# 2. TABLA REAL en la base de datos (table=True)
class Categoria(CategoriaBase, table=True):
    id: Optional[int] = Field(default=None, primary_key=True)


# 3. Schema para crear (POST)
class CategoriaCreate(CategoriaBase):
    pass


# 4. Schema para devolver al cliente
class CategoriaRead(CategoriaBase):
    id: int


# 5. Schema para actualizar (PUT)
class CategoriaUpdate(SQLModel):
    codigo: Optional[str] = None
    descripcion: Optional[str] = None
    activo: Optional[bool] = None
