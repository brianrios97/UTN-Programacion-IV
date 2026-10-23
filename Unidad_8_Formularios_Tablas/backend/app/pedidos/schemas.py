from datetime import datetime
from typing import Optional, List
from pydantic import field_validator
from sqlmodel import SQLModel, Field

ESTADOS_VALIDOS = {"PENDIENTE", "CONFIRMADO", "ENTREGADO", "CANCELADO"}


class DetallePedidoItem(SQLModel):
    producto_id: int
    cantidad: int = Field(ge=1)


class PedidoCreate(SQLModel):
    detalles: List[DetallePedidoItem]

    @field_validator("detalles")
    @classmethod
    def validar_detalles(cls, v: List[DetallePedidoItem]):
        if not v or len(v) == 0:
            raise ValueError("Un pedido debe tener al menos un DetallePedido para ser creado")
        
        producto_ids = [item.producto_id for item in v]
        if len(producto_ids) != len(set(producto_ids)):
            raise ValueError("Un mismo producto no puede repetirse entre los detalles del pedido")
        
        for item in v:
            if item.cantidad < 1:
                raise ValueError("La cantidad de cada detalle debe ser mayor o igual a 1")
        return v


class DetallePedidoRead(SQLModel):
    pedido_id: int
    producto_id: int
    cantidad: int
    precio_unitario: float


class PedidoRead(SQLModel):
    id: int
    fecha: datetime
    estado: str
    total: float
    detalles: List[DetallePedidoRead] = []


class PedidoUpdate(SQLModel):
    estado: str

    @field_validator("estado")
    @classmethod
    def validar_estado(cls, v: str):
        v_upper = v.strip().upper()
        if v_upper not in ESTADOS_VALIDOS:
            raise ValueError(f"Estado invalido '{v}'. Estados permitidos: {', '.join(sorted(ESTADOS_VALIDOS))}")
        return v_upper
