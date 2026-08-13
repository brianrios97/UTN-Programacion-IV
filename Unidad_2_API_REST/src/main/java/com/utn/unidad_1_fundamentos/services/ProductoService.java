package com.utn.unidad_1_fundamentos.services;

import com.utn.unidad_1_fundamentos.dtos.producto.ProductoCreate;
import com.utn.unidad_1_fundamentos.dtos.producto.ProductoDto;
import com.utn.unidad_1_fundamentos.dtos.producto.ProductoEdit;
import com.utn.unidad_1_fundamentos.entities.Categoria;
import com.utn.unidad_1_fundamentos.entities.Producto;
import com.utn.unidad_1_fundamentos.repositories.CategoriaRepository;
import com.utn.unidad_1_fundamentos.repositories.ProductoRepository;
import org.springframework.stereotype.Service;

import java.time.LocalDateTime;
import java.util.List;

@Service
public class ProductoService {

    private final ProductoRepository productoRepository;
    private final CategoriaRepository categoriaRepository;

    public ProductoService(ProductoRepository productoRepository, CategoriaRepository categoriaRepository) {
        this.productoRepository = productoRepository;
        this.categoriaRepository = categoriaRepository;
    }

    public List<ProductoDto> listarTodos() {
        return productoRepository.findAll().stream()
                .filter(p -> !p.isEliminado())
                .map(this::toDto)
                .toList();
    }

    public ProductoDto buscarPorId(Long id) {
        Producto p = productoRepository.findById(id)
                .orElseThrow(() -> new IllegalArgumentException("Producto no encontrado con ID: " + id));
        return toDto(p);
    }

    public ProductoDto crear(ProductoCreate dto) {
        Categoria cat = categoriaRepository.findById(dto.categoriaId())
                .orElseThrow(() -> new IllegalArgumentException("Categoría no encontrada con ID: " + dto.categoriaId()));

        Producto p = new Producto();
        p.setNombre(dto.nombre());
        p.setPrecio(dto.precio());
        p.setDescripcion(dto.descripcion());
        p.setStock(dto.stock());
        p.setImagen(dto.imagen());
        p.setDisponible(dto.disponible());
        p.setCategoria(cat);
        p.setCreatedAt(LocalDateTime.now());
        p.setEliminado(false);

        Producto guardado = productoRepository.save(p);
        return toDto(guardado);
    }

    public ProductoDto actualizar(Long id, ProductoEdit dto) {
        Producto p = productoRepository.findById(id)
                .orElseThrow(() -> new IllegalArgumentException("Producto no encontrado con ID: " + id));

        Categoria cat = categoriaRepository.findById(dto.categoriaId())
                .orElseThrow(() -> new IllegalArgumentException("Categoría no encontrada con ID: " + dto.categoriaId()));

        p.setNombre(dto.nombre());
        p.setPrecio(dto.precio());
        p.setDescripcion(dto.descripcion());
        p.setStock(dto.stock());
        p.setImagen(dto.imagen());
        p.setDisponible(dto.disponible());
        p.setCategoria(cat);

        Producto actualizado = productoRepository.save(p);
        return toDto(actualizado);
    }

    private ProductoDto toDto(Producto p) {
        return new ProductoDto(
                p.getId(),
                p.getNombre(),
                p.getPrecio(),
                p.getDescripcion(),
                p.getStock(),
                p.getImagen(),
                p.getDisponible(),
                p.getCategoria() != null ? p.getCategoria().getNombre() : "Sin categoría"
        );
    }
}