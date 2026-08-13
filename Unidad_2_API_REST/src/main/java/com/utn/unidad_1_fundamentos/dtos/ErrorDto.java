package com.utn.unidad_1_fundamentos.dtos;

import java.time.LocalDateTime;

public record ErrorDto(
        LocalDateTime timestamp,
        int status,
        String mensaje,
        String detalles
) {
}