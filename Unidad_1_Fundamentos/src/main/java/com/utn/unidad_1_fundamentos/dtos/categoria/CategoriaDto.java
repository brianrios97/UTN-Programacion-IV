package com.utn.unidad_1_fundamentos.dtos.categoria;

import lombok.*;
import java.time.LocalDateTime;

@Data
@NoArgsConstructor
@AllArgsConstructor
@Builder
public class CategoriaDto {
    private Long id;
    private String nombre;
    private String descripcion;
    private boolean eliminado;
    private LocalDateTime createdAt;
}