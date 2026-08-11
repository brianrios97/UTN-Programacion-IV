package com.utn.unidad_1_fundamentos.dtos.categoria;

import lombok.*;

@Data
@NoArgsConstructor
@AllArgsConstructor
@Builder
public class CategoriaCreate {
    private String nombre;
    private String descripcion;
}