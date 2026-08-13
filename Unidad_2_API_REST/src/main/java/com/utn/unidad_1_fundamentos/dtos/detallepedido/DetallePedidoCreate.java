package com.utn.unidad_1_fundamentos.dtos.detallepedido;

public record DetallePedidoCreate(
        int cantidad,
        Long productoId
) {
}