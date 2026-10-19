from sqlmodel import SQLModel, Field
from typing import Optional


# 1. Campos base compartidos con validaciones
class ProductoBase(SQLModel):
    nombre: str = Field(min_length=1, schema_extra={"example": "Teclado Mecánico RGB"})
    descripcion: str = Field(default="", schema_extra={"example": "Switches blue retroiluminado"})
    precio: float = Field(ge=0, schema_extra={"example": 45000.0})
    categoria: str = Field(default="MUE-01", schema_extra={"example": "MUE-01"})
    stock: int = Field(default=0, ge=0, schema_extra={"example": 10})
    stock_minimo: int = Field(default=0, ge=0, schema_extra={"example": 5})
    activo: bool = Field(default=True)


# 2. TABLA REAL en la base de datos (table=True)
class Producto(ProductoBase, table=True):
    id: Optional[int] = Field(default=None, primary_key=True)


# 3. Schema para crear (POST)
class ProductoCreate(ProductoBase):
    pass


# 4. Schema para devolver al cliente (GET y respuestas)
class ProductoRead(ProductoBase):
    id: int


# 5. Schema para actualizar (PUT / PATCH)
class ProductoUpdate(SQLModel):
    nombre: Optional[str] = None
    descripcion: Optional[str] = None
    precio: Optional[float] = None
    categoria: Optional[str] = None
    stock: Optional[int] = None
    stock_minimo: Optional[int] = None
    activo: Optional[bool] = None
