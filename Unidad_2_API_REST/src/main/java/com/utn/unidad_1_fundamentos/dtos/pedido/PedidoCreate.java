package com.utn.unidad_1_fundamentos.dtos.pedido;

import com.utn.unidad_1_fundamentos.dtos.detallepedido.DetallePedidoCreate;
import com.utn.unidad_1_fundamentos.entities.enums.FormaPago;

import java.util.List;

public record PedidoCreate(
        Long usuarioId,
        FormaPago formaPago,
        List<DetallePedidoCreate> detalles
) {
}