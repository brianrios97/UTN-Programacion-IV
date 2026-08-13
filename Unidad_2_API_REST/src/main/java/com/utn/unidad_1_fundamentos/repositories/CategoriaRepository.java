package com.utn.unidad_1_fundamentos.repositories;

import com.utn.unidad_1_fundamentos.entities.Categoria;
import org.springframework.data.jpa.repository.JpaRepository;
import org.springframework.stereotype.Repository;

@Repository
public interface CategoriaRepository extends JpaRepository<Categoria, Long> {
}