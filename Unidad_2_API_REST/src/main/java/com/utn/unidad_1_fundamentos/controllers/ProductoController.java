package com.utn.unidad_1_fundamentos.controllers;

import com.utn.unidad_1_fundamentos.dtos.producto.ProductoCreate;
import com.utn.unidad_1_fundamentos.dtos.producto.ProductoDto;
import com.utn.unidad_1_fundamentos.dtos.producto.ProductoEdit;
import com.utn.unidad_1_fundamentos.services.ProductoService;
import org.springframework.http.HttpStatus;
import org.springframework.http.ResponseEntity;
import org.springframework.web.bind.annotation.*;

import java.util.List;

@RestController
@RequestMapping("/api/productos")
public class ProductoController {

    private final ProductoService productoService;

    public ProductoController(ProductoService productoService) {
        this.productoService = productoService;
    }

    @GetMapping
    public ResponseEntity<List<ProductoDto>> listarTodos() {
        return ResponseEntity.ok(productoService.listarTodos());
    }

    @GetMapping("/{id}")
    public ResponseEntity<ProductoDto> buscarPorId(@PathVariable Long id) {
        return ResponseEntity.ok(productoService.buscarPorId(id));
    }

    @PostMapping
    public ResponseEntity<ProductoDto> crear(@RequestBody ProductoCreate dto) {
        return ResponseEntity.status(HttpStatus.CREATED).body(productoService.crear(dto));
    }

    @PutMapping("/{id}")
    public ResponseEntity<ProductoDto> actualizar(@PathVariable Long id, @RequestBody ProductoEdit dto) {
        return ResponseEntity.ok(productoService.actualizar(id, dto));
    }
}