package com.utn.unidad_1_fundamentos.controllers;

import com.utn.unidad_1_fundamentos.dtos.usuario.UsuarioCreate;
import com.utn.unidad_1_fundamentos.dtos.usuario.UsuarioDto;
import com.utn.unidad_1_fundamentos.dtos.usuario.UsuarioEdit;
import com.utn.unidad_1_fundamentos.services.UsuarioService;
import org.springframework.http.HttpStatus;
import org.springframework.http.ResponseEntity;
import org.springframework.web.bind.annotation.*;

import java.util.List;

@RestController
@RequestMapping("/api/usuarios")
public class UsuarioController {

    private final UsuarioService usuarioService;

    public UsuarioController(UsuarioService usuarioService) {
        this.usuarioService = usuarioService;
    }

    @GetMapping
    public ResponseEntity<List<UsuarioDto>> listarTodos() {
        return ResponseEntity.ok(usuarioService.listarTodos());
    }

    // PUNTO 7 DEL TP: Buscar por ID (El service ya lo muestra por consola)
    @GetMapping("/{id}")
    public ResponseEntity<UsuarioDto> buscarPorId(@PathVariable Long id) {
        return ResponseEntity.ok(usuarioService.buscarPorId(id));
    }

    // PUNTO 8 DEL TP: Buscar por Mail (El service ya lo muestra por consola)
    @GetMapping("/mail/{mail}")
    public ResponseEntity<UsuarioDto> buscarPorMail(@PathVariable String mail) {
        return ResponseEntity.ok(usuarioService.buscarPorMail(mail));
    }

    @PostMapping
    public ResponseEntity<UsuarioDto> crear(@RequestBody UsuarioCreate dto) {
        return ResponseEntity.status(HttpStatus.CREATED).body(usuarioService.crear(dto));
    }

    @PutMapping("/{id}")
    public ResponseEntity<UsuarioDto> actualizar(@PathVariable Long id, @RequestBody UsuarioEdit dto) {
        return ResponseEntity.ok(usuarioService.actualizar(id, dto));
    }
}