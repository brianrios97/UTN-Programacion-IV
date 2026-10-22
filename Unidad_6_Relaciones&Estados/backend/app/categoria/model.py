from typing import TYPE_CHECKING, Optional
from sqlmodel import Field, Relationship, SQLModel

if TYPE_CHECKING:
    from app.producto.model import Producto


# 1. Tabla intermedia (Link Table) para la relación N:N
class ProductoCategoria(SQLModel, table=True):
    __tablename__ = "producto_categoria"

    producto_id: Optional[int] = Field(
        default=None, foreign_key="producto.id", primary_key=True
    )
    categoria_id: Optional[int] = Field(
        default=None, foreign_key="categoria.id", primary_key=True
    )


# 2. Entidad Categoria
class Categoria(SQLModel, table=True):
    __tablename__ = "categoria"

    id: Optional[int] = Field(default=None, primary_key=True)
    nombre: str = Field(index=True)
    descripcion: str

    # Relación bidireccional navegable hacia Producto cruzando la tabla intermedia
    productos: list["Producto"] = Relationship(
        back_populates="categorias", link_model=ProductoCategoria
    )
