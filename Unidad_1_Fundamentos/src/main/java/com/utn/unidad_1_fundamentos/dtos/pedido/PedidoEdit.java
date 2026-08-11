package com.utn.unidad_1_fundamentos.dtos.pedido;

import com.utn.unidad_1_fundamentos.entities.enums.Estado;
import com.utn.unidad_1_fundamentos.entities.enums.FormaPago;
import lombok.*;

@Data
@NoArgsConstructor
@AllArgsConstructor
@Builder
public class PedidoEdit {
    private Long id;
    private Estado estado;
    private FormaPago formaPago;
}