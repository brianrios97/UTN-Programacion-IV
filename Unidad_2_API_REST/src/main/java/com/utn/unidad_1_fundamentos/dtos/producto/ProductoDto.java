package com.utn.unidad_1_fundamentos.dtos.producto;

public record ProductoDto(
        Long id,
        String nombre,
        Double precio,
        String descripcion,
        Integer stock,
        String imagen,
        Boolean disponible,
        String categoriaNombre
) {
}