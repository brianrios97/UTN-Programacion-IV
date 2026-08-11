package com.utn.unidad_1_fundamentos.dtos.detallepedido;

import com.utn.unidad_1_fundamentos.dtos.producto.ProductoDto;
import lombok.*;
import java.time.LocalDateTime;

@Data
@NoArgsConstructor
@AllArgsConstructor
@Builder
public class DetallePedidoDto {
    private Long id;
    private int cantidad;
    private Double subtotal;
    private ProductoDto producto;
    private boolean eliminado;
    private LocalDateTime createdAt;
}