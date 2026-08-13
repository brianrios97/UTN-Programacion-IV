package com.utn.unidad_1_fundamentos.dtos.producto;

public record ProductoEdit(
        String nombre,
        Double precio,
        String descripcion,
        Integer stock,
        String imagen,
        Boolean disponible,
        Long categoriaId
) {
}