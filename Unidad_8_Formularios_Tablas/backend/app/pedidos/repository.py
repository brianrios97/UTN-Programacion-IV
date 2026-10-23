from typing import Optional, List
from sqlalchemy.orm import selectinload
from sqlmodel import Session, select
from app.core.repository import BaseRepository
from app.pedidos.models import Pedido, DetallePedido
from app.producto.model import Producto


class PedidoRepository(BaseRepository[Pedido]):
    def __init__(self, session: Session):
        super().__init__(Pedido, session)

    def get_all_active(self) -> List[Pedido]:
        query = (
            select(Pedido)
            .where(Pedido.deleted_at == None)
            .options(selectinload(Pedido.detalles))
            .order_by(Pedido.id.desc())
        )
        return list(self.session.exec(query).all())

    def get_by_id_active(self, pedido_id: int) -> Optional[Pedido]:
        query = (
            select(Pedido)
            .where(Pedido.id == pedido_id, Pedido.deleted_at == None)
            .options(selectinload(Pedido.detalles))
        )
        return self.session.exec(query).first()


class DetallePedidoRepository(BaseRepository[DetallePedido]):
    def __init__(self, session: Session):
        super().__init__(DetallePedido, session)


class ProductoRepository(BaseRepository[Producto]):
    def __init__(self, session: Session):
        super().__init__(Producto, session)
