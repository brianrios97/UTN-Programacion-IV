from typing import Callable
from sqlmodel import Session
from app.core.unit_of_work import AbstractUnitOfWork
from app.pedidos.repository import PedidoRepository, DetallePedidoRepository, ProductoRepository


class PedidosUnitOfWork(AbstractUnitOfWork):
    def __init__(self, session_factory: Callable[[], Session]):
        super().__init__(session_factory)
        self.pedidos: PedidoRepository | None = None
        self.detalles: DetallePedidoRepository | None = None
        self.productos: ProductoRepository | None = None

    def __enter__(self):
        super().__enter__()
        self.pedidos = PedidoRepository(self.session)
        self.detalles = DetallePedidoRepository(self.session)
        self.productos = ProductoRepository(self.session)
        return self
