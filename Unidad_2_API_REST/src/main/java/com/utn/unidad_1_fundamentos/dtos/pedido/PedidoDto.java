package com.utn.unidad_1_fundamentos.dtos.pedido;

import com.utn.unidad_1_fundamentos.dtos.detallepedido.DetallePedidoDto;
import com.utn.unidad_1_fundamentos.entities.enums.Estado;
import com.utn.unidad_1_fundamentos.entities.enums.FormaPago;
import lombok.*;

import java.time.LocalDate;
import java.time.LocalDateTime;
import java.util.List;

@Data
@NoArgsConstructor
@AllArgsConstructor
@Builder
public class PedidoDto {
    private Long id;
    private LocalDate fecha;
    private Estado estado;
    private Double total;
    private FormaPago formaPago;
    private Long usuarioId;
    private List<DetallePedidoDto> detalles;
    private boolean eliminado;
    private LocalDateTime createdAt;
}