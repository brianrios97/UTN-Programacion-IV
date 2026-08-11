package com.utn.unidad_1_fundamentos.dtos.categoria;

import lombok.*;

@Data
@NoArgsConstructor
@AllArgsConstructor
@Builder
public class CategoriaEdit {
    private Long id;
    private String nombre;
    private String descripcion;
}