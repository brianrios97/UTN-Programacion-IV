package com.utn.unidad_1_fundamentos.dtos.usuario;

import com.utn.unidad_1_fundamentos.entities.enums.Rol;

public record UsuarioCreate(
        String nombre,
        String apellido,
        String mail,
        String celular,
        String contraseña,
        Rol rol
) {
}