from sqlmodel import SQLModel, Field
from typing import Optional


# 1. Campos base con validaciones
class ProveedorBase(SQLModel):
    codigo: str = Field(min_length=1, schema_extra={"example": "PRV-01"})
    razon_social: str = Field(min_length=3, schema_extra={"example": "Distribuidora Mayorista S.A."})
    cuit: str = Field(min_length=11, max_length=15, schema_extra={"example": "30-11223344-9"})
    email: str = Field(default="", schema_extra={"example": "contacto@distribuidora.com"})
    telefono: str = Field(default="", schema_extra={"example": "11-4455-6677"})
    activo: bool = Field(default=True)


# 2. TABLA REAL en la base de datos (table=True)
class Proveedor(ProveedorBase, table=True):
    id: Optional[int] = Field(default=None, primary_key=True)


# 3. Schema para crear (POST)
class ProveedorCreate(ProveedorBase):
    pass


# 4. Schema para devolver al cliente
class ProveedorRead(ProveedorBase):
    id: int


# 5. Schema para actualizar (PUT)
class ProveedorUpdate(SQLModel):
    codigo: Optional[str] = None
    razon_social: Optional[str] = None
    cuit: Optional[str] = None
    email: Optional[str] = None
    telefono: Optional[str] = None
    activo: Optional[bool] = None
