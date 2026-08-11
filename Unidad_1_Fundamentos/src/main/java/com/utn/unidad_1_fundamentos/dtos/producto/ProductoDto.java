package com.utn.unidad_1_fundamentos.dtos.producto;

import lombok.*;
import java.time.LocalDateTime;

@Data
@NoArgsConstructor
@AllArgsConstructor
@Builder
public class ProductoDto {
    private Long id;
    private String nombre;
    private Double precio;
    private String descripcion;
    private int stock;
    private String imagen;
    private Boolean disponible;
    private Long categoriaId;
    private boolean eliminado;
    private LocalDateTime createdAt;
}