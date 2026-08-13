package com.utn.unidad_1_fundamentos.controllers;

import com.utn.unidad_1_fundamentos.dtos.pedido.PedidoCreate;
import com.utn.unidad_1_fundamentos.dtos.pedido.PedidoDto;
import com.utn.unidad_1_fundamentos.dtos.pedido.PedidoEdit;
import com.utn.unidad_1_fundamentos.services.PedidoService;
import org.springframework.http.HttpStatus;
import org.springframework.http.ResponseEntity;
import org.springframework.web.bind.annotation.*;

import java.util.List;

@RestController
@RequestMapping("/api/pedidos")
public class PedidoController {

    private final PedidoService pedidoService;

    public PedidoController(PedidoService pedidoService) {
        this.pedidoService = pedidoService;
    }

    @GetMapping
    public ResponseEntity<List<PedidoDto>> listarTodos() {
        return ResponseEntity.ok(pedidoService.listarTodos());
    }

    @GetMapping("/{id}")
    public ResponseEntity<PedidoDto> buscarPorId(@PathVariable Long id) {
        return ResponseEntity.ok(pedidoService.buscarPorId(id));
    }

    @PostMapping
    public ResponseEntity<PedidoDto> crear(@RequestBody PedidoCreate dto) {
        return ResponseEntity.status(HttpStatus.CREATED).body(pedidoService.crear(dto));
    }

    // Actualizamos solo el Estado del pedido
    @PutMapping("/{id}/estado")
    public ResponseEntity<PedidoDto> actualizarEstado(@PathVariable Long id, @RequestBody PedidoEdit dto) {
        return ResponseEntity.ok(pedidoService.actualizarEstado(id, dto));
    }
}