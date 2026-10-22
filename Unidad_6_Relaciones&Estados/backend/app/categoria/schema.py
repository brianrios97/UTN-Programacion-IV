from typing import Optional
from sqlmodel import SQLModel


# 1. Base común con campos obligatorios de negocio
class CategoriaBase(SQLModel):
    nombre: str
    descripcion: str


# 2. Schema para Crear (POST) - Sin id
class CategoriaCreate(CategoriaBase):
    pass


# 3. Schema para Leer (GET) - Con id generado por la DB
class CategoriaRead(CategoriaBase):
    id: int


# 4. Schema para Actualizar (PUT) - Campos opcionales
class CategoriaUpdate(SQLModel):
    nombre: Optional[str] = None
    descripcion: Optional[str] = None
