from typing import List
from fastapi import APIRouter, Depends, HTTPException, status, Response
from sqlmodel import Session
from app.core.database import engine
from app.pedidos.schemas import PedidoCreate, PedidoRead, PedidoUpdate
from app.pedidos.unit_of_work import PedidosUnitOfWork
from app.pedidos.service import (
    PedidoService,
    ProductoNoEncontrado,
    PedidoNoEncontrado,
)

router = APIRouter(prefix="/pedidos", tags=["pedidos"])


def get_session():
    return Session(engine)


def get_pedido_service() -> PedidoService:
    uow = PedidosUnitOfWork(get_session)
    return PedidoService(uow)


@router.get("/", response_model=List[PedidoRead])
def listar_pedidos(service: PedidoService = Depends(get_pedido_service)):
    return service.listar()


@router.get("/{id}", response_model=PedidoRead)
def obtener_pedido(id: int, service: PedidoService = Depends(get_pedido_service)):
    try:
        return service.obtener_por_id(id)
    except PedidoNoEncontrado as e:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=str(e))


@router.post("/", response_model=PedidoRead, status_code=status.HTTP_201_CREATED)
def crear_pedido(data: PedidoCreate, service: PedidoService = Depends(get_pedido_service)):
    try:
        return service.crear(data)
    except ProductoNoEncontrado as e:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=str(e))
    except ValueError as e:
        raise HTTPException(status_code=status.HTTP_422_UNPROCESSABLE_ENTITY, detail=str(e))


@router.put("/{id}", response_model=PedidoRead)
def actualizar_estado_pedido(
    id: int,
    data: PedidoUpdate,
    service: PedidoService = Depends(get_pedido_service),
):
    try:
        return service.actualizar_estado(id, data)
    except PedidoNoEncontrado as e:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=str(e))
    except ValueError as e:
        raise HTTPException(status_code=status.HTTP_422_UNPROCESSABLE_ENTITY, detail=str(e))


@router.delete("/{id}", status_code=status.HTTP_204_NO_CONTENT)
def eliminar_pedido(id: int, service: PedidoService = Depends(get_pedido_service)):
    try:
        service.eliminar_logico(id)
        return Response(status_code=status.HTTP_204_NO_CONTENT)
    except PedidoNoEncontrado as e:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=str(e))
