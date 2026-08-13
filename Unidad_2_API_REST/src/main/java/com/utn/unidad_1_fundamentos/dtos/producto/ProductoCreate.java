package com.utn.unidad_1_fundamentos.dtos.producto;

public record ProductoCreate(
        String nombre,
        Double precio,
        String descripcion,
        Integer stock,
        String imagen,
        Boolean disponible,
        Long categoriaId
) {
}