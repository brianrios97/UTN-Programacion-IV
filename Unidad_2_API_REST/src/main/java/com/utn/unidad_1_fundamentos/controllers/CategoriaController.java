package com.utn.unidad_1_fundamentos.controllers;

import com.utn.unidad_1_fundamentos.dtos.categoria.CategoriaCreate;
import com.utn.unidad_1_fundamentos.dtos.categoria.CategoriaDto;
import com.utn.unidad_1_fundamentos.dtos.categoria.CategoriaEdit;
import com.utn.unidad_1_fundamentos.services.CategoriaService;
import org.springframework.http.HttpStatus;
import org.springframework.http.ResponseEntity;
import org.springframework.web.bind.annotation.*;

import java.util.List;

// 1. Avisamos que es un controlador REST (devuelve JSON)
@RestController
// 2. Definimos la URL base para este controlador
@RequestMapping("/api/categorias")
public class CategoriaController {

    // 3. Inyectamos a nuestro "Chef" (El Service)
    private final CategoriaService categoriaService;

    public CategoriaController(CategoriaService categoriaService) {
        this.categoriaService = categoriaService;
    }

    // --- ENDPOINTS ---

    // GET a /api/categorias
    @GetMapping
    public ResponseEntity<List<CategoriaDto>> listarTodas() {
        // Le pedimos la lista al Service
        List<CategoriaDto> lista = categoriaService.listarTodas();
        // Devolvemos la lista en una caja con status 200 OK
        return ResponseEntity.ok(lista);
    }

    // GET a /api/categorias/{id} (ej: /api/categorias/1)
    @GetMapping("/{id}")
    public ResponseEntity<CategoriaDto> buscarPorId(@PathVariable Long id) {
        // @PathVariable atrapa el "1" de la URL y lo mete en la variable "id"
        CategoriaDto categoria = categoriaService.buscarPorId(id);
        return ResponseEntity.ok(categoria);
    }

    // POST a /api/categorias (Para CREAR)
    @PostMapping
    public ResponseEntity<CategoriaDto> crear(@RequestBody CategoriaCreate dto) {
        // @RequestBody agarra el JSON de Postman y lo convierte en CategoriaCreate
        CategoriaDto nuevaCategoria = categoriaService.crear(dto);
        // Cuando creamos algo, las buenas prácticas REST dicen que devolvamos 201 CREATED
        return ResponseEntity.status(HttpStatus.CREATED).body(nuevaCategoria);
    }

    // PUT a /api/categorias/{id} (Para ACTUALIZAR)
    @PutMapping("/{id}")
    public ResponseEntity<CategoriaDto> actualizar(@PathVariable Long id, @RequestBody CategoriaEdit dto) {
        // Necesitamos el ID de la URL y el JSON con los datos nuevos
        CategoriaDto categoriaActualizada = categoriaService.actualizar(id, dto);
        return ResponseEntity.ok(categoriaActualizada);
    }
}