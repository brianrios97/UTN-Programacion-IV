package com.utn.unidad_1_fundamentos.dtos.pedido;

import com.utn.unidad_1_fundamentos.dtos.detallepedido.DetallePedidoDto;
import com.utn.unidad_1_fundamentos.entities.enums.Estado;
import com.utn.unidad_1_fundamentos.entities.enums.FormaPago;

import java.time.LocalDate;
import java.util.List;

public record PedidoDto(
        Long id,
        LocalDate fecha,
        Estado estado,
        Double total,
        FormaPago formaPago,
        String usuarioNombre,
        List<DetallePedidoDto> detalles
) {
}