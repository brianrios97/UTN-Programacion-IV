from typing import Optional
from sqlmodel import SQLModel
from app.categoria.schema import CategoriaRead


# 1. Base común de Producto
class ProductoBase(SQLModel):
    nombre: str
    descripcion: str
    precio_base: str
    imagen_url: list[str] = []
    disponible: bool = True


# 2. Schema para Crear (POST)
# Permite asociar categorías directamente pasando una lista de sus IDs: [1, 2]
class ProductoCreate(ProductoBase):
    categoria_ids: list[int] = []


# 3. Schema para Leer básico (GET /productos/)
class ProductoRead(ProductoBase):
    id: int


# 4. Schema para Leer completo (GET /productos/{id}) con sus categorías anidadas
class ProductoReadWithCategorias(ProductoRead):
    categorias: list[CategoriaRead] = []


# 5. Schema para Actualizar (PUT)
class ProductoUpdate(SQLModel):
    nombre: Optional[str] = None
    descripcion: Optional[str] = None
    precio_base: Optional[str] = None
    imagen_url: Optional[list[str]] = None
    disponible: Optional[bool] = None
    categoria_ids: Optional[list[int]] = None


# 6. Schemas para vincular/desvincular directamente Producto <-> Categoria
class ProductoCategoriaLink(SQLModel):
    producto_id: int
    categoria_id: int
