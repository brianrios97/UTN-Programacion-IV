package com.utn.unidad_1_fundamentos.dtos.usuario;

import com.utn.unidad_1_fundamentos.entities.enums.Rol;

public record UsuarioDto(
        Long id,
        String nombre,
        String apellido,
        String mail,
        String celular,
        Rol rol
) {
}