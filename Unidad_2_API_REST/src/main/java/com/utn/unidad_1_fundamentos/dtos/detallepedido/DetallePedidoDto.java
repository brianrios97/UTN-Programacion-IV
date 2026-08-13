package com.utn.unidad_1_fundamentos.dtos.detallepedido;

public record DetallePedidoDto(
        Long id,
        int cantidad,
        Double subtotal,
        String productoNombre
) {
}