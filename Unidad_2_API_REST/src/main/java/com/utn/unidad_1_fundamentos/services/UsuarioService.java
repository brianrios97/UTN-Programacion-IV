package com.utn.unidad_1_fundamentos.services;

import com.utn.unidad_1_fundamentos.dtos.usuario.UsuarioCreate;
import com.utn.unidad_1_fundamentos.dtos.usuario.UsuarioDto;
import com.utn.unidad_1_fundamentos.dtos.usuario.UsuarioEdit;
import com.utn.unidad_1_fundamentos.entities.Usuario;
import com.utn.unidad_1_fundamentos.repositories.UsuarioRepository;
import org.springframework.stereotype.Service;

import java.time.LocalDateTime;
import java.util.List;

@Service
public class UsuarioService {

    private final UsuarioRepository usuarioRepository;

    public UsuarioService(UsuarioRepository usuarioRepository) {
        this.usuarioRepository = usuarioRepository;
    }

    public List<UsuarioDto> listarTodos() {
        return usuarioRepository.findAll().stream()
                .filter(u -> !u.isEliminado())
                .map(this::toDto)
                .toList();
    }

    public UsuarioDto buscarPorId(Long id) {
        Usuario u = usuarioRepository.findById(id)
                .orElseThrow(() -> new IllegalArgumentException("Usuario no encontrado con ID: " + id));
        System.out.println("🔍 [CONSOLA - BÚSQUEDA POR ID]: " + u);
        return toDto(u);
    }

    public UsuarioDto buscarPorMail(String mail) {
        Usuario u = usuarioRepository.findByMail(mail)
                .orElseThrow(() -> new IllegalArgumentException("Usuario no encontrado con mail: " + mail));
        System.out.println("✉️ [CONSOLA - BÚSQUEDA POR MAIL]: " + u);
        return toDto(u);
    }

    public UsuarioDto crear(UsuarioCreate dto) {
        Usuario u = new Usuario();
        u.setNombre(dto.nombre());
        u.setApellido(dto.apellido());
        u.setMail(dto.mail());
        u.setCelular(dto.celular());
        u.setContraseña(dto.contraseña());
        u.setRol(dto.rol());
        u.setCreatedAt(LocalDateTime.now());
        u.setEliminado(false);

        Usuario guardado = usuarioRepository.save(u);
        return toDto(guardado);
    }

    public UsuarioDto actualizar(Long id, UsuarioEdit dto) {
        Usuario u = usuarioRepository.findById(id)
                .orElseThrow(() -> new IllegalArgumentException("Usuario no encontrado con ID: " + id));

        u.setNombre(dto.nombre());
        u.setApellido(dto.apellido());
        u.setMail(dto.mail());
        u.setCelular(dto.celular());
        u.setContraseña(dto.contraseña());
        u.setRol(dto.rol());

        Usuario actualizado = usuarioRepository.save(u);
        return toDto(actualizado);
    }

    private UsuarioDto toDto(Usuario u) {
        return new UsuarioDto(
                u.getId(),
                u.getNombre(),
                u.getApellido(),
                u.getMail(),
                u.getCelular(),
                u.getRol()
        );
    }
}