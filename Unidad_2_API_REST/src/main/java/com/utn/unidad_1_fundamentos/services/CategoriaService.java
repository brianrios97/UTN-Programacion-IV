package com.utn.unidad_1_fundamentos.services;

import com.utn.unidad_1_fundamentos.dtos.categoria.CategoriaCreate;
import com.utn.unidad_1_fundamentos.dtos.categoria.CategoriaDto;
import com.utn.unidad_1_fundamentos.dtos.categoria.CategoriaEdit;
import com.utn.unidad_1_fundamentos.entities.Categoria;
import com.utn.unidad_1_fundamentos.repositories.CategoriaRepository;
import org.springframework.stereotype.Service;

import java.time.LocalDateTime;
import java.util.List;

@Service
public class CategoriaService {

    private final CategoriaRepository categoriaRepository;

    public CategoriaService(CategoriaRepository categoriaRepository) {
        this.categoriaRepository = categoriaRepository;
    }

    public List<CategoriaDto> listarTodas() {
        return categoriaRepository.findAll().stream()
                .filter(c -> !c.isEliminado())
                .map(this::toDto)
                .toList();
    }

    public CategoriaDto buscarPorId(Long id) {
        Categoria c = categoriaRepository.findById(id)
                .orElseThrow(() -> new IllegalArgumentException("Categoría no encontrada con ID: " + id));
        return toDto(c);
    }

    public CategoriaDto crear(CategoriaCreate createDto) {
        Categoria c = new Categoria();
        c.setNombre(createDto.nombre());
        c.setDescripcion(createDto.descripcion());
        c.setCreatedAt(LocalDateTime.now());
        c.setEliminado(false);

        Categoria guardada = categoriaRepository.save(c);
        return toDto(guardada);
    }

    public CategoriaDto actualizar(Long id, CategoriaEdit editDto) {
        Categoria c = categoriaRepository.findById(id)
                .orElseThrow(() -> new IllegalArgumentException("Categoría no encontrada con ID: " + id));

        c.setNombre(editDto.nombre());
        c.setDescripcion(editDto.descripcion());

        Categoria actualizada = categoriaRepository.save(c);
        return toDto(actualizada);
    }

    private CategoriaDto toDto(Categoria c) {
        return new CategoriaDto(c.getId(), c.getNombre(), c.getDescripcion());
    }
}