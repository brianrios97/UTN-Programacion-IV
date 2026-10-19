from pydantic import BaseModel, Field
from typing import Optional

class ProveedorBase(BaseModel):
    codigo: str = Field(..., min_length=1, example="PRV-01")
    razon_social: str = Field(..., min_length=3, example="Distribuidora Mayorista S.A.")
    cuit: str = Field(..., min_length=11, max_length=15, example="30-11223344-9")
    email: str = Field(default="", example="contacto@distribuidora.com")
    telefono: str = Field(default="", example="11-4455-6677")
    activo: bool = True


class ProveedorCreate(ProveedorBase):
    pass

class ProveedorRead(ProveedorBase):
    id: int

class ProveedorUpdate(BaseModel):
    codigo: Optional[str] = Field(None, min_length=1)
    razon_social: Optional[str] = Field(None, min_length=3)
    cuit: Optional[str] = Field(None, min_length=11, max_length=15)
    email: Optional[str] = None
    telefono: Optional[str] = None
    activo: Optional[bool] = None
