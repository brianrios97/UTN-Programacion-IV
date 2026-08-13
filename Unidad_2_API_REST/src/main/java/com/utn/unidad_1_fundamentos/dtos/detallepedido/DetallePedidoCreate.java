package com.utn.unidad_1_fundamentos.dtos.detallepedido;

import lombok.*;

@Data
@NoArgsConstructor
@AllArgsConstructor
@Builder
public class DetallePedidoCreate {
    private int cantidad;
    private Long productoId;
}