from typing import TYPE_CHECKING, Optional
from sqlalchemy import Column, String, JSON
from sqlalchemy.dialects.postgresql import ARRAY
from sqlmodel import Field, Relationship, SQLModel
from app.categoria.model import ProductoCategoria

if TYPE_CHECKING:
    from app.categoria.model import Categoria


class Producto(SQLModel, table=True):
    __tablename__ = "producto"

    id: Optional[int] = Field(default=None, primary_key=True)
    nombre: str = Field(index=True, max_length=150)
    descripcion: str
    precio_base: float = Field(ge=0)
    # Compatible con PostgreSQL ARRAY(String) y con SQLite JSON
    imagenes_url: list[str] = Field(
        default_factory=list,
        sa_column=Column(ARRAY(String).with_variant(JSON, "sqlite")),
    )
    disponible: bool = Field(default=True)

    categorias: list["Categoria"] = Relationship(
        back_populates="productos", link_model=ProductoCategoria
    )
