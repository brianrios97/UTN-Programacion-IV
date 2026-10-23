from typing import Optional
from sqlmodel import Field, SQLModel
from app.categoria.schema import CategoriaRead


class ProductoBase(SQLModel):
    nombre: str
    descripcion: str
    precio_base: float = Field(ge=0)
    imagenes_url: list[str] = []
    disponible: bool = True


class ProductoCreate(ProductoBase):
    categoria_ids: list[int] = []


class ProductoRead(ProductoBase):
    id: int


class ProductoReadWithCategorias(ProductoRead):
    categorias: list[CategoriaRead] = []


class ProductoUpdate(SQLModel):
    nombre: Optional[str] = None
    descripcion: Optional[str] = None
    precio_base: Optional[float] = Field(default=None, ge=0)
    imagenes_url: Optional[list[str]] = None
    disponible: Optional[bool] = None
    categoria_ids: Optional[list[int]] = None
