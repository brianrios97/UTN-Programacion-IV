from typing import TYPE_CHECKING, Optional
from sqlmodel import Column, Field, JSON, Relationship, SQLModel
from app.categoria.model import ProductoCategoria

if TYPE_CHECKING:
    from app.categoria.model import Categoria


# Entidad Producto
class Producto(SQLModel, table=True):
    __tablename__ = "producto"

    id: Optional[int] = Field(default=None, primary_key=True)
    nombre: str = Field(index=True)
    descripcion: str
    precio_base: str
    # Usamos Column(JSON) para que list[] se almacene limpiamente tanto en SQLite como en PostgreSQL
    imagen_url: list[str] = Field(default_factory=list, sa_column=Column(JSON))
    disponible: bool = Field(default=True)

    # Relación bidireccional navegable hacia Categoria
    categorias: list["Categoria"] = Relationship(
        back_populates="productos", link_model=ProductoCategoria
    )
