package com.utn.unidad_1_fundamentos.dtos.usuario;

import com.utn.unidad_1_fundamentos.entities.enums.Rol;
import lombok.*;

@Data
@NoArgsConstructor
@AllArgsConstructor
@Builder
public class UsuarioEdit {
    private Long id;
    private String nombre;
    private String apellido;
    private String mail;
    private String celular;
    private String contraseña;
    private Rol rol;
}