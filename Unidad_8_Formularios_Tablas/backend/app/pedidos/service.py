from datetime import datetime, timezone
from typing import List
from app.pedidos.models import Pedido, DetallePedido
from app.pedidos.schemas import PedidoCreate, PedidoRead, PedidoUpdate
from app.pedidos.unit_of_work import PedidosUnitOfWork


class ProductoNoEncontrado(Exception):
    def __init__(self, producto_id: int):
        super().__init__(f"El producto con ID {producto_id} no existe")
        self.producto_id = producto_id


class PedidoNoEncontrado(Exception):
    def __init__(self, pedido_id: int):
        super().__init__(f"El pedido con ID {pedido_id} no fue encontrado o ha sido eliminado")
        self.pedido_id = pedido_id


class PedidoService:
    def __init__(self, uow: PedidosUnitOfWork):
        self.uow = uow

    def listar(self) -> List[PedidoRead]:
        with self.uow as uow:
            pedidos = uow.pedidos.get_all_active()
            return [PedidoRead.model_validate(p) for p in pedidos]

    def obtener_por_id(self, pedido_id: int) -> PedidoRead:
        with self.uow as uow:
            pedido = uow.pedidos.get_by_id_active(pedido_id)
            if not pedido:
                raise PedidoNoEncontrado(pedido_id)
            return PedidoRead.model_validate(pedido)

    def crear(self, data: PedidoCreate) -> PedidoRead:
        with self.uow as uow:
            pedido = uow.pedidos.create(Pedido(estado="PENDIENTE", total=0.0))
            total = 0.0

            for item in data.detalles:
                producto = uow.productos.get_by_id(item.producto_id)
                if producto is None:
                    raise ProductoNoEncontrado(item.producto_id)

                detalle = DetallePedido(
                    pedido_id=pedido.id,
                    producto_id=producto.id,
                    cantidad=item.cantidad,
                    precio_unitario=producto.precio_base,
                )
                uow.detalles.create(detalle)
                total += item.cantidad * producto.precio_base

            pedido.total = round(total, 2)
            uow.session.flush()
            # Cargar detalles en memoria antes de que se cierre el contexto del commit
            uow.session.refresh(pedido)
            return PedidoRead.model_validate(pedido)

    def actualizar_estado(self, pedido_id: int, data: PedidoUpdate) -> PedidoRead:
        with self.uow as uow:
            pedido = uow.pedidos.get_by_id_active(pedido_id)
            if not pedido:
                raise PedidoNoEncontrado(pedido_id)

            pedido.estado = data.estado
            uow.session.flush()
            uow.session.refresh(pedido)
            return PedidoRead.model_validate(pedido)

    def eliminar_logico(self, pedido_id: int) -> None:
        with self.uow as uow:
            pedido = uow.pedidos.get_by_id_active(pedido_id)
            if not pedido:
                raise PedidoNoEncontrado(pedido_id)

            pedido.deleted_at = datetime.now(timezone.utc)
            uow.session.flush()
